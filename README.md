# Musical Project

MusicalProject is a single view application that aggregates and reconciles data from multiple sources. In this case a csv file is provided as a source from where the information for musical works and their metadata are read and saved on a PostgresSQL database.


## Project Setup

Musical Project requires Python3.9 and Docker installed beforehand.

Please follow the steps downbelow to continue with project setup:

```sh
git clone https://github.com/sprifti/musicalProject.git
```

Copy the **env** file that I have provided in the folder to the root directory of the project.
Open project on termial and execute the following commands
```sh
docker-compose build
docker-compose up
```

The first command will pull and build the necessary images and containers required for the project. 
The second will start the project and we can see the resuls on http://0.0.0.0:8000/
where we can see three main api's for all three of our models.
{
    "musicalwork": "http://0.0.0.0:8000/musicalwork/",
    "contributors": "http://0.0.0.0:8000/contributors/",
    "musicalcontributors": "http://0.0.0.0:8000/musicalcontributors/"
}
Before clicking on any of the url we must continue with the migrations of our models on the database.

To continue with migrations check the list of the created containers
```sh
docker container ls
```
Get the id of the container named musicalproject_web_1 and execute the following command

```sh
docker exec -it CONTAINER_ID /bin/bash 
```
This command will allow you to get inside the container where we will create and migrate all database changes needed as well as populating our models
Once inside the container please execute the following command:
```sh
./manage.py makemigrations
./manage.py migrate
```

There is a small test we can execute to check if the application is up and running
```sh
./manage.py test
```

Now that we have the changes reflected on the database we can continue with the insert of the data in the database:
```sh
./manage.py ingest_data
```

This command will populate the models and will allow us to browse the information available.

To get the information for a specified "iswc" to fill a report we can use the url in this format:
http://0.0.0.0:8000/musicalwork/?iswc={iswc}
example: http://0.0.0.0:8000/musicalwork/?iswc=T9214745718

Thank you!



