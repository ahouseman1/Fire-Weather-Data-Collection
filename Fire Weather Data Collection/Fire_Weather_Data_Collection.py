from re import findall
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import os

# Define the URL for the weather page
url = "https://forecast.weather.gov/MapClick.php?w0=t&w3=sfcwind&w3u=1&w4=sky&w5=pop&w6=rh&w13=mhgt&w13u=0&w16u=1&w17u=1&AheadHour=48&FcstType=digital&textField1=37.5334&textField2=-97.6715&site=ict&unit=0&dd=&bw=&BackDay.x=59&BackDay.y=9"

# Make a request to the webpage
response = requests.get(url)
response.raise_for_status()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Get the table from the HTML content
table = soup.table

#iterate to find the fourth table on the page which contains the data we want
for x in range(4):
    table = table.findNext("table")

#create array to store extracted table data
data = []

#store all table rows into rows variable
rows = table.find_all("tr")

#Iterate through rows
for row in rows:
    
    #find data from cells in that row
    cells = row.find_all("td")

    #get text from each cell and strip uneccicary information and store in row data
    row_data = [cell.get_text(strip=True) for cell in cells]

    if row_data:  # Avoid empty rows

        data.append(row_data)

#intitialise exportable data array and date variables
exportableData = []
date = '0/0'

#iterate through hours up to 24 hours
for y in range(1,25):
    #get date as array from array of arrays 
    get_date = data[1]
    #check if date is empty
    if get_date[y] != '':
        date = get_date[y]
    #get time from array of arrays
    get_time = data[2]
    
    #get temperature from array of arrays
    get_temperature = data[3]
    #setup data in row
    temperature = [date, get_time[y],'Temperature', 'degreesF',get_temperature[y]]
    #add data row to exportable data
    exportableData.append(temperature)
    
    #get surface wind from array of arrays
    get_surface_wind = data[4]
    #setup data in row
    surface_wind = [date, get_time[y], 'Surface Wind', 'mph', get_surface_wind[y]]
    #add data row to exportable data
    exportableData.append(surface_wind)
    
    #get wind direction from array of arrays
    get_wind_direction = data[5]
    #check array for empty values and replace them with 'NA'
    for z, value in enumerate(get_wind_direction):
        if value == '':
            get_wind_direction[z] = 'NA'
    #setup data in row
    wind_direction = [date, get_time[y], 'Wind Direction', 'direction', get_wind_direction[y]]
    #add data row to exportable data
    exportableData.append(wind_direction)

    #get gust from array of arrays
    get_gust = data[6]
    #check array for empty values and replac them with '0'
    for a, value in enumerate(get_gust):
        if value == '':
            get_gust[a] = '0'
    #setup data in row
    gust = [date, get_time[y], 'Gust', 'mph', get_gust[y]]
    #add data row to exportable data
    exportableData.append(gust)

    #get sky cover from array of arrays
    get_sky_cover = data[7]
    #setup data in row
    sky_cover = [date, get_time[y], 'Sky Cover', 'pct', get_sky_cover[y]]
    #add data row to exportable data
    exportableData.append(sky_cover)
    
    #get precipitation potential from array of arrays
    get_precipitation_potential = data[8]
    #setup data in row
    precipitation_potential = [date, get_time[y], 'Precipitation Potential', 'pct', get_precipitation_potential[y]]
    #add data row to exportable data
    exportableData.append(precipitation_potential)
    
    #get relative humidity from array of arrays
    get_relative_humidity = data[9]
    #setup data in row
    relative_humidity = [date, get_time[y], 'Relative Humitity', 'pct', get_relative_humidity[y]]
    #add data row to exportable data
    exportableData.append(relative_humidity)
    
    #get mixing height from array of arrays
    get_mixing_height = data[10]
    #setup data in row
    mixing_height = [date, get_time[y], 'Mixing Height', 'x100ft', get_mixing_height[y]]
    #add data row to exportable data
    exportableData.append(mixing_height)
    
print(exportableData)

#Define filename of export file
filename = "Fire Weather Data.csv"
#if file is missing create new file
if not os.path.isfile(filename):
     # Define the column headers
    columns = ["Date", "Hour", "Parameter", "Units", "Value"]
    
    # Create an empty DataFrame with the column headers
    header = pd.DataFrame(columns=columns)
    
    # Save the DataFrame to a CSV file
    header.to_csv(filename, index=False)

#Convert exportable data to pandas dataframe
exportatbleDataframe = pd.DataFrame(exportableData)
#Append dataframe to defined csv file
exportatbleDataframe.to_csv(filename, mode='a', index=False, header=False)