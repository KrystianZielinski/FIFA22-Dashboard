# layouts/radar_layout.py
from dash import html, dcc
from utils import get_attributes

# Layout for the radar chart and dropdown
dropdown_list = html.Div(
    [
        html.H2("Select Skills"),  # Apply Bootstrap class for light text
        html.Div(
            [
                dcc.Dropdown(
                    id="category-dropdown",
                    options=[
                        {"label": key, "value": key} for key in get_attributes().keys()
                    ],
                    value="Physical Condition",
                    clearable=False,
                    className="custom-dropdown",
                    style={
                        "backgroundColor": "#343434",
                        "color": "white",
                        "width": "225px",  # Optionally set a fixed width
                    },
                ),
                html.Div(
                    [
                        html.Div(
                            id="selected-skills-text",
                            style={
                                "fontSize": "52px",
                                "marginTop": "-50px",
                                "color": "white",
                                "paddingLeft": "75px",
                            },
                        ),
                        html.Hr(
                            style={
                                "border": "none",
                                "borderBottom": "1px solid #ddd",  # Szara linia
                                "marginLeft": "75px",
                                "marginRight": "0x",
                                "marginTop": "10px",
                            }
                        ),
                    ]
                ),
            ],
            style={
                "display": "flex",  # Arranges children horizontally
                "alignItems": "center",  # Vertically centers the children
            },
        ),
    ],
    style={"padding-right": "100px"},
)  # Add some padding
