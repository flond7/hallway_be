
# INSTALL AND SETUP ON UBUNTU

## allow ssh on ubuntu
- sudo apt-get update upgrade
- sudo apt-get install openssh-server
- sudo systemctl enable ssh
- sudo systemctl start ssh

## allow rdp
- sudo apt install xrdp ********************* windows remote desktop
- sudo systemctl enable --now xrdp ********** enable to start after reboot and run the remote desktop sharing server xrdp

## set proxy
- sudo nano /etc/environment
- add config proxy insiel
  export proxy_http="http://172.25.10.10:801"
  export proxy_https="https://172.25.10.10:801"
  export proxy_ftp="http://172.25.10.10:801"
  export no_proxy="localhost,172.0.0.1"

## initial setup for venv and mariaDB (do it in the server terminal)
- sudo apt-get install python3-venv python3-pip
- sudo apt install wget
- wget https://dlm.mariadb.com/enterprise-release-helpers/mariadb_es_repo_setup
- chmod +x mariadb_es_repo_setup
- sudo apt install libmariadb3 libmariadb-dev
- sudo apt install mariadb-server mariadb-client -y
- sudo systemctl status mariadb ********************************** check the version
- sudo systemctl start mariadb *********************************** 
- sudo systemctl enable mariadb ********************************** ensures that MariaDB starts every time the server is rebooted
- sudo mysql_secure_installation ********************************* answer the questions
- CREATE USER 'admin_mariaDB'@'localhost' IDENTIFIED BY 'mun*07*****';
- GRANT ALL PRIVILEGES ON *.* TO 'admin_mariaDB'@'localhost';
- FLUSH PRIVILEGES;
- EXIT;

# enter mariaDB e create the main db
- sudo mariadb sudo mariadb -u admin_user_name -p 
- CREATE DATABASE name_db; (es: hallway_aviano)
- FLUSH PRIVILEGES


https://www.cherryservers.com/blog/how-to-install-and-start-using-mariadb-on-ubuntu-20-04

## install mysql
- apt install mysql-server libmysqlclient-dev -y
- systemctl start mysql
- systemctl enable mysql
- sudo mysql **************************** enter
- CREATE DATABASE djangodb;
- CREATE USER 'admin_mysqlDB'@'localhost' IDENTIFIED BY 'mun*07*****';
- GRANT ALL PRIVILEGES ON *.* TO 'admin_mysqlDB'@'localhost';
- FLUSH PRIVILEGES;
- EXIT;


## create main project folder in /var/www/html
- mkdir folder_name (eg: project_folder)
- cd project_folder

## install apache
- sudo apt-get update ********************************************* (repository update) for update problems see section ERRORS
- sudo apt-get install apache2 apache2-utils libexpat1 ssl-cert python (then check with http://localhost to see if everything is ok)

## install mod_wsgi (needed to deploy django in apache)
- sudo apt-get install libapache2-mod-wsgi-py3  
- sudo a2enmod wsgi
- sudo nano /etc/apache2/sites-available/000-default.conf ********* substitute the default config with this one)

  <VirtualHost *:80>

    ServerAdmin webmaster@localhost
    DocumentRoot /var/www/html/

    # where to save error logs
    # folder has to exist so check or create it
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combine

    # to correctly serve static files specify where to go when apache sees /static pointing to the static directory with absolute path
    # and grant all permissions for that directory
    alias /static /var/www/html/utenti/handleUsers/static
    <Directory /var/www/html/utenti/handleUsers/static>
      Require all granted
    </Directory>

    # to correctly serve static admin files use a trick, copy the admin folder you find in 
    # venv/Lib/site-packages/django/contrib/admin/static to the server where you put the custom front end static files
    # /var/www/html/utenti/handleUsers/static

    # directory points to where wsgi.py is
    <Directory /var/www/html/utenti/handleUsers/handleUsers>
      Require all granted
    </Directory>

    # first param is the process name, it can be whatever you want, es "handleUsers"
    # python-home points to /venv
    # python-path point to where manage.py is
    WSGIDaemonProcess handleUsers python-home=/var/www/html/utenti/venv python-path=/var/www/html/utenti/handleUsers
    # processGroup just has to have the same name as the process above
    WSGIProcessGroup handleUsers
    # when apache sees root I want it to see the django app (points to wsgi.py)
    WSGIScriptAlias / /var/www/html/utenti/handleUsers/handleUsers/wsgi.py
  </VirtualHost>

- apachectl configtest (check if syntax is ok, don't worry about eventual server name error)
- service apache2 restart

## set permissions
- cd /var/www
- change the html folder owner and set it as the administrator user. If you put : after the user name it will choose authomatically the right group
  chown NOMEUTENTE: html
- cd html
- mkdir NOME_CARTELLA_PROGETTO (es: utenti) 
- check if the new folder has the right owner (ls -la) and eventually change them
  sudo chown NOMEUTENTE: NOME_CARTELLA_PROGETTO (es sudo chown nodeweaver: utenti)

## install php8
- sudo apt update upgrade
- sudo apt install software-properties-common
- sudo add-apt-repository ppa:ondrej/apache2 
If there is an error try
- sudo -E add-apt-repository ppa:ondrej/apache2
- sudo apt update
- sudo apt install php8.1 
- sudo nano /etc/php/8.1/apache2/php.ini
- change display_errors = Off to On
************************************** if there are errors check the last php8.x version

## copy files
- use something like bitwise/filezilla to transfer the files to the new server
- ** don't copy the venv folder, it will have to be created and populated from scratch ** 

## django setup (do it on VS connected via ssh to the server)
- sudo apt install python3.10-venv
- python3 -m venv venv (the second venv is the name of the virtual environment)
- source venv/bin/activate
- sudo apt install python3-django
- sudo apt-get install python3-dev default-libmysqlclient-dev build-essential **** needed to install mysqlclient
- pip install --proxy=http://proxy-xxxxxxxxxxxxxxxxxxx:801 django mysqlclient

## correctly serve static files
- create a STATIC_ROOT in settings.py with the absolute url from apache pointing to the static folder
  STATIC_ROOT = '/var/www/html/handleUsers'
- test the application

## make sure the correct user is running the files
- nano /etc/apache2/envars
  look for APACHE_RUN_USER and APACHE_RUN_GROUP to know which user and group you need to abilitate as owners (probably www-data)
- cd where the db is
  cd /var/www/html/utenti/handleUsers
- sudo chown www-data:www-data db.sqlite3
- sudo chmod +rwx db.sqlite3
- cd to the enclosing folder and change owner there too
  cd ..
  sudo chown www-data:www-data handleUsers
  sudo chmod +rwx handleUsers
- service apache2 restart
### WARNING !
### changing the owner to www-data gives an error when you try to move files with ftp that uses another user (es: nodeweaver)
### upload everything, then change the owner, then use just the copy on the server and remember to use VScode on the server copy
### ENJOY :)


## connect vs to ubuntu remotely
- F1, then select Remote-SSH connect to host
- username@host.ip.xxx.xx
- select OS
- enter password
- click on open folder and go to /var/www/html/YOUR_FOLDER_HERE















### SUDO UPDATE ERRORS
- check the date is correct
  -- timedatectl status (check status)
  -- sudo timedatectl set-ntp true (abilitate ntp synch)
  - per modificare manualmente data e ora disabilitare il synch ntp e poi impostare manualmente: 
  -- sudo timedatectl set-ntp false
  -- sudo timedatectl set-time 'Y:M:D HH:mm:ss'
- Software and udpates > Download from main server (change the server for updates)
- ** IF INTERNET NAVIGATION WORKS BUT YOU CAN'T UPDATE** 
  set proxy for apt-get (different than general proxy - UBUNTU VERSION)
  -- sudo nano /etc/apt/apt.conf.d/80proxy
     Acquire::http::proxy "http://10.10.1.10:8080/";
     Acquire::https::proxy "https://10.10.1.10:8080/";
     Acquire::ftp::proxy "ftp://10.10.1.10:8080/";

https://computingforgeeks.com/how-to-set-system-wide-proxy-on-ubuntu-debian/


### Sub-process /usr/bin/dpkg returned an error code (1)
- if the error is on install-info check etc/environment, it's likely its a grammar error there
- otherwise look here https://itsfoss.com/dpkg-returned-an-error-code-1/


### AH00558: Could not reliably determine the server's fully qualified domain name
- sudo nano /etc/apache2/apache2.conf
- Add at the end of file
  ServerName 127.0.0.1
- sudo apachectl configtest (answer should be Syntax OK)
- service apache2 restart

### LOG ERRORS
- tail -f /var/log/apache2/error.log