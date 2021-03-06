import json
import csv
import requests
import media
import fresh_tomatoes

# list where the movie object will be stored
movies = []

# Open the list of preferred movies
with open("preferred_movies.csv", 'r') as f:

    # In the lines below, carry a Dict because it is easier to convert to json.
    # Then I do the parse because for me it is much easier to manipulate json data.
    # if I want to save this information in a database as the latest
    # version of Postgres is also easy to do this. Point.

    # Change each fieldname to the appropriate field name.
    reader = csv.DictReader(f, delimiter=';')

    # Parse the CSV into JSON
    out = json.dumps([row for row in reader], sort_keys=True, indent=4, separators=(',', ': '))

    obj = json.loads(out)

    # del null elements
    for el in obj:
        del el['']

    # interate in json object to consume api omdb
    # and create the instances for each movie
    # in prefered_movies.csv
    for i in range(0, len(obj)):
        movie = obj[i]['title']

        # get the title movie and preparing to search on omdb
        for j in movie:
            movie = movie.replace(' ', '+')

        # get information about the movie at OMDB
        response = requests.get("http://www.omdbapi.com/?t="+movie + "&y=&plot=short&r=json")

        # storing the json response in json_data
        json_data = json.loads(response.text)


        # creating the movie object
        # I chose to do it that way because it is better
        # than doing a lot of instance.
        i = media.Movie(json_data['Title'], json_data['Plot'], json_data['Poster'], json_data['Director'],
                        json_data['Actors'],json_data['Released'], obj[i]['link'])

        # It includes the object in the movies list
        movies.append(i)

    f.close()

# opening the fresh tomatoes page
fresh_tomatoes.open_movies_page(movies)
