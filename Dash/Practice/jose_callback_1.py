import dash_html_components as html
import dash
import dash_core_components as dcc
from dash.dependencies import Input,Output

app = dash.Dash()

app.layout = html.Div([
                        dcc.Input(id = "my-id" , value = "Initial Text" , type = "text",style={'border' : '2px solid red'})
                        ,html.Div(id = "my-div", style={'border' : '2px solid blue'})


])

@app.callback(
                Output(component_id = "my-div" , component_property="children")
                ,[Input(component_id = "my-id" , component_property="value")]




)

def update_value(input_value):
    return "You entered {}".format(input_value)

if __name__  =="__main__":
    app.run_server()
