import apt
import os
from datetime import datetime
import time
cache = apt.Cache()
dir_path = r'/var/lib/dpkg/info/'
files =  os.listdir(dir_path)

for mypkg in cache:
    if mypkg.is_installed:
        print(mypkg.name)
        print(mypkg.installed)
        print(mypkg.architecture())

        if os.path.isfile("/var/lib/dpkg/info/" + mypkg.name + ':amd64.list'):
#            exit()
#            raise Exception('sdfsdf')
            list_file = "/var/lib/dpkg/info/" + mypkg.name + ":amd64.list"
        elif os.path.isfile("/var/lib/dpkg/info/" + mypkg.name + '.list'):
            list_file = "/var/lib/dpkg/info/" + mypkg.name + ".list"
        else:
            raise Exception('Could not find .list file')
        timestamp = str(
            datetime.strptime(
            time.ctime(os.path.getctime(list_file)),
                "%a %b %d %H:%M:%S %Y",
        ))
        print(timestamp)
            
