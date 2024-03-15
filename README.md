## Проект-платформа для блогов, имеющая возможность зарегистрироваться, создать, отредактировать или удалить собственный пост, прокомментировать пост другого автора и подписаться на него. 
Для каждого поста нужно указать категорию — например «путешествия», «кулинария» или «python-разработка», а также опционально локацию, с которой связан пост, например «Остров отчаянья» или «Караганда». 
Пользователь может перейти на страницу любой категории и увидеть все посты, которые к ней относятся.
Пользователи смогут заходить на чужие страницы, читать и комментировать чужие посты.

## Использованные технологии:
- Python 3.9
- Django 3.2
- SQLite
- 
## Запуск проекта
1. ### Склонируйте репозиторий:
```
https://github.com/romatimon/blogicum
```

2. ### Создайте и активируйте виртуальное окружение:
Команда для установки виртуального окружения на Mac или Linux:
```
python3 -m venv env
source env/bin/activate
```

Команда для установки виртуального окружения на Windows:
```
python -m venv venv
source venv/Scripts/activate
```

3. ### Установите зависимости:
```
pip install -r requirements.txt
```

5. ### Проведите миграции:
```
python manage.py migrate
```

6. ### Запустите локальный сервер:
```
python manage.py runserver
```
Автор [romatimon](https://github.com/romatimon)
