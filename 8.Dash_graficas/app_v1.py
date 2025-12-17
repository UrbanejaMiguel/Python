from dash import Dash, html

# Crear la app
app = Dash(__name__)

# Definir un pequeño interfaz
app.layout = html.Div(
    [html.H1("Mi primera app con dash"), html.P("Está pintando una interfaz en python")]
)

# Arranvar el servidor
if __name__ == "__main__":
    app.run(
        debug=True
    )  # run_server ya no funciona y lo de debug se desactiva cuando se lo pases a cliente
