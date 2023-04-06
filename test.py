import apt
import os
from datetime import datetime
import time
dir_path = r'/var/lib/dpkg/info/'
packages = []
package = {}
cache = apt.Cache()

print(cache["libusb-1.0-0"].versions)
print('----------------')
for file in os.listdir(dir_path):
    if file.endswith('.list'):
        package["name"] = file.split('.')[0]
        apt_pkg = cache[package["name"]]
        package["installed_on"] = str(
        datetime.strptime(
            time.ctime(os.path.getctime(dir_path + file)),
            "%a %b %d %H:%M:%S %Y",
        ))
        print(package["name"])
        print(max(apt_pkg.versions))
        print(package["installed_on"])


