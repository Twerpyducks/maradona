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

#print(df["club_goals"])

# years = list(range(df["year"].min(), df["year"].max()+1))

# df2 = pd.DataFrame(years, columns = ['year'])
#
# df2["club"] = ""
# df2["club_goals"] = 0
#
# for i in df2["year"]:
#     for j in df["year"]:
#         if (i == j):
#             print(df.loc["team"])

#print(df.loc[0].at['year'])

# is_club = df["type"] == "club"
# club_stats = df[is_club]
# club_goals = df[is_club]["goals"]
# club_labels = df[is_club]["year"]

# is_country = df["type"] == "country"
# country_stats = df[is_country]
# country_goals = df[is_country]["goals"]
# country_labels = df[is_country]["year"]
#
# club_labels = list(range(df[is_club]["year"].min(), df[is_club]["year"].max()+1))
# country_labels = list(range(df[is_country]["year"].min(), df[is_country]["year"].max()+1))
#
# print(f"club shape: {club_stats.shape}")
# print(f"country shape: {country_stats.shape}")
# print(f"club min: {club_stats['year'].min()}")
# print(f"club max: {club_stats['year'].max()}")
# print(f"country min: {country_stats['year'].min()}")
# print(f"country max: {country_stats['year'].max()}")
# print(f"total min: {df['year'].min()}")
# print(f"total max: {df['year'].max()}")
# print(labels)
# print(club_labels)
# print(country_labels)

width = 0.75

#fig, ax = plt.subplots()

fig = plt.figure(figsize=(16,8))
ax = fig.add_subplot(1,1,1)

ax.bar(labels, df["club_goals"], width, label='Club')
ax.bar(labels, df["country_goals"], width, label='Country')

ax.grid(color='LIGHTGRAY')
ax.set_ylabel('Goals')
ax.set_xlabel('Years')
ax.set_title('Goals by year')
ax.legend()

plt.show()
