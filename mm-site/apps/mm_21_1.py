import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import requests
import plotly.express as px

from app import app
from navbar import Navbar

df = pd.read_excel('assets/RailsToTrails_National Count Data_week.xlsx')
df = df.dropna(axis=0, subset=["Week"])
df["BikesPerPed"] = (df['Bikes (14 counters)']/df['Pedestrians (14 counters)'])-1
fig = px.line(df, x="Timeframe", y="Counts (31 counters)", color="Year")
fig2 = px.line(df, x="Timeframe", y="BikesPerPed", color="Year")
nav = Navbar()

body = html.Div([
    dbc.Row([
        dbc.Col(width=4),
        dbc.Col(
            dcc.Graph(figure=fig2, id="line-chart"),
            width=8
        ),
    ])
])

layout = html.Div([nav, body])
