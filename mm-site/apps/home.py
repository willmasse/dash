import dash_bootstrap_components as dbc
import dash_html_components as html

from app import app
from navbar import Navbar

nav = Navbar()

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
                        dbc.Row([
                            html.A(html.I(className="fab fa-linkedin fa-4x"),href="https://www.linkedin.com/in/willmasse/"),
                            html.A(html.I(className="fab fa-medium fa-4x"), href="https://willmasse.medium.com/"),
                            html.A(html.I(className="fab fa-twitter-square fa-4x"), href="https://twitter.com/willmasse2"),
                        ], className="justify-content-around")
                    ]),
                ])
            ],
            fluid=True,
        )
    ],
    className="m-3"
)

cards = html.Div([
    dbc.Card(
        dbc.CardBody(
            [
                html.H4("Title", className="card-title"),
                html.H6("Card subtitle", className="card-subtitle"),
                html.P(
                    "Some quick example text to build on the card title and make "
                    "up the bulk of the card's content.",
                    className="card-text",
                ),
                dbc.CardLink("Card link", href="#"),
                dbc.CardLink("External link", href="https://google.com"),
            ]
        ),
        style={"width": "18rem"},
    )
], className="m-3")


body = html.Div([
    jumbotron,
    cards
])

layout = html.Div([nav, body])
