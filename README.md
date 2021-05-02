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

#### Run the following steps to get the webserver  started (the webserver starts at http://127.0.0.1:5000)

   `flask run` 





## API:

1. '/snippets' :   create_snippet (POST Only)


2. '/snippets/<name> get_snippet (GET)


3. '/' welcome page




## TODO:

1. implement setup.py file that sets up libs and initializes the db
2. https ssl certify
3. comments and explanation




 



