import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

dbc

# Importacion de datos
data = pd.read_csv("./data/cartera.csv")
app = Dash(__name__)

# Asegurarnos que prima_anual sea numerica
data["prima_anual"] = pd.to_numeric(data["prima_anual"], errors="coerce")

# Agrupacion por producto: suma de prima anual por producto
tabla_resumen = (
    (data.dropna(subset=["prodcuto", "prima_anual"]))
    .groupby("producto", as_index=False)["prima_anual"]
    .sum()
    .sort_values("prima_anual", ascending=False)
)

fig = px.bar(
    tabla_resumen,
    x="producto",
    y="prima_anual",
    title="Suma de prima anual por producto",
    template="plotly_dark",
)
fig.update_layout(xaxis_title="Producto", yaxis_title="Prima anual total")

app.layout = html.Div(
    children=[
        html.H2("Probabilidad de fallecimiento en funcion de la edad"),
        dcc.Store(id="store-data", data=data.to_dict("records")),
        dcc.Graph(id="grafica"),
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
