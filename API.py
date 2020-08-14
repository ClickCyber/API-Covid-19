from flask import Flask
from covid import Covid
data = Covid()
Country = []
for i in data.list_countries():
    Country.append(i['name'])

apps = Flask('covid')


@apps.route('/')
def main():
    return """<h1>Working</h1><a href='/Help'>Help</a><br><a href='/Country'>Stasus covid</a><br><a href='/list_Country'>list Country covid</a>"""

@apps.route('/list_Country')
def all_Country():
    return "<br>".join(Country)
    
@apps.route('/Country')
def erro_country():
    return 'send parameter "Country&israel"'
    
    
@apps.route('/Country&<get_country>')
def view_country(get_country):
    DataJson = data.get_status_by_country_name(get_country)
    return DataJson
    
@apps.route('/Help')
def help():
    return 'Example:<br>send parameter "Country&israel"<br>No send parameter "/list_Country"'

 
apps.run('127.0.0.1',port=80,debug=True)
