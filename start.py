from copy import copy
import requests
from bs4 import BeautifulSoup
from flask import Flask
from flask import request

from flask import render_template



app = Flask(__name__, template_folder='.')
page = requests.get(
    "https://nationaltoday.com/today/")
soup = BeautifulSoup(page.content, 'html.parser')

all_a_tags = []

for element in soup.select('a'):
    all_a_tags.append(element.text)
"""
page_with_cats = request.get('https://genrandom.com/cats/')
soup = BeautifulSoup(page_with_cats.content, 'html.parser')

images_of_cat = []

for element in soup.select('img'):
    images_of_cat.append(element.text)

image_of_cat = images_of_cat[0]
print(image_of_cat)
"""

@app.route('/test', methods=['GET'])
def test():
    return 'test'

@app.route('/holiday', methods=['GET'])
def holiday():
    arg = request.args
    player = arg.get('player')
    print(all_a_tags[99], all_a_tags[101], all_a_tags[103]) #+2
    a = ['hi ' + player + ' !!!!!', all_a_tags[99], all_a_tags[101], all_a_tags[103]]
    return render_template('cat_picture.html', name=player, first=all_a_tags[99], second=all_a_tags[101], third=all_a_tags[103])
    #return webbrowser.open_new_tab('cat_picture.html', name=player, first=all_a_tags[99], second=all_a_tags[101], third=all_a_tags[103])
    #return os.startfile('cat_picture.html')
if __name__ == '__main__':
    app.run(port=5001)