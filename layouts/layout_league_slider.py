from dash import html, dcc
from utils import get_leagues

leagues, data = get_leagues("data/leagues_clubs.csv")

league_slider = html.Div(
    [
        html.Div(
            [
                html.Div(
                    id="selected-league-text",
                    style={
                        "textAlign": "center",
                        "fontSize": "26px",
                        "marginTop": "0px",
                        "color": "white",
                        "paddingLeft": "0px",
                    },
                ),
                html.Hr(
                    style={
                        "border": "none",
                        "borderBottom": "1px solid #ddd",  # Gray line
                        "marginRight": "0px",  # Fixed typo
                        "marginTop": "10px",
                    }
                ),
            ]
        ),
        html.Div(
            [
                # Create the range slider for selecting multiple teams
                dcc.RangeSlider(
                    id="slider-league",
                    className="vertical-slider",
                    min=1,  # The minimum value will be 0 (start of the list)
                    max=100,  # This will be dynamically updated to the number of teams in the selected league - 1
                    step=1,
                    value=[1, 100],
                    marks={i: str(101 - i) for i in range(1, 101, 10)},
                    vertical=True,
                ),
                dcc.Store(id="previous-selected-league", storage_type="memory"),
                dcc.Store(id="selected-teams", storage_type="memory"),
            ],
            style={
                "display": "flex",
                "width": "100%",  # Ensure full width for horizontal centering
                "margin-left": "30px",
            },
        ),
    ]
)
