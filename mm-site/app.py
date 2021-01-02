import dash
import dash_bootstrap_components as dbc

external_stylesheets = [
    dbc.themes.LITERA
    ]

external_scripts = [
    {
        'src':"https://kit.fontawesome.com/d635403d5c.js",
        'crossorigin':'anonymous'
    }
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, external_scripts=external_scripts, suppress_callback_exceptions=True)

server = app.server