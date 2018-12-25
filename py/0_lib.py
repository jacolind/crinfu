# ------------------------------------------------------------------------------

# always
import os
import pandas as pd
import numpy as np

# dates
from pandas.tseries.offsets import *

# plotting
import matplotlib.pyplot as plt
import matplotlib.backends as pltb
from bokeh import *

# test ggplot
# http://ggplot.yhathq.com/install.html
# from ggplot import *

# handle many files
import glob

# import stocks
import datetime
#import pandas_datareader.data as web

# statistical modelling
import statsmodels.api as sm
import scipy.stats as stats

# options
save_large_png = False
pd.options.display.max_rows = 20