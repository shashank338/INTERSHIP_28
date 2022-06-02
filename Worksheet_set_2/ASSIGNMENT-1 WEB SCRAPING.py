#!/usr/bin/env python
# coding: utf-8

# # 1.Write a python program to display all the header tags from wikipedia.org.
# 
# 
# 

# In[31]:


from bs4 import BeautifulSoup
import requests
import pandas as pd

# Here we checked respone found ok 
page = requests.get("https://en.wikipedia.org/wiki/Main_Page")
page 

# Here we get page content of all webpage
soup = BeautifulSoup(page.content)
soup

header_tags = []# empty list for store the L
for i in soup.find_all("span",class_="mw-headline"):
    header_tags.append(i.text)
header_tags

# Crearing the dataframe
df=pd.DataFrame({'HEADER TAGS':header_tags})
df.index +=1
df


# # 2.Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of release)and make data frame.

# In[2]:


from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get('https://www.imdb.com/chart/top/')
page   #checked web page response range
soup = BeautifulSoup(page.content)
soup

movie_titles = []# empty list for store the 
for i in soup.find_all('td',class_="titleColumn"):
    movie_titles.append(i.text.replace('\n',''))
movie_titles

movie_ratings = []# empty list for store the 
for i in soup.find_all('strong'):
    movie_ratings.append(i.text)
movie_ratings

year_relese = []# empty list for store the 
for i in soup.find_all('span',class_="secondaryInfo"):
    year_relese.append(i.text)
year_relese

df3=pd.DataFrame({'MOVIE RATINGS':movie_ratings,'YEAR OF RELESE':year_relese})# Creating the dataFrame 
df3
df1=pd.DataFrame({'TITLES':movie_titles})#Here movie titles made dataframe due to remove unwanted characteristics from movie_titles
df1
df1=df1['TITLES'].str.extract(r'([A-Za-z]+(?: [A-Za-z]+)*)')#Here removed unwanted characteristics from movie_titles 
df1
df2 = df1.set_axis(['TITLES'], axis=1, inplace=False)#Here changed the header after removed  characteristics from movie_titles 
df2
df4=df2.join(df3)# after joins the dataframe2 to dataframe3 +
df4              # the out put got 
df5=df4.iloc[:100]
df5.index +=1 # Here the final DataFrame output shows
df5


# # 3.Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. name, rating, year of release) and make data frame.

# In[52]:


from bs4 import BeautifulSoup
import requests as reqs
import pandas as pd
from itertools import chain
page = requests.get('https://www.imdb.com/india/top-rated-indian-movies/')
page
soup = BeautifulSoup(page.content)
soup     #checked web page response range

movie_titles = []# empty list for store the 
for i in soup.find_all('td',class_="titleColumn"):
    movie_titles.append(i.text.strip())
    
movie_titles

movie_ratings=[]# empty list for store the 
for i in soup.find_all('strong'):
    movie_ratings.append(i.text)

movie_ratings

year_relese = []# empty list for store the 
for i in soup.find_all('span',class_="secondaryInfo"):
    year_relese.append(i.text)

year_relese

df3=pd.DataFrame({'MOVIE RATINGS':movie_ratings,'YEAR OF RELESE':year_relese})
df3

df1=pd.DataFrame({'TITLES':movie_titles})#Here movie titles made dataframe due to remove unwanted characteristics from movie_titles
df1
df1=df1['TITLES'].str.extract(r'([A-Za-z]+(?: [A-Za-z]+)*)')#Here removed unwanted characteristics from movie_titles 
df1
df2 = df1.set_axis(['TITLES'], axis=1, inplace=False)#Here changed the header after removed  characteristics from movie_titles 
df2
df4=df2.join(df3)# after joins the dataframe2 to dataframe3 
df4              # the out put got 
df5=df4.iloc[:100]
df5.index+=1
df5          # Here the final DataFrame output shows


# # 4.Write s python program to display list of respected former presidents of India(i.e. Name , Term of office)
# from https://presidentofindia.nic.in/former-presidents.htm

# In[5]:


from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get('https://presidentofindia.nic.in/former-presidents.htm')
page    # Here we checked respone found ok
soup = BeautifulSoup(page.content)
soup

presidents_name = []# empty list for store the 
for i in soup.find_all('h3'):
    presidents_name.append(i.text.replace('values',''))
    
presidents_name
term_office = []# empty list for store the 
for i in soup.find_all('p'):
    term_office.append(i.text)
    
term_office
#creating the dataframe 
df=pd.DataFrame({'TERM OF OFFICE':term_office})
df

df1 = df.drop(df.index[[1, 3,5,16,17,18]])# Here we dropout the unwanted in term of office 
df1
df1 = df1.reset_index(drop=True)# index reset done due to dataframe joining purpose 
df1
#creating the dataframe
df2=pd.DataFrame({'PRESIDENTS NAME':presidents_name})
df2

df3=df2.join(df1)#here joins the two dataframe
df3.index +=1
df3 # The final dataframe shows 


# # 5) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:
# 

# # a.Top 10 ODI teams in men’s cricket along with the records for matches, points and rating1

# In[64]:


from bs4 import BeautifulSoup # Here improted necessary libraries 
import requests
import pandas as pd

def ODI_TEAMS(url):
    teams=[]
    matches=[]
    points=[]
    ratings=[]
    odi_team_page=requests.get(url)
    odi_team_soup=BeautifulSoup(odi_team_page.content,'html.parser')
    
    odi_team=odi_team_soup.find_all('span',class_='u-hide-phablet')
    for i in odi_team:
        teams.append(i.text)
    teams=teams[:10]
    
    # here table showing diffrent and seperatly so extratcing required content
    # both are seperalty extracted 
    
    match_row1=odi_team_soup.find_all('td',class_='rankings-block__banner--matches')
    
    for i in match_row1:
        matches.append(i.text)

               
    # another row 
    match_row2=odi_team_soup.find_all('td',class_='table-body__cell u-center-text')
    for i in range(0,len(match_row2),2):
        matches.append(match_row2[i].text)
    matches=matches[:10]
    
    
    # the point also top and other rows is in diffrent 
    odi_point1=odi_team_soup.find_all('td',class_='rankings-block__banner--points')
    
    for i in odi_point1:
        points.append(i.text)
        
    # here the another table points 
    odi_point2=odi_team_soup.find_all('td',class_='table-body__cell u-center-text')
    for i in range(1,len(match_row2),2):
        points.append(odi_point2[i].text)
        points=points[:10]
    
    # the ratings also top and other rows is in diffrent 
    odi_rating=odi_team_soup.find_all('td',class_='rankings-block__banner--rating u-text-right')
    for i in odi_rating:
        ratings.append(i.text.replace('\n','').replace(' ',''))
    
    # here the another table ratings
    odi_rating=odi_team_soup.find_all('td',class_='table-body__cell u-text-right rating')
    for i in odi_rating:
        ratings.append(i.text.replace('\n','').replace(' ',''))
        ratings=ratings[:10]
    
    teams_odi=pd.DataFrame({})
    teams_odi['TEAMS']=teams
    teams_odi['MATCHS']=matches
    teams_odi['POINTS']=points
    teams_odi['RATINGS']=ratings
    return(teams_odi)

ODI_TEAM_MEN=ODI_TEAMS('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')
ODI_TEAM_MEN.index+=1
ODI_TEAM_MEN
 # The final DataFrame shows


# # b.Top 10 ODI Batsmen along with the records of their team and rating.

# In[65]:


from bs4 import BeautifulSoup # Here improted necessary libraries
import requests
import pandas as pd

def ODI_BATSMEN(url):
    players=[]
    teams=[]
    ratings=[]
    batsmen_page=requests.get(url)
    batsmen_soup=BeautifulSoup(batsmen_page.content,'html.parser')
    
    # here taken first row from table 
    odi_player=batsmen_soup.find_all('div',class_='rankings-block__banner--name-large')
    for i in odi_player:
        players.append(i.text)
    
    # Another row table
    odi_player=batsmen_soup.find_all('td',class_='table-body__cell rankings-table__name name')
    for i in odi_player:
        players.append(i.find('a').text)
    players=players[:10]
    
    # here taken first row from table 
    odi_team=batsmen_soup.find_all('div',class_='rankings-block__banner--nationality')
    for i in odi_team:
        teams.append(i.text.replace('\n',''))
        
      # Another row table
    odi_team=batsmen_soup.find_all('span',class_='table-body__logo-text')
    for i in odi_team:
        teams.append(i.text.replace('\n',''))
    teams=teams[:10]
    
    # First Row of the table# here taken first row from table 
    odi_rating=batsmen_soup.find_all('div',class_='rankings-block__banner--rating')
    for i in odi_rating:
        ratings.append(i.text)
        
    # Another row table
    odi_rating=batsmen_soup.find_all('td',class_='table-body__cell rating')
    for i in odi_rating:
        ratings.append(i.text)
    ratings=ratings[:10]
    
    batsmen_odi=pd.DataFrame({})
    batsmen_odi['PLAYERS']=players
    batsmen_odi['TEAMS']=teams
    batsmen_odi['RATINGS']=ratings
    return(batsmen_odi)


TOP_ODI_BATSMEN=ODI_BATSMEN('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting')
TOP_ODI_BATSMEN.index+=1
TOP_ODI_BATSMEN   # The final DataFrame shows


# # c.Top 10 ODI bowlers along with the records of their team and rating.

# In[66]:


from bs4 import BeautifulSoup # Here improted necessary libraries
import requests
import pandas as pd

def ODI_BOWLER(url):
    players=[]
    teams=[]
    ratings=[]
    bowler_page=requests.get(url)
    bowler_soup=BeautifulSoup(bowler_page.content,'html.parser')
    
    # here taken first row from table 
    odi_player=bowler_soup.find_all('div',class_='rankings-block__banner--name-large')
    for i in odi_player:
        players.append(i.text)
    
    # Another row table
    odi_player=bowler_soup.find_all('td',class_='table-body__cell rankings-table__name name')
    for i in odi_player:
        players.append(i.find('a').text)
    players=players[:10]
    
    # here taken first row from table 
    odi_team=bowler_soup.find_all('div',class_='rankings-block__banner--nationality')
    for i in odi_team:
        teams.append(i.text.replace('\n',''))
        
    #  Another row table
    odi_team=bowler_soup.find_all('span',class_='table-body__logo-text')
    for i in odi_team:
        teams.append(i.text.replace('\n',''))
    teams=teams[:10]
    
    # here taken first row from table 
    odi_rating=bowler_soup.find_all('div',class_='rankings-block__banner--rating')
    for i in odi_rating:
        ratings.append(i.text)
        
    #  Another row table
    odi_rating=bowler_soup.find_all('td',class_='table-body__cell rating')
    for i in odi_rating:
        ratings.append(i.text)
    ratings=ratings[:10]
    
    bowler_odi=pd.DataFrame({})
    bowler_odi['PLAYERS']=players
    bowler_odi['TEAMS']=teams
    bowler_odi['RATINGS']=ratings
    return(bowler_odi)

TOP_ODI_BOWLER=ODI_BOWLER('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling')
TOP_ODI_BOWLER.index+=1
TOP_ODI_BOWLER  # The final DataFrame shows


# # 6) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:
# 

# # a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.

# In[78]:


from bs4 import BeautifulSoup # Here improted necessary libraries
import requests
import pandas as pd

def ODI_WOMEN_TEAM(url):
    teams=[]
    matches=[]
    points=[]
    ratings=[]
    odi_team_page=requests.get(url)
    odi_team_soup=BeautifulSoup(odi_team_page.content,'html.parser')
    
    odi_team=odi_team_soup.find_all('span',class_='u-hide-phablet')
    for i in odi_team:
        teams.append(i.text)
    teams=teams[:10]
    
     # here table showing diffrent and seperatly so extratcing required content
     # both are seperalty extracted 
    match_row1=odi_team_soup.find_all('td',class_='rankings-block__banner--matches')
    for i in match_row1:
        matches.append(i.text)

               
    # another rows table
    match_row2=odi_team_soup.find_all('td',class_='table-body__cell u-center-text')
    for i in range(0,len(match_row2),2):
        matches.append(match_row2[i].text)
    matches=matches[:10]

    # here the ponts also in diffrent format and another table also 
    odi_point1=odi_team_soup.find_all('td',class_='rankings-block__banner--points')
    for i in odi_point1:
        points.append(i.text)
        
    odi_point2=odi_team_soup.find_all('td',class_='table-body__cell u-center-text')
    for i in range(1,len(match_row2),2):
        points.append(odi_point2[i].text)
    points=points[:10]
    
    odi_rating=odi_team_soup.find_all('td',class_='rankings-block__banner--rating u-text-right')
    for i in odi_rating:
        ratings.append(i.text.replace('\n','').replace(' ',''))
    
    odi_rating=odi_team_soup.find_all('td',class_='table-body__cell u-text-right rating')
    for i in odi_rating:
        ratings.append(i.text.replace('\n','').replace(' ',''))
    ratings=ratings[:10]
    
    
    
    teams_odi=pd.DataFrame({})
    teams_odi['TEAMS']=teams
    teams_odi['MATCHS']=matches
    teams_odi['POINTS']=points
    teams_odi['RATINGS']=ratings
    return(teams_odi)
ODI_TEAM_WOMEN=ODI_WOMEN_TEAM('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')
ODI_TEAM_WOMEN.index+=1
ODI_TEAM_WOMEN   # The final DataFrame shows


# # b.Top 10 women’s ODI Batting players along with the records of their team and rating.

# In[89]:


from bs4 import BeautifulSoup # Here improted necessary libraries
import requests
import pandas as pd

def ODI_WOMEN_PLAYER(url):
    players=[]
    teams=[]
    ratings=[]
    batsmen_page=requests.get(url)
    batsmen_soup=BeautifulSoup(batsmen_page.content,'html.parser')
    
    # here taken first row from table
    odi_player=batsmen_soup.find_all('div',class_='rankings-block__banner--name-large')
    for i in odi_player:
        players.append(i.text)
    
    
    # Another row table
    odi_player=batsmen_soup.find_all('td',class_='table-body__cell rankings-table__name name')
    for i in odi_player:
        players.append(i.find('a').text)
    players=players[:10]
    
    # here taken first row from table
    odi_team=batsmen_soup.find_all('div',class_='rankings-block__banner--nationality')
    for i in odi_team:
        teams.append(i.text.replace('\n',''))
        
    # Another row table
    odi_team=batsmen_soup.find_all('span',class_='table-body__logo-text')
    for i in odi_team:
        teams.append(i.text.replace('\n',''))
    teams=teams[:10]
    
    # here taken first row from table
    odi_rating=batsmen_soup.find_all('div',class_='rankings-block__banner--rating')
    for i in odi_rating:
        ratings.append(i.text)
        
   # Another row table
    odi_rating=batsmen_soup.find_all('td',class_='table-body__cell rating')
    for i in odi_rating:
        ratings.append(i.text)
    ratings=ratings[:10]
    
    
    
    batsmen_odi=pd.DataFrame({})
    batsmen_odi['PLAYERS']=players
    batsmen_odi['TEAMS']=teams
    batsmen_odi['RATINGS']=ratings
    return(batsmen_odi)
TOP_ODI_BATSMEN=ODI_WOMEN_PLAYER('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting')
TOP_ODI_BATSMEN.index+=1
TOP_ODI_BATSMEN   # The final DataFrame shows


# # c.Top 10 women’s ODI all-rounder along with the records of their team and rating.

# In[88]:


from bs4 import BeautifulSoup # Here improted necessary libraries
import requests
import pandas as pd

def ODI_WOMEN_ALLROUNDER_PLAYER(url):
    players=[]
    teams=[]
    ratings=[]
    bowler_page=requests.get(url)
    bowler_soup=BeautifulSoup(bowler_page.content,'html.parser')
    
   # here taken first row from table
    odi_player=bowler_soup.find_all('div',class_='rankings-block__banner--name-large')
    for i in odi_player:
        players.append(i.text)
    
     # Another row table
    odi_player=bowler_soup.find_all('td',class_='table-body__cell rankings-table__name name')
    for i in odi_player:
        players.append(i.find('a').text)
    players=players[:10]
    
    # here taken first row from table
    odi_team=bowler_soup.find_all('div',class_='rankings-block__banner--nationality')
    for i in odi_team:
        teams.append(i.text.replace('\n',''))
        
      # Another row table
    odi_team=bowler_soup.find_all('span',class_='table-body__logo-text')
    for i in odi_team:
        teams.append(i.text.replace('\n',''))
    teams=teams[:10]
    
    # here taken first row from table
    odi_rating=bowler_soup.find_all('div',class_='rankings-block__banner--rating')
    for i in odi_rating:
        ratings.append(i.text)
        
     # Another row table
    odi_rating=bowler_soup.find_all('td',class_='table-body__cell rating')
    for i in odi_rating:
        ratings.append(i.text)
    ratings=ratings[:10]
    
    
    
    bowler_odi=pd.DataFrame({})
    bowler_odi['PLAYERS']=players
    bowler_odi['TEAMS']=teams
    bowler_odi['RATINGS']=ratings
    return(bowler_odi)
ODI_WOMEN_ALLROUNDER_PLAYER=ODI_WOMEN_ALLROUNDER_PLAYER('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder')
ODI_WOMEN_ALLROUNDER_PLAYER.index+=1
ODI_WOMEN_ALLROUNDER_PLAYER  # The final DataFrame shows


# # 7) Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world :
# i) Headline
# ii) Time
# iii) News Link

# In[87]:


from bs4 import BeautifulSoup   # Here improted necessary libraries
import requests
import pandas as pd

page = requests.get('https://www.cnbc.com/world/?region=world')
page 
soup = BeautifulSoup(page.content)
soup

# scrape data for latest news headline
news = []
for i in soup.find_all("a",class_="LatestNews-headline"):
    news.append(i.text.replace('\n',''))

# scrape data for time of headline
time = []
for i in soup.find_all("time",class_="LatestNews-timestamp"):
    time.append(i.text.replace('\n',''))

# scrape data for news link
link = []
for i in soup.find_all("a",class_="LatestNews-headline"):
    link.append(i['href'])
    
# display news | time | news link
for val in range(0,len(news)):
    print(val+1,news[val],'|',time[val],'\n',link[val],'\n')
db_news = pd.DataFrame({'NEWS TITLE':news,'TIME':time,'NEWS LINK':link})# Creating the dataframe 
db_news.index +=1
db_news      # The final DataFrame shows


# # 8) Write a python program to scrape the details of most downloaded articles from AI in last 90 days.
# https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles
# 
# Scrape below mentioned details :
# i) Paper Title
# ii) Authors
# iii) Published Date
# iv) Paper URL

# In[90]:


from bs4 import BeautifulSoup # Here improted necessary libraries
import requests
import pandas as pd

page = requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')
page #checked web page response range

soup = BeautifulSoup(page.content)
soup

paper_title = []# empty list for store the 
for i in soup.find_all('h2',class_="sc-1qrq3sd-1 MKjKb sc-1nmom32-0 sc-1nmom32-1 hqhUYH ebTA-dR"):
     paper_title.append(i.text)
    
paper_title

authors = []# empty list for store the 
for i in soup.find_all('span',class_="sc-1w3fpd7-0 pgLAT"):
     authors.append(i.text)
    
authors 

published_date = []# empty list for store the 
for i in soup.find_all('span',class_="sc-1thf9ly-2 bKddwo"):
     published_date.append(i.text)
    
published_date

links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))

links

df=pd.DataFrame({'LINKS':links})# Here links dataframe done due to removing the unwanted links
df
v=df.iloc[48:] # unwanted links are removed from links
v
df2=v.iloc[:25]   # unwanted links are removed from links
df2
df2 = df2.reset_index(drop=True)#Here index of the link made reset starts from 0
df2
df1=pd.DataFrame({'PAPER TITLE':paper_title,'AUTHORS':authors,'PUBLISHED DATE':published_date })
df1
df3=df1.join(df2)# after joins the dataframe1 to dataframe2 the final dataframe
df3.index +=1
df3    # The final DataFrame shows


# # 9) Write a python program to scrape mentioned details from dineout.co.in :
# i) Restaurant name
# ii) Cuisine
# iii) Location
# iv) Ratings
# v) Image URL

# In[115]:


from bs4 import BeautifulSoup # Here improted necessary libraries
import requests
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
  
def DINE_OUT(x):

#   requesting the url
    page= requests.get(x)

    soup=BeautifulSoup(page.content)
    
# empty list to store data
    cusine=[]
    name=[]
    location=[]
    rating=[]
    z=[]
    rank=[]
    
#      fetching the required data

    for i in soup.find_all('img',class_="no-img"):
        z.append(i['data-src'])
        
    for i in soup.find_all('div',class_="restnt-loc ellipsis"):
        location.append(i.text)
        
    for i in soup.find_all('a',class_="restnt-name ellipsis"):
        name.append(i.text.split()) 
    
    for l in soup.find_all('span',class_="double-line-ellipsis"):
        cusine.append(l.text.split("|"))
    

    for l in soup.find_all('div',class_="restnt-rating rating-4"):
        rating.append(l.text)
            
    for k in range(1,len(name)+1):
        rank.append(k)
            
    
#     creating the dataframe
    DATA=pd.DataFrame({"S.No":rank,"Retaurant":name,"Cusine":cusine,"Location":location,"Rating":rating,"image":z})
    DATA.set_index('S.No',inplace =True)

    # display the data
    return DATA
DINE_OUT('https://www.dineout.co.in/delhi-restaurants/buffet-special')  # The final DataFrame shows


# # 10) Write a python program to scrape the details of top publications from Google Scholar from
# https://scholar.google.com/citations?view_op=top_venues&hl=en
# 
# i) Rank
# ii) Publication
# iii) h5-index
# iv) h5-median

# In[116]:


from bs4 import BeautifulSoup # Here improted necessary libraries
import requests
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
  

def PUBLICATION(x):

#   requesting the url
    page= requests.get(x)

    soup=BeautifulSoup(page.content)
    
# empty list to store data
    rank=[]
    publication=[]
    h5_index=[]
    h5_median=[]
    obj=[]

#     fetching the required data

    for i in soup.find_all('td',class_="gsc_mvt_t"):
        publication.append(i.text)
        
    for i in soup.find_all('td',class_="gsc_mvt_p"):
        rank.append(i.text)
        
    for i in soup.find_all('a',class_="gs_ibl gsc_mp_anchor"):
        h5_index.append(i.text)
    
    for i in soup.find_all('span',class_="gs_ibl gsc_mp_anchor"):
        h5_median.append(i.text)
    
    import pandas as pd
#     creating a dataframe
    DATA=pd.DataFrame({"RANK":rank,"PUBLICATION":publication,"H5-INDEX":h5_index,"H5-MEDIAN":h5_median})
    
    DATA.set_index('RANK',inplace =True)
    

    
#     display the data
    return DATA

PUBLICATION('https://scholar.google.com/citations?view_op=top_venues&hl=en')# The final DataFrame shows


# In[ ]:





# In[ ]:





# In[ ]:




