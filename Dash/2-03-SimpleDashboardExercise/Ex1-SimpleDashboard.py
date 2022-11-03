#######
# Objective: build a dashboard that imports OldFaithful.csv
# from the data directory, and displays a scatterplot.
# The field names are:
# 'D' = date of recordings in month (in August),
# 'X' = duration of the current eruption in minutes (to nearest 0.1 minute),
# 'Y' = waiting time until the next eruption in minutes (to nearest minute).
######

# Perform imports here:
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import plotly.offline as pyo

# Launch the application:

app = dash.Dash()

# Create a DataFrame from the .csv file:

df = pd.read_csv("H:/Python/Plotly-Dashboards-with-Dash-master/data/OldFaithful.csv")

# Create a Dash layout that contains a Graph component:

graph = [go.Scatter(x=df["X"]
                    ,y =df["Y"]
                    ,mode="markers"
                    ,marker=dict(size = 12 , color = 'blue' , symbol = "pentagon" , line = dict(width = 3))

                    )]


layout = go.Layout(title="OldFaithful"
                ,xaxis = dict(title = " duration of the current eruption in minutes (to nearest 0.1 minute)")
                ,yaxis=dict(title = "waiting time until the next eruption in minutes (to nearest minute)")

                )

figure = go.Figure(data = graph , layout=layout)

#pyo.plot(figure)

app.layout = html.Div([dcc.Graph(id = "Sactter 1"
                                    ,figure = figure)
                        ])



if __name__ == '__main__':
    app.run_server()






# Add the server clause:
