#######
# Objective: Using the iris dataset, develop a Distplot
# that compares the petal lengths of each class.
# File: '../data/iris.csv'
# Fields: 'sepal_length','sepal_width','petal_length','petal_width','class'
# Classes: 'Iris-setosa','Iris-versicolor','Iris-virginica'
######

# Perform imports here:
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo
import plotly.figure_factory as ff


# create a DataFrame from the .csv file:

df = pd.read_csv("H:/Python/Plotly-Dashboards-with-Dash-master/data/iris.csv")
#for flower in Classes:
#print(df[df['class']==flower]['petal_length'])
# Define the traces
trace0 = df[df['class']=='Iris-setosa']['petal_length']
trace1 = df[df['class']=='Iris-versicolor']['petal_length']
trace2 = df[df['class']=='Iris-virginica']['petal_length']


# HINT:
# This grabs the petal_length column for a particular flower
# Define a data variable

hist_data = [trace0,trace1,trace2]
group_labels = ['Iris-setosa','Iris-versicolor','Iris-virginica']
#
# # Create a fig from data and layout, and plot the fig
#
fig = ff.create_distplot(hist_data , group_labels)
pyo.plot(fig)
