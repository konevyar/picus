# Picus
Social media app, written in Python, based on Django.

## Picus ##
### Description: ###
Picus is an Instagram-like social network that allows users to post pictures accompanied by text, subscribe to other users, get likes and see recommendations. Each user can have a userpic and a bio. Only authorized users can read posts.

Picus is built using Django framework and open source page templates, tailored to the needs of the application.

## Project start: ##

### 1. Clone the repository: ###

    git clone https://github.com/konevyar/Picus.git

### 2. Go to project directory: ###
    cd Picus

### 3. Create and activate a virtual environment: ###
    python3 -m venv venv

###### on Windows
    source venv/Scripts/activate

###### on Mac/Linux
    source venv/bin/activate

### 4. Install dependencies from the requirements.txt file: ###
    pip install -r requirements.txt
  
### Make migration: ###
    python3 manage.py migrate

### Start project: ###
    python3 manage.py runserver
