import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import Dash, Input, Output, dash_table, dcc, html

# INCOMPLETO --> Ir a lo del profesor

# Importacion de datos
data = pd.read_csv("./data/cartera.csv")
app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# Asegurarnos que prima_anual sea numerica
data["prima_anual"] = pd.to_numeric(data["prima_anual"], errors="coerce")

# Agrupacion por producto: suma de prima anual por producto
tabla_resumen = (
    data.dropna(subset=["producto", "prima_anual"])
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
fig.update_layout(
    xaxis_title="Producto",
    yaxis_title="Prima anual total",
    margin=dict(l=40, r=20, t=60, b=40),
)

app.layout = dbc.Container(
    fluid=True,
    style={"height": "100vh", "padding": "20px"},
    children=[
        # Primera fila: Título + botón | Gráfica
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            html.H2("Dashboard simple con gráfica"),
                            html.Br(),
                            dbc.Button(
                                "Mostrar tabla", id="btn-tabla", color="primary"
                            ),
                        ],
                        style={
                            "display": "flex",
                            "flexDirection": "column",
                            "justifyContent": "center",
                            "alignItems": "center",
                            "height": "100%",
                        },
                    ),
                    width=6,
                ),
                dbc.Col(
                    html.Div(
                        dcc.Graph(
                            figure=fig, style={"height": "45vh", "width": "100%"}
                        ),
                        style={"height": "100%"},
                    ),
                    width=6,
                ),
            ],
            style={"height": "50vh"},
        ),
        # Segunda fila: Tabla (ocupa todo el ancho)
        dbc.Row(
            dbc.Col(
                html.Div(
                    id="contenedor-tabla", style={"width": "100%", "marginTop": "20px"}
                ),
                width=12,
            ),
            style={"height": "auto"},
        ),
    ],
)


@app.callback(
    Output("contenedor-tabla", "children"),
    Input("btn-tabla", "n_clicks"),
)
def mostrar_tabla(n_clicks):
    if not n_clicks:
        return ""
    return dash_table.DataTable(
        data=tabla_resumen.to_dict("records"),
        columns=[{"name": col, "id": col} for col in tabla_resumen.columns],
        page_size=10,
        filter_action="native",
        style_table={"width": "100%"},
        style_cell={
            "backgroundColor": "#1b1b1b",
            "color": "white",
            "textAlign": "left",
            "font-family": "Roboto, Arial, sans-serif",
        },
        style_header={
            "backgroundColor": "#222222",
            "color": "white",
            "fontWeight": "bold",
        },
    )


if __name__ == "__main__":
    app.run(debug=True)
