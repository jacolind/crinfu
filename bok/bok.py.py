# adding from snotes 

### lib

from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.io import output_file, show

### minimal code

cdf = ColumnDataSource(pri_fin_mat)
p = figure()
p.line(pri_fin_mat.index, pri_fin_mat.Stocks, color='blue', line_width=2)
p.legend.location = 'bottomleft'
p.legend.background_fill_color = 'lightgray'
hover = HoverTool()
p.add_tools(hover)
output_file('plot1.html', mode='cdn')
show(p)

### notes

# snotes
# bokeh.py 20180427 1609
# folder 13-interactive-data-visualization-with-bokeh

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

## slider

# Create ColumnDataSource: source
source = ColumnDataSource(data={'x': pri_fin_mat.index,
                                'y': pri_fin_mat.Stocks})

# Add a line to the plot
plot = figure()
plot.line('x', 'y', source=source)

# Define a callback function: callback
def callback(attr, old, new):

    # Read the current value of the slider: scale
    scale = slider.value

    # Compute the updated y using np.sin(scale/x): new_y
    new_y = np.sin(scale/x)

    # Update source with the new data values
    source.data = {'x': x, 'y': new_y}

# Attach the callback to the 'value' property of slider
slider.on_change('value', callback)

# Create layout and add to current document
layout = column(widgetbox(slider), plot)
curdoc().add_root(layout)

## dropdown

# Perform necessary imports
from bokeh.models import ColumnDataSource, Select

# Create ColumnDataSource: source
source = ColumnDataSource(data={
    'x' : fertility,
    'y' : female_literacy
})

# Create a new plot: plot
plot = figure()

# Add circles to the plot
plot.circle('x', 'y', source=source)

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
select = Select(title="distribution",
                options=['female_literacy', 'population'],
                value = 'female_literacy')

# Attach the update_plot callback to the 'value' property of select
select.on_change('value', update_plot)

# Create layout and add to current document
layout = row(select, plot)
curdoc().add_root(layout)


## sync dropdowns

# display different options of 2 depending on 1

# Create two dropdown Select widgets: select1, select2
select1 = Select(title='First', options=['A', 'B'], value='A')
select2 = Select(title='Second', options=['1', '2', '3'], value='1')

# Define a callback function: callback
def callback(attr, old, new):
    # If select1 is 'A'
    if select1.value == "A":
        # Set select2 options to ['1', '2', '3']
        select2.options = ['1', '2', '3']

        # Set select2 value to '1'
        select2.value = '1'
    else:
        # Set select2 options to ['100', '200', '300']
        select2.options =  ['100', '200', '300']

        # Set select2 value to '100'
        select2.value = '100'

# Attach the callback to the 'value' property of select1
select1.on_change('value', callback)

# Create layout and add to current document
layout = widgetbox(select1, select2)
curdoc().add_root(layout)

## button

# Create a Button with label 'Update Data'
button = Button(label='Update Data')

# Define an update callback with no arguments: update
def update():

    # Compute new y values: y
    y = np.sin(x) + np.random.random(N)

    # Update the ColumnDataSource data dictionary
    source.data = {'x': x, 'y': y}

# Add the update callback to the button
button.on_click(update)

# Create layout and add to current document
layout = column(widgetbox(button), plot)
curdoc().add_root(layout)
