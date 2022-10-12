import pandas as pd
from collections import defaultdict
import random
import json

df = pd.read_csv('../data/beer_reviews.csv')
df_short = df[['review_profilename', 'beer_beerid', 'review_time']].groupby(['review_profilename', 'beer_beerid']).min().reset_index(drop=False)

chains_per_reviewer = defaultdict(list)
pairs = defaultdict(dict)
for name in set(df_short.review_profilename):
    beers = df_short.beer_beerid[df_short.review_profilename == name].values
    for i, beer in enumerate(beers):
        if i == 0:
            chains_per_reviewer[name].append([beer])
        elif i == 1:
            chains_per_reviewer[name][-1].append(beer)
            pairs[chains_per_reviewer[name][-1][0]][chains_per_reviewer[name][-1][1]] = pairs[chains_per_reviewer[name][
                -1][0]].get(chains_per_reviewer[name][-1][1], 0) + 1
        else:
            chains_per_reviewer[name].append([chains_per_reviewer[name][-1][-1], beer])
            pairs[chains_per_reviewer[name][-1][0]][chains_per_reviewer[name][-1][1]] = pairs[chains_per_reviewer[name][
                -1][0]].get(chains_per_reviewer[name][-1][1], 0) + 1

recommendations = {}
for beer in pairs:
    max_count = max(pairs[beer].values())
    recommendations[str(beer)] = str(random.choice([k for k, v in pairs[beer].items() if v == max_count]))

with open('baseline_output.json', 'w') as f:
    json.dump(recommendations, f, indent=4)