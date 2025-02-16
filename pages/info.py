import dash
from dash import html
from layouts.title_bar_layout import title_bar

# Register the Info page
dash.register_page(__name__, path="/info")  # Make sure this is for the home page

layout = html.Div(
    [
        title_bar,
        html.H1("About this app", style={"color": "white", "textAlign": "center"}),
        html.Hr(
            style={
                "border": "none",
                "borderBottom": "1px solid #ddd",  # Gray line
                "marginRight": "0px",  # Fixed typo
                "marginTop": "10px",
                "width": "1300px",
                "margin": "0 auto",  # Center the horizontal rule
            }
        ),
        html.Div(
            [
                html.H5(
                    "This dashboard visualizes pre-processed FIFA 22 player attributes within the selected league. "
                    "Filtered teams are displayed, with the best team highlighted in white, "
                    "while the rest of the league appears in blue. "
                    "You can also select a team for further analysis. The selected team will appear in red. "
                    "The middle section allows you to choose specific players' best positions and view their "
                    "distribution across leagues. "
                    "On the right, you can select a skill set for visualization. "
                    "To get back to home page click on the FIFA 22 text."
                ),
            ],
            style={
                "color": "white",
                "max-width": "1300px",
                "margin": "0 auto",
                "margin-top": "20px",
            },
        ),
        html.H1(
            "How do I interpret these visuals?",
            style={"color": "white", "textAlign": "center"},
        ),
        html.Hr(
            style={
                "border": "none",
                "borderBottom": "1px solid #ddd",  # Gray line
                "marginRight": "0px",  # Fixed typo
                "marginTop": "10px",
                "width": "1300px",
                "margin": "0 auto",  # Center the horizontal rule
            }
        ),
        html.Div(
            [  # Wrap text sections in a div with max-width
                html.H3(
                    "1. Overall Rating Bar Plot",
                    style={"color": "white", "textAlign": "center"},
                ),
                html.H5(
                    "This plot shows the average overall skill rating of all players in the selected league, "
                    "the best team in the league, and the selected team.",
                    style={"color": "white"},
                ),
                html.H3(
                    "2. League Slider", style={"color": "white", "textAlign": "center"}
                ),
                html.H5(
                    "The slider allows you to select teams for analysis and visualization. "
                    "Teams are ranked from highest to lowest based on their average Overall rating. "
                    "The best team is highlighted in white, and the selected team is highlighted in red. "
                    "Unselected teams have adjusted font styles for visual clarity.",
                    style={"color": "white"},
                ),
                html.H3(
                    "3. Football Pitch Figure",
                    style={"color": "white", "textAlign": "center"},
                ),
                html.H5(
                    "This figure allows you to select player positions for analysis. "
                    "Selected positions are highlighted with an orange shirt. "
                    "Clicking on a shirt will select or deselect the corresponding position.",
                    style={"color": "white"},
                ),
                html.H3(
                    "4. Sunburst Figure",
                    style={"color": "white", "textAlign": "center"},
                ),
                html.H5(
                    "This figure displays the distribution of players' best positions across the league. "
                    "The first level shows four position categories, and the second level shows "
                    "the specific positions within each category.",
                    style={"color": "white"},
                ),
                html.H3(
                    "5. Scatter Plot", style={"color": "white", "textAlign": "center"}
                ),
                html.H5(
                    "This plot visualizes the relationship between two selected attributes for all analyzed players. "
                    "Attributes can be chosen using the radio items next to the plot. "
                    "Points are color-coded for the best team, the selected team, and the rest of the league. "
                    "The LOWESS (Locally Weighted Scatterplot Smoothing) line shows the trend of the relationship "
                    "between the two attributes.",
                    style={"color": "white"},
                ),
                html.H3(
                    "6. Violin Plot", style={"color": "white", "textAlign": "center"}
                ),
                html.H5(
                    "This plot shows the distribution of a selected attribute for all analyzed players. "
                    "The distribution is split into two halves: League vs. Best Team. "
                    "Selecting a team from the dropdown will add another distribution, "
                    "comparing the Selected Team vs. League and Selected Team vs. Best Team.",
                    style={"color": "white"},
                ),
                html.H3(
                    "7. Radar Chart", style={"color": "white", "textAlign": "center"}
                ),
                html.H5(
                    "This chart displays the average or median values for each attribute within the selected skill category. "
                    "Use the radio items to switch between average and median calculations.",
                    style={"color": "white"},
                ),
                html.H3("8. Bar Plot", style={"color": "white", "textAlign": "center"}),
                html.H5(
                    "This plot shows the average values of all attributes within the selected skill category, "
                    "grouped by the four position categories.",
                    style={"color": "white"},
                ),
            ],
            style={"max-width": "1300px", "margin": "0 auto", "margin-top": "15px"},
        ),  # Limit text width and center it
    ]
)
