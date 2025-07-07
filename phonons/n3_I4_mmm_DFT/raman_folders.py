import os
#bands =[6,7,8,9,17,18,19,22,23,27,29,30,33,34,35,36,40,44,46,47,51]
bands = [6, 7, 8, 9, 17, 18, 19, 22, 23, 27, 29, 30, 33, 34, 35, 36, 40, 43, 45, 46, 47, 51]
for i in bands:
    for j in range(1,3):
        #os.mkdir('dielectric_%03d_%03d'%(i,j))
        os.chdir('dielectric_%03d_%03d'%(i,j))
        #os.system('mv ../Raman-geometry.%04d.%03d.aims geometry.in'%(i,j))
        os.system('cp aims.out ../Raman-outfile.%04d.%03d.aims '%(i,j))
        os.system('cp aims.out ../OUTCAR.%04d.%03d '%(i,j))
        #os.system('cp ../../dielectric/control.in control.in')
        os.chdir('../')
