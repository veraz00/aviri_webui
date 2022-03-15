
from ast import Param
from flask import render_template, url_for, redirect , request, current_app, flash
from flask_login import current_user, login_required
from . import image_up
from app.extensions import db
import os 
from werkzeug.utils import secure_filename
import requests
from PIL import Image
import json
import base64
from io import BytesIO
import shutil
from app.forms import PredictionForm

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'tiff', 'dicom', 'bmp', 'tif'])
API_URI = 'http://192.168.50.239:5050/api/v1/image'  # un der the same network\; LAN
API_PREDICTION = 'http://192.168.50.239:5050/api/v1/prediction' 
API_HEATMAP = 'http://192.168.50.239:5050/api/v1/heatmap' 
headers = {
        'Content-Type': 'application/json'
    }



def image_to_str(img):  # img is RGB
	buffered = BytesIO()
	img.save(buffered, format="JPEG")
	img_byte = buffered.getvalue() # bytes
	img_base64 = base64.b64encode(img_byte) #Base64-encoded bytes * not str
	#It's still bytes so json.Convert to str to dumps(Because the json element does not support bytes type)
	img_str = img_base64.decode('utf-8') # str
	return img_str

def write_as_heatmap(str, name):
	data = base64.b64decode(str)
	f = open(os.path.join(current_app.config['HEATMAP_FOLDER'], name), 'wb')
	f.write(data)
	f.close()


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@image_up.route('/', methods=['GET', 'POST'])  
def upload_image():
	if request.method == 'POST':
		if 'file' not in request.files:
			flash('No file part')
			return redirect(url_for('image_up.upload_image'))
		file = request.files['file']
		if file.filename == '':
			flash('No image selected for uploading')
			return redirect(url_for('image_up.upload_image'))
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))  # build database to do image management
	#print('upload_image filename: ' + filename)
			

			## send file into back 
			img = Image.open(os.path.join(current_app.config['UPLOAD_FOLDER'], filename)).convert('RGB')
			#Convert Pillow Image to bytes and then to base64
			buffered = BytesIO()
			img.save(buffered, format="JPEG")
			img_byte = buffered.getvalue() # bytes
			img_base64 = base64.b64encode(img_byte) #Base64-encoded bytes * not str
			#It's still bytes so json.Convert to str to dumps(Because the json element does not support bytes type)
			img_str = img_base64.decode('utf-8') # str
			data = {"filename": filename, "content":img_str}  # content: base64 str
			response = requests.post(API_URI, json=data, headers = headers)  
			if response.status_code == 200:
				id = response.json()['id']
				print('id: ', id)  
				flash('Image successfully uploaded and displayed below')
				return render_template('image_up/home.html', filename=filename, id = id) 
			else:
				errorMsg = response.json()['errorMsg']
				flash(errorMsg)
				print(response.json())
		else: 
			flash('Allowed image types are - png, jpg, jpeg, gif')
			return redirect(url_for('image_up.upload_image'))
	return render_template('image_up/home.html')

@image_up.route('/display/<subdir>/<filename>')
def display_image(subdir, filename):
#print('display_image filename: ' + filename)
	print('url_dispaly', url_for('static', filename=f'{subdir}/{filename}'))
	return redirect(url_for('static', filename=f'{subdir}/{filename}'), code=301)

@image_up.route('/prediction', methods = ['GET', 'POST'])
def get_prediction():
	form = PredictionForm()
	# if request.method == 'POST':  # GET HEATMAP-- 
	if form.validate_on_submit():  # if it is 'Post'
		id = form.image_id.data
		model_name= form.model_name.data

		prediction = requests.get(API_PREDICTION + f'/{id}/{model_name}').json()
		print('prediction:', prediction)
		heatmap_str = requests.get(API_HEATMAP + f'/download/{prediction["heatmap_name_id"]}').json()
		write_as_heatmap( heatmap_str['heatmap_content'], prediction['heatmap_name'])
		filename = secure_filename(prediction['heatmap_name'])
		print('filename', filename)
		return render_template('image_up/prediction.html', prediction = prediction, filename = filename) 
	else:
		return render_template('image_up/prediction.html', form = form)	

# "filename": "111_tyj_Retina_OD_20220124_150803_6000.png", 
#   "filename_id": "8a4164bf437c4bafafa2d7df9a18f239", 
#   "heatmap_name": "111_tyj_Retina_OD_20220124_150803_6000_heatmap.jpg", 
#   "heatmap_name_id": "f4033591ff664951bc6b205d35e351c0", 
#   "model_name": "VI_CNN", 
#   "probability_VI0": 0.048641374073796984, 
#   "result": "1", 
#   "timestamp": "2022-03-07-14:22:59"

# get the heatmap; 
# show it and downlaod



