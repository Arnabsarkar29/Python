#######
# Objective: Create a stacked bar chart from
# the file ../data/mocksurvey.csv. Note that questions appear in
# the index (and should be used for the x-axis), while responses
# appear as column labels.  Extra Credit: make a horizontal bar chart!
######

# Perform imports here:
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

# create a DataFrame from the .csv file:

df  = pd.read_csv('H:/Python/Plotly-Dashboards-with-Dash-master/data/mocksurvey.csv',index_col=0)
#print(df)

# create traces using a list comprehension:

data = [go.Bar(x = df.index ,
                y = df[response]
                ,name = response,
                ) for response in df.columns]


# create a layout, remember to set the barmode here



layout = go.Layout(title="Mock Survey Results" , barmode="stack")


# create a fig from data & layout, and plot the fig.

fig = go.Figure(data = data,layout=layout)
pyo.plot(fig)
