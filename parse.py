# must manually switch between train.json and test.json
import json
import csv
file_list = ['test.json', 'train.json']
train_files = []
test_files = []
for file in file_list:
	string = ''
	if file=='test.json':
		string = '-test'
	else:
		string = '-train'
	with open(file) as data_file:    
	    data = json.load(data_file)
	    for key, value in data.items():
	    	filename = key + string + '.csv'
	    	if string=='-test':
	    		test_files.append(filename)
	    	else:
	    		train_files.append(filename)
	    	with open(filename, 'w') as csvfile:
	    		fieldnames = ['id', key]
	    		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	    		writer.writeheader()
	    		for subkey, subvalue in value.items():
	    			writer.writerow({'id': subkey, key: subvalue})

# print('TRAIN_FILES')
# for tf in train_files:
# 	print(tf,end=', ')
# print('TEST_FILES')
# for tf in test_files:
# 	print(tf, end=',')

df1 = train_files[0]

