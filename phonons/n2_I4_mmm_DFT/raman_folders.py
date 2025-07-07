import os

bands = [6,7,10,11,17,18,19,20,21,26,27,29,31,34,35]
for i in bands:
    for j in range(1,3):
        #os.mkdir('dielectric_%03d_%03d'%(i,j))
        os.chdir('dielectric_%03d_%03d'%(i,j))
        os.system('cp aims.out ../Raman-outfile.%04d.%03d.aims '%(i,j))
        #os.system('cp ../Raman-geometry.%04d.%03d.aims geometry.in'%(i,j))
        #os.system('cp ../../dielectric/control.in .')
        os.chdir('../')
