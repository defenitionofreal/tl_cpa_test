Тестовое задание от Traffic Light.
=====================
***
### Описание

Создайте веб страницу, которая будет выводить древовидную структуру отделов со списком сотрудников

Информация о каждом сотруднике должна храниться в базе данных  и
содержать следующие данные

* ФИО
* Должность
* Дата приема на работу
* Размер заработной платы
* Подразделение - подразделения имеют структуру до 5 уровней

Дерево должно отображаться в свернутом виде.
База данных должна содержать не менее 50 000 сотрудников и 25 подразделений в 5 уровнях иерархий.
Управление записями CRUD через административную часть Django.
Django 3+, Python 3.5+, база на свое усмотрение
Используйте Twitter Bootstrap для создания базовых стилей Вашей страницы.
 
Если используете дополнительные библиотеки, то необходимо оформить все в requirements.txt

***
### Решение

Чтобы создать и заполнить данные (50.000 сотрудников на 25 разделов) я использовал Faker.
Написал скрипт и создать новую команду:
```
python manage.py createdata 
```
После запуска команды мы увидим следующее:
![createdata](https://testingsite.tmweb.ru/pics/cpa_workers.png)

Чтобы процес наполнения базы был быстрее, можно изменить число в константе NUM_USERS.


Для создания древовидной структуры можно было использовать популярную библиотеку 'django-mptt', но решение было принято написать код с нуля.
Создал кастомный шаблонный тег. В папке приложения 'templatetags' лежат два файла: в utils хранится логика, в draw_menu создается дерево.

По итогу на веб страницу мы увидим следующее:
![tree](https://testingsite.tmweb.ru/pics/cpa_tree.png)



### Установка
```
python3 -m venv venv
source bin/venv/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createdata
```

Данные ещё можно заполнить через fixtures. 
Я сделал дамп тестовой базы, но она настолько большая, что гитхаб её не может подгрузить) 
После миграций выполните команду:
```
python manage.py loaddata fixtures/db.json
```
По итогу мы увидим следующее:
![fixtures](https://testingsite.tmweb.ru/pics/cpa_fixtures.png)
