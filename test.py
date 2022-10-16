import pandas as pd
import numpy as np
import os
import json
from tqdm import tqdm


def read_json(path):
    with open(path, 'r') as f:
        return json.load(f)


j = read_json("./cmr_ops27000.json")

for i in j:
    print(i['meta'])
    print(i['umm'])
    break
