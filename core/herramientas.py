import dash_bootstrap_components as dbc
from dash import html

herramientas_layout = html.Div(
    [
        html.H1(["herramientas", dbc.Badge("New", className="ms-1")]),
        html.H2(["herramientas", dbc.Badge("New", className="ms-1")]),
        html.H3(["herramientas", dbc.Badge("New", className="ms-1")]),
        html.H4(["herramientas", dbc.Badge("New", className="ms-1")]),
        html.H5(["herramientas", dbc.Badge("New", className="ms-1")]),
        html.H6(["herramientas", dbc.Badge("New", className="ms-1")]),
    ]
)