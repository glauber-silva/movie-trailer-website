from bottle import route, run, static_file
from src.entertainment_center import ContentService


@route('/')
def main():
    content = ContentService()
    content.create_main_page()
    return static_file('fresh_tomatoes.html', root='.')


run(host="localhost", port=8080, debug=True, reloader=True)
