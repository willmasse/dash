import dash_bootstrap_components as dbc
import dash_html_components as html

from app import app
from navbar import Navbar

nav = Navbar()

social = dbc.Row([
    dbc.Col([html.A(html.I(className="fab fa-linkedin fa-4x"),href="https://www.linkedin.com/in/willmasse/"),html.Br(),html.P("LinkedIn", className='lead')],className="text-center"),
    dbc.Col([html.A(html.I(className="fab fa-medium fa-4x"), href="https://willmasse.medium.com/"),html.Br(), html.P("Medium", className='lead')],className="text-center"),
    dbc.Col([html.A(html.I(className="fab fa-twitter-square fa-4x"), href="https://twitter.com/willmasse2"),html.Br(), html.P("Twitter", className='lead')],className="text-center")
], className="justify-content-center mt-3")

jumbotron = dbc.Jumbotron(
    [
        dbc.Container(
            [
                dbc.Row([
                    dbc.Col([html.Img(src="https://media-exp1.licdn.com/dms/image/C4D03AQHg1_GizmYZvQ/profile-displayphoto-shrink_200_200/0/1552605908647?e=1614816000&v=beta&t=h2nITY04SgHosjEg_tGzvInArUbKWETjw2aO8gXQG8g", className="rounded-circle")], className="text-center", width=4),
                    dbc.Col([
                        html.H3("About Me"),
                        html.P(
                            "My name is William Masse. I'm a Data Analyst whose passion is transforming data into interactive and compelling visulizations.",
                            className="lead"),
                        html.Div([
                            dbc.Badge("Python", pill=True, color="secondary", className="m-2"),
                            dbc.Badge("R", pill=True, color="secondary", className="m-2"),
                            dbc.Badge("SQL", pill=True, color="secondary", className="m-2"),
                            dbc.Badge("Web (HTML, CSS, Javascript)", pill=True, color="secondary", className="m-2"),
                            dbc.Badge("Django", pill=True, color="secondary", className="m-2"),
                            dbc.Badge("Visualization (Matplotlib, Altair, Highcharts)", pill=True, color="secondary", className="m-2"),
                            dbc.Badge("Plotly/Dash", pill=True, color="secondary", className="m-2"),
                            dbc.Badge("Tableau", pill=True, color="secondary", className="m-2"),
                        ]),
                    ]),
                ]),
            ],
            fluid=True,
        ),
        html.Hr(),
        social
    ],
    className="m-4", id="my_jumbo"
)



cards = dbc.Row([
    dbc.Card(
        dbc.CardBody(
            [
                html.H5("MM VIZ 2021 - Week 1", className="card-title"),
                html.H6("Who owns the trails?", className="card-subtitle"),
                html.P(
                    "Comparing the ratio of bikers and walkers week over week. Using plotly.",
                    className="card-text",
                ),
                dbc.CardLink("View", href="/mm/2021-w1"),
            ]
        ),
        style={"width": "18rem"}, className="m-3"
    ),
    dbc.Card(
        dbc.CardBody(
            [
                html.H5("MM VIZ 2021 - Week 2", className="card-title"),
                html.H6("Operation Fistula - HIV and Gender", className="card-subtitle"),
                html.P(
                    "Exploring the Gender Gap in HIV Infection Rate in Sub-Saharan Africa. Using streamlit.",
                    className="card-text",
                ),
                dbc.CardLink("View", href="/mm/2021-w2"),
            ]
        ),
        style={"width": "18rem"}, className="m-3"
    ),

], className="m-4")


body = dbc.Container([
    jumbotron,
    cards
])

layout = html.Div([nav, body])
