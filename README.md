# list_packages
Lists RPM packages and/or Python modules installed on a system, along with their installations date. Output may be in CSV (default) or JSON.

## Installation:
`# python3 setup.py`

## Test
`$ python3 runtests.py`

## Usage Examples
List all installed RPM packages and Python modules. Print to STDOUT in CSV format:

`$ python3 interview_example.py`

List all installed RPM packages and Python modules. Print to STDOUT in JSON:

`$ python3 interview_example.py --json`

List all installed RPM packages only. Print to STDOUT in CSV format:

`$ python3 interview_example.py --rpms_only`

List all installed Python modules only. Print to STDOUT in CSV format:

`$ python3 interview_example.py --python_only`

List all installed RPM packages and Python modules. Print to STDOUT and to text file in JSON:

`$ python3 interview_example.py --json -O packages.json`
