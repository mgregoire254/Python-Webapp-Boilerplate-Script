"""
Web App Boilerplate
====================

Description:
------------
A utility to simplify the initialization of Flask projects. The program asks the user for their project
name and then builds the boilerplate file structure.

Developer Information:
----------------------
Name: Michael Gregoire

"""

import os
import shutil
from shutil import Error

# Take user preference input
project_name = input("What is the name of your project? ")
root_path = "./" + project_name

'''Function to create directories'''
def make_directory(path):
    try:
        os.mkdir(path)
        print("Folder %s created!" % path)
    except FileExistsError:
        print("Folder %s already exists" % path)

'''Function to create files'''
def make_file(dir, name, cont, ext):
    n = name + ext
    try:
        with open(n, "w") as file:
            file.writelines([cont])
            file.close()
        print("File %s%s created successfully!" % (name, ext))
    except FileExistsError:
        print("File %s%s already exists" % (name, ext))

    try:
        if dir != "":
            shutil.move(n, dir)
            print("File %s moved to %s", (n, dir))
    except Error as err:
        print("File %s already exists in %s", (n, dir))           

# Create Folder Structure
make_directory(root_path)
make_directory(root_path + "/templates")
make_directory(root_path + "/static")
make_directory(root_path + "/static/images")
make_directory(root_path + "/tests")
  
# Data for files
base = " "
style = " "
app = " "
readme = "#" + project_name

# Create Files
make_file("", "app", app, ".py")
make_file("./stuff/templates", "base", base, ".html")
make_file("./stuff/static", "style", style, ".css")

# Closing message
print("Happy Coding!")

# To Do
# Create virtual environment
# Install dependencies
