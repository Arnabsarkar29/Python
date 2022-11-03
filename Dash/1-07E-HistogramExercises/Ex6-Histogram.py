#######
# Objective: Create a histogram that plots the 'length' field
# from the Abalone dataset (../data/abalone.csv).
# Set the range from 0 to 1, with a bin size of 0.02
######

# Perform imports here:
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo



# create a DataFrame from the .csv file:
df=pd.read_csv("H:/Python/Plotly-Dashboards-with-Dash-master/data/abalone.csv")

# create a data variable:

data = [go.Histogram(x=df['length'],xbins=dict(start =0.0 ,end =1.0 ,size= 0.02))]




# add a layout
layout=go.Layout(title="Length")

fig = go.Figure(data=data,layout=layout)



# create a fig from data & layout, and plot the fig
pyo.plot(fig)
