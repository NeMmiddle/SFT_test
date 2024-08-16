# 🚀 SFT_test


## 📦 Собрка и запуск проекта.

Выполните следующие действия, чтобы создать и запустить приложение с помощью Docker.
### 1. Сборка и запуск приложения

Сначала создайте контейнер Docker и запустите приложение:

```sh
docker-compose up --build
```

### 1. Конечная точка API

- **URL**: [http://127.0.0.1:8000/api/manufacturers/\<int:contract_id\>/](http://127.0.0.1:8000/api/manufacturers/<int:contract_id>/)
  
  Замените `<int:contract_id>` фактическим идентификатором контракта, который вы хотите запросить.

### 2. Админка

- **Панель администратора**: [http://127.0.0.1:8000/admin/login/?next=/admin/](http://127.0.0.1:8000/admin/login/?next=/admin/)

  - **Username**: `admin`
  - **Password**: `admin`

---
