import dash_bootstrap_components as dbc
from dash import html

index_layout = html.Div(
    [
        html.H1(["Index", dbc.Badge("New", className="ms-1")]),
        html.H2(["Index", dbc.Badge("New", className="ms-1")]),
        html.H3(["Index", dbc.Badge("New", className="ms-1")]),
        html.H4(["Index", dbc.Badge("New", className="ms-1")]),
        html.H5(["Index", dbc.Badge("New", className="ms-1")]),
        html.H6(["Index", dbc.Badge("New", className="ms-1")]),
    ]
)