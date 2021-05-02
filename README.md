## About:

  This is a simple flask app that has two functionalities :
      1. create text snippet with expiration and return URL
      2. the user can use the returned URL to retrieve the text snippet within its expiration time
      3. return 404 not found if expired/current time at request is greater than the expiration timestamp
      3. the text snippets are saved to file (sqlite is a filetype db)



##  dependencies:

1. This project needs you to use:  Python 3.9.2



.


##  setup:

 **TODO:  in future we will include a setup.py file that does that for you**



#### All the dependent libraries are listed in requirements.txt file. please install libraies with following command:
    
   `pip install requirements.txt`

#### setup sqlite file DB
   `flask initdb`  	

#### setup ssl cert openssl

    ` openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365`

#### Run the following steps to get the webserver  started (the webserver starts at http://127.0.0.1:5000)

   `flask run --cert=cert.pem --key=key.pem` 





## API:

1. '/snippets' :   create_snippet (POST Only)


2. '/snippets/<name> get_snippet (GET)


3. '/' welcome page




## TODO:

1. implement setup.py file that sets up libs and initializes the db
2. https ssl certify
3. comments and explanation



## dependencies explanation:

 1. chosed Flask because it is lightweight webserver. For our usecase we dont have much heavy lifting so flask makes perfect sense.

 2. Couldn't implement SSL certify in time. But installed openssl as part of dependencies and the webserver should be able to start if passed the arguments --certify

 3. This way it could handle https requests. 

 4. Chose sqllite because it is lightweight and can be easily created (single file) and teardown. For our simple use case this makes sense
    And python comes with default sqlite3 library
 





 



