import dash_html_components as html
import dash_core_components as dcc
import dash
import plotly.graph_objs as go
from dash.dependencies import Input,Output,State
import pandas as pd
import pandas_datareader as web
import datetime as dt

nsdq = pd.read_csv("../data/NASDAQcompanylist.csv")
nsdq.set_index("Symbol",inplace = True)
options = []
for tic in nsdq.index:
    options.append({"label":'{} {}'.format(tic,nsdq.loc[tic]['Name']), 'value':tic})


app = dash.Dash()


app.layout = html.Div([
             html.H1("Stock ticker Dashboard"),
             html.Div([
             html.H3("Select stock ticker",style={"paddingRight":"30px"}),
             dcc.Dropdown(
                        id='stock',
                        options = options,
                        value=['TSLA'],
                        multi = True

                        ),

                        ],style={"display":"inline-block","verticalAlign":"top",'width':"30%"}),
            html.Div([
            html.H3("Select a date range",style={"paddingRight":"30px"}),
            dcc.DatePickerRange(
                        id='my-date-picker-range',
                        min_date_allowed=dt.datetime(2015, 1, 1),
                        max_date_allowed=dt.datetime.today(),
                        start_date=dt.datetime(2017, 1, 1),
                        end_date=dt.datetime.today()
                        )

                        ],style={"display":"inline-block","verticalAlign":"top"}),
            html.Div([
            html.H3("   ",style={"paddingRight":"30px"}),
            html.Button(
                        id = "submit-button",
                        n_clicks = 0,
                        children = "Submit",
                        style = {"fontSize":35,"marginLeft":"30px"}

                        )

                        ],style={"display":"inline-block","paddingTop":"40px"}),

            html.Div([
            dcc.Graph(id = "price-chart",

                    )])

                    ])

@app.callback(
                Output("price-chart","figure"),
                [Input("submit-button","n_clicks")],
                [State("stock","value"),
                State('my-date-picker-range', 'start_date'),
                State('my-date-picker-range', 'end_date')]
            )

def graph(n_clicks,value,start_date,end_date):
    start = start_date
    end = end_date
    traces = []
    for tic in value:
        df=web.DataReader(tic,"yahoo",start,end)
        traces.append({'x':df.index, 'y': df["Adj Close"], 'name':tic})


    figure = {"data":traces,
             "layout":go.Layout(title = "{} Price chart".format(value)
                                )
             }
    return figure


if __name__ == "__main__":
    app.run_server()
