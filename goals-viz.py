import json
import pandas as pd
import matplotlib.pyplot as plt

f = open('Maradona-goals.json')
jsonObject = json.load(f)

f.close()

l = []
for c, cl in jsonObject.items():
    for d in cl:
        d.update({'player' : c})
        l.append(d)
df = pd.DataFrame(l)

labels = df["year"]

width = 0.75

fig = plt.figure(figsize=(16,8))
ax = fig.add_subplot(1,1,1)

ax.set_xticks(labels)
ax.set_xticklabels(labels, rotation=45)
ax.set_yticks(range(0,45))

ax.bar(labels, df["club_goals"], width, label='Club')
ax.bar(labels, df["country_goals"], width, label='Country')

#ax.grid(color='LIGHTGRAY')
ax.set_ylabel('Goals')
ax.set_xlabel('Years')
ax.set_title('Goals by year')
ax.legend()

plt.show()
