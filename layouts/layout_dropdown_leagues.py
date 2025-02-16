from dash import html, dcc
from utils import get_leagues

leagues, data = get_leagues("data/leagues_clubs.csv")
# Define the layout of the app
dropdown_leagues = html.Div(
    [
        html.H2("Select League"),  # Add spacing below
        # Dropdown for selecting league
        dcc.Dropdown(
            id="dropdown-leagues",  # The ID used in callbacks
            value=leagues[0],
            options=[{"label": league, "value": league} for league in leagues],
            placeholder="Select a league",
            className="custom-dropdown",
            clearable=False,
        ),
    ],
    style={"marginTop": "0px"},
)  # Move the entire container up
