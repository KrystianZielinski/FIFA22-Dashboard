import plotly.express as px
import pandas as pd
from utils import colors


def create_horizontal_bar_plot(teams_in_league, selected_team1, selected_team2):
    teams_in_league_overall = teams_in_league["Overall"].mean()
    selected_team1_overall = selected_team1["Overall"].mean()

    if not selected_team2.empty:
        selected_team2_overall = selected_team2["Overall"].mean()

        df = pd.DataFrame(
            {
                "Club": [
                    teams_in_league["Club"].iloc[0],
                    selected_team1["Club"].iloc[0],
                    selected_team2["Club"].iloc[0],
                ],
                "Overall": [
                    teams_in_league_overall,
                    selected_team1_overall,
                    selected_team2_overall,
                ],
            }
        )
    else:
        df = pd.DataFrame(
            {
                "Club": [
                    teams_in_league["Club"].iloc[0],
                    selected_team1["Club"].iloc[0],
                ],
                "Overall": [teams_in_league_overall, selected_team1_overall],
            }
        )

    low_color, medium_color, high_color = colors()

    fig = px.bar(
        df,
        x="Overall",
        y="Club",
        color="Club",
        orientation="h",
        color_discrete_sequence=[high_color, medium_color, low_color],
        text_auto=".1f",
    )

    # Update layout
    fig.update_layout(
        margin=dict(t=115, r=10, l=10, b=50),
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        width=350,
        height=300,
        title={
            "text": "Overall Skill",  # Dynamic title text
            "x": 0.5,  # Centers title horizontally
            "xanchor": "center",  # Ensures proper centering
            "yanchor": "top",  # Keeps title anchored at the top
            "y": 0.96,
        },  # Moves title slightly higher
        title_font=dict(
            family="Roboto, Arial, sans-serif",  # Font family
            size=22,  # Font size
            weight="bold",
        ),
        yaxis_title=None,
        yaxis_showticklabels=False,
        hovermode="closest",
        legend=dict(
            title=None,
            orientation="h",  # Horizontal legend
            yanchor="bottom",  # Align legend to the bottom of its box
            y=1.02,  # Place legend above the plot
            xanchor="left",  # Align legend to the left
            x=0.0,  # Start from the left
            font=dict(
                family="Roboto, Arial, sans-serif",  # Set the font to Roboto
                size=15,  # Increase the font size
            ),
        ),
    )

    return fig
