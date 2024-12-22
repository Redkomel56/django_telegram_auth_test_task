from django.db import models
# migrations

class UserRecord(models.Model):
    # TODO: Минимальный набор полей для работы приложения, при желание расширить
    auth_uuid = models.CharField(max_length=100, unique=True)
    tg_id = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.auth_uuid}: {self.username if self.username is not None else self.tg_id}"
