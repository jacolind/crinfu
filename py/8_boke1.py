# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 

"""

from bokeh.plotting import figure
from bokeh.charts import Area
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.io import output_file, show

# 1
pri_fin_mat.isnull().sum()
p = figure()
p.line(pri_fin_mat.index, pri_fin_mat.Stocks, color='blue', line_width=2)
p.legend.location = 'bottomleft'
p.legend.background_fill_color = 'lightgray'
hover = HoverTool()
p.add_tools(hover)
output_file('output/boke/stocks.html', mode='cdn')
show(p)

# 2
p2 = Area(pri_fin_mat.Stocks.fillna(0))
output_file("output/boke/p2.html")
show(p2)

# 3
cdf = ColumnDataSource(pri_fin_mat)
p3 = figure()
#p3.line('date', 'Stocks', source=cdf)
p3.line(pri_fin_mat.index, pri_fin_mat.Bonds)
p3.add_tools(hover)
output_file('output/boke/s2.html', mode='cdn')
show(p3)

# 4

# 5 
tkr_mcafr = tkr_sel + ['Others']
mcafr_vcc_mat.columns
mcafr_vcc_mat_mthly = mcafr_vcc_mat.resample('M', convention='start').asfreq()
mcafr_vcc_mat_mthly = mcafr_vcc_mat_mthly.fillna(method='ffill')
mcafr_vcc_mat_mthly[tkr_mcafr].isnull().sum()
mcafr_vcc_mat_mthly.loc['2016':, tkr_mcafr].isnull().sum()
mcafr_vcc_mat_mthly.loc['2016':, tkr_mcafr]
mcafr_vcc_mat_mthly.loc['2016':, tkr_mcafr].plot.area()
p4 = Area(mcafr_vcc_mat_mthly.loc['2016':, tkr_mcafr],
          stack=True, color=['Orange','Green','Grey'])
#p4.line(mcafr_vcc_mat_mthly.loc['2016':,'BLX'].index,
#        mcafr_vcc_mat_mthly.loc['2016':,'BLX'])

hover = HoverTool(tooltips=[('BTC','@BTC'), 
                            ('ETH', '@ETH'),
                            ('Others', '@Others')
                            ])
p4.add_tools(hover)
output_file('output/boke/mcafr2.html', mode='cdn')
show(p4)

# p6 
mcafr_vcc_mat.columns
p5 = Area(mcafr_vcc_mat.loc[:,tkr_mcafr], 
          stack=True, color=['Orange','Green','Grey'])
p5.line(mcafr_vcc_mat.index, mcafr_vcc_mat.BLX)
#hover = HoverTool(tooltips=[('BTC','@BTC'), 
#                            ('ETH', '@ETH'),
#                            ('Others', '@Others')
#                            ])
#p4.add_tools(hover)
output_file('output/boke/mcafr1.html', mode='cdn')
show(p5)

test = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
p6 = Area(test, stack=True)
output_file('output/boke/p6.html', mode='cdn')
show(p6)

### bokeh server

# Perform necessary imports
from bokeh.io import curdoc
from bokeh.layouts import widgetbox
from bokeh.models import Slider

# Create first slider: slider1
slider1 = Slider(title='slider1', start=0, end=10, step=0.1, value=2)

# Create second slider: slider2
slider2 = Slider(title='slider2', start=10, end=100, step=1, value=20)

# Add slider1 and slider2 to a widgetbox
layout = widgetbox(slider1, slider2)

# Add the layout to the current document
curdoc().add_root(layout)
