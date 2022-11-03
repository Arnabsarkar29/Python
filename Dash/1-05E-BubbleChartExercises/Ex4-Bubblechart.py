#######
# Objective: Create a bubble chart that compares three other features
# from the mpg.csv dataset. Fields include: 'mpg', 'cylinders', 'displacement'
# 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'
######

# Perform imports here:

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# create a DataFrame from the .csv file:

df= pd.read_csv('H:/Python/Plotly-Dashboards-with-Dash-master/data/mpg.csv')
#print(df)


# create data by choosing fields for x, y and marker size attributes

data = [go.Scatter(x=df['mpg'] , y = df['horsepower'] , mode = "markers"
        ,text=df["name"]  , marker=dict(size=df['weight']/200,  colorscale= 'Picnic',color= df['model_year'],showscale = True)
            )]




# create a layout with a title and axis labels

layout = go.Layout(title="Vehicle acceleration vs. displacement"
                      ,xaxis = dict(title = "displacement")
                      ,yaxis = dict(title = "acceleration = seconds to reach 60mph")
                      ,hovermode = "closest")





# create a fig from data & layout, and plot the fig
fig= go.Figure(data=data ,layout=layout)
pyo.plot(fig)
