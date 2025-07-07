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
	if os.path.exists('aims.out'):
		outfile = open('aims.out','r')
		lines = outfile.readlines()
		if not 'Have a nice day' in lines[-2]:
			print(lines[-2])
			os.system('cp ../../dielectric/run.slm .')
			os.system('sbatch run.slm')	
	os.chdir('../') 
	#list_dirs = list_dirs[2:]
	#sleep(1200)

