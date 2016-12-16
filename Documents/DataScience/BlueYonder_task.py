# -*- coding: utf-8 -*-
"""
Spyder Editor
"""

import requests
import os

'''Functions, which are used in the main function'''
# Function, which gets a list of the urls of the plaintext file
def get_urls(plainfile):
    with open(plainfile,"r") as f:           
        line = f.readline()
        
        url_list = list()                                                                     
        
        while line.strip():                                                                                                           
            line = line.replace('\n', '')
            line = line.replace('\r', '')
            url_list.append(line)                                                            
            line = f.readline() 
    return url_list

# Function, which opens the URLs and checks, if they exist and contain an image     
def open_url(url):
    splitted_url = url.split('/')
    try:
        image = requests.get(url)
        content_type = image.headers['Content-type']
        if content_type.find('image') != -1:
            save_image(image,splitted_url[-1])
        else:
            print('The URL %s doesn\'t contain an jpg-image\n' % url)
    except requests.ConnectionError:
        print('The URL %s doesn\'t exist\n' % url)

# Function, which saves the image of each URL in the folder 'Images'            
def save_image(image,imagename):
    if not os.path.exists('./Images'):
        os.makedirs('./Images') 
    Path = './Images/'+imagename
    with open(Path,'wb') as f:
        f.write(image.content)
        
'''Main function'''
# Downloading the images of the plaintext file
def download_image(plainfile):
    url_list = get_urls(plainfile)
    for url in url_list:
        open_url(url)