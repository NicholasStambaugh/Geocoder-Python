# Geocoding CSV Addresses
This is a simple Python script that uses the geopy library to geocode a CSV file containing addresses and add the latitude and longitude coordinates as new columns.

### Getting Started
To get started, clone the repository and install the dependencies:

```
git clone https://github.com/NicholasStambaugh/Geocoder-Python.git
cd geocoding-csv-addresses
pip install -r requirements.txt
```

### Usage
To use the script, follow these steps:

Place the CSV file containing the addresses in the same directory as the geoconvert.py script.

Open the geoconvert.py script in a text editor and set the appropriate values for the address_column, latitude_column, and longitude_column variables.

Save the changes to the geoconvert.py script.

Run the geoconvert.py script with the following command:

```
python geoconvert.py
```

The script will read the CSV file, geocode the addresses, add the latitude and longitude columns, and write the results to a new CSV file in the same directory.

### Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

### License
MIT
