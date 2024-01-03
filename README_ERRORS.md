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



## ERROR attempt to write a readonly database (SQLITE)
- permission might be setted wrong, check both the sqlite db and the folder enclosing it, they have to have all permissions with the right user
- cd /var/www/html/utenti/handleUsers
- chmod +rwx db.sqlite3



DJANGO ERRORS

*** WITH ERROR NotImplementedError: Database objects do not implement truth value testing or bool(). Please compare with None instead: database is not None ***
- pymongo version might be wrong, use 3.12.1
  pip uninstall pymongo
  pip install --proxy=http://proxy-bc-el.regione.fvg.it:801 pymongo==3.12.1

*** WITH ERROR cannot be of type "<class \'django.db.models.fields.BigAutoField\'>" ***
- If it's a mega object with nested objects defined as models, remember to add abstract = True to the Meta class, wich means that djongo won't create a new "table" for the model just include the field where you embedded them
- it's best to reset the DB and migrate again by
  -- in migration folder KEEP __init__.py and delete all the other files
  -- python manage.py makepigrations
  -- python manage.py migrate

*** WITH CORS ERROR - Access to XMLHttpRequest at 'url’' from origin  has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource ***


*** WITH CSS NOT LOADING ***
- https://learndjango.com/tutorials/django-static-files
- https://docs.djangoproject.com/en/4.0/howto/static-files/

*** GIT NOT PUSHING ***
- chek if the proxy is setted with 
  git config --list
- if it's not setted to id 
  git config --global http.proxy http://proxyuser:proxypwd@proxy.server.com:8080


*** API ERROR ***
*** Expected a list of items but got type bytes ***
- add json.loads to the django view to turn bytes into a readable json data 
  data = json.loads(request.body)
- It might be that you're sending a list [] instead of an object {}. Check that in front end. 
- If you want to send a list and see this error update serializer adding (many=True) - SEE README_DJANGO.MD




*** Runserver not working because django model cant be found *** 
Recreate virtual environmente
- Delete old venv
  rm -r /var/www/html/hallway_be/venv
- Recreate new venv
  cd /var/www/html/hallway_be
  python3 -m venv venv
- activate venv
  source /var/www/html/hallway_be/venv/bin/activate
- check if django is installed with
  pip list
- if it's not installed run
  pip install --proxy=http://proxy-bc-el.regione.fvg.it:801 django 
- if there are still problems re-install everything
  pip install --proxy=http://proxy-bc-el.regione.fvg.it:801 -r requirements.txt


- check django version
  python -m django --version

- check if django version works outside venv
- if it works chec PYTHONPATH, with
  echo $PYTHONPATH
- if PYTHONPATH is empty it might need to be setted in a parmenent way modifying the config file. Check wich shell is being used with
  echo $SHELL
- if answer is /bin/bash then the shell is bash and to modify the config file type 
  nano ~/.bashrc
- to modify the PYTHONPATH you need to know the path to python (enter the venv folder, lib and then ls, that should be it) 
- at the end of file you have to add the next line with PYTHON3.10 or 11 or whatever instead  
  export PYTHONPATH=/var/www/html/hallway_be/hallway_be/venv/lib/python3.10/site-packages:$PYTHONPATH
- apply changes with
  source ~/.bashrc

