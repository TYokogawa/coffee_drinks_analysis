## amazon review json parse

import json
import gzip

meta = []
with gzip.open('meta_Home_and_Kitchen.json.gz','r') as f:
    for line in f:
        meta.append(json.loads(line))

data = []
with open('reviews_Home_and_Kitchen.json') as f:
    for line in f:
        data.append(json.loads(line))