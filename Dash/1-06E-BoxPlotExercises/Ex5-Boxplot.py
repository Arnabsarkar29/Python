#######
# Objective: Make a DataFrame using the Abalone dataset (../data/abalone.csv).
# Take two independent random samples of different sizes from the 'rings' field.
# HINT: np.random.choice(df['rings'],10,replace=False) takes 10 random values
# Use box plots to show that the samples do derive from the same population.
######

# Perform imports here:
import numpy as np
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go



# create a DataFrame from the .csv file:

df =  pd.read_csv("H:/Python/Plotly-Dashboards-with-Dash-master/data/abalone.csv")
#print(df)
# take two random samples of different sizes:
x=np.random.choice(df['rings'],100,replace=False)
y=np.random.choice(df['rings'],200,replace=False)


# create a data variable with two Box plots:


data = [go.Box(y=x,name="x"),go.Box(y=y,name="y")]








# add a layout

layout = go.Layout(title="Samples")


# create a fig from data & layout, and plot the fig
fig=go.Figure(data=data,layout=layout)
pyo.plot(fig)
