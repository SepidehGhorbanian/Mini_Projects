
"""

@author: UNISEPP
"""
# Plotting a data set regarding movies (boxplot and scatter plot)
#We need the domestic gross range in 5 genres : action , comedy , adventure , animation , drama
#from these studios: Buena Vista Studios , Sony , Universal , WB , Fox , Paramount Pictures
#We have a csv file as a dataset

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Movies = pd.read_csv('Movies_Dataset.csv')
# print(Movies.info())

Movies.rename(columns = {'Gross % US' : 'Gross'} , inplace = True)

Studios = [ 'Buena Vista Studios' , 'Sony' , 'Universal' , 'WB' , 'Fox' , 'Paramount Pictures']
Genres = ['action' , 'comedy' , 'adventure' ,'drama' , 'animation']

# filtering data
temp1 = Movies[Movies.Studio.isin(Studios)]
temp2 = temp1[temp1.Genre.isin(Genres)]

sns.set_style('darkgrid')
vis1 = sns.stripplot( data = temp2, x = 'Genre' , y='Gross' , hue='Studio' )
vis2 = sns.boxplot(data = temp2, x= 'Genre' , y = 'Gross' , color = 'lightgray')
vis1.set(title = 'Domestic Gross % by Genre')
vis1.set(ylabel = 'Gross % US')
vis1.legend(bbox_to_anchor = (1,1), loc = 2 )

