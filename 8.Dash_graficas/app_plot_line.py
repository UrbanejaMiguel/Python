import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

# Importacion de datos
data = pd.read_excel("./data/mortalidad.xlsx")
app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H2("Probabilidad de fallecimiento en funcion de la edad"),
        dcc.Store(id="store-data", data=data.to_dict("records")),
        dcc.Graph(id="grafica"),
    ]
)


@app.callback(Output("grafica", "figure"), Input("store-data", "data"))
def plot_show(data):
    fig = px.line(data, x="edad", y="qx", title="Tabla de mortalidad")
    return fig


if __name__ == "__main__":
    app.run(debug=True)
