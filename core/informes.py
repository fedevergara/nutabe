import dash_bootstrap_components as dbc
from dash import html

informes_layout = html.Div(
    [
        html.H1(["informes", dbc.Badge("New", className="ms-1")]),
        html.H2(["informes", dbc.Badge("New", className="ms-1")]),
        html.H3(["informes", dbc.Badge("New", className="ms-1")]),
        html.H4(["informes", dbc.Badge("New", className="ms-1")]),
        html.H5(["informes", dbc.Badge("New", className="ms-1")]),
        html.H6(["informes", dbc.Badge("New", className="ms-1")]),
    ]
)