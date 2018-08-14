# API

To run the api, you will need docker-compose v2 installed. Execute:

    docker-compose up

The API is a very basic Django single app project. There are many things left to be done before this api could be deployed correctly:

* Review security settings
* Split settings files into environments
* Read sensitive variables from environment ala twelver-factor
* django-rest-framework would be a good third-party app candidate to build a complex REST API
* Add an app for snapshot testing
* Use class based views
* Add an authentication layer
* Add an authorization layer
...

## Testing it

The API has a really simple test, that makes sure endpoint `phones/` does work. You can run it with:

    docker-compose run api python2 manage.py test
