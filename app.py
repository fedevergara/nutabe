import dash
import dash_bootstrap_components as dbc
from core.navbar import navbar
from dash import Input, Output, State, html, dcc
from core.index import index_layout
from core.herramientas import herramientas_layout
from core.informes import informes_layout
from core.observatorio import observatorio_layout

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

#app.layout = html.Div([navbar, badges])
# Define el layout con el componente dcc.Location
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
])

# Callback para actualizar el contenido de la página según la URL
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])

def display_page(pathname):
    print(f"Pathname: {pathname}")
    if pathname == '/':
        return [navbar, index_layout]  # Página principal con el índice
    elif pathname == '/informes_academia':
        return [navbar, informes_layout]
    elif pathname == '/informes_convenios':
        return [navbar, informes_layout]
    elif pathname == '/informes_movilidad':
        return [navbar, informes_layout]
    elif pathname == '/informes_snies':
        return [navbar, informes_layout]
    elif pathname == '/herramientas_cartas':
        return [navbar, herramientas_layout]
    elif pathname == '/herramientas_eventos':
        return [navbar, herramientas_layout]
    elif pathname == '/herramientas_movilidad':
        return [navbar, herramientas_layout]
    elif pathname == '/observatorio':
        return [navbar, observatorio_layout]
    else:
        return '404 Page Not Found'


# add callback for toggling the collapse on small screens
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")]
)
def toggle_navbar_collapse(n_clicks, is_open):
    if n_clicks:
        return not is_open
    return is_open

if __name__ == "__main__":
    app.run_server(debug=True)