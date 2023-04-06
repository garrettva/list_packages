import unittest
import json
from list_packages import CombinedList
from list_packages import InstalledRpms
from list_packages import InstalledModules


class TestListPackages(unittest.TestCase):
    def test_helper_rpms(self):
        my_rpms = InstalledRpms()
        rpm_list = my_rpms.list_rpms()
        self.assertIn("name", rpm_list[0].keys())
        self.assertIn("version", rpm_list[0].keys())

    def test_helper_modules(self):
        my_modules = InstalledModules()
        rpm_list = my_modules.list_modules()
        self.assertIn("name", rpm_list[0].keys())
        self.assertIn("version", rpm_list[0].keys())

    def test_rpms_csv(self):
        args = {
            "json": False,
            "csv": True,
            "rpms_only": True,
            "python_only": False,
            "all": True,
            "output_file": None,
            "silent": False,
        }
        pkgs = CombinedList(**args)
        my_pkgs = pkgs.fetch()
        self.assertIn("name", my_pkgs)
        self.assertIn("version", my_pkgs)

    def test_rpms_json(self):
        args = {
            "json": True,
            "csv": False,
            "rpms_only": True,
            "python_only": False,
            "all": True,
            "output_file": None,
            "silent": False,
        }
        pkgs = CombinedList(**args)
        my_pkgs = pkgs.fetch()
        self.assertIn("name", json.loads(my_pkgs)[0].keys())
        self.assertIn("version", json.loads(my_pkgs)[0].keys())

    def test_modules_csv(self):
        args = {
            "json": False,
            "csv": True,
            "rpms_only": False,
            "python_only": True,
            "all": True,
            "output_file": None,
            "silent": False,
        }
        pkgs = CombinedList(**args)
        my_pkgs = pkgs.fetch()
        self.assertIn("name", my_pkgs)
        self.assertIn("version", my_pkgs)

    def test_modules_json(self):
        args = {
            "json": True,
            "csv": False,
            "rpms_only": False,
            "python_only": True,
            "all": True,
            "output_file": None,
            "silent": False,
        }
        pkgs = CombinedList(**args)
        my_pkgs = pkgs.fetch()
        self.assertIn("name", json.loads(my_pkgs)[0].keys())
        self.assertIn("version", json.loads(my_pkgs)[0].keys())

    def test_combined_csv(self):
        args = {
            "json": False,
            "csv": True,
            "rpms_only": False,
            "python_only": False,
            "all": True,
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
            "rpms_only": False,
            "python_only": False,
            "all": True,
            "output_file": None,
            "silent": False,
        }
        pkgs = CombinedList(**args)
        my_pkgs = pkgs.fetch()
        self.assertIn("name", json.loads(my_pkgs)[0].keys())
        self.assertIn("version", json.loads(my_pkgs)[0].keys())


if __name__ == "__main__":
    unittest.main()
