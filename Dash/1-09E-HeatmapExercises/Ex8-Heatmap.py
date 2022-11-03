#######
# Objective: Using the "flights" dataset available
# from the data folder as flights.csv
# create a heatmap with the following parameters:
# x-axis="year"
# y-axis="month"
# z-axis(color)="passengers"
######

# Perform imports here:
import plotly.offline as pyo
import pandas as pd
import plotly.graph_objs as go


# Create a DataFrame from  "flights" data
df = pd.read_csv('H:/Python/Plotly-Dashboards-with-Dash-master/data/flights.csv')
#print(df)
# Define a data variable

data =[go.Heatmap(x = df['year']
                ,y = df['month']
                ,z = df['passengers'].values.tolist()
                ,colorscale="Picnic"
                )]



# Define the layout

layout = go.Layout(title = "Airline Passengers")

# Create a fig from data and layout, and plot the fig

fig = go.Figure(data=data,layout=layout)

pyo.plot(fig)
