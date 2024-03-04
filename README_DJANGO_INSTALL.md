# Configure machine
- Install VS code
- Install GIT from VS code
- In VS terminal set the global proxy as 
  git config --global http.proxy http://proxy-bc-el.regione.fvg.it:801          or 
  git config --global http.proxy http://proxy-bc.regione.fvg.it:8002
- In VS terminal set the global user config 
- Install python 64 (check the last compatible version with this django version wich is 4.1)
- Check python works as a variable using the cmd and 
  python --v
  If it's not working add the python .exe to the system variables in path
- Install pip and add the pip .exe to path (same as python). It's located in the Script directory in python
  C:\Users\XXXXXXXXXXXXXXXXXXXXXXXXX\AppData\Local\Programs\Python\Python311\Scripts
- Install MariaDB
- Install MariaDB and Mysql connectors (mysql just in case, I haven't checked without it)
* open cmd and log in with mysql -u root -pXXXXXXXXXXX (no space for the password)
* CREATE DATABASE db_name;
* CREATE USER user_name@localhost IDENTIFIED BY 'user_password';
* GRANT ALL PRIVILEGES ON db_name.* TO user_name@localhost;

# Retrieve git project and make it run
- Open new window in VS go to the git tab and choose clone repository
- Add the repository and check for windows that might open to ask for credentials or popups (either in the bottom-right corner or up center) that ask for some input in VS
- Let VS register with github and let it download
- don't move from the main directory and create a new venv
  python -m venv name-virtual-environment
- activate the venv
  .\venv\Scripts\activate  (in Windows)
  source venv/bin/activate (in Linux)
- install everything
  pip install -r requirements.txt                                                       or
  pip install --proxy=http://proxy-bc-el.regione.fvg.it:801 -r requirements.txt
- Create the db and run the server to test it
  python manage.py migrate
  python manage.py runserver (just as a test, then CTRL+C)
- Create the superuser and check if it works
  python manage.py createsuperuser (administrator - administrator@localhost.com - com04***)
  python manage.py migrate
  python manage.py runserver http://127.0.0.1:8000/admin/
  
# PROBLEM: mysqlclient install
- https://www.youtube.com/watch?v=JipL3uyoHcw 

# PROBLEM: python not found
- cmd and check python is installed with 
  py --list   (lists all python versions)       or
  python --version
- check system ambient variables, go to system variables, select path and add the path to python.exe (while you're there check for pip too, it's in python/Script and has to be added to path)

# PROBLEM: git connect tunnel failed response 403
Possibly a login issue. Set the global vars to log in and proxy
* git config --global user.email "elisa.utilivenza@gmail.com"
* git config --global user.password "xxxx"
* git config --global user.name "flond7"
* git config --global http.proxy http://proxy-bc-el.regione.fvg.it:801

# PROBLEM: Failed to establish a new connection:
Proxy problem. Check proxy settings in the pc. If the proxy is set from a script hardcode it as a single value. It is possible that the proxy gets resetted everytime you restart the pc (in working context) so be aware of that.

# PROBLEM: ServicePointManager does not support with schema XXXXXXXXXX.
- Most likely the proxy doesn't have the http http://davanti (do not use https, seems to not be working)
  git config --global http.proxy http://xxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# PROBLEM: Could not find a version that satisfies the requirement setuptools>=40.8.0
- check if it is installed with 
  pip show setuptools
- It might happen if you're using an older version of pip, try to update 
  python.exe -m pip install --upgrade pip

# PROBLEM: Could not build wheels for mysqlclient, which is required to install pyproject.toml-based projects
This is actually a problem explained in the lines before the red error. It looks for a MariaDB connector that you have to download from the mariadb website
The key is in the line before:

"C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\MSVC\14.29.30133\bin\HostX86\x64\cl.exe" /c /nologo /O2 /W3 /GL /DNDEBUG /MD -Dversion_info=(2,1,1,'final',0) -D__version__=2.1.1 "-IC:\Program Files\MariaDB\MariaDB Connector C\include\mariadb" "-IC:\Program Files\MariaDB\MariaDB Connector C\include" -IC:\Python312\include -IC:\Python312\Include "-IC:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\MSVC\14.29.30133\include" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.19041.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.19041.0\shared" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.19041.0\um" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.19041.0\winrt" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.19041.0\cppwinrt" /TcMySQLdb/_mysql.c /Fobuild\temp.win-amd64-cpython-312\Release\MySQLdb/_mysql.obj

It means that you have to copy in C:\Program Files\MariaDB\MariaDB Connector C\include\mariadb the contents of C:\Program Files\MariaDB\MariaDB Connector C\include
Be aware that you might have installed the wrong version of the connector (64bit is specified in the folder name while 32bit is not)
If there is no MariaDB Connector C then create it

- If there is no "MariaDB Connector C" folder but the connector has been installed (both 64 and 32 bit versions), then change the name of the existing folder to match qhat the error requires

https://stackoverflow.com/questions/51294268/pip-install-mysqlclient-returns-fatal-error-c1083-cannot-open-file-mysql-h

# PROBLEM: django.core.exceptions.ImproperlyConfigured: Set the DATABASE_NAME environment variable
Temporary fix: hardcode the variables in settings

# PROBLEM: Impossibile trovare il file specificato: 'C:\\Python312\\Scripts\\sqlformat.exe' or Impossibile trovare il file specificato: 'C:\\Python312\\Scripts\\pycodestyle.exe'
- The folder C:\\Python312\\Scripts\\ is a read only. Remove the restriction and it should be fine
- Add --user to the end of the installation command (eg: pip install --proxy=http://proxy-bc.regione.fvg.it:8002 -r requirements.txt --user)


#PROBLEM
- Check if python is 32 o 64 using in cmd
  python -c "import sys; print(sys.maxsize > 2**32)"    (if it's true then it's 32bit)