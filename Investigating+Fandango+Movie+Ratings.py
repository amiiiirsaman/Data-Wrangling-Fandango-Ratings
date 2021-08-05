#!/usr/bin/env python
# coding: utf-8

# In[66]:


#project objective
#In this project, we'll analyze more recent movie ratings data to determine whether there has been any change in Fandango's rating system after Hickey's analysis.


# In[67]:


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import seaborn as sns
import numpy as np

before = pd.read_csv('fandango_score_comparison.csv')
after = pd.read_csv('movie_ratings_16_17.csv')


# In[68]:


print(before.head(), '\n')


# In[69]:


print(after.head())


# In[70]:


before.describe()


# In[71]:


after.describe()


# In[72]:


before.shape


# In[73]:


after.shape


# In[74]:


Fandango_before = before[['FILM', 'Fandango_Stars', 'Fandango_Ratingvalue', 'Fandango_votes', 'Fandango_Difference']]
print(Fandango_before.head())


# In[75]:


Fandango_after = after[['movie', 'year', 'fandango']]
print(Fandango_after.head()) 


# In[76]:


Fandango_after.info


# In[77]:


Fandango_after['year'].unique()


# In[84]:


Fandango_after_2016 = Fandango_after[Fandango_after['year'] == 2016]


# In[85]:


print(Fandango_after_2016['year'].value_counts())


# In[86]:


Fandango_before['year'] = Fandango_before['FILM'].str[-5:-1]
print(Fandango_before['year'].head(5))
print(Fandango_before['year'].unique())


# In[87]:


Fandango_before_2015 = Fandango_before[Fandango_before['year'] == '2015']
print(Fandango_before_2015['year'].unique())


# In[88]:


Fandango_before_2015['year'].astype(int)


# In[117]:


import matplotlib.pyplot as plt
from numpy import arange
import seaborn as sns

get_ipython().magic('matplotlib inline')

fig, ax = plt.subplots(figsize=(10,8))
plt.style.use('fivethirtyeight')


sns.kdeplot(Fandango_before_2015['Fandango_Stars'], color='green', shade=True, legend=True, label = '2015')
sns.kdeplot(Fandango_after_2016['fandango'], color='blue', shade=True, legend=True, label = '2016')

plt.title("Comparing distribution shapes for Fandango's ratings\n(2015 vs 2016)",
          y = 1.07) # the `y` parameter pads the title upward
plt.xlabel('Stars')
plt.xlim(0,5) # because ratings start at 0 and end at 5
plt.xticks(arange(0,5.1,.5))
plt.show()



# In[97]:


Fandango_before_2015['Fandango_Stars'].value_counts(normalize = True).sort_index()*100


# In[98]:


Fandango_after_2016['fandango'].value_counts(normalize = True).sort_index()*100


# In[132]:


import matplotlib.pyplot as plt

mean_2015 = Fandango_before_2015['Fandango_Stars'].mean()
mode_2015 = Fandango_before_2015['Fandango_Stars'].mode()
median_2015 = Fandango_before_2015['Fandango_Stars'].median()

mean_2016 = Fandango_after_2016['fandango'].mean()
mode_2016 = Fandango_after_2016['fandango'].mode()
median_2016 = Fandango_after_2016['fandango'].median()

summary = pd.DataFrame()
summary['2015'] = [mean_2015, median_2015, mode_2015]
summary['2016'] = [mean_2016, median_2016, mode_2016]
summary.index = ['mean', 'median', 'mode']
summary
            


# In[138]:


mean_2015 = Fandango_before_2015['Fandango_Stars'].mean()
mean_2016 = Fandango_after_2016['fandango'].mean()

median_2015 = Fandango_before_2015['Fandango_Stars'].median()
median_2016 = Fandango_after_2016['fandango'].median()

mode_2015 = Fandango_before_2015['Fandango_Stars'].mode()[0] # the output of Series.mode() is a bit uncommon
mode_2016 = Fandango_after_2016['fandango'].mode()[0]

summary = pd.DataFrame()
summary['2015'] = [mean_2015, median_2015, mode_2015]
summary['2016'] = [mean_2016, median_2016, mode_2016]
summary.index = ['mean', 'median', 'mode']
summary


# In[139]:


plt.style.use('fivethirtyeight')
summary['2015'].plot.bar(color = '#0066FF', align = 'center', label = '2015', width = .25)
summary['2016'].plot.bar(color = '#CC0000', align = 'edge', label = '2016', width = .25,
                         rot = 0, figsize = (8,5))

plt.title('Comparing summary statistics: 2015 vs 2016', y = 1.07)
plt.ylim(0,5.5)
plt.yticks(arange(0,5.1,.5))
plt.ylabel('Stars')
plt.legend(framealpha = 0, loc = 'upper center')
plt.show()


# In[ ]:




