# azure_command_parsing

_The script for removing old files_

_To use, you must transfer input data (stdin), as well as the parameter you need to specify the number of images that should be left (-q)_

_Installing necessary packages_

_Linux_
* pip3 install -r requirements.txt

_Windows_
* pip install -r requirements.txt 

_Usage example:_

* cat .\data\wide_data.txt | python .\wide_data_parsing.py -q 6 (Windows PowerShell)
* more .\data\wide_data.txt | python .\wide_data_parsing.py -q 6 (Windows CommandPrompt)
* cat data/wide_data.txt | python3 wide_data_parsing.py -q 6 (Linux)

_last 6 images will not be displayed_
