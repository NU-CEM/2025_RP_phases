import os

bands = [6,7,12,13,14,19]
for i in bands:
    for j in range(1,3):
        #os.mkdir('dielectric_%03d_%03d'%(i,j))
        os.chdir('dielectric_%03d_%03d'%(i,j))
        os.system('cp aims.out ../Raman-outfile.%04d.%03d.aims '%(i,j))
        os.system('cp aims.out ../OUTCAR.%04d.%03d '%(i,j))
        #os.system('mv ../Raman-geometry.%04d.%03d.aims geometry.in'%(i,j))
        #os.system('cp ../../dielectric/control.in .')
        os.chdir('../')
