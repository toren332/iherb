<h4>Реализованная функциональность</h4>
<ul>
    <li>Система администрирования БАДов, Статей и ключевых компонентов БАДов</li>
    <li>API для работы мобильного приложения с БАДами, Статьями и ключевыми компонентами БАДов</li>
    <li>Импорт из файлов базы БАДов и статей, автоматическое вычленение и создание ключевых компонентов БАДов</li>
</ul> 
<h4>Особенность проекта в следующем:</h4>
<ul>
 <li>Гибкая архитектура проекта</li>
 <li>Простое заполнение данными</li>
 <li>REST API для комфортной работы</li>  
 </ul>
<h4>Основной стек технологий:</h4>
<ul>
    <li>Python, Django, DjangoRestFramework, Pandas,  </li>
	<li>HTML, CSS, JavaScript</li>
	<li>REST API</li>
	<li>Postgres</li>
	<li>Docker, DockerCompose</li>
	<li>Git</li>
 </ul>
<h4>Демо</h4>
<p>Админ панель сервиса доступна по адресу: <a href="http://5.63.155.51:8000/admin/">http://5.63.155.51:8000/admin/</a> </p>
<p>API сервиса доступно по адресу: <a href="http://5.63.155.51:8000/api/">http://5.63.155.51:8000/api/</a> </p>
<p>Реквизиты тестового пользователя: email: <b>toren332</b>, пароль: <b>mypass321</b></p>




СРЕДА ЗАПУСКА
------------
1) развертывание сервиса производится на любой ОС с развёрнутым <a href="https://www.docker.com/">Docker и DockerCompose</a>


УСТАНОВКА
------------
### Установка Docker

Выполните инструкцию на сайте в зависимости от ОС

<a href="https://docs.docker.com/engine/install/">Ссылка</a>


### Развертывание проекта

Добавьте файл .env с приведенной ниже структурой 
~~~
POSTGRES_USER=POSTGRES_USER
POSTGRES_PASS=POSTGRES_PASS
~~~
Должны быть свободны порты 5432 и 8000

~~~
docker compose up
~~~

### Миграции базы данных и заполнение

~~~
docker exec -it iherb_django python manage.py migrate
docker exec -it iherb_django python manage.py create_onboarding
docker exec -it iherb_django python manage.py create_articles
~~~

### Создание суперпользователя

С помощью введенных на этом шаге данных можно войти в панель администрирования

~~~
docker exec -it iherb_django python manage.py createsuperuser
~~~

При правильной установке пользоваться проектом можно по адресу
<p>Админ панель сервиса: <a href="http://0.0.0.0:8000/admin/">http://0.0.0.0:8000/admin/</a> </p>
<p>API сервиса: <a href="http://0.0.0.0:8000/api/">http://0.0.0.0:8000/api/</a> </p>


РАЗРАБОТЧИКИ

<h4>Малинин Тимофей Илларионович fullstack https://t.me/toren332 </h4>


