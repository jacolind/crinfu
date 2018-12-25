# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 

"""

from bokeh.plotting import figure, output_file, show
from bokeh.charts import Area
from bokeh.models import ColumnDataSource, HoverTool, BoxSelectTool
from bokeh.io import output_file, show


# 1
pri_fin_mat.isnull().sum()
p = figure()
p.line(pri_fin_mat.index, pri_fin_mat.Stocks, color='blue', line_width=2)
p.legend.location = 'bottomleft'
p.legend.background_fill_color = 'lightgray'
hover = HoverTool()
p.add_tools(hover)
output_file('output/bokeh/stocks.html', mode='cdn')
show(p)

#
pri_fin_mat2 = pri_fin_mat
pri_fin_mat2['Date'] = pri_fin_mat2.index
cdf = ColumnDataSource(pri_fin_mat2)
del pri_fin_mat2
p = figure()
p.line(x='Date', y='Gold', source=cdf)
output_file('output/bokeh/stocks.html', mode='cdn')
show(p)


# 2
p2 = Area(pri_fin_mat.Stocks.fillna(0))
output_file("output/bokeh/p2.html")
show(p2)

# 3
cdf = ColumnDataSource(pri_fin_mat)
p3 = figure()
#p3.line('date', 'Stocks', source=cdf)
p3.line(pri_fin_mat.index, pri_fin_mat.Bonds)
hover = HoverTool()
p3.add_tools(hover)
output_file('output/bokeh/s2.html', mode='cdn')
show(p3)

# 4

# 5
tkr_sel = ['BTC', 'ETH']
mcafr_vcc_mat = mca_vcc_mat.div(mca_vcc_mat.sum(1), axis=0)
mcafr_vcc_mat.columns
mcafr_vcc_mat_mthly = mcafr_vcc_mat.resample('MS').first()
mcafr_vcc_mat_mthly[tkr_sel].isnull().sum()
p4 = Area(mcafr_vcc_mat_mthly.loc['2016':, tkr_sel],
          stack=True, color=['Orange','Green'])
#p4.line(mcafr_vcc_mat_mthly.loc['2016':,'BLX'].index,
#        mcafr_vcc_mat_mthly.loc['2016':,'BLX'])

hover = HoverTool(tooltips=[('BTC', '@BTC'),
                            ('ETH', '@ETH')])
p4.add_tools(hover)
output_file('output/bokeh/mcafr2.html', mode='cdn')
show(p4)

# test
test = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
p6 = Area(test, stack=True)
output_file('output/bokeh/p6.html', mode='cdn')
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


# ---------------------------------------------------------------------

## testin bokeh

cols = ['ETH', 'XRP']
cdf = pri_vcc_mat.iloc[0:200][cols].fillna(0)
cdf['Date'] = cdf.index
cdf = ColumnDataSource(cdf)
start = '2017-01'
end = '2018-04'
p = figure(x_axis_label='Date', y_axis_label='Price')
p.line(x='Date', y='XRP', source=cdf)
p.legend.location = 'bottomleft'
p.legend.background_fill_color = 'lightgray'
hover = HoverTool(tooltips='$name')
p.add_tools(hover)
output_file('plot10.html', mode='cdn')
show(p)


##

p = figure()
p.line(x=pri_vcc_mat.index, y=pri_vcc_mat.ETH)
output_file('plot11.html')
show(p)

## corr over time - learn bokeh tools to do it

from bokeh.models import Select
from bokeh.models.widgets import CheckboxGroup
from bokeh.layouts import widgetbox

output_file("checkbox_group.html")

checkbox_group = CheckboxGroup(
        labels=["Option 1", "Option 2", "Option 3"], active=[0, 1])

show(widgetbox(checkbox_group))


# Create ColumnDataSource: source
cols = ['ETH', 'XRP', 'BTC', 'LTC']
source = ColumnDataSource(pri_vcc_mat.iloc[100:300][cols])

# Create a new plot: plot
plot = figure()

# Add circles to the plot
plot.circle('index', 'ETH', source=source)

# Define a callback function: update_plot
def update_plot(attr, old, new):
    # If the new Selection is 'female_literacy', update 'y' to female_literacy
    if new == 'female_literacy':
        source.data = {
            'x' : fertility,
            'y' : female_literacy
        }
    # Else, update 'y' to population
    else:
        source.data = {
            'x' : fertility,
            'y' : population
        }

# Create a dropdown Select widget: select
select = Select(title="asset",
                options=['ETH', 'XRP'],
                value = 'ETH')

# Attach the update_plot callback to the 'value' property of select
select.on_change('value', update_plot)

# Create layout and add to current document
layout = row(select, plot)
curdoc().add_root(layout)

## gapminder case study

from bokeh.layouts import row


# Define the callback: update_plot
def update_plot(attr, old, new):
    # Read the current value off the slider and 2 dropdowns: yr, x, y
    yr = slider.value
    x = x_select.value
    y = y_select.value
    # Label axes of plot
    plot.xaxis.axis_label = x
    plot.yaxis.axis_label = y
    # Set new_data
    new_data = {
        'x'       : data.loc[yr][x],
        'y'       : data.loc[yr][y],
        'country' : data.loc[yr].Country,
        'pop'     : (data.loc[yr].population / 20000000) + 2,
        'region'  : data.loc[yr].region,
    }
    # Assign new_data to source.data
    source.data = new_data

    # Set the range of all axes
    plot.x_range.start = min(data[x])
    plot.x_range.end = max(data[x])
    plot.y_range.start = min(data[y])
    plot.y_range.end = max(data[y])

    # Add title to plot
    plot.title.text = 'Gapminder data for %d' % yr

# Create a dropdown slider widget: slider
slider = Slider(start=1970, end=2010, step=1, value=1970, title='Year')

# Attach the callback to the 'value' property of slider
slider.on_change('value', update_plot)

# Create a dropdown Select widget for the x data: x_select
x_select = Select(
    options=['fertility', 'life', 'child_mortality', 'gdp'],
    value='fertility',
    title='x-axis data'
)

# Attach the update_plot callback to the 'value' property of x_select
x_select.on_change('value', update_plot)

# Create a dropdown Select widget for the y data: y_select
y_select = Select(
    options=['fertility', 'life', 'child_mortality', 'gdp'],
    value='life',
    title='y-axis data'
)

# Attach the update_plot callback to the 'value' property of y_select
y_select.on_change('value', update_plot)

# Create layout and add to current document
layout = row(widgetbox(slider, x_select, y_select), plot)
curdoc().add_root(layout)





## gapminder case study modified


# data
pri_vcc_mat2 = pri_vcc_mat
pri_vcc_mat2['Date'] = pri_vcc_mat2.index
COLS_1 = ['ETH', 'LTC', 'XRP']
data = pri_vcc_mat2.iloc[0:200][COLS_1].fillna(0)
data

plot = figure()
source = ColumnDataSource(data)
plot.line(x='Date', y='ETH', source=source)


# Define the callback: update_plot
def update_plot(attr, old, new):
    # Read the current value off the slider and 2 dropdowns: yr, x, y
    yr = slider.value
    x = 'Date'
    y = y_select.value
    # Label axes of plot
    plot.xaxis.axis_label = x
    plot.yaxis.axis_label = y
    # Set new_data
    new_data = {
        'x'       : data.loc[x],
        'y'       : data.loc[y],
    }
    # Assign new_data to source.data
    source.data = new_data

    # Set the range of all axes
    plot.x_range.start = min(data[x])
    plot.x_range.end = max(data[x])
    plot.y_range.start = min(data[y])
    plot.y_range.end = max(data[y])

    # Add title to plot
    plot.title.text = 'Gapminder data for %d' % yr

# Create a dropdown slider widget: slider
slider = Slider(start=1970, end=2010, step=1, value=1970, title='Year')

# Attach the callback to the 'value' property of slider
slider.on_change('value', update_plot)

# Create a dropdown Select widget for the y data: y_select
y_select = Select(
    options=COLS_1,
    value='ETH',
    title='Assets'
)

# Attach the update_plot callback to the 'value' property of y_select
y_select.on_change('value', update_plot)

# Create layout and add to current document
layout = row(widgetbox(slider, x_select, y_select), plot)
curdoc().add_root(layout)

show(plot)

## corr over time

#input: 2-6 assets
#output: rollcorr graph.




## index competition with ggindex()

#use the ggindex function to generate shiny app. plot the aum of usd 100 #invesment. show table with return and risk (vol, IR, sharpe, sortino, 95% VaR).


