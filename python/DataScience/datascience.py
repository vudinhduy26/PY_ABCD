# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 00:01:33 2021

@author: duy
"""

import pandas as pd
import numpy as np
from urllib.request import urlretrieve
urlretrieve("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv", 'chipotle.tsv')
chipo = pd.read_csv("chipotle.tsv", sep ='\t')
print(chipo.info())