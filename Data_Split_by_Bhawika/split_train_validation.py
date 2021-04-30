import os
from os import path
import sys
import random
import shutil
from shutil import copyfile

def split_data(SOURCE, TRAINING, VALIDATION, TESTING, SPLIT_SIZE):
    files = []
    print('Split Data')
    for filename in os.listdir(SOURCE):
        file = SOURCE +'/'+ filename
        if os.path.getsize(file) > 0:
            files.append(filename)
        else:
            print(filename + " is zero length, so ignoring.")

    training_length = int( len(files)* SPLIT_SIZE)
    validation_length = int(len(files) * 0.10)
    testing_length = int(len(files) - training_length - validation_length)
    
    print('SOURCE: ',SOURCE, '\n TRAINING', TRAINING, '\n VALIDATION',VALIDATION, '\n ',len(files))
    print('training_length:',training_length)
    print('validation_length:',validation_length)
    print('testing_length:',testing_length)
    
    shuffled_set = random.sample(files, len(files))
    training_set = shuffled_set[0:training_length]
    validation_set = shuffled_set[training_length:(training_length+validation_length)]
    testing_set=shuffled_set[:testing_length]

    print(len(training_set))
    print(len(validation_set))
    print(len(testing_set))
    
    for filename in training_set:
        this_file = SOURCE +'/'+ filename
        destination = TRAINING +'/'+ filename
        try:
        	copyfile(this_file, destination)
        except shutil.SameFileError:
        	pass

    for filename in validation_set:
        this_file = SOURCE +'/'+ filename
        destination = VALIDATION+'/' + filename
        try:
        	copyfile(this_file, destination)
        except shutil.SameFileError:
        	pass
        
    for filename in validation_set:
        this_file = SOURCE +'/'+ filename
        destination = TESTING+'/' + filename
        try:
        	copyfile(this_file, destination)
        except shutil.SameFileError:
        	pass
def main():
	try:
		if(len(sys.argv)==0):
			raise Exception("Please Enter Correct no of parameters in the format \n python rajeev_topsis.py <Input Directory> <Train Split>")
	except Exception as e:
		print(e)
		exit(0)
	data_dir=sys.argv[1]
	try:
		if(not path.exists(data_dir)):
			raise Exception("Directory Does Not Exist")
	except Exception as e:
		print(e)
		exit(0)
	try:
		if(len(os.listdir(data_dir))==0):
			raise Exception("Empty Directory")
	except Exception as e:
		print(e)
		exit(0)
	print("Current Path is " ,os.listdir(data_dir))
	classes=os.listdir(data_dir)
	if(data_dir[-1]=='/'):
		data_dir=data_dir[:-1]
	source_path=[f'{data_dir}/{a}' for a in classes]
	classes_dir=[f'{a}_dir' for a in classes]
	try:
	    os.mkdir(f'{data_dir}/training')
	    os.mkdir(f'{data_dir}/validation')
	    os.mkdir(f'{data_dir}/testing')
	except OSError:
	    pass
	TRAINING_PATH=f'{data_dir}/training'
	VALIDATION_PATH=f'{data_dir}/validation'
	training_dir_path=[f'{data_dir}/training/{a}' for a in classes]
	validation_dir_path=[f'{data_dir}/validation/{a}' for a in classes]
	testing_dir_path=[f'{data_dir}/testing/{a}' for a in classes]

	for train_dir_path in training_dir_path:
	    try:
	        os.mkdir(train_dir_path)
	    except OSError:
	        pass
	for val_dir_path in validation_dir_path:
	    try:
	        os.mkdir(val_dir_path)
	    except OSError:
	        pass
	for test_dir_path in testing_dir_path:
	    try:
	        os.mkdir(test_dir_path)
	    except OSError:
	        pass

	split_size = float(sys.argv[2])
	for source,train_dir_path,val_dir_path,test_dir_path in zip(source_path,\
	                                training_dir_path,validation_dir_path, testing_dir_path):
	    split_data(source,train_dir_path,val_dir_path,test_dir_path, split_size)
	    print('Splitting \n')

if __name__ == '__main__':
	main()