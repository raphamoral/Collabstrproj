![Python](https://img.shields.io/badge/Python-3.10.11-blue)
![Django](https://img.shields.io/badge/Django-5.0.6-green)
![Django REST Framework](https://img.shields.io/badge/Django%20REST%20Framework-3.15.1-red)
# Colabstr Project Test

This README provides instructions to set up and use this test with Pipenv in a Django project on Linux or Windows


Table of Contents

- [Prerequisites](#prerequisites)
-  [Install Pipenv in Linux or Windows](#install-pipenv)
    - [Configure the enviroment variables in Linux](#configure-the-environment-variables-in-linux)
    - [Configure the environment variables in Windows](#windows-installer)
- [Installing the Dependencies](#Insttall-the-dependencies)
- [Start the application](#start)
- [REST APIS and endpoints](#rest-api-and-endpoints)
  - [List of all parts](#list-of-all-parts)
  - [Post one part](#post-one-part)
  - [Update one part](#update-one-part)
  - [Delete one part](#delete-one-part)
  - [Retrieve a specific part](#retrieve-a-specific-part)
  - [Common Words](#get-the-5-most-common-words-in-descriptions)
## Prerequisites

Before you start, ensure you have the following installed on your system:

- Python 3.10.11
- Pip (usually included with Python 3)
- Git (for version control)

## Install Pipenv in Linux or Windows

 Pipenv is the environment for this project.To install Pipenv globally, use the pip command:


``pip install pipenv
``
## Configure the Environment Variables in Linux
You need to add Pipenv to your system's environment variables. Open the terminal and add the following lines to your .bashrc file (located in your home directory):

<br />``export PIPENV_VENV_IN_PROJECT=1 ``
<br />``export PIPENV_IGNORE_VIRTUALENVS=1
``
<br />``export PIPENV_NO_INHERIT=1``

<br /> After that, you should consider to restart you Linux System

## Windows Installer
<br />You should have to install pipenv before start this API
<br />-Clone the repository
<br />Open terminal in folder project and write the command:
<br /> ``pip install pipenv``
<br />Add in your systems variables it to create enviroment in folder project, click in Edit the system Variables if you are using Windows System and If you are using Linux, you have to add this variables to bashrc.
<br />![image](https://user-images.githubusercontent.com/80533929/182413666-2c01c3f7-2e95-42a2-88fc-3f8c6951f5aa.png)
<br />Click on enviroment Variables
<br />![image](https://user-images.githubusercontent.com/80533929/182413835-4aaf8163-e0e5-4e1d-85ec-0ff9673cca7b.png)
<br />Now you can add new varaibles in your system, you can click in New.. and add new system variable.
<br />![image](https://user-images.githubusercontent.com/80533929/182415073-55acab9c-6987-4434-b514-da5a33add382.png)
<br />![image](https://user-images.githubusercontent.com/80533929/182415611-13e113c8-33f2-4517-8493-060f3f4d2895.png)

<br />This is variables you are going to add.


<table>
  <thead>
    <tr>
      <th>Variable</th>
      <th>Value</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>PIPENV_VENV_IN_PROJECT</code></td>
      <td><code>1</code></td>
      <td>Creates virtual environment inside the project</td>
    </tr>
    <tr>
      <td><code>PIPENV_IGNORE_VIRTUALENVS</code></td>
      <td><code>1</code></td>
      <td>Ignores any active virtual environments</td>
    </tr>
    <tr>
      <td><code>PIPENV_NO_INHERIT</code></td>
      <td><code>1</code></td>
      <td>Disables inheritance of environment variables</td>
    </tr>
  </tbody>
</table>

<br />After that, you should have to restart your machine.

# Install the dependencies and libraries

<br /> If you have already a environment in this folder project, please delete it and open terminal in folder project and write the command:

 <br />`pipenv install`

 <br /> Now all libraries are installed for this project.

# Start the application

   <br/>Open the terminal in this directory <i>qventus/qventustestproject</i> .After that, you can this command in your terminal:

<br/>```python manage.py runserver```
