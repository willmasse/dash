import dash_bootstrap_components as dbc

def Navbar():
    navbar = dbc.NavbarSimple(
        children = [
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("2021-W1", href="#"),
                    dbc.DropdownMenuItem("2021-W2", href="#")
                ],
                nav=True,
                in_navbar=True,
                label="Makeover Monday"

            )
        ],
        brand = "William Masse",
        brand_href="#",
        color="primary",
        dark=True
    )

    return navbar