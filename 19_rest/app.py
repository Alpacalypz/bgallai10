import requests

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def get_image():
	with open('key_nasa.txt', 'r') as api_file:
		api_key = api_file.readline()[:-1]
	
	webpage = requests.get('https://api.nasa.gov/planetary/apod?api_key=' + api_key)
	
	with open('request.json', 'wb') as request:
		request.write(webpage.content)
	
	with open('request.json', 'r') as request:
		request_str = request.read()
	
	img_desc = request_str.split('","')[1][14:]
	img_title = request_str.split('","')[5][8:]
	img_url = request_str.split('","')[6][6:-3]
	
	return render_template('img.html', title=img_title, img_url=img_url, description=img_desc)

if __name__ == "__main__":
    app.debug = True
    app.run()
