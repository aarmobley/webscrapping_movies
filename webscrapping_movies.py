# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 15:46:13 2023

@author: Aaron Mobley
"""
#import data

from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib
import pandas as pd
import csv
#webscrapping


URL = 'https://editorial.rottentomatoes.com/guide/rt25-critics-top-movies-of-the-last-25-years/?utm_campaign=mb&utm_medium=newsletter&utm_source=morning_brew'

#user agent can be found at https://httpbin.org/get
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

page = requests.get(URL, headers=headers)

#get html and parse html
soup1 = BeautifulSoup(page.content, 'html.parser')

#make html pretty
soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')
soup2



#for loop to get movie titles

movie_titles = soup2.find_all('a', href=lambda href: href and 'rottentomatoes.com/m/' in href)

for movie_title in movie_titles:
    title = movie_title.text.strip()
    print(title)
    
#for loop to get movie ratings and store them in a list
#create empty list named ratings

ratings = []
movie_ratings = soup2.find_all('span', 'tMeterScore')

for movie_rating in movie_ratings:
    rating = movie_rating.text.strip()
    ratings.append(rating)
    
 
#for loop to get directors and create empty list to store directors in
directors = []
movie_directors = soup2.find_all('a', href=lambda href: href and 'rottentomatoes.com/celebrity/' in href)

for movie_director in movie_directors:
     director = movie_director.text.strip() 
     directors.append(director)
#could only grab directors with all the actors
     
'''
for getting the year we needed to use a more explicit approach using the 
'select' method. find_all was not getting any results
create empty year list to store movie year in
'''
year = []
movie_years = soup2.select('span.subtle.start-year')

for movie_year in movie_years:
    years = movie_year.text.strip()
    year.append(years)
    






#need to pass an index in order to move on
raw_data={
 'movie_title':movie_title}

dataframe = pd.DataFrame(raw_data, columns=['movie_title'])
dataframe.to_csv('raw_data.csv', index=False)


