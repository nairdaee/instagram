# INSTAGRAM
![App logo](https://www.logopik.com/wp-content/uploads/edd/2018/06/New-Instagram-logo-vector-black-and-white-free-download.png)


Created on _May 31, 2020_

---

## AUTHOR

__ADRIAN ETENYI__

### Description

This is a clone of instagram web app that has most of the functionality expected on an image sharing application

___

### User stories

A user is able to:

* Sign in to the application to start using.
* Upload pictures to the application.
* See their profile with all their pictures.
* Follow other users and see their pictures on their timeline.
* Like a picture and leave a comment on it.
* Search for other users.

### Application setup

* Since the app uses a remote database provided by Heroku, you will need to configure your own local database  to be able to use it. Follow these steps:
    * Create a virtual environment i.e `virtualenv --python=/usr/bin/python3 <env name> ` and activate it
    * Install all the requirements....__see requirements__
    * Configure your own database...__see db configurations__ and make migrations
    * Run application



### Requirements

`python 3.7.5` _(Python 3.6 - 3.8)_

```
    Django==1.11.29
    django-bootstrap3==12.1.0
    gunicorn==20.0.4
    Pillow==7.1.2
    psycopg2==2.8.5
    pytz==2020.1
    whitenoise==5.1.0
```

> To install them just use `pip3 install -r requirements.txt`

### DB Configurations

> Go to postgresql i.e `psql`
 * Create your database `CREATE DATABASE <database name>;`

* Change the contents of database to the following:
    ```
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': '< Your database name >',
                'USER': '< Your Database Username >',
                'PASSWORD':'< Your Database Password >',
             }
        }
    ```

* Make migrations i.e `python3.7 manage.py makemigrations` then run them to update your db `python3.7 manage.py migrate`

> Note: _if you want you can use the .env file to store your db credentials for safety purposes_

### Known bugs

~~Implementing the F object used for resolving references to existing query objects~~

### Live site

> https://nairdaee.herokuapp.com/

---

### Support and contact details

Feel free to send me comments,queries and/or feedback via email @etadriano2@gmail.com

### License

Copyright (c) 2020 Adrian Etenyi.
Licensed under the [MIT license](LICENSE)
