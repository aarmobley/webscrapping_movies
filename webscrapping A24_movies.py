# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 18:40:34 2023

@author: Aaron Mobley
"""

#webscrapping A24 Independent movies to see which actor appeares in the most indpendnet films

#Import libraries 
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import csv
import matplotlib.pyplot as plt


URL =  'https://editorial.rottentomatoes.com/guide/all-a24-movies-ranked/'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

soup1 = BeautifulSoup(soup.prettify(), 'html.parser')

#check soup1 html code
soup1

#for loop to grab all movie titles. A lot of emptpy space in html led
#to additional if statement
titles = soup1.find_all('a', href=lambda href: href and 'https://www.rottentomatoes.com/m/' in href)
for title in titles:
    movie_title = title.text.strip()
    if "[More]" in movie_title:
        continue
    movie_title = ' '.join(movie_title.split())
    print(movie_title)
    
#for loop to grab the year
#use select option instead of find_all
years = soup1.select('span.subtle.start-year')
for year in years:
    movie_year = year.text.strip()
    print(movie_year)
    
#for loop to grab acotrs in each movie
actors = soup1.find_all('a', href=lambda href: href and 'rottentomatoes.com/celebrity/' in href)
for actor in actors:
    movie_actor = actor.text.strip()
    print(movie_actor)
    
    
#store title, year and actors in lists
movie_titles2 = []
movie_years = []
movie_actors =[]

#for loop to grab all movie titles
titles = soup1.find_all('a', href=lambda href: href and 'https://www.rottentomatoes.com/m/' in href)
for title in titles:
    movie_title = title.text.strip()
    if "[More]" in movie_title:
        continue
    movie_title = ' '.join(movie_title.split())
    if movie_title:
        movie_titles2.append(movie_title)
    
#for loop to grab the year
#use select option instead of find_all
years = soup1.select('span.subtle.start-year')
for year in years:
    movie_year = year.text.strip()
    movie_years.append(movie_year)
    
#for loop to grab acotrs in each movie
actors = soup1.find_all('a', href=lambda href: href and 'rottentomatoes.com/celebrity/' in href)
for actor in actors:
    movie_actor = actor.text.strip()
    movie_actors.append(movie_actor)
    
    
#write and save actors/directors to csv file
with open(r'C:\Users\Aaron Mobley\Desktop\A24 movies\A24_movies.csv', mode = 'w') as A24_movie:
    movie_writer = csv.writer(A24_movie, delimiter = ',', quotechar = '"',
                              quoting = csv.QUOTE_ALL)
    for i in range (len(movie_actors)):
            movie_writer.writerows([movie_actors[i]])
    
#store in a dataframe
df = pd.DataFrame(movie_actors, columns = ['movie_actor'])

df.value_counts()

#find how many different actors are in A24 moviea and graph which actors appeared in most movies
actor_counts = df['movie_actor'].value_counts()
top_10_actors = actor_counts.head(10)

#bargraph
plt.figure(figsize=(10,8))
plt.bar(top_10_actors.index, top_10_actors.values)
plt.xlabel('Actor')
plt.ylabel('Number of Movies')
plt.title('Number of Movies per Actor')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


