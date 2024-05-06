# Create a Python script that performs the following:

# Prompt the user to type a string input as the variable for your destination URL.

# Prompt the user to select a HTTP Method of the following options:
# GET
# POST
# PUT
# DELETE
# HEAD
# PATCH
# OPTIONS
# Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.
# Add some comments of what these request are doing to your script
# Using the requests library, perform a GET request to your github.

# For the given header, translate the codes into plain terms that print to the screen; for example, a 404 error should print Site not found to the terminal instead of 404.
#response = requests.get()
# For the given URL, print response header information to the screen.
from urllib import response
import requests
b = input("Get, Post, Put, Delete , Head, Patch, Options:\n")
if b == "Get":
    response = requests.get("https://github.com")
    print(response)
    print("ok, the command was successful")
elif b == "Post":
    response = requests.post("https://espn.com")
    print(response)
    print("Forbidden Error")
elif b == "Put":
    response = requests.put("https://espn.com")
    print(response)
    print("Forbidden Request")
elif b == "Delete":
    response = requests.delete("https://espn.com")
    print(response)
    print("Forbidden Error")
elif b == "Patch":
    response = requests.patch("https://espn.com")
    print(response)   
    print("Forbidden Error") 
elif b =="Head":
    response = requests.head("https://github.com/Aingargiola/Learning-github-")
    print(response)
    print("OK, the command was successful")
elif b == "Options":
    response = requests.options("https://github.com/Aingargiola/Learning-github-")
    print(response)
    print("Site not found")
else:
    print("input error")
