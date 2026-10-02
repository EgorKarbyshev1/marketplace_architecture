# Marketplace Architecture

Учебный проект маркетплейса. Пока реализован только каркас `catalog-service`
на Python 3.12 и FastAPI, без бизнес-логики и внешней инфраструктуры.

## Запуск

Требуются Docker Engine (или Docker Desktop) и Docker Compose v2.
Из корня репозитория:

```sh
docker compose up --build -d
```

Проверка:

```sh
curl -i http://localhost:8000/health
```

Ожидается HTTP `200 OK` и JSON `{"status":"ok"}`.
В PowerShell можно использовать `curl.exe` вместо `curl`.

Состояние контейнера и остановка:

```sh
docker compose ps
docker compose down
```

Заготовки документации: [архитектура](docs/architecture.md),
[решения](docs/decisions.md), [C4 Container](docs/diagrams/container.puml).
