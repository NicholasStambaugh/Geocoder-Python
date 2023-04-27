import pandas as pd
from geopy.geocoders import Nominatim

# Initialize Nominatim geocoder
geolocator = Nominatim(user_agent="my-app")

# Read CSV file into a pandas dataframe
df = pd.read_csv("input_file.csv")

# Define the column name that contains the addresses
address_column = "Address"

# Define the column names for latitude and longitude
latitude_column = "Latitude"
longitude_column = "Longitude"

# Define a function to get the latitude and longitude of an address
def get_lat_lon(address):
    location = geolocator.geocode(address)
    if location is None:
        return None, None
    else:
        return location.latitude, location.longitude

# Apply the get_lat_lon function to the address column and create new latitude and longitude columns
df[[latitude_column, longitude_column]] = df[address_column].apply(lambda x: pd.Series(get_lat_lon(x)))

# Write the dataframe with latitude and longitude columns to a new CSV file
df.to_csv("output_file.csv", index=False)
