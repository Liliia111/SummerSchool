# SummerSchool
Environment setup:

 sudo apt-get install python3

 If pip3 not installed run:
 sudo apt-get install -y python3-pip

 pip3 install virtualen

 git clone https://github.com/Liliia111/SummerSchool.git

 cd SummerSchool
 
 virtualenv env
 
 env/bin/activate
 
 pip3 install -r requirements.txt


installing psycopg2: 
 pip3 install psycopg2 

if u have some troubles try:
 sudo apt-get install libpq-dev

in file 'local_settings.py' u have to initialize two variables 
POSTGRES_DB_USERNAME = 'name'
POSTGRES_DB_PASSWORD = 'password'
and change database user and password in 'settings.py' to this variables

 python3 manage.py makemigrations
 python3 manage.py migrate
 
 To run project:
 python3 manage.py runserver

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

To check if everything is installed, use the following command:
```bash
npm run dev-server
```

