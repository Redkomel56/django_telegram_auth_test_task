from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import UserRecord
import uuid
import json
from backend.settings import API_KEY


@api_view(['POST'])
def generate_load(request):
    auth_uuid = str(uuid.uuid4())
    # Запись в Dragonfly
    cache.set(auth_uuid, json.dumps({"tg_id": None, "username": None}), timeout=3600)
    return Response({"auth_uuid": auth_uuid, "url": f"https://t.me/asdklppp_bot?start=auth_{auth_uuid}"}, status=status.HTTP_200_OK)


@api_view(['GET'])
def check_status(request, auth_uuid):
    # Проверка в кэше
    data = cache.get(auth_uuid)
    if data:
        data = json.loads(data)
        if data['tg_id']:
            return Response({"tg_id": data['tg_id'], "username": data['username']}, status=status.HTTP_200_OK)
        return Response({"status": "pending"}, status=status.HTTP_202_ACCEPTED)

    try:
        record = UserRecord.objects.get(auth_uuid=auth_uuid)
        if record.tg_id and record.username:
            return Response({"tg_id": record.tg_id, "username": record.username}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "pending"}, status=status.HTTP_202_ACCEPTED)
    except UserRecord.DoesNotExist:
        return Response({"error": "Invalid auth_uuid"}, status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
@api_view(['POST'])
def create_user(request):
    if request.headers.get('X-API-KEY') != API_KEY:
        return Response({"error": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)
    try:
        payload = json.loads(request.body.decode('utf-8'))
    except json.JSONDecodeError:
        return Response({"error": "Invalid JSON payload"}, status=status.HTTP_400_BAD_REQUEST)

    auth_uuid = payload.get('auth_uuid')
    tg_id = payload.get('tg_id')
    username = payload.get('username')

    if not all([auth_uuid, tg_id, username]):
        return Response({"error": "Missing data"}, status=status.HTTP_400_BAD_REQUEST)
    data = cache.get(auth_uuid)

    if not data:
        return Response({"error": "Invalid auth_uuid"}, status=status.HTTP_404_NOT_FOUND)

    record, created = UserRecord.objects.get_or_create(
        auth_uuid=auth_uuid,
        defaults={"tg_id": tg_id, "username": username}
    )

    if not created:
        return Response({"error": "User already exists"}, status=status.HTTP_400_BAD_REQUEST)

    cache.set(auth_uuid, json.dumps({"tg_id": tg_id, "username": username}), timeout=3600)

    return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
