#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 12:30:51 2023

@author: leo
"""

# Hello! 
# I'm a comment 
# I'm here to help someone who's reading what I wrote to navigate!
# You can use me. And you should!
# Hello!
# I'm a function! You can call me with an argument.
print("Hello students! I'm the argument of the function!")

print("""
        If yo need to write me in multiple lines 
        you can use the triple  quotes!
""")

print('I work with single quotes too!')
print("By, the way! I am a string. You don't believe me? Check this out!\n")
print(type("By, the way! I am a string. You don't believe me? Check this out!\n"))

# Let's do some math

# Addition
print(2+2)

# Subtraction
print(4-2)
print(4+(-2)) # Surprise! Subtraction is sum by the inverse element in the group (R,+). Yeah, I know, mindblowing!
# Notice than when there are multiple, nested function, the compiler will start from the innermost functions up to the outermost.
# This hierachy, known from the high school algebra, is quite usefull to understand how a function works.

# Multiplication
print(3*2)

# Division
print(10/3)

#Hey! Why the five at the end of 3.3(...)35? Because that is the rappresentation of the quantity 10/3 = 3.3... in this enviroment.

# Exponent
print(12 ** 2)
# Notice that the exponent is a repeated multiplication, therefore the right symbol should be **


# Square root of a number
print(16 ** 1/2.)

# Defyning a function

def my_function(x):
  '''
  This is the comment of the function.
  Is usefull for the documentation of you code.
  All the good codes have function comments
  ... but not all codes with function comments are good.
  Anyway this function prints the value of x using formatted string
  and returns 1 if the operation was succesfull!
  '''

  print(f"The value of the argument is: {x}")
  return 1

# Calling the function
my_function(3)

#import (library name)
#import (library name) as (alias)
import numpy as np

# calling modules
my_list = [1,2,3]
np.array(my_list)


# Python ≥3.5 is required
import sys
assert sys.version_info >= (3, 5)

# Scikit-Learn ≥0.20 is required
import sklearn
assert sklearn.__version__ >= "0.20"

# These are surprise tools that will help us later
import numpy as np
import os
import tarfile
import urllib.request
import pandas as pd
import seaborn as sns

# To plot pretty figures
%matplotlib inline
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)

# Where to save the figures
PROJECT_ROOT_DIR = "."
CHAPTER_ID = "end_to_end_project"
IMAGES_PATH = os.path.join(PROJECT_ROOT_DIR, "images", CHAPTER_ID)
os.makedirs(IMAGES_PATH, exist_ok=True)

def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    path = os.path.join(IMAGES_PATH, fig_id + "." + fig_extension)
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)
    
    
DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    # is the folder available? If not create it
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    
    # set the path
    tgz_path = os.path.join(housing_path, "housing.tgz")
    # retrive the data and download it
    urllib.request.urlretrieve(housing_url, tgz_path)

    # open and extract
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close() # it's a good practice to close a file if it is no more necessary

def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)

# Download the data
fetch_housing_data()

# Load the data
housing_data = load_housing_data()

display(housing_data)