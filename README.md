# SummerSchool
## Environment setup:
```bash
sudo apt-get install python3
```
If pip3 not installed run:
```bash
sudo apt-get install -y python3-pip
```
Then do the following:
```bash
pip3 install virtualen
git clone https://github.com/Liliia111/SummerSchool.git
cd SummerSchool
virtualenv env
env/bin/activate
pip3 install -r requirements.txt
```

To install psycopg2:
```bash 
pip3 install psycopg2 
```
If u have some troubles try:
```bash
sudo apt-get install libpq-dev
```
Create **local_settings.py** file on the **manage.py** level. In the file **local_settings.py** u have to initialize all the necessary variables: 
```bash
POSTGRES_DB_USERNAME = 'name'
POSTGRES_DB_PASSWORD = 'password'
SENDGRID_API_KEY = 'your key'
DEFAULT_FROM_EMAIL = 'email'
```
And change database user and password in **settings.py** to this variables.

Then to have all tables in your database, you must do following commands:
```bash
python3 manage.py makemigrations
python3 manage.py migrate
``` 
To run project:
```bash
python3 manage.py runserver
```
To use hitcount package, in **hitcount/models.py** inside **HitCount** class change **object_pk** type from TextField to IntegerField:
```bash
object_pk = models.IntegerField('object ID')
```
### Celery configuration
To use Celery, install packages from requirements.txt (or run ```pip3 install celery``` and ```pip3 install celery redis```). Then install Redis as a Celery “broker” through ranning these commands:
```bash
$ wget http://download.redis.io/releases/redis-5.0.5.tar.gz
$ tar xzf redis-5.0.5.tar.gz
$ cd redis-5.0.5
$ make
```
Run Redis with:
```bash
$ src/redis-server
```
## UI setup
Install Node.js:
```bash
sudo apt install node.js
```
Once installed, you verify it by checking the installed version of Node.js with this command:
```bash
nodejs --version
```
The version must be 10 or upper, if the version is older, use [nvm](https://www.digitalocean.com/community/tutorials/node-js-ubuntu-18-04-ru) to change version.

To install npm, use the following command:
```bash
sudo apt install npm
```

To install all requirements for UI use next commands:
```bash
cd SummerSchool
npm install 
```

To check if everything is installed, use the following command:
```bash
npm run dev-server
```

To add bundle.js:
```bash
npm run build
```

