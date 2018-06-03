
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
* A working virtual environment
* python 2.7 or higher


##### Run The Tests
$ nosetests --with-coverage

#### The API Endpoints

### Requests Endpoints

Method | Endpoint | Description
--- | --- | ---
POST | /maintenance_tracker/api/v1/requests | Creates a new request
GET | /maintenance_tracker/api/v1/requests | Lists all requests of a logged in user
GET | /maintenance_tracker/api/v1/requests/request-Id | List a request of a logged in user
PUT | /maintenance_tracker/api/v1/requests/request-Id | Edit a request of a logged in user
DELETE | /maintenance_tracker/api/v1/requests/request-Id | Delete a request of a logged in user


## Testing the EndPoints

Clone the repository into your local environment 

$ git clone https://github.com/gtsofa/maintenance-tracker.git 

Change into the project folder maintenance-tracker  $ cd maintenance-tracker

Create a virtual environment $ virtualenv virtualenv-name

Activate your virtual environment  $ source <virtualenv-name>/bin/activate

Install the project dependencies pip install -r requirements.txt

Launch the application   $ python run.py

Copy and Paste the URL on postman

Test the endpoints by changing  the http methods

## Screenshots 

Registered User
[Registered User](<img src="/designs/img/mockups/users/register_user.png"/>)

Created Request
[Register User](<img src="/designs/img/mockups/requests/request_created.png" />)

Get all Request
[Get all Request](<img src="/designs/img/mockups/requests/get_all_requests.png" />)

Get Request by ID
[Get all Request](<img src="/designs/img/mockups/requests/get_a_request_by_ID.png" />)

Edit a request
[Get all Request](<img src="/designs/img/mockups/requests/edit_request.png" />)

Delete a request
![Get all Request](https://github.com/gtsofa/maintenance-tracker/blob/ft-crud-api-endpoints/designs/UI/img/mockups/requests/after_delete_request.png "Trial text")





