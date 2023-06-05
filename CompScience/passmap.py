import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from mplsoccer.pitch import Pitch
import mplsoccer

df = pd.read_csv("Tottenham.csv")
df = df[df["teamId"] == "Tottenham"]
df["passer"] = df["playerId"]
df["receiver"] = df["playerId"].shift(-1)

passes = df[df["type"] == "Pass"]
successful = passes[passes["outcome"]== "Successful"]

subs = df[df["type"] == "SubstitutionOff"]
subs = subs["minute"]
firstSub = subs.min()

successful = successful[successful["minute"] < firstSub]

pas = pd.to_numeric(successful['passer'], downcast='integer')
rec = pd.to_numeric(successful['receiver'], downcast='integer')
successful['passer'] = pas
successful['receiver'] = rec

average_locations = successful.groupby('passer').agg({'x':['mean'],'y':['mean','count']})
average_locations.columns = ['x', 'y', 'count']

pass_between = successful.groupby(['passer', 'receiver']).id.count().reset_index()
pass_between.rename({'id':'pass_count'},axis='columns',inplace=True)

pass_between = pass_between.merge(average_locations, left_on='passer',right_index=True)
pass_between = pass_between.merge(average_locations, left_on='receiver',right_index=True,suffixes=['', '_end'])

pass_between = pass_between[pass_between['pass_count'] > 5]

pitch = Pitch(pitch_type='statsbomb')
fig, ax = pitch.draw()

arrows = pitch.arrows(1.2*pass_between.x,.8*pass_between.y, 1.2*pass_between.x_end,.8*pass_between.y_end,
                     width = 3, headwidth = 5, color = 'black', ax = ax, zorder = 1, alpha = .5)


nodes = pitch.scatter(1.2*average_locations.x,.8*average_locations.y,
                     s=300, color='#FFFFFF', edgecolors='black', linewidth=.5, alpha=1, zorder = 1, ax=ax)

plt.show()

