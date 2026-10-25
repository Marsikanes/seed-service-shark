# Guestbook Workshop (Capstone)

Учебный проект: гостевая книга на FastAPI + PostgreSQL.

## Запуск локально
1. `cp .env.example .env` (заполнить пароль)
2. `docker compose up --build -d`
3. Открыть http://localhost:8000

## CI/CD
- Пайплайн: GitHub Actions (`.github/workflows/pipeline.yml`)
- Образы: `ghcr.io/marsikanes/cretor-guestbook-workshop`
```
