import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import mm_21_1, home

app.title="William Masse"

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
            Input('url', 'pathname'))
def display_page(pathname):
    if pathname =="/mm/2021-w1":
        return mm_21_1.layout
    else:
        return home.layout

if __name__ == '__main__':
    app.run_server(debug=True)