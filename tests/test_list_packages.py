import unittest
import json
from list_packages import CombinedList
from list_packages import InstalledDebs
from list_packages import InstalledRpms
from list_packages import InstalledModules
from shutil import which

class TestListPackages(unittest.TestCase):
    def test_helper_rpms(self):
        if which('rpm') != None:
            my_rpms = InstalledRpms()
            rpm_list = my_rpms.list_rpms()
        else:
            self.skipTest('The rpm utility is not installed.')
        self.assertIn("name", rpm_list[0].keys())
        self.assertIn("version", rpm_list[0].keys())

    def test_helper_modules(self):
        my_modules = InstalledModules()
        module_list = my_modules.list_modules()
        self.assertIn("name", module_list[0].keys())
        self.assertIn("version", module_list[0].keys())
 
    def test_helper_debs(self):
        if which('apt-cache') != None:
            my_debs = InstalledDebs()
            deb_list = my_debs.list_debs()
        else:
            self.skipTest('The apt-cache utility is not installed.')
        self.assertIn("name", deb_list[0].keys())
        self.assertIn("version", deb_list[0].keys())

    def test_combined_csv(self):
        args = {
            "json": False,
            "csv": True,
            "output_file": None,
            "silent": False,
        }
        pkgs = CombinedList(**args)
        my_pkgs = pkgs.fetch()
        self.assertIn("name", my_pkgs)
        self.assertIn("version", my_pkgs)

    def test_combined_json(self):
        args = {
            "json": True,
            "csv": False,
            "output_file": None,
            "silent": False,
        }
        pkgs = CombinedList(**args)
        my_pkgs = pkgs.fetch()
        self.assertIn("name", json.loads(my_pkgs)[0].keys())
        self.assertIn("version", json.loads(my_pkgs)[0].keys())


if __name__ == "__main__":
    unittest.main()
