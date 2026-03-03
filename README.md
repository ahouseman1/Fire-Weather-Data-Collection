#Fire Weather Data Collection

This program collects the Data from the NOAA National Weather Sevice page at: 
https://forecast.weather.gov/MapClick.php?w0=t&w3=sfcwind&w3u=1&w4=sky&w5=pop&w6=rh&w13=mhgt&w13u=0&w16u=1&w17u=1&AheadHour=48&FcstType=digital&textField1=37.5334&textField2=-97.6715&site=ict&unit=0&dd=&bw=&BackDay.x=59&BackDay.y=9
which provides weather data about the conditions surrounding perscribed burns at the Wichita State research station near Viola, KS.

The program then finds the table containing the weather data for the next 24 Hours and stores it to a csv, creating the file if none exists. 
The python libraries used to do this are: Beautiful Soup (which handles interpreting the page html), numpy, and pandas (which handles exporting the data to the csv)

The program is intended to be built with PyInstaller and run daily using a Windows Task Scheduler task that runs each day.

This program was commissioned by Dr. Gregory Houseman at WSU to decide when to perfom perscribed burns.
