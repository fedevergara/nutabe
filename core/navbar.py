import dash_bootstrap_components as dbc
from dash import html

DRI_LOGO = "static/images/icons/send.svg"

# Crear el menú desplegable de Informes
dropdown_informes = dbc.DropdownMenu(
    label="Informes",
    children=[
        dbc.DropdownMenuItem("Academia Glocal", href="/informes_academia"),
        dbc.DropdownMenuItem("Convenios próximos a vencer", href="/informes_convenios"),
        dbc.DropdownMenuItem("Movilidad Internacional", href="/informes_movilidad"),
        dbc.DropdownMenuItem("SNIES", href="/informes_snies"),
    ],
    className="white",
    nav=True,
)

# Crear el menú desplegable de Herramientas
dropdown_herramientas = dbc.DropdownMenu(
    label="Herramientas",
    children=[
        dbc.DropdownMenuItem("Cartas de invitación", href="/herramientas_cartas"),
        dbc.DropdownMenuItem("Formulario asistencia a eventos", href="/herramientas_eventos"),
        dbc.DropdownMenuItem("Formulario registro de movilidad", href="/herramientas_movilidad"),
    ],
    nav=True,
)
observatorio = dbc.NavItem(dbc.NavLink("Observatorio", href="/observatorio", class_name="text-white", id="observatorio"))

navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.NavbarBrand(
                html.Img(
                    src=DRI_LOGO,
                    height="30px",
                ), href="/",
            ),
            dbc.NavbarBrand("Nutabe", className="ms-2", href="/"),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                dbc.Nav(
                    [dropdown_informes, dropdown_herramientas, observatorio],
                    className="ms-auto",
                    navbar=True,
                ),
                id="navbar-collapse",
                navbar=True,
                is_open=False,
            ),
        ]
    ),
    color="#007473",
    dark=True,
    className="b-5",
)