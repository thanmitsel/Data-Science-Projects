import pandas as pd
import numpy as np

# from bokeh.io import show, curdoc
# from bokeh.plotting import figure
#
# from bokeh.models import CategoricalColorMapper, HoverTool, ColumnDataSource, Panel
# from bokeh.models.widgets import CheckboxGroup, Slider, RangeSlider, Tabs
#
# from bokeh.layouts import column, row, WidgetBox
# from bokeh.palettes import Category20_16

from functools import lru_cache

from os.path import dirname, join
import os

import pandas as pd

from bokeh.io import curdoc
from bokeh.layouts import row, column
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import PreText, Select
from bokeh.plotting import figure

features = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"]
DATA_DIR = os.getcwd()

@lru_cache()
def load_ticker(ticker):
    fname = join(DATA_DIR, 'dataset.txt')
    data = pd.read_csv(fname, header=None,
                       names=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Labels"])
    return data

@lru_cache()
def get_data(t1, t2):
    df1 = load_ticker(t1)
    df2 = load_ticker(t2)
    data = pd.concat([df1, df2], axis=1)
    data = data.dropna()
    data['t1'] = data[t1]
    data['t2'] = data[t2]
    data['t1_returns'] = data[t1+'_returns']
    data['t2_returns'] = data[t2+'_returns']
    return data


def nix(val, lst):
    return [x for x in lst if x!=val]

stats = PreText(text='', width=500)
feature1 = Select(value='Sepal Length', options=nix('Sepal Width', features))
feature2 = Select(value='Sepal Width', options=nix('Sepal Length', features))


# Available carrier list
#available_carriers = list(flights['name'].unique())

# Sort the list in-place (alphabetical order)
#available_carriers.sort()