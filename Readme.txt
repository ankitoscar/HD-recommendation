On the part of the webpage:
The following things are accomplished till now:
-A basic home-page
-A signup page to create the account of the user with different parameters that help to create a datasaet for us to analyze
-A SQL database to store the data from the signup page
-A result page which at the moment says nothing but is mae to display the result of destinations



Things yet to be done:
-A login page to actually login the singed up user 
-Adding the login manager feature to have the data of current user from the data live on the webpage
-Converting the daaataset from the db to the format of training dataset (EASY PART)
-Adding the ML part (DEBUGGING HARD)
-BETTER FRONTEND UI

Expolanation of files:
run.py --> used to run the flask wepage
__init__.py --> main file after packaging
forms.py --> forms defined for input of the user for signup/signin
routes.py --> defined routes to different URLS
database.db --> SQL database

templates -->
	_formhelpers.html --> valid/invaid helpers i created 
	home.html --> homepage
	layout.html --> basic layout for all pages
	result.html --> destination result page
	signin.html and signup.html --> logina nd signup pages respectively
static -->
	FRONTEND STUFF  like css and images.
