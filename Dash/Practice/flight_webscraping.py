import dash_html_components as html
import dash_core_components as dcc
import dash
from dash.dependencies import Input,Output
import requests
import plotly.graph_objs as go

app = dash.Dash()

app.layout = html.Div([
             html.Div([
             html.Iframe(src="https://www.youtube.com",
                        height = 400 , width = 1350
                        )
             ]),
             html.Div([
             html.Pre(
                       id = "counter_text",
                       children = "Active Flights Worldwide"
                       ),
            dcc.Graph(
                        id = "live-update-graph",
                        style = {"width":1350}

                      ),
            dcc.Interval(id="interval-component",
                         interval = 1000,
                         n_intervals = 0)
                        ])

                        ])

counter_list = []

@app.callback(Output("counter_text","children"),
              [Input("interval-component","n_intervals")]
              )

def update_layout(n):
    url = "https://data-live.flightradar24.com/zones/fcgi/feed.js?faa=1\
           &mlat=1&flarm=1&adsb=1&gnd=1&air=1&vehicles=1&estimated=1&stats=1"
    res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    data = res.json()
    counter = 0
    for element in data["stats"]["total"]:
        counter += data["stats"]["total"][element]
    counter_list.append(counter)
    return 'Active flights worldwide: {}'.format(counter)



@app.callback(Output("live-update-graph","figure"),
              [Input("interval-component","n_intervals")]
              )

def update_graph(n):
    fig = go.Figure(
        data = [go.Scatter(
        x = list(range(len(counter_list))),
        y = counter_list,
        fill = "tozeroy",
        fillcolor = "33ff7d"
        )],
        layout= go.Layout(yaxis =dict(range = [min(counter_list),max(counter_list)]

        ))

        )
    return fig


if __name__ == "__main__":
    app.run_server()
