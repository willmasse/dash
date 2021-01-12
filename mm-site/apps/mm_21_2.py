import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html


from app import app
from navbar import Navbar


nav = Navbar()

body = dbc.Row([
    html.Iframe(src="https://share.streamlit.io/willmasse/streamlit/mm_2021_w2.py",
    style={"height":"100%", "width":"100%", "frameborder":"0"}
    )
], className="vh-100")

layout = html.Div([nav, body],  id="body-id")
