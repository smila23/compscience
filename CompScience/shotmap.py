import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from mplsoccer.pitch import VerticalPitch
import mplsoccer

#base_url = "https://understat.com/match/"
#url = base_url

#res = requests.get(url)
#soup = BeautifulSoup(res.content, "lxml")
#scripts = soup.find_all("script")

#strings = scripts[1].string
#ind_start = strings.index("('")+2
#ind_end = strings.index("')")

#json_data = strings[ind_start:ind_end]
#json_data = json_data.encode("utf8").decode("unicode_escape")

#data = json.loads(json_data)

#X = []
#Y = []
#xG = []
#result = []
#team = []
#data_away = data['a']
#data_home = data['h']

#for index in range(len(data_home)):
    #for key in data_home[index]:
        #if key == 'X':
            #X.append(data_home[index][key])
        #if key == 'Y':
            #Y.append(data_home[index][key])
        #if key == 'h_team':
            #team.append(data_home[index][key])
        #if key == 'xG':
            #xG.append(data_home[index][key])
        #if key == 'result':
            #result.append(data_home[index][key])

#for index in range(len(data_away)):
    #for key in data_away[index]:
        #if key == 'X':
            #X.append(data_away[index][key])
        #if key == 'Y':
            #Y.append(data_away[index][key])
        #if key == 'a_team':
            #team.append(data_away[index][key])
        #if key == 'xG':
            #xG.append(data_away[index][key])
        #if key == 'result':
            #result.append(data_away[index][key])


#col_names = ['X','Y','xG','result','team']
#df = pd.DataFrame([X,Y,xG,result,team],index=col_names)
#df = df.T

data = pd.read_csv("shotmaps.csv")

fig, ax = plt.subplots(figsize=(13, 8))
fig.set_facecolor("#FFFFFF")
ax.patch.set_facecolor("#FFFFFF")
pitch = VerticalPitch(pitch_type='statsbomb',
              pitch_color='#000000', line_color='#c7d5cc', half=True
                )

pitch.draw(ax=ax)

plt.scatter(data["x"], data["y"], s=data["xG"]*800)
plt.xlabel('Spurs shot map vs Leeds',color='black', fontsize=15)
plt.show()
web = "h"



#fig, ax = plt.subplots(figsize=(13, 8, 5))
#fig.set_facecolor("#22312b")
#ax.patch.set_facecolor("#22312b")

#fig, ax = plt.subplots(figsize=(15.6,10.4))
#fig.set_facecolor("black")

#pitch = Pitch(pitch_type="statsbomb", positional=True, positional_color="#FFFFFF", pitch_color="grass", line_color="FFFFFF", goal_type="box",)
#pitch.draw(ax=ax)

