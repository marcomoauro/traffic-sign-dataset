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
	txts_size = calculate_txts_size()
	train_files_size = int(float(config['train_perc']) * txts_size)
	data_dir = os.getcwd() + "/data/"
	files = os.listdir(data_dir)
	random.shuffle(files)
	count = 0
	for file in files:
		number, ext = file.split('.')
		if ext == 'jpg':
			continue
		count += 1
		if count <= train_files_size:
			train_files.append(file)
		else:
			test_files.append(file)
	write_file(train_files, 'train.txt')
	write_file(test_files, 'test.txt')

def calculate_txts_size():
	data_dir = os.getcwd() + "/data/"
	txts = os.listdir(data_dir)
	count = 0
	for txt in txts:
		number, ext = txt.split('.')
		if ext == 'jpg':
			continue
		count += 1
	return count

def write_file(files, file_name):
	file_name_path = os.getcwd()+"/data/"+file_name
	with open(file_name_path, 'w') as f:
		for file in files:
			f.write("{0}\n".format(os.getcwd()+"/data/"+file))


create_files()
