=================
Car Hire Management System
=================

-----------------
Development setup
-----------------

#### Create www directory where project sites and environment dir

.. code-block:: bash

    $ mkdir /var/www && mkdir /var/envs && mkdir /var/envs/bin
    
#### Install virtualenvwrapper

.. code-block:: bash

    $ sudo pip3 install virtualenvwrapper
    $ sudo pip3 install --upgrade virtualenv
    
#### Add these to your bashrc virtual env wrapper work

.. code-block:: bash

    export WORKON_HOME=/var/envs
    export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3.8
    export PROJECT_HOME=/var/www
    export VIRTUALENVWRAPPER_HOOK_DIR=/var/envs/bin
    export IS_LOCAL=True
    source /usr/local/bin/virtualenvwrapper.sh
    
#### Create virtualenv

.. code-block:: bash

    $ cd /var/envs && mkvirtualenv car_hire_system --python=/usr/bin/python3.8
    
#### Install requirements for a project.

.. code-block:: bash

    $ cd /var/www/car_hire_sytem && pip install -r requirements.txt

#### Configure DB

.. code-block:: bash

    $ mysql -u <user> -p
    $ CREATE DATABASE car_hire_management
    