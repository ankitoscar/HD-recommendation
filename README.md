# Airbnb New User Booking project

![Airbnb.png](https://ichef.bbci.co.uk/news/800/cpsprodpb/B38D/production/_109556954_airbnb.png)

This is a ML-based project which tracks a users details and predicts what will be the most preferred destination of the user. It takes data like age, gender, date when the account is created and where they saw the marketing and predicts what will be the preferred destination of the user.

    The objectives of this project:
  - See how user behaviour predicts their preferred destination
  - Learning how to make end-to-end web based ML project

# Features

  - Although the project is still incomplete, we intend to have live prediction for any user entering their data.
  - We also aspire to add some features to make sure the prediction seem more accurate to user.


# Data

  - The data is taken from the [competition organised by Airbnb on kaggle](https://www.kaggle.com/c/airbnb-recruiting-new-user-bookings), which as data regarding various users and their activities on the Airbnb website and apps, using which we have to track which country is their preferred destination.
  - The data used assumes that all the users are from the United States of America.
  -  The countries among the preferred destinations are  'US', 'FR', 'CA', 'GB', 'ES', 'IT', 'PT', 'NL','DE', 'AU', 'NDF' (no destination found), and 'other'.
  -   Please note that 'NDF' is different from 'other' because 'other' means there was a booking, but is to a country not included in the list, while 'NDF' means there wasn't a booking.
  
### The files in the data set and their features are:
   

- train_users.csv - the training set of users
- test_users.csv - the test set of users:
    - id: user id
    - date_account_created: the date of account creation
    - timestamp_first_active: timestamp of the first activity, note that it can be earlier    than date_account_created or date_first_booking because a user can search before signing up
    - date_first_booking: date of first booking
    - gender
    - age
    - signup_method
    - signup_flow: the page a user came to signup up from
    - language: international language preference
    - affiliate_channel: what kind of paid marketing
    - affiliate_provider: where the marketing is e.g. google, craigslist, other
    - first_affiliate_tracked: whats the first marketing the user interacted with before the signing up
    - signup_app
    - first_device_type
    - first_browser
    - country_destination: this is the target variable you are to predict
- sessions.csv - web sessions log for users
    - user_id: to be joined with the column 'id' in users table
    - action
    - action_type
    - action_detail
    - device_type
    - secs_elapsed
- countries.csv - summary statistics of destination countries in this dataset and their locations
- age_gender_bkts.csv - summary statistics of users' age group, gender, country of destination
- sample_submission.csv - correct format for submitting your predictions

The data can be found at this [link.](https://www.kaggle.com/c/airbnb-recruiting-new-user-bookings/data)


### Tech

The libraries and frameworks used in this project till now are:

* [Pandas](https://pandas.pydata.org/) - Used for data analysis
* [NumPy](https://numpy.org/) - Awesome mathematical library for python
* [Matplotlib](https://matplotlib.org/) - For data visualization.
* [Scikit-learn](https://scikit-learn.org/) - For implementing ML algorithms.
* [Xg-boost](https://xgboost.readthedocs.io/) - For implementing boosted algorithms.
* [Jupyter](https://jupyter.org/) - For making python notebook.
* [Flask](https://flask.palletsprojects.com/) - For making web application.


In future we will add more features, hence other tech used in the project will be also mentioned.

### Todos

 - Improve the model.
 - Create an interactive UI and build a real-time prediction mechanism.

![abnb.png](https://www.esquireme.com/public/styles/full_img/public/images/2019/11/03/airbnb-678x381.jpg?itok=y2zwacRr)
## Contributors

- [Siddharth Sharma](github.com/pao0318)
- [Ankit Oscar Xalxo](github.com/ankitoscar)
- [Tanishq Dubey](github.com/tanishq12442)
- [Biplov Pokhrel](githu.com/)

### Versions:

- 1.0 - Only some basic files, will add more files and attach UI images soon in future.


License
----

MIT


**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
