from dash import Dash, dcc, html
from dash.dependencies import Input, Output

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H2("Calculo de prima simple"),
        html.Label("Introduce la edad "),
        dcc.Input(id="edad", type="number"),
        html.Label("Capital asegurado "),
        dcc.Input(id="capital", type="number", value=100000),
        html.Br(),  # Linea grafica horizontal para separar elementos
        html.Div(id="resultado"),
    ]
)


@app.callback(  # Primero van los Outputs
    Output("resultado", "children"),  # children sinifica dentro del objeto
    Input("edad", "value"),
    Input("capital", "value"),
)  # Funcion decoradora que va siempre pegada por arriba a la funcion que decorta
def cal_prima(edad, capital):
    if edad is None:
        return "Introduce una edad valida"

    if capital is None:
        return "Introduce un capital valido"

    prima = edad * capital

    return f"La prima anual estimada es {prima}€"


if __name__ == "__main__":
    app.run(debug=True)
