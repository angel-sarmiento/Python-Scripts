#%%
"Preamble for importing libraries"

import numpy as np
from numpy.random import randn
import pandas as pd 
from pandas import Series, DataFrame

from scipy import stats

import seaborn as sns

import matplotlib as mlib
import matplotlib.pyplot as plt 

#%%
titanic_df = pd.read_csv('/Users/angelsarmiento/Documents/Python/data-analytics-course/Titanic Project/train.csv')

titanic_df.head()
titanic_df.describe()

#%%
sns.catplot(x='Sex', data=titanic_df, hue='Pclass', kind='count')

sns.catplot('Survived', col='Embarked', col_wrap=4, data=titanic_df[titanic_df.Embarked.notnull()], kind='count', height=2.5, aspect=0.8)


# %%
# functions

def male_female_child(passenger):
    age,sex = passenger

    if age < 16:
        return 'child'
    else:
        return sex




# %%
titanic_df['person'] = titanic_df[['Age', 'Sex']].apply(male_female_child, axis=1)

sns.catplot('Survived', col='person', data=titanic_df, kind='count', height=2.5, aspect=0.8)

beans = titanic_df.groupby(['Survived', 'person']).size()


sns.catplot(x='Pclass', data=titanic_df, kind='count', hue='person')
beans

sns.catplot('Pclass','Survived', kind='point' ,data=titanic_df, hue='person')

generations = [10,20,30,40,50,60,70,80]
sns.lmplot('Age', 'Survived', data=titanic_df, hue='Sex', x_bins = generations)
sns.lmplot('Age', 'Survived', data=titanic_df, hue='Pclass', x_bins = generations)

# %%
deck = titanic_df['Cabin'].dropna()

levels = []

for level in deck:
    levels.sort()
    levels.append(level[0])

cabin_df = DataFrame(levels)
cabin_df.columns = ['Cabin']

cabin_df['Survived'] = titanic_df['Survived']
sns.catplot('Cabin', kind='count', data=cabin_df, palette='RdBu')
sns.catplot('Survived', kind='count', data=cabin_df, hue='Cabin', palette='RdBu')


##FAILED STUFF 
cabin_ratio_s = np.divide(cabin_df.groupby(['Cabin', 'Survived']).size(), cabin_df.groupby(['Cabin']).size())
cabin_ratio  = DataFrame(cabin_ratio_s)

#sns.catplot('Survived', y='cabin_ratio', kind='bar', data=cabin_df, hue='Cabin', palette='RdBu')


# %%


# %%
