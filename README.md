# atx-geocoder
Uses [geocoder](https://pypi.python.org/pypi/geocoder) to access googlemaps api and return address lat/lon. 

Output coordinate system is WGS 1984

Geocode up to 2500 addresses per 24hr period

#### Instructions
1. create a list of Austin street addresses (excluding city/state/zip) with one address per line and save as "addresses.txt" in the same folder as the script
2. run script
3. results are written to geohappy.tab in same folder **WARNING:** this file is overwritten each time the module is run
