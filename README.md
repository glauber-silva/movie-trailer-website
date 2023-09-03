# Movie Trailer Website
Simple project using some modules python to consume an API and set up a simple website with trailers and informations
about my favorite movies.

Project developed for self study.

![CircleCI](https://circleci.com/gh/glauber-silva/movie-trailer-websaite.svg?style=svg)
_______________________________________________________________________________


To execute this project on Linux ( Debian / Ubuntu ), follow this step by step

Run the following command in a directory of your choice.

1 - $ git clone https://github.com/glauber-silva/movie-trailer-website.git

If not installed git, run this command:

$ sudo apt-ger install git

Run the step 1, again:

Install Python3:

2 - $ sudo add-apt-repository ppa:fkrull/deadsnakes

3 - $ sudo apt-get update

4 - $ sudo apt-get install python3.4

Install the 'requests' package needed for this project:

5 - $ sudo python3.4 -m pip install requests

If you have not pip installed, run the following command:

$ sudo apt-get install python3-pip

Run the step 5 again

Finally, run the command to execute the project

6 - $ python3 entertainment_center.py




PS : If you want to change the list of movies. Edit the file preferred_movies.csv replacing existing information there
for other movie names and links to the corresponding trailers on youtube.