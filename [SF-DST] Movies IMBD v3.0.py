#!/usr/bin/env python
# coding: utf-8

# In[61]:


import numpy as np
import datetime
import pandas as pd
import seaborn as sns
import itertools
import matplotlib.pyplot as plt
import os
import collections
from itertools import combinations
from collections import Counter
print(os.listdir('data'))


# In[62]:


data = pd.read_csv('data.csv')
data.head(5)


# In[63]:


len(data)


# # Предобработка датасета

# In[64]:


answer_ls = [] # создадим список с ответами. сюда будем добавлять ответы по мере прохождения теста
# сюда можем вписать создание новых колонок в датасете


# # 1. У какого фильма из списка самый большой бюджет?
# Варианты ответов:
# 1. The Dark Knight Rises (tt1345836)
# 2. Spider-Man 3 (tt0413300)
# 3. Avengers: Age of Ultron (tt2395427)
# 4. The Warrior's Way	(tt1032751)
# 5. Pirates of the Caribbean: On Stranger Tides (tt1298650)

# In[65]:


data2=data.query('imdb_id in ["tt1345836","tt0413300","tt2395427","tt1032751","tt1298650"]')
data3=data2.query('budget==budget.max()')
display(data3)
answer_ls.append(4)


# # 2. Какой из фильмов самый длительный (в минутах)
# 1. The Lord of the Rings: The Return of the King	(tt0167260)
# 2. Gods and Generals	(tt0279111)
# 3. King Kong	(tt0360717)
# 4. Pearl Harbor	(tt0213149)
# 5. Alexander	(tt0346491)

# In[66]:


data5=data.query('runtime==runtime.max()')
display(data5)
answer_ls.append(2)


# # 3. Какой из фильмов самый короткий (в минутах)
# Варианты ответов:
# 
# 1. Home on the Range	tt0299172
# 2. The Jungle Book 2	tt0283426
# 3. Winnie the Pooh	tt1449283
# 4. Corpse Bride	tt0121164
# 5. Hoodwinked!	tt0443536

# In[67]:


data7=data.query('runtime==runtime.min()')
display(data7)
answer_ls.append(3)


# # 4. Средняя длительность фильма?
# 
# Варианты ответов:
# 1. 115
# 2. 110
# 3. 105
# 4. 120
# 5. 100
# 

# In[68]:


print(round(data.runtime.mean(),0))
answer_ls.append(2)


# # 5. Средняя длительность фильма по медиане?
# Варианты ответов:
# 1. 106
# 2. 112
# 3. 101
# 4. 120
# 5. 115
# 
# 
# 

# In[69]:


print(round(data.runtime.median(),0))
answer_ls.append(1)


# # 6. Какой самый прибыльный фильм?
# Варианты ответов:
# 1. The Avengers	tt0848228
# 2. Minions	tt2293640
# 3. Star Wars: The Force Awakens	tt2488496
# 4. Furious 7	tt2820852
# 5. Avatar	tt0499549

# In[70]:


data['profit'] = data.revenue - data.budget
data9=data.query('profit==profit.max()')
print(data9)
answer_ls.append(5)


# # 7. Какой фильм самый убыточный?
# Варианты ответов:
# 1. Supernova tt0134983
# 2. The Warrior's Way tt1032751
# 3. Flushed Away	tt0424095
# 4. The Adventures of Pluto Nash	tt0180052
# 5. The Lone Ranger	tt1210819

# In[71]:


data['profit'] = data.revenue - data.budget
data9=data.query('profit==profit.min()')
print(data9)
answer_ls.append(2)


# # 8. Сколько всего фильмов в прибыли?
# Варианты ответов:
# 1. 1478
# 2. 1520
# 3. 1241
# 4. 1135
# 5. 1398
# 

# In[72]:


data['profit'] = data.revenue - data.budget
data12=len(data.query('profit>0'))
display(data12)
answer_ls.append(1)


# # 9. Самый прибыльный фильм в 2008 году?
# Варианты ответов:
# 1. Madagascar: Escape 2 Africa	tt0479952
# 2. Iron Man	tt0371746
# 3. Kung Fu Panda	tt0441773
# 4. The Dark Knight	tt0468569
# 5. Mamma Mia!	tt0795421

# In[73]:


release_date_select=data.query('release_year==2008')
rev=release_date_select.query('revenue==revenue.max()')
display(rev)
answer_ls.append(4)


# # 10. Самый убыточный фильм за период с 2012 по 2014 (включительно)?
# Варианты ответов:
# 1. Winter's Tale	tt1837709
# 2. Stolen	tt1656186
# 3. Broken City	tt1235522
# 4. Upside Down	tt1374992
# 5. The Lone Ranger	tt1210819
# 

# In[75]:


data13=data.query('release_year in ["2012","2013","2014"]')
data14=data13.query('profit==profit.min()')
display(data14)
answer_ls.append(5)


# # 11. Какого жанра фильмов больше всего?
# Варианты ответов:
# 1. Action
# 2. Adventure
# 3. Drama
# 4. Comedy
# 5. Thriller

# In[76]:


all_genres=data.genres.str.split('|').sum()
counter=collections.Counter(all_genres)
print(counter.most_common(1))
answer_ls.append(3)


# # 12. Какого жанра среди прибыльных фильмов больше всего?
# Варианты ответов:
# 1. Drama
# 2. Comedy
# 3. Action
# 4. Thriller
# 5. Adventure

# In[77]:


data_genres=data.query('profit>0')
all_genres_in_profit=data_genres.genres.str.split('|').sum()
counter=collections.Counter(all_genres_in_profit)
print(counter.most_common(1))
answer_ls.append(1)


# # 13. Кто из режиссеров снял больше всего фильмов?
# Варианты ответов:
# 1. Steven Spielberg
# 2. Ridley Scott 
# 3. Steven Soderbergh
# 4. Christopher Nolan
# 5. Clint Eastwood

# In[78]:


popular_dir=data.director
counter=collections.Counter(popular_dir)
print(counter.most_common(1))
answer_ls.append(3)


# # 14. Кто из режиссеров снял больше всего Прибыльных фильмов?
# Варианты ответов:
# 1. Steven Soderbergh
# 2. Clint Eastwood
# 3. Steven Spielberg
# 4. Ridley Scott
# 5. Christopher Nolan

# In[79]:


data18=data.query('profit>0')
a=data18.director
counter=collections.Counter(a)
print(counter.most_common(1))
answer_ls.append(4)


# # 15. Кто из режиссеров принес больше всего прибыли?
# Варианты ответов:
# 1. Steven Spielberg
# 2. Christopher Nolan
# 3. David Yates
# 4. James Cameron
# 5. Peter Jackson
# 

# In[80]:


grouped_df = data.groupby(['director']).sum()
display(grouped_df.profit.sort_values(ascending=False).head(1))
answer_ls.append(5)


# # 16. Какой актер принес больше всего прибыли?
# Варианты ответов:
# 1. Emma Watson
# 2. Johnny Depp
# 3. Michelle Rodriguez
# 4. Orlando Bloom
# 5. Rupert Grint

# In[81]:


actors = set(data.cast.str.split('|').sum())
all_cast = pd.Series({x:data[data.cast.str.contains(x)].profit.sum()
for x in actors}).sort_values(ascending = False)
display(all_cast.head(1))
answer_ls.append(1)


# # 17. Какой актер принес меньше всего прибыли в 2012 году?
# Варианты ответов:
# 1. Nicolas Cage
# 2. Danny Huston
# 3. Kirsten Dunst
# 4. Jim Sturgess
# 5. Sami Gayle

# In[82]:


data19=data.query('release_year==2012')
actors = set(data19.cast.str.split('|').sum())
cast_2012 = pd.Series({x:data19[data19.cast.str.contains(x)].profit.sum()
for x in actors}).sort_values(ascending = True)
display(cast_2012.head(1))
answer_ls.append(3)


# # 18. Какой актер снялся в большем количестве высокобюджетных фильмов? (в фильмах где бюджет выше среднего по данной выборке)
# Варианты ответов:
# 1. Tom Cruise
# 2. Mark Wahlberg 
# 3. Matt Damon
# 4. Angelina Jolie
# 5. Adam Sandler

# In[83]:


data20=data.query('budget>budget.mean()')
cas_t=data20.cast.str.split('|').sum()
counter=collections.Counter(cas_t)
print(counter.most_common(1))
answer_ls.append(3)


# # 19. В фильмах какого жанра больше всего снимался Nicolas Cage?  
# Варианты ответа:
# 1. Drama
# 2. Action
# 3. Thriller
# 4. Adventure
# 5. Crime

# In[84]:


data21=data[data.cast.str.match("Nicolas Cage", na=False)]
a_21=data21.genres.str.split('|').sum()
counter=collections.Counter(a_21)
print(counter.most_common(1))
answer_ls.append(2)


# # 20. Какая студия сняла больше всего фильмов?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Paramount Pictures
# 3. Columbia Pictures
# 4. Warner Bros
# 5. Twentieth Century Fox Film Corporation

# In[85]:


companies_all=data.production_companies.str.split('|').sum()
counter=collections.Counter(companies_all)
print(counter.most_common(1))
answer_ls.append(1)


# # 21. Какая студия сняла больше всего фильмов в 2015 году?
# Варианты ответа:
# 1. Universal Pictures
# 2. Paramount Pictures
# 3. Columbia Pictures
# 4. Warner Bros
# 5. Twentieth Century Fox Film Corporation

# In[86]:


data22=data.query('release_year == 2015')
prod_22=data22.production_companies.str.split('|').sum()
counter=collections.Counter(prod_22)
print(counter.most_common(1))
answer_ls.append(4)


# # 22. Какая студия заработала больше всего денег в жанре комедий за все время?
# Варианты ответа:
# 1. Warner Bros
# 2. Universal Pictures (Universal)
# 3. Columbia Pictures
# 4. Paramount Pictures
# 5. Walt Disney

# In[87]:


data_comedy=data[data.genres.str.match("Comedy", na=False)]
prod_comedy = set(data_comedy.production_companies.str.split('|').sum())
count_prod = pd.Series({x:data_comedy[data_comedy.production_companies.str.contains(x)].profit.sum()
for x in prod_comedy}).sort_values(ascending = False)
display(count_prod.head(1))
answer_ls.append(2)


# # 23. Какая студия заработала больше всего денег в 2012 году?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Warner Bros
# 3. Columbia Pictures
# 4. Paramount Pictures
# 5. Lucasfilm

# In[88]:


data_2012=data.query('release_year==2012')
prod_2012 = set(data_2012.production_companies.str.split('|').sum())
sum_prod = pd.Series({x:data_2012[data_2012.production_companies.str.contains(x)].profit.sum()
for x in prod_2012}).sort_values(ascending = False)
display(sum_prod.head(1))
answer_ls.append(3)


# # 24. Самый убыточный фильм от Paramount Pictures
# Варианты ответа:
# 
# 1. K-19: The Widowmaker tt0267626
# 2. Next tt0435705
# 3. Twisted tt0315297
# 4. The Love Guru tt0811138
# 5. The Fighter tt0964517

# In[89]:


data25=data[data.production_companies.str.match("Paramount Pictures", na=False)]
display(data25.query('profit == profit.min()'))


answer_ls.append(1)


# # 25. Какой Самый прибыльный год (заработали больше всего)?
# Варианты ответа:
# 1. 2014
# 2. 2008
# 3. 2012
# 4. 2002
# 5. 2015

# In[90]:


grouped_df_best_year = data.groupby(['release_year']).sum()
display(grouped_df_best_year.profit.sort_values(ascending=False))
answer_ls.append(5)


# # 26. Какой Самый прибыльный год для студии Warner Bros?
# Варианты ответа:
# 1. 2014
# 2. 2008
# 3. 2012
# 4. 2010
# 5. 2015

# In[91]:


data26=data[data.production_companies.str.contains("Warner", na=False)]
grouped_df2 = data26.groupby(['release_year']).sum()
display(grouped_df2.profit.sort_values(ascending=False).head(1))
answer_ls.append(1)


# # 27. В каком месяце за все годы суммарно вышло больше всего фильмов?
# Варианты ответа:
# 1. Январь
# 2. Июнь
# 3. Декабрь
# 4. Сентябрь
# 5. Май

# In[92]:


data['release_date'] = pd.to_datetime(data['release_date'])
conv_date=data['release_date'].dt.month
counter=collections.Counter(conv_date)
print(counter.most_common(1))
answer_ls.append(4)


# # 28. Сколько суммарно вышло фильмов летом? (за июнь, июль, август)
# Варианты ответа:
# 1. 345
# 2. 450
# 3. 478
# 4. 523
# 5. 381

# In[98]:


data['summer_release'] =data['release_date'].dt.month.isin([6,7,8])
summer=data[data.summer_release==True].imdb_id.count()
display(summer)
answer_ls.append(2)


# # 29. Какой режисер выпускает (суммарно по годам) больше всего фильмов зимой?
# Варианты ответов:
# 1. Steven Soderbergh
# 2. Christopher Nolan
# 3. Clint Eastwood
# 4. Ridley Scott
# 5. Peter Jackson

# In[99]:


data['winter_release'] =data['release_date'].dt.month.isin([12,1,2])
winter=data[data.winter_release==True].director.value_counts()
display(winter)
answer_ls.append(5)


# # 30. Какой месяц чаще всего по годам самый прибыльный?
# Варианты ответа:
# 1. Январь
# 2. Июнь
# 3. Декабрь
# 4. Сентябрь
# 5. Май

# In[100]:


data['month'] =data['release_date'].dt.month
table_month = pd.pivot_table(data, values='profit', index=['release_year'], columns=['month'], aggfunc=np.sum)
table_month['max_mo']=table_month.idxmax(axis=1)
counter=collections.Counter(table_month['max_mo'])
print(counter.most_common(1))
answer_ls.append(2)


# # 31. Названия фильмов какой студии в среднем самые длинные по количеству символов?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Warner Bros
# 3. Jim Henson Company, The
# 4. Paramount Pictures
# 5. Four By Two Productions

# In[101]:


data['title_lenght']=data['original_title'].str.len()
production_c = set(data.production_companies.str.split('|').sum())
prod_leng = pd.Series({x:data[data.production_companies.str.contains(x)].title_lenght.mean()
for x in production_c}).sort_values(ascending = False)
display(prod_leng)

answer_ls.append(5)


# # 32. Названия фильмов какой студии в среднем самые длинные по количеству слов?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Warner Bros
# 3. Jim Henson Company, The
# 4. Paramount Pictures
# 5. Four By Two Productions

# In[102]:


data['words_lenght']=data['original_title'].str.split().str.len()
production_w = set(data.production_companies.str.split('|').sum())
prod_words= pd.Series({x:data[data.production_companies.str.contains(x)].words_lenght.mean()
for x in production_w}).sort_values(ascending = False)
display(prod_words)
answer_ls.append(5)


# # 33. Сколько разных слов используется в названиях фильмов?(без учета регистра)
# Варианты ответа:
# 1. 6540
# 2. 1002
# 3. 2461
# 4. 28304
# 5. 3432

# In[103]:


results = set()
lenght_words=data['original_title'].str.lower().replace('  ',' ').str.split().apply(results.update)
print(len(list(results)))
answer_ls.append(3)


# # 34. Какие фильмы входят в 1 процент лучших по рейтингу?
# Варианты ответа:
# 1. Inside Out, Gone Girl, 12 Years a Slave
# 2. BloodRayne, The Adventures of Rocky & Bullwinkle
# 3. The Lord of the Rings: The Return of the King
# 4. 300, Lucky Number Slevin

# In[104]:


data_1_per=data.loc[data['vote_average']>data.quantile(0.99, numeric_only=True)['vote_average']]['original_title']
display(data_1_per)
answer_ls.append(1)


# # 35. Какие актеры чаще всего снимаются в одном фильме вместе
# Варианты ответа:
# 1. Johnny Depp & Helena Bonham Carter
# 2. Hugh Jackman & Ian McKellen
# 3. Vin Diesel & Paul Walker
# 4. Adam Sandler & Kevin James
# 5. Daniel Radcliffe & Rupert Grint

# In[105]:


data['new_cast']=data.cast.str.split('|')
data['new_cast']=data.new_cast.apply(lambda r: list(combinations(r, 2)))
cast_nuova=data.new_cast.to_list()
out = list(itertools.chain(*cast_nuova))
counter=collections.Counter(out)
print(counter.most_common(1))
answer_ls.append(5)


# # 36. У какого из режиссеров выше вероятность выпустить фильм в прибыли? (5 баллов)101
# Варианты ответа:
# 1. Quentin Tarantino
# 2. Steven Soderbergh
# 3. Robert Rodriguez
# 4. Christopher Nolan
# 5. Clint Eastwood

# In[106]:


data100=data[data.profit > 0]
directors = set(data.director.str.split('|').sum())
directors1 = set(data100.director.str.split('|').sum())
ttl_directors = pd.Series({x:data[data.director.str.contains(x)].imdb_id.count()
for x in directors}).sort_values(ascending = False)
prof_directors=pd.Series({x:data100[data100.director.str.contains(x)].imdb_id.count()
for x in directors1}).sort_values(ascending = False)
all_mov=ttl_directors.to_frame().reset_index()
all_mov.columns=['dirs','ttl_mov']
prof_only=prof_directors.to_frame().reset_index()  
prof_only.columns=['dirs','profitable_mov']

joined = all_mov.merge(prof_only, on='dirs', how='inner')

joined['success_rate']=round(joined.profitable_mov/joined.ttl_mov,2)*100
best_rate=joined.query('success_rate==success_rate.max()')
best_rate
answer_ls.append(4)


# # Submission

# In[109]:


len(answer_ls)


# In[108]:


pd.DataFrame({'Id':range(1,len(answer_ls)+1), 'Answer':answer_ls}, columns=['Id', 'Answer'])


# In[ ]:




