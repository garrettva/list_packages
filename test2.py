import apt
import os
cache = apt.Cache()
dir_path = r'/var/lib/dpkg/info/'
files =  os.listdir(dir_path)

for mypkg in cache:
    if mypkg.is_installed:
        print(mypkg.name)
        print(mypkg.installed)
        print(mypkg.architecture)

#       for x in mypkg.installed_files:
            #if x.endswith('.list'):
#            print(x)
        if os.path.isfile("/var/lib/dpkg/info/" + mypkg.name + ':amd64.list') or os.path.isfile("/var/lib/dpkg/info/" + mypkg.name + '.list'):
            print('FILE EXISTS!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        else:
            print('NOPE')
        #           print('Exists')

 #       else:
 #           print('DOES NOT EXIST!!!!!!!!!!!!!!!!!!!!')
print('--------------------------')
print(dir(mypkg))

