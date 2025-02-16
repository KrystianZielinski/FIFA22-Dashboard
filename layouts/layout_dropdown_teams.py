from dash import html, dcc

dropdown_teams = html.Div(
    [
        html.H2("Select Team", style={"padding-top": "20px"}),
        dcc.Dropdown(
            id="dropdown-teams",
            placeholder="Select a team",
            className="custom-dropdown",
            clearable=True,
        ),
    ]
)
