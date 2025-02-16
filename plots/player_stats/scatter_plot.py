import plotly.express as px
import pandas as pd
from utils import colors


def create_scatter_plot(
    teams_in_league,
    selected_team1,
    selected_team2,
    selected_category_x,
    selected_category_y,
):
    if teams_in_league.empty:
        data = pd.DataFrame(columns=[selected_category_x, selected_category_y])

        # Create an empty px.scatter plot
        fig = px.scatter(
            data,
            x=selected_category_x,
            y=selected_category_y,
            title="Scatter Plot: No data",
        )

        fig.add_annotation(
            x=0.5,
            y=0.5,
            text="No data",
            showarrow=False,
            font=dict(size=16),
            xref="paper",
            yref="paper",  # Position in the center of the plot
        )

        fig.update_layout(
            width=1025,  # Set the plot width
            height=575,  # Set the plot height
            title={
                "x": 0.5,  # Centers title
                "xanchor": "center",  # Ensures true centering
                "yanchor": "top",
                "y": 0.95,  # Moves title higher up
            },
            title_font=dict(
                family="Roboto, Arial, sans-serif",  # Dashboard-friendly fonts
                size=22,  # Font size
                weight="bold",  # Make the font bold
            ),
            margin=dict(t=110, r=200),
        )

        return fig

    scatter_data = pd.concat([teams_in_league, selected_team1, selected_team2])

    # Generate dynamic title
    chosen_set_title = f"{selected_category_x} vs {selected_category_y} "

    low_color, medium_color, high_color = colors()

    fig = px.scatter(
        scatter_data,
        x=selected_category_x,
        y=selected_category_y,
        title="Scatter Plot: " + chosen_set_title,
        color="Club",
        color_discrete_sequence=[high_color, medium_color, low_color],
        hover_data=[
            "Original Club",
            "Name",
            "Best Position",
        ],  # Include 'Name' in the hover information
        labels={
            selected_category_x: selected_category_x,
            selected_category_y: selected_category_y,
            "Name": "Player Name",
            "Original Club": "Club",
        },
        trendline="lowess",
    )

    fig.update_layout(
        width=1025,  # Set the plot width
        height=550,  # Set the plot height
        title={
            "x": 0.5,  # Centers title
            "xanchor": "center",  # Ensures true centering
            "yanchor": "top",
            "y": 0.95,  # Moves title higher up
        },
        title_font=dict(
            family="Roboto, Arial, sans-serif",  # Dashboard-friendly fonts
            size=22,  # Font size
            weight="bold",  # Make the font bold
        ),
        legend=dict(
            title=None,
            orientation="h",  # Horizontal legend
            yanchor="bottom",  # Align legend to the bottom of its box
            y=1.02,  # Place legend above the plot
            xanchor="left",  # Ensures true centering
            x=0,  # Start from the left
            font=dict(
                family="Roboto, Arial, sans-serif",  # Set the font to Roboto
                size=15,  # Increase the font size
            ),
        ),
        margin=dict(t=110, r=200),
    )

    return fig
