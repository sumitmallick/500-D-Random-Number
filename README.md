# Generate Random Number

### SETUP
$ git clone https://github.com/sumitmallick/500-D-Random-Number
$ cd randomNumber
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python main.py
```

* For requests using httpie: *[https://httpie.io/]()*
* For requests using curl: *[https://curl.haxx.se/download.html]()*

> __Example user, admin and super admin users are created in database initializer class. You can use these users to login, logout and data handlers. For register handler, use new user information, otherwise returns already exist user.__


| Test Users        | Email Address           | Password  |
| ------------- |:-------------:| -----:|
| User      | test_email@example.com | test_password |
| Admin      | admin_email@example.com      |   admin_password |
| Super Admin | sa_email@example.com      |    sa_password |

#### Register:

* HTTPIE Request:
```sh
http POST :5000/v1/auth/register username=example_username password=example_password email=example@example.com
```
* Curl Request:
```sh
curl -H "Content-Type: application/json" --data '{"username":"example_name","password":"example_password", "email":"example@example.com"}' http://localhost:5000/v1/auth/register
```

#### Login:
* HTTPIE Request:
```sh
http POST :5000/v1/auth/login email=example@example.com password=example_password
```
* Curl Request:
```sh
curl -H "Content-Type: application/json" --data '{"email":"example@example.com", "password":"example_password"}' http://localhost:5000/v1/auth/login
```

> Response: Got access token and refresh token!


#### Logout:
* HTTPIE Request:
```sh
http POST :5000/v1/auth/logout Authorization:"Bearer ACCESS_TOKEN" refresh_token=REFRESH_TOKEN
```
* Curl Request:
```sh
curl -H "Content-Type: application/json" -H "Authorization: Bearer ACCESS_TOKEN" --data '{"refresh_token":"REFRESH_TOKEN"}' http://localhost:5000/v1/auth/logout
```

#### Reset Password:
* HTTPIE Request:
```sh
http POST :5000/v1/auth/password_reset Authorization:"Bearer ACCESS_TOKEN" old_pass=<OLD-PASSWORD> new_pass=<NEW-PASSWORD>
```
* Curl Request:
```sh
curl -H "Content-Type: application/json" -H "Authorization: Bearer ACCESS_TOKEN" --data '{"old_pass":"OLD-PASSWORD", "new_pass":"NEW-PASSWORD"}' http://localhost:5000/v1/auth/password_reset
```


>__There are some example routes in UserHandlers file. These handlers mostly return only text. To use them:__


#### Example routes that require authentication
Route addresses according to user privileges 
| User Type        | Route Address           |
| ------------- |:-------------:|
| User      | /data_user |
| Admin      | /data_admin      |
| Super Admin | /data_super_admin      |

* HTTPIE Request:
```sh
http GET :5000/<ROUTE-ADDRESS> Authorization:"Bearer ACCESS_TOKEN"
```
* Curl Request:
```sh
curl -H "Content-Type: application/json" -H "Authorization: Bearer ACCESS_TOKEN" http://localhost:5000/<ROUTE-ADDRESS>
```

#### Super admin requiring authentication extra example handler, list users
This handler searches username, email or creation dates (range) in users table and returns information these users to super admin.
* HTTPIE Request:
```sh
http GET :5000/users Authorization:"Bearer ACCESS_TOKEN" usernames==test_username,admin_username emails==test_email@example.com,admin_email@example.com start_date==01.01.1990 end_date==01.01.2050
```
* Curl Request:
```sh
curl -X GET 'localhost:5000/users?usernames=test_username,admin_username&emails=test_email@example.com,admin_email@example.com&start_date=01.01.1990&end_date=01.01.2050' -H "Content-Type: application/json" -H "Authorization: Bearer ACCESS_TOKEN" 
```

#### Generate Random Number API with User Authentication

* HTTPIE Request:
```sh
http GET http://localhost:5000/generate_random_number Accept:'*/*' Authorization:'Bearer ACCESS_TOKEN'
```

* Curl Request:
```sh
curl  -X GET 'http://localhost:5000/generate_random_number' --header 'Accept: */*' --header 'Authorization: Bearer ACCESS_TOKEN'
```

#### Possible Improvements:

* Addition of Swagger Docs
* Addition of test case of random number generator
* Addition of user generated random number saving
* As per the user who authenticated the api by saving 
a new relation of user and it's generated numbers list 
we can retrieve it from the db itself but then in that 
case that generation will not always be random
* Addition of cache management is also a possibility
* Better project structure with controllers/routes and services/handlers and BO with DTO
* Improved authentication and time out handling

