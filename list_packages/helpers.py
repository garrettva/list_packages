#!/usr/bin/env python3
from datetime import datetime
from subprocess import check_output
import time
import os
import pkg_resources
import re
from shutil import which
if which("apt-cache") != None:
    import apt


class InstalledRpms:
    """Returns list of installed RPMs with timestamps"""
    def list_rpms(self):
        out = (
            check_output(["rpm -qa --last"], shell=True)
            .decode("utf-8")
            .strip()
            .split("\n")
        )
        packages = []
        for x in out:
            if len(x) > 1:
                package = {}
                dt_string = ""
                diced = x.split()
                split_up = re.split('-(\d+)', diced.pop(0), maxsplit = 1)
                package["name"] = split_up.pop(0)
                ver_str = ''.join(split_up)
                package["version"] = re.split('\.\D', ver_str)[0]
                ver_str
                dt_string = " ".join(diced)
                dt = datetime.strptime(dt_string, "%a %d %b %Y %I:%M:%S %p %Z")
                package["type"] = "rpm"
                package["installed_on"] = str(dt)
                packages.append(package)
        return packages
    

class InstalledDebs:
    """Returns list of installed Debian packages with timestamps"""
    def list_debs(self):
        cache = apt.Cache()
        dir_path = r'/var/lib/dpkg/info/'
        packages = []
        for mypkg in cache:
            package = {}
            if mypkg.is_installed:
                if os.path.isfile("/var/lib/dpkg/info/" + mypkg.name + ":" + mypkg.architecture() + ".list"):
                    list_file = "/var/lib/dpkg/info/" + mypkg.name + ":" + mypkg.architecture() + ".list"
                elif os.path.isfile("/var/lib/dpkg/info/" + mypkg.name + '.list'):
                    list_file = "/var/lib/dpkg/info/" + mypkg.name + ".list"
                else:
                    raise Exception('Could not find .list file')
                timestamp = str(
                    datetime.strptime(
                    time.ctime(os.path.getctime(list_file)),
                        "%a %b %d %H:%M:%S %Y",
                ))
                name_version = mypkg.installed
                package["name"], package["version"] = str(name_version).split("=")
                package["type"] = "deb"
                package["installed_on"] = timestamp
                packages.append(package)
        return packages
        


class InstalledModules:
    def list_modules(self):
        """Returns list of installed python modules with timestamps"""
        python_modules = []
        dists = [d for d in pkg_resources.working_set]
        for package in dists:
            python_module = {}
            python_module["name"], python_module["version"] = str(package).split(" ")
            python_module["type"] = "python_module"
            python_module["installed_on"] = str(
                datetime.strptime(
                    time.ctime(os.path.getctime(package.location)),
                    "%a %b %d %H:%M:%S %Y",
                )
            )
            python_modules.append(python_module)
        return python_modules
