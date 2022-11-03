import dash
import dash_core_components as  dcc
import dash_html_components as html
from dash.dependencies import Input ,Output


app =  dash.Dash()

app.layout = html.Div(children=[dcc.Input(id = "Input" , value = "Enter Something" ,type ="text")
            ,html.Div(id = "Output")
            ])

@app.callback(
                Output(component_id = "Output" , component_property = "children") ,
                [Input(component_id = "Input" , component_property = "value")]
)

def update_value(input_data):
    try:
        return str("Input is {}".format(float(input_data)**2))
    except :
        return "Some Error"



if __name__ == '__main__':
    app.run_server()
