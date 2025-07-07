import os
import subprocess
from time import time,sleep

list_dirs = next(os.walk('.'))[1]
list_dirs = [x for x in list_dirs if "phonopy" not in x]
#while not len(list_dirs) == 0:
#	temp_list = list_dirs[:2]
#	temp_list = list_dirs
	#output = subprocess.check_output("squeue -u prakaya", shell=True)
	#print(output)
	#if len(output) == 85:
for i in list_dirs:
	os.chdir(i)
	os.system('pwd')
	if not os.path.exists('aims.out'):
		os.system('cp ../run.slm .')
		os.system('sbatch run.slm')	
	os.chdir('../') 
	#list_dirs = list_dirs[2:]
	#sleep(1200)

