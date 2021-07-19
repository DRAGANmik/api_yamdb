[![pep8 codestyle](https://github.com/DRAGANmik/api_yamdb/actions/workflows/codestyle.yml/badge.svg?branch=master)](https://github.com/DRAGANmik/api_yamdb/actions/workflows/codestyle.yml)
[![tests](https://github.com/DRAGANmik/api_yamdb/actions/workflows/tests.yml/badge.svg)](https://github.com/DRAGANmik/api_yamdb/actions/workflows/tests.yml)
# api_yamdb

Бэкенд для проекта YaMDb - сервис для оценивая, музыки и книг.

## Команда разработки:
* Драган Михаил
* Софья Клочко
* Александр Трайнич


## Технологии
```
Python 3.7+
Django
Django REST Framework
*тут нужно дополнить*
```
## В проект добавлен Makefile для облегчения запуска management команд

Запуск django сервера c локальными настройками

```shell
make runserver
```

Создать и применить миграции
```shell
make migrate
```

Создать суперпользователя:
```shell
make createsuperuser
```

# Запуск тестов

```shell
pytest
```
# Просмотр документации по API

```shell
127.0.0.1:8000/redoc
