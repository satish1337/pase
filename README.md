# pase
django base project template for user and client based applications.
this project is completely REST based.


**Base Setup:** (for ubuntu)

1. Dev tools installations
    * sudo apt-get install build-essential python-dev libevent-dev libxml2-dev libmysqlclient-dev python-setuptools python-pip libpq-dev libxslt1-dev

2. Virtual Env. setup
    * sudo pip install virtualenvwrapper
    * sudo mkdir -p ~/.Envs
    * sudo chmod -R 777 ~/.Envs
    
3. Add these lines to .bashrc
    * export WORKON_HOME=~/.Envs
	* source /usr/local/bin/virtualenvwrapper.sh

4. Install REST framework
	* pip install djangorestframework
    * pip install markdown       # Markdown support for the browsable API.
    * pip install django-filter  # Filtering support

==============================================================================================================

**Setup Steps:**

1. Environment Setup:
       * Create a virtual environment
           * mkvirtualenv pase
       * Install the requirements by running the command:
           * pip install -r **file_name**
               
2. Settings Environment
       * Default setting environment on local machine will always be settings/dev.py
       * Override any kind of setting required to be updated.
       
