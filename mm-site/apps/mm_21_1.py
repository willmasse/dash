import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
import requests
import plotly.express as px

from app import app
from navbar import Navbar

df = pd.read_excel('assets/RailsToTrails_National Count Data_week.xlsx')
df = df.dropna(axis=0, subset=["Week"])
df["Year"] = df['Year'].astype('int').astype("str")
df["Bike Week"] = df["Bikes (14 counters)"] > df["Pedestrians (14 counters)"]


def agg_func(row):
    if row["Bikes (14 counters)"] >= row["Pedestrians (14 counters)"]:
        return (row['Bikes (14 counters)']/row['Pedestrians (14 counters)'])-1
    else:
        return 0-((row['Pedestrians (14 counters)']/row['Bikes (14 counters)'])-1)

def about_func(row):
    if row["Bikes (14 counters)"] >= row["Pedestrians (14 counters)"]:
        return "Bikers outnumbered Walkers " + str(round(row['Bikes (14 counters)']/row['Pedestrians (14 counters)'], 2)) + " to 1."
    elif row["Bikes (14 counters)"] < row["Pedestrians (14 counters)"]:
        return "Bikers outnumbered Walkers " + str(round(row['Pedestrians (14 counters)']/row['Bikes (14 counters)'], 2)) + " to 1."
    else:
        return "None"


df["Ratio"] = df.apply(agg_func, axis=1)
df["About"] = df.apply(about_func, axis=1)


fig = px.line(df, x="Timeframe", y="Counts (31 counters)", color="Year", labels ={
    "Counts (31 counters)":"Trail Users",
    "Timeframe":"Week"
})


fig_2_text = html.Div([
    dbc.Button(
        html.Div([
            html.H5("Walkers outnumber bikers..."),
            html.P("In 58 weeks out of the 92 weeks observed walkers outnumbered bikers.")
        ]),
        id="button-1", className="mb-2 mr-3 mt-3", color="light"),
    dbc.Button(
        html.Div([
            html.H5("In 2019.."),
            html.P("In 2019 bikers only outnumbered walkers on 13 out of the 46 weeks observed. Walkers seemed to own the trails.")
        ]),
        id="button-2", className="mt-2 mr-3", color="light"),
    dbc.Button(
        html.Div([
            html.H5("But...In 2020 bikers are catching up!"),
            html.P("In 2020 bikers outnumbered walkers in 21 out of the 46 weeks observed. Seems like bikers are getting a bit more common!")
        ]),
        id="button-3", className="mt-3 mr-3", color="light"
    )
])


nav = Navbar()

body = dbc.Container([
    dbc.Row([
        html.H3("Who owns the trails?"),
        html.P(children=[
            html.Span("Rails-to-Trails Conservancy (RTC), a non-profit organization dedicated to making more multi-use walking and biking paths, conducts weekly analysis of their national trail usage. 31 counters hit the trails to count the number of pedestrians and bikers on their trails each week. In an attempt to visualize the impacts of the COVID-19 pandemic on trail-use we compared the ratios of bikers to walkers over the past two years on RTC trails. Check out the visualization below, and "),
            html.Strong("click on our key findings to see them higlighted in the chart!")
        ])
    ], className="justify-content-center m-3"),
    dbc.Row([
        dbc.Col(
            dcc.Graph(id="graph2", config={
        'displayModeBar': False
    }),
            width=8),
        dbc.Col(fig_2_text,width=4)
    ], className="mt-4"),

    dbc.Row([
    html.Em(children=["Visualization by William Masse, Data from ", 
    html.A("Rails to Trails Conservancy", href="https://www.railstotrails.org/about/")])
    ], className="mb-4")
    

])

layout = html.Div([nav, body])

@app.callback(
    Output("graph2", 'figure'),
    Input('button-1', 'n_clicks'),
    Input('button-2', "n_clicks"),
    Input('button-3', "n_clicks")
)
def display(button1, button2, button3):
    ctx = dash.callback_context

    fig2 = px.scatter(df, x="Ratio", y="Timeframe", color="Year", height=800, hover_data={
        "Year":True,
        "Timeframe":True,
        "Ratio":False,
        "About":True
    })
    fig2.update_yaxes(dtick=2, autorange="reversed")
    fig2.update_layout(shapes=[dict(
        type="line",
        yref='paper', y0=0, y1=1,
        xref="x", x0=0, x1=0,
        line=dict(color="Black", width=3, dash="dash")
    )])
    fig2.update_xaxes(
        tickmode="array",
        tickvals=[-2, -1, -.5, 0, .5, 1 ,2],
        ticktext=["3/1", "2/1", "1.5/1", "1/1", "1.5/1", "2/1", "3/1"],
        range=[-3,3],
        side="top"
    )
    fig2.add_annotation(
        x=1,
        y=-1,
        text="More Bikers per Walkers",
        showarrow=False

    )
    fig2.add_annotation(
        x=-1,
        y=-1,
        text="More Walkers per Bikers",
        showarrow=False

    )

    fig2.update_traces(marker=dict(
    size=12,
    line=dict(
        width=2,
        color="DarkSlateGrey")),
    selector=dict(mode="markers")
    )

    for week in df["Timeframe"].unique():
        row_2019 = df.loc[(df["Timeframe"]==week) & (df["Year"]=="2019")]
        row_2020 = df.loc[(df["Timeframe"]==week) & (df["Year"]=="2020")]
        if not pd.isna(row_2019["Ratio"].iloc[0]):
            fig2.add_shape(
                type="line",
                x0=row_2019["Ratio"].iloc[0], y0=week,
                x1=row_2020["Ratio"].iloc[0] , y1=week,
                line_color="#cccccc"
            )

    if not ctx.triggered:
        pass
    else:
        button_id = ctx.triggered[0]['prop_id'].split(".")[0]
        if button_id == "button-1":
            t_df = df[df["Ratio"] < 0]
        elif button_id == "button-2":
            t_df = df[(df["Ratio"]>0)&(df["Year"]=="2019")]
        elif button_id == "button-3":
            t_df = df[(df["Ratio"]>0)&(df["Year"]=="2020")]
        fig2.add_trace(px.scatter(t_df, x="Ratio", y="Timeframe", height=800, hover_data={
        "Year":True,
        "Timeframe":True,
        "Ratio":False,
        "About":True}).update_traces(marker=dict(
                size=12,
                color="rgba(135, 206, 250, 0)",
                line=dict(
                    width=4,
                    color="Black")),
                selector=dict(mode="markers")
                ).data[0])
                
    
    return fig2


