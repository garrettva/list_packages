#!/usr/bin/env python3
from list_packages.helpers import InstalledRpms
from list_packages.helpers import InstalledModules
from list_packages.helpers import InstalledDebs
from shutil import which
import json


class CombinedList:
    """Combines RPM and Python modules list and creates a CSV or JSON string"""
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_csv_str(self, packages):
        csv_str = ",".join(list(packages[0].keys())) + "\n"
        for package in packages:
            csv_str += ",".join(package.values()) + "\n"
        return csv_str


    def fetch(self):
        """Returns selected lists combined"""
        output_list = []
        output_format = ""
        if self.json == True:
            self.csv = False
            output_format = "json"
        if self.csv != False:
            if self.json != False:
                raise Exception("CSV and JSON output is mutually exclusive.")
            output_format = "csv"
        my_modules = InstalledModules()
        output_list = my_modules.list_modules()
        if which('rpm'):
            my_rpms = InstalledRpms()
            output_list += my_rpms.list_rpms()
        if which('apt-cache'):
            my_debs = InstalledDebs()
            output_list += my_debs.list_debs()        
        if output_format == "json":
            str_out = json.dumps(output_list, indent=4)
        else:
            str_out = self.to_csv_str(output_list)
        return str_out
