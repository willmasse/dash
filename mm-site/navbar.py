import dash_bootstrap_components as dbc

def Navbar():
    navbar = dbc.NavbarSimple(
        children = [
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("2021-W1", href="/mm/2021-w1"),
                    dbc.DropdownMenuItem("2021-W2", href="/mm/2021-w2")
                ],
                nav=True,
                in_navbar=True,
                label="Makeover Monday"

            )
        ],
        brand = "William Masse",
        brand_href="/",
        dark=False
    )

    return navbar