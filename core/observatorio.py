import dash_bootstrap_components as dbc
from dash import html

observatorio_layout = html.Div(
    [
        html.H1(["observatorio", dbc.Badge("New", className="ms-1")]),
        html.H2(["observatorio", dbc.Badge("New", className="ms-1")]),
        html.H3(["observatorio", dbc.Badge("New", className="ms-1")]),
        html.H4(["observatorio", dbc.Badge("New", className="ms-1")]),
        html.H5(["observatorio", dbc.Badge("New", className="ms-1")]),
        html.H6(["observatorio", dbc.Badge("New", className="ms-1")]),
    ]
)