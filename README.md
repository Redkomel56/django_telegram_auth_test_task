# Проект: Telegram Bot и Django Backend

## Описание

Этот проект включает Telegram-бота, который работает на основе библиотеки `aiogram`, и серверный бэкенд, реализованный на Django. Основная задача — взаимодействие между ботом и сервером через упрощённый API-коннектор. База данных напрямую не доступна боту, обеспечивая лучшую безопасность и изоляцию компонентов.

---

## Стек технологий

- **Бэкенд**:
  - `Django` — серверный фреймворк.
  - `djangorestframework` — для создания REST API.
  - `django-cors-headers` — для поддержки CORS.
  - `django-environ` — для работы с переменными окружения.
  - `redis` — кеширование через Dragonfly.
- **Бот**:
  - `aiogram==3.5.0` — библиотека для разработки Telegram-ботов.
  - `requests==2.31.0` — для взаимодействия с API бэкенда.
  - `pyyaml==6.0.1` — для работы с YAML-файлами.
  - `pymongo==4.6.1` — для хранения данных (MongoDB, опционально).
  - `cachetools` — вспомогательная библиотека.
- **Инфраструктура**:
  - `Dragonfly` — высокопроизводительная альтернатива Redis для кеширования.
  - `Docker` и `docker-compose` — для контейнеризации и удобного развёртывания.

---

## Как поднять проект с использованием `docker-compose`

1. Убедитесь, что Docker и docker-compose установлены на вашем устройстве.
2. Склонируйте репозиторий с проектом:
   ```bash
   git clone <repository_url>
   cd <project_directory>
   ```
3. Создайте файл `.env` в корне проекта с содержимым:
   ```env
   SECRET_KEY=your_secret_key
   DEBUG=True
   ALLOWED_HOSTS=127.0.0.1,localhost,192.168.1.154
   DATABASE_NAME=db.sqlite3
   DATABASE_USER=
   DATABASE_PASSWORD=
   DATABASE_HOST=
   DATABASE_PORT=
   REDIS_LOCATION=redis://dragonfly-django:6379/2
   API_KEY=your_secret_api_key
   BOT_TOKEN=your_telegram_bot_token
   BASE_API_URL=http://192.168.1.154:8000/api
   ```
4. Запустите `docker-compose`:
   ```bash
   docker-compose up --build
   ```

После успешного запуска:
- Django-бэкенд будет доступен по адресу: [http://localhost:8000](http://localhost:8000)
- Dragonfly запущен на порту `6379`.
- Telegram-бот начнёт свою работу автоматически.

---

## Особенности

- **Telegram Bot**:
  - Основан на уменьшенном шаблоне для ботов с использованием `aiogram`.
  - Использует упрощённый API-коннектор для взаимодействия с бэкендом.
  - Не имеет прямого доступа к базе данных, что повышает безопасность.
- **Бэкенд**:
  - Обрабатывает API-запросы через Django REST Framework.
  - Кеширование реализовано через Dragonfly для ускорения обработки.

---

## Переменные окружения

| Переменная           | Описание                                                      |
|----------------------|--------------------------------------------------------------|
| `SECRET_KEY`         | Секретный ключ Django.                                        |
| `DEBUG`              | Включает режим отладки (`True` или `False`).                  |
| `ALLOWED_HOSTS`      | Список разрешённых хостов для Django.                         |
| `DATABASE_NAME`      | Имя базы данных.                                              |
| `DATABASE_USER`      | Пользователь базы данных (для PostgreSQL/MySQL).             |
| `DATABASE_PASSWORD`  | Пароль пользователя базы данных.                              |
| `DATABASE_HOST`      | Хост базы данных.                                             |
| `DATABASE_PORT`      | Порт базы данных.                                             |
| `REDIS_LOCATION`     | URL для подключения к Dragonfly.                              |
| `API_KEY`            | Ключ для взаимодействия бота с бэкендом.                     |
| `BOT_TOKEN`          | Токен Telegram-бота.                                          |
| `BASE_API_URL`       | URL API бэкенда.                                              |

---

## Личное мнение

Для реализации аналогичного проекта я бы предпочёл использовать:
- **FastAPI** — для создания лёгкого и производительного бэкенда.
- **React** — для построения пользовательского интерфейса.
- **aiogram** — как инструмент для разработки Telegram-ботов.

Основная причина — более современный подход и гибкость, чем у Django, который из-за своего жёсткого декларативного стиля не всегда подходит для динамичных приложений.

---

## Временные затраты

На выполнение данного проекта ушло **около 2 часов**. Я опустил множество деталей, минимизировал оформление кода и не использовал сложные приёмы для ускорения работы. Этот код представляет собой минимально жизнеспособный продукт (MVP).