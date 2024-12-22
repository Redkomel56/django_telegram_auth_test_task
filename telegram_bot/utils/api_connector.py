import requests

from config import BASE_API_URL, BASE_API_KEY


class APIError(Exception):
    """Базовый класс для ошибок API"""
    def __init__(self, message="An API error occurred", status_code=None):
        self.status_code = status_code
        super().__init__(message)


class UserAlreadyExistsError(APIError):
    """Ошибка: Пользователь уже существует"""
    def __init__(self, message="User already exists"):
        super().__init__(message, status_code=400)


class UnexpectedError(APIError):
    """Ошибка: Неожиданная ошибка"""
    def __init__(self, message="Unexpected error occurred"):
        super().__init__(message)


class UserCreationClient:
    def __init__(self, base_url=BASE_API_URL, api_key=BASE_API_KEY):
        """
        Инициализация клиента.

        :param base_url: URL API (например, "http://127.0.0.1:8000/api/")
        :param api_key: Ваш API-ключ
        """
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key

    def create_user(self, auth_uuid, tg_id, username):
        """
        Создаёт пользователя через защищённый эндпоинт.

        :param auth_uuid: Уникальный UUID для авторизации
        :param tg_id: Telegram ID пользователя
        :param username: Telegram username
        :raises APIError: При возникновении ошибки запроса
        :return: Ответ сервера в формате JSON
        """
        url = f"{self.base_url}/create-user"
        headers = {
            "Content-Type": "application/json",
            "X-API-KEY": self.api_key,
        }
        payload = {
            "auth_uuid": auth_uuid,
            "tg_id": tg_id,
            "username": username,
        }

        try:
            response = requests.post(url, json=payload, headers=headers)
        except requests.RequestException as e:
            raise UnexpectedError(f"Network error: {e}")

        if response.status_code == 400:
            raise UserAlreadyExistsError()
        elif not response.ok:
            raise APIError(f"Unexpected error: {response.status_code}", status_code=response.status_code)

        try:
            return response.json()
        except ValueError:
            raise UnexpectedError("Invalid JSON response from server")


# Пример использования
if __name__ == "__main__":
    # Инициализация клиента
    client = UserCreationClient(base_url="http://127.0.0.1:8000/api", api_key="your_secret_api_key")

    # Пример данных для создания пользователя
    auth_uuid = "exampdle-authl-uuid"
    tg_id = "12345679"
    username = "example_use"

    try:
        response = client.create_user(auth_uuid=auth_uuid, tg_id=tg_id, username=username)
        print("User created successfully:", response)
    except APIError as e:
        print(f"API error: {e}")

