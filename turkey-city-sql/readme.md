# Python Application to Retrieve and Save All Provinces and Counties in Turkey

This Python application retrieves data from the turkiyeapi.herokuapp.com API to get all provinces and counties in Turkey. The data is then processed and saved into two separate text files: cities.txt and counties.txt.

# Prerequests

* Python 3.x
* requests library (You can install it using pip install requests)

1. Clone the Repository:

If this is part of a repository, clone it using:

bash
into adp_dev_dsp.counties
git clone <repository-url>
Install Required Libraries:

2. Run the following command to install the required libraries:

bash

pip install requests
Usage

3. Run the Python Script: Execute the script using the following command:

bash

python script_name.py
This script will fetch all provinces and counties in Turkey from the turkiyeapi.herokuapp.com API.

# Output:

The provinces (cities) will be saved in cities.txt, with each line containing the city's name, code, whether it is a metropolitan area, and the region it belongs to.
The counties will be saved in counties.txt, with each line containing the county code, the corresponding city code, and the county's name.

# Example
Here’s a brief breakdown of what each file will contain:

cities.txt:

graphql

Istanbul, 1, True, Marmara
Ankara, 2, True, İç Anadolu
Izmir, 3, True, Ege
...
counties.txt:

yaml

0101, 1, Beşiktaş
0102, 1, Kadıköy
0201, 2, Çankaya
...

# Error Handling
The script assumes the API is accessible and responds with valid JSON data. If there are network issues or problems with the API, make sure to include appropriate error handling or log messages to debug.

# Notes
Ensure you have a stable internet connection as the data is fetched in real-time from the API.
Modify the file paths in the script if you want to save the files in a different directory.

# License
This project is licensed under the MIT License - see the LICENSE file for details.
