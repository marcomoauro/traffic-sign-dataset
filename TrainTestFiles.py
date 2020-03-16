import os
import json
import random

def create_files():
	hash_config = config()
	files(hash_config)

def config():
	path = os.getcwd()
	config_file_path = str(path) + "/TrainTestFiles.json"
	with open(config_file_path) as json_file:
		return json.load(json_file)

def files(config):
	train_files = []
	test_files = []
	train_files_size = int(float(config['train_perc']) * int(config['txts_size']))
	data_dir = os.getcwd() + "/data/"
	txts = os.listdir(data_dir)
	random.shuffle(txts)
	count = 0
	for txt in txts:
		number, ext = txt.split('.')
		if ext == 'jpg':
			continue
		count += 1
		if count <= train_files_size:
			train_files.append(txt)
		else:
			test_files.append(txt)
	write_file(train_files, 'train.txt')
	write_file(test_files, 'test.txt')

def write_file(files, file_name):
	file_name_path = os.getcwd()+"/data/"+file_name
	with open(file_name_path, 'w') as f:
		for file in files:
			f.write("{0}\n".format(os.getcwd()+"/data/"+file))


create_files()
