import dash_bootstrap_components as dbc
from dash import html

index_layout = html.Div(
    [
        html.Main(
            html.Div([
                html.H1("¡Bienvenido!"),
                html.P("Este portal que está en construcción, se dedicará a ofrecer indicadores, informes y herramientas para Dirección de Relaciones Internacionales de la Universidad de Antioquia.", className="lead"),
        ], className="bg-body-tertiary p-4 rounded"), className="container"),
    ]
)