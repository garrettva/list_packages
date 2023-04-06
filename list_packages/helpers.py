#!/usr/bin/env python3
import pip
from datetime import datetime
from subprocess import check_output
import time
import os


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
                package["name"], package["version"] = diced.pop(0).split("-", 1)
                dt_string = " ".join(diced)
                dt = datetime.strptime(dt_string, "%a %d %b %Y %I:%M:%S %p %Z")
                package["type"] = "rpm"
                package["installed_on"] = str(dt)
                packages.append(package)
        return packages


class InstalledModules:
    def list_modules(self):
        """Returns list of installed python modules with timestamps"""
        python_modules = []
        for package in pip.get_installed_distributions():
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
