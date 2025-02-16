from dash import html, dcc
from utils import football_pitch_positions

# Layout for the Football Pitch
football_pitch_layout = html.Div(
    [
        html.H2("Select Positions", style={"marginTop": "0px"}),
        # Store for keeping selected players, initialized with all players selected
        dcc.Store(
            id="selected-players-store", data=list(football_pitch_positions().keys())
        ),  # Initialize
        dcc.Graph(
            id="pitch-plot",
            config={"displayModeBar": False},
            style={"marginTop": "95px"},  # Add margin only to the pitch plot
        ),
    ],
    style={"marginTop": "0px"},
)
