set FLASK_APP=manager
python -m flask run 

# init database
python -m flask db init
python -m flask db migrate -m "Admin" 
python -m flask db upgrade

# add admmin

https://download-directory.github.io/
googl chome
https://www.youtube.com/watch?v=6lL5ijLEoZg


API_URI = 'http://192.168.50.170:5050/api/v1/image'
headers = {'Content-Type': 'application/json'}

## image - get
	# r = requests.get('http://192.168.50.170:5050/api/v1/home')
	# print(r.text)

	# r = requests.get(API_URI + '/2aa7ccd5f7334ead90c5170ae62ceca2')
	# print(r.json())
	
	# payload = {'id': '2aa7ccd5f7334ead90c5170ae62ceca2'}
	# r = requests.get(API_URI, params = payload)
	# print(r.json())

	# image: download??
	# r = requests.get(API_URI + 'download/6307b4f63f2d47b8be4cc1d1b8f79fa6/wer_retina_os_20222222_111123.jpg')
	# path = 'D:\\zenglinlin\\flask_example\\linlin-front\\app\\static\\downloads'
	# if r.status_code == 200:
	# 	with open(path, 'wb') as f:
	# 		r.raw.decode_content = True
	# 		shutil.copyfileobj(r.raw, f)  

## image post
    # data = {"filename": filename, "content":img_str}
    # response = requests.post(API_URI, json=data, headers = headers) 
    # if response.status_code == 200:
    # 	id = response.json()['id']
    # 	print('id: ', id)
    # else:
    # 	print(response.json())


## image patch 
			# id = '6dbdc84decaa4e45be967cbd0cbac038'
			# data = {"content":img_str}
			# response = requests.patch(API_URI + '/' + id, json=data, headers = headers) 
			# if response.status_code == 200:
			# 	print('reponse.text', response.text) 
			# 	print('response.url', response.url)
			# else:
			# 	print(response.json())

## image delete
	# id = '6dbdc84decaa4e45be967cbd0cbac038'
	# response = requests.delete(API_URI + '/' + id)
	# print('response.status_code', response.status_code)

# prediction 

git rm -r --cached app/static/uploads


http://cde.peru21.pe/ima/0/0/0/9/3/93726.jpg
http://jsfiddle.net/jcE8f/
https://jsbin.com/xisocucehu/edit?html,js,output
