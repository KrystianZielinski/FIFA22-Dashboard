import plotly.express as px
from utils import positions_category, get_attributes, colors
import pandas as pd


def create_bar_plot(teams_in_league, selected_team1, selected_team2, selected_category):
    attributes = get_attributes()

    def calculate_avg(df, category):
        cols = attributes.get(category, [])  # Get the relevant attribute columns
        existing_cols = [
            col for col in cols if col in df.columns
        ]  # Ensure columns exist in DataFrame
        if not existing_cols:
            return f"No matching columns found for '{category}'"
        return df[existing_cols].mean(axis=1)  # Calculate row-wise average

    position_cat = positions_category()
    position_map = {pos: key for key, values in position_cat.items() for pos in values}

    teams_in_league["Position Category"] = teams_in_league["Best Position"].map(
        position_map
    )
    teams_in_league["Category Avg"] = calculate_avg(teams_in_league, selected_category)
    avg_teams_in_league = (
        teams_in_league.groupby("Position Category")
        .agg(
            {
                "Category Avg": "mean",
                "Club": "first",  # Keep the first value of 'Club' for each group
            }
        )
        .reset_index()
    )

    selected_team1["Position Category"] = selected_team1["Best Position"].map(
        position_map
    )
    selected_team1["Category Avg"] = calculate_avg(selected_team1, selected_category)
    avg_selected_team1 = (
        selected_team1.groupby("Position Category")
        .agg({"Category Avg": "mean", "Club": "first"})
        .reset_index()
    )

    if not selected_team2.empty:
        selected_team2["Position Category"] = selected_team2["Best Position"].map(
            position_map
        )
        selected_team2["Category Avg"] = calculate_avg(
            selected_team2, selected_category
        )
        avg_selected_team2 = (
            selected_team2.groupby("Position Category")
            .agg({"Category Avg": "mean", "Club": "first"})
            .reset_index()
        )
        df_combined = pd.concat(
            [avg_teams_in_league, avg_selected_team1, avg_selected_team2]
        )

    # Concatenate the three DataFrames into a single DataFrame
    else:
        df_combined = pd.concat([avg_teams_in_league, avg_selected_team1])

    low_color, medium_color, high_color = colors()

    fig = px.bar(
        df_combined,
        x="Position Category",
        y="Category Avg",
        color="Club",  # Different colors for each team/group
        color_discrete_sequence=[high_color, medium_color, low_color],
        labels={
            "Position Category": "Position Category",
            "Category Avg": f"Average {selected_category}",
            "Club": "Club",
        },
        barmode="group",  # This ensures the bars are grouped
        text="Category Avg",
        text_auto=".1f",
        category_orders={
            "Position Category": ["GK", "DEF", "MID", "ATK"]
        },  # Specify the order here
    )  # Optional: add text labels on the bars

    # Update layout
    fig.update_layout(
        margin=dict(t=110),
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        width=650,
        height=550,
        title={
            "text": f"{selected_category} Across Positions",  # Dynamic title text
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
