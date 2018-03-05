<dl>
	<dt><H2>List install</H2></dt>
</dl>


```sudo pip3 install virtualenv```


```virtualenv venv```


```source venv/bin/activate or  deactivate```


```pip install django```


```pip install psycopg2```


```python manage.py makemigrations todo```


```python manage.py migrate```


```pip install django-filter```


```API link http://127.0.0.1:8000/todo/API/```


```TODO link http://127.0.0.1:8000/dashboard/```


```docker-compose run web python src/manage.py migrate```


```docker-compose build```


```docker-compose up```

docker ps

docker stats djangotodo_web_1

Qwerty12345

makemigrations todo

docker-compose run web python src/manage.py migrate

docker-compose run web src/manage.py dumpdata --exclude auth.permission --exclude contenttypes --indent 4 > db_psg.json