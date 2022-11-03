#######
# Objective: Create a dashboard that takes in two or more
# input values and returns their product as the output.
######

# Perform imports here:
import numpy as np
import dash_html_components as html
import dash_core_components as dcc
import dash
from dash.dependencies import Input , Output

# Launch the application:

app = dash.Dash()

# Create a Dash layout that contains input components
# and at least one output. Assign IDs to each component:



app.layout = html.Div([
                        dcc.RangeSlider(
                            id='my-range-slider',
                            min=-5,
                            max=6,
                            marks = {i:str(i) for i in range(-5,6)},
                            step=1,
                            value=[-3, 7]
                        ),
                        html.Div(html.H1(id = "output"))
                        ])

# Create a Dash callback:

@app.callback(Output(component_id ='output' , component_property='children'),
                [Input(component_id = 'my-range-slider' , component_property='value')])

def callback_a(value):
    return "{}".format(value[0]*value[1])

# Add the server clause:

if __name__ == "__main__":
    app.run_server()
