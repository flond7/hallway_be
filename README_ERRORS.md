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