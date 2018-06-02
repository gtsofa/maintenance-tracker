
[![Build Status](https://travis-ci.org/gtsofa/maintenance-tracker.svg?branch=ft-crud-api-endpoints)](https://travis-ci.org/gtsofa/maintenance-tracker)

# maintenance-tracker

##### Introduction
Maintenance Tracker App is an application that provides users with the ability to reach out to operations or repairs department regarding repair or maintenance requests and monitor the status of their request.

##### The Interface
[Home Page](https://gtsofa.github.io/maintenance-tracker/UI/index.html)

[User Sign Up Page](https://gtsofa.github.io/maintenance-tracker/UI/sign_up.html)

[User Sign in Page](https://gtsofa.github.io/maintenance-tracker/UI/sign_in.html)


##### Requirements
Before getting started ensure you have the following step up on your local environment.
A working virtual environment
python 2.7 or higher

##### Installation
Clone the repository into your local environment 
$ git clone https://github.com/gtsofa/maintenance-tracker.git 
Change into the project folder maintenance-tracker by $ cd maintenance-tracker
Create a virtual environment $ virtualenv virtualenv-name
Activate your virtual environment by $ source <virtualenv-name>/bin/activate
Install the project dependencies by
pip install -r requirements.txt
Launch the application by running $ python run.py

##### Run The Tests
$ nosetests --with-coverage

The API Endpoints

Users Endpoints
POST /api/v1/auth/register Creates a user account
POST /api/v1/auth/signin Logs in a user
POST /api/v1/auth/signout Logs out a user
PUT /api/v1/auth/reset-password Resets a user password

Requests Endpoints
POST /maintenance_tracker/api/v1/requests Creates a new request
GET /maintenance_tracker/api/v1/requests List all logged in user requests
GET /maintenance_tracker/api/v1/requests/<request-Id>List a request that belongs to a logged in user
PUT /maintenance_tracker/api/v1/requests<request-Id> Edit a user request
DELETE /maintenance_tracker/api/v1/requests<request-Id> Removes a user request

