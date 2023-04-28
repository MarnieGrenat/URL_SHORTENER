# Author: Gabriela Dellamora Paim
# Version: 2023.04.28

####################################### Imports #######################################
import pyshorteners

type_tiny= pyshorteners.Shortener()
long_url= str(input("Insert your URL to shorten: "))
short_url= type_tiny.tinyurl.short(long_url)
print(f"Your shorten URL is: {short_url}")