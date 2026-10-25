# RUNBOOK (Аварийная инструкция)

## 1. Сервис не отвечает (500 / 502)
- Проверить статус контейнеров: `docker compose -f compose.prod.yaml ps`
- Посмотреть логи приложения: `docker compose -f compose.prod.yaml logs app --tail 100`
- Посмотреть логи БД: `docker compose -f compose.prod.yaml logs db --tail 100`

## 2. Откат релиза (Rollback)
Если новая версия сломала прод, выполнить откат на предыдущий тег:
```powershell
$env:TAG="1.0.0" 
docker compose -f compose.prod.yaml up -d

