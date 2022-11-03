


import dash_core_components as dcc
import dash_html_components as html
import dash
from dash.dependencies import Input,Output , State

app = dash.Dash()

app.layout  = html.Div([
                        dcc.Input(
                                    id  = "input",
                                    type='text',
                                    value='Enter a value...',style = {'fontSize':24}),
                        html.Button(id="submit_button",n_clicks = 0 ,children = "Submit" , style = {"fontSize":24}),
                        html.Hr(),
                        html.H1(id="output",style = {'fontSize':24})
                            ])

@app.callback(
                Output(component_id = "output" , component_property="children"),
                [Input(component_id = "submit_button",component_property="n_clicks")],
                [State(component_id = "input" ,component_property="value")]
)

def output_state(n_clicks,value):
    return('{} was typed in and button was clicked {} times'.format(value,n_clicks))

if __name__ == "__main__":
    app.run_server()
