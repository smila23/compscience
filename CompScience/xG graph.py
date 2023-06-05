import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


df = pd.read_csv("spursvsleedsxg.csv")

away_xG = [0]
home_xG = [0]
away_min = [0]
home_min = [0]

hteam = df['team'].iloc[0]
ateam = df['team'].iloc[-1]

for x in range(len(df['xG'])):
    if df['team'][x] == ateam:
        away_xG.append(df['xG'][x])
        away_min.append(df['minute'][x])
    if df['team'][x] == hteam:
        home_xG.append(df['xG'][x])
        home_min.append(df['minute'][x])

def nums_cumulative_sum(nums_list):
    return [sum(nums_list[:i+1]) for i in range(len(nums_list))]



away_cumulative = nums_cumulative_sum(away_xG)
home_cumulative = nums_cumulative_sum(home_xG)

alast = round(away_cumulative[-1], 2)
hlast = round(home_cumulative[-1], 2)

fig, ax = plt.subplots(figsize=(12, 6))
fig.set_facecolor('#3d4849')
ax.patch.set_facecolor('#3d4849')

mpl.rcParams['xtick.color'] = 'white'
mpl.rcParams['ytick.color'] = 'white'

ax.grid(ls='dotted', lw=.2, color='lightgrey', axis='y', zorder=1)
spines = ['top', 'bottom', 'left', 'right']
for x in spines:
    if x in spines:
        ax.spines[x].set_visible(False)

plt.xticks([0, 15, 30, 45, 60, 75, 90])
plt.xlabel('Minute',color='white', fontsize=12)
plt.ylabel('xG', color='white', fontsize=12)

ax.step(x=away_min, y=away_cumulative, color='#FFFF00', label=ateam, linewidth=5, where='post')
ax.step(x=home_min, y=home_cumulative, color='#d3d3d3', label=ateam, linewidth=5, where='post')
plt.show()
