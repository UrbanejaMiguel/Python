import pandas as pd
from dash import Dash, dash_table, html

df = pd.read_csv("./data/cartera.csv")

# Para ordenar con fecha, convierto el campo "fecha" en un objeto fecha
df["fecha_inicio"] = pd.to_datetime(df["fecha_inicio"], errors="coerce")

app = Dash(__name__)

app.layout = html.Div(
    style={
        "maxWidth": "1100px",
        "margin": "30px 20px",
        "fontFamily": "Arial",
        "color": "#1e1c4a",
    },  # Si solo tiene objetos no hace falta poner children=
    children=[
        html.H2("Cartera de polizas - Tabla filtrable"),
        dash_table.DataTable(
            id="Tabla de polizas",
            columns=[{"name": c, "id": c} for c in df.columns],
            data=df.to_dict("records"),
            # Filtros por columnas (si es numero debe ser =x o >x o <x)
            filter_action="native",
            # Ordenar por columnas
            sort_action="native",
            sort_mode="multi",
            # Paginacion
            page_action="native",
            page_size=10,
            # Estilo de celfa
            style_cell={"padding": "10px", "textAlign": "center"},
        ),
    ],
)

if __name__ == "__main__":
    app.run(debug=True)
