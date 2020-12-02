import json
import pandas as pd

# f = open('Maradona-goals.json')
# resp_dict = json.load(f)
# f.close()
#
# l = []
# for c, cl in resp_dict.items():
#     for d in cl:
#         d.update({'club' : c})
#         l.append(d)
# df = pd.DataFrame(l)
#
# print(df)

def _ingest_json():
	f = open('Maradona-goals.json')
    resp_dict = json.load(f)
    f.close()

    l = []
    for c, cl in resp_dict.items():
        for d in cl:
            d.update({'club' : c})
            l.append(d)
    df = pd.DataFrame(l)

    return df

print(_ingest_json)
