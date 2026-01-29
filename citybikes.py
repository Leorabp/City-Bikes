"""
API LAB: Calling Real Data from the Internet

GOAL:
Learn how to use an API to get real data from the internet using Python.

An API is just a URL that returns DATA instead of a webpage.
"""

# STEP 1: Choose an API (USE THIS LIST ONLY) 

# Pick ONE API from this list on schoology https://github.com/teacher-aj/public-apis?tab=readme-ov-file#social


# STEP 2: Make an API Call

# Paste the API URL you chose as a STRING below

# Convert the response into Python data (dictionary or list) below

# ALWAYS print the full data first so you can see its structure



# STEP 3: Extract a Piece of Data

# Look at what printed above.
# Find ONE specific value you want to use.

# Examples (yours will be different):

# cat_fact = data["fact"]
# print(cat_fact)

# latitude = data["iss_position"]["latitude"]
# print(latitude)

# write your code here


# STEP 4: Do Something With the Data


# Do ONE of the following:
# - Print it in a sentence
# - Store it in a variable
# - Add it to a list
# - Combine it with text

# Example:
# print(f"The ISS is currently at latitude {latitude}.")


# https://api.citybik.es/v2/

import requests


url = "https://api.citybik.es/v2/networks/citi-bike-nyc"
response = requests.get(url)

data = response.json()

stations = data["network"]["stations"]

total_bikes = 0
for station in stations:
 total_bikes += station["free_bikes"]

print("Total available Citi Bikes in NYC:", total_bikes)

print(f"There are {total_bikes} bikes available in NYC")



