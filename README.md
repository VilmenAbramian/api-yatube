# Проект CRUD для Yatube
CRUD для Yatube - проект, реализущий REST API для сервиса, подобного [blogicum](https://github.com/VilmenAbramian/blogicum-3), а именно команды CRUD (create-read-update-delete).

### Используемые технологии:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

### Запуск проекта:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/VilmenAbramian/telegram-bot
```
```
cd telegram-bot
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
```
-   Для Linux/macOS
```
source env/bin/activate
```
-   Для Windows
```
source env/scripts/activate
```
Обновить менеджер пакетов pip
```
python3 -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Выполнить миграции
```
python manage.py migrate
```
Запустить проект
```
python manage.py runserver
```
### Устройство проекта:
В данном проекте реализован только бэкэнд (описаны приложения, модели, работа с API). Функциональность Rest API реализована с помощью Django Rest API.

API доступен только для аутентифицированных пользователей (использовался **TokenAuthentication**) и реализован для всех моделей из приложения **posts**, при этом вся логика API вынесена в отдельное приложение **api**

Аутентифицированный пользователь авторизован на изменение и удаление своего контента; в остальных случаях доступ предоставляется только для чтения. При попытке изменить чужие данные возвращается код ответа **403 Forbidden**.

Для взаимодействия с ресурсами описаны и настроены такие эндпоинты:

-   `api/v1/api-token-auth/` (POST): передаём логин и пароль, получаем токен.
-   `api/v1/posts/` (GET, POST): получаем список всех постов или создаём новый пост.
-   `api/v1/posts/{post_id}/` (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем пост с идентификатором`{post_id}`.
-   `api/v1/groups/` (GET): получаем список всех групп.
-   `api/v1/groups/{group_id}/` (GET): получаем информацию о группе с идентификатором `{group_id}`.
-   `api/v1/posts/{post_id}/comments/` (GET): получаем список всех комментариев поста с идентификатором `post_id` (POST): создаём новый комментарий для поста с идентификатором `{post_id}`.
-   `api/v1/posts/{post_id}/comments/{comment_id}/` (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем комментарий с идентификатором `{comment_id}` в посте с `id=post_id`.

В ответ на запросы POST, PUT и PATCH API должен возвращает объект, который был добавлен или изменён.

### Примеры запросов
Пример POST-запроса с токеном Антона Чехова: добавление нового поста.
_POST .../api/v1/posts/_
```
{
    "text": "Вечером собрались в редакции «Русской мысли», чтобы поговорить о народном театре. Проект Шехтеля всем нравится.",
    "group": 1
}
```
Пример ответа:
```
{
    "id": 14,
    "text": "Вечером собрались в редакции «Русской мысли», чтобы поговорить о народном театре. Проект Шехтеля всем нравится.",
    "author": "anton",
    "image": null,
    "group": 1,
    "pub_date": "2021-06-01T08:47:11.084589Z"
}
```
Пример POST-запроса с токеном Антона Чехова: отправляем новый комментарий к посту с `id=14`.
_POST .../api/v1/posts/14/comments/_
```
{ "text": "тест тест" }
```
Пример ответа:
```
{
    "id": 4,
    "author": "anton",
    "post": 14,
    "text": "тест тест",
    "created": "2021-06-01T10:14:51.388932Z"
}
```
Пример GET-запроса с токеном Антона Чехова: получаем информацию о группе.
GET _.../api/v1/groups/2/_
Пример ответа:
```
{
    "id": 2,
    "title": "Математика",
    "slug": "math",
    "description": "Посты на тему математики"
}
```

Связь с автором: abramian.vl@phystech.edu
Проект-13

![GitHub top language](https://img.shields.io/github/languages/top/VilmenAbramian/api-yatube)
