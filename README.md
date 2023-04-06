# list_packages
Lists RPM packages and/or Python modules installed on a system, along with their installations date. Output may be in CSV (default) or JSON.

## Installation:
`$ sudo python3 setup.py`

## Test
`$ python3 runtests.py`

## Usage
<code>usage: python3 interview_example.py [-h] [-j] [-c] [-r] [-p] [-a] [-O OUTPUT_FILE] [-s]
optional arguments:
  -h, --help            show this help message and exit
  -j, --json            Output in JSON format (default: False)
  -c, --csv             Output in CSV format (default: True)
  -r, --rpms_only       Show only RPM packages (default: False)
  -p, --python_only     Show only Python modules (default: False)
  -a, --all             Show both RPM Packages and Python modules (default:
                        True)
  -O OUTPUT_FILE, --output_file OUTPUT_FILE Write results to file (default: None)
  -s, --silent          Suppress STDOUT (see --output_file) (default: False)</code> 
  

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
