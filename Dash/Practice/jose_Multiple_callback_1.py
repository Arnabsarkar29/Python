import dash_html_components as html
import dash
import dash_core_components as dcc
from dash.dependencies import Input,Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv("../data/mpg.csv")

app = dash.Dash()

features =df.columns

app.layout = html.Div([
                html.Div([dcc.Dropdown(id = "xaxis" , options =[{'label':i , 'value':i
                } for i in features ]
                ,value = "displacement")] , style = {"width":'48%' , 'display':"inline-block"})
                ,html.Div([dcc.Dropdown(id = "yaxis" , options =[{'label':i , 'value':i
                } for i in features ]
                ,value = "mpg"
                )], style = {"width":'48%' , 'display':"inline-block"})
                ,html.Div(dcc.Graph(id = "feature-graphic"))

] , style = {"padding":10})


@app.callback(
                Output(component_id = "feature-graphic", component_property="figure")
                ,[Input(component_id = "xaxis", component_property="value")
                ,Input(component_id = "yaxis", component_property="value")]


)

def update_graph(xaxis_name , yaxis_name):
    return{
    'data':[go.Scatter(x=df[xaxis_name], y = df[yaxis_name], text=df['name'] , mode ="markers" , marker={'size':15
    , 'opacity':0.5
    ,'line':{'width':0.5 , "color":"white"}})]
    ,'layout':go.Layout(title="My Dashboard" ,xaxis = {"title":xaxis_name} , yaxis={"title":yaxis_name}
    ,hovermode = "closest")

    }




if __name__ == "__main__":
    app.run_server()
