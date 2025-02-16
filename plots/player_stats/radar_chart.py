import plotly.graph_objects as go
from utils import get_attributes, colors
from plots.player_stats.radar_chart_empty import create_radar_chart_empty


def create_radar_chart(
    teams_in_league,
    selected_team1,
    selected_team2,
    selected_category="Physical Condition",
    aggregation_method="Average",
):
    if teams_in_league.empty:
        fig = create_radar_chart_empty(selected_category)
        return fig

    fig = go.Figure()
    # Get the attribute categories and their corresponding values
    all_attributes = get_attributes()
    # Get the selected attributes for the category
    selected_attributes = all_attributes[selected_category]

    # Get club names
    league_name = teams_in_league["Club"].iloc[0]
    if not selected_team1.empty:
        top_club_name = selected_team1["Club"].iloc[0]
    if not selected_team2.empty:
        main_club_name = selected_team2["Club"].iloc[0]

    if aggregation_method == "Average":
        # Compute averages for the selected category
        stats_league = [teams_in_league[attr].mean() for attr in selected_attributes]
        if not selected_team1.empty:
            stats_team1 = [selected_team1[attr].mean() for attr in selected_attributes]
        if not selected_team2.empty:
            stats_team2 = [selected_team2[attr].mean() for attr in selected_attributes]
    else:
        # Compute median for the selected category
        stats_league = [teams_in_league[attr].median() for attr in selected_attributes]
        if not selected_team1.empty:
            stats_team1 = [
                selected_team1[attr].median() for attr in selected_attributes
            ]
        if not selected_team2.empty:
            stats_team2 = [
                selected_team2[attr].median() for attr in selected_attributes
            ]

    low_color, medium_color, high_color = colors()

    # print(low_color, medium_color, high_color)
    low_color_rgba = "rgba(196, 60, 60, 0.3)"
    medium_color_rgba = "rgba(250, 233, 233, 0.3)"
    high_color_rgba = "rgba(19, 75, 135, 0.3)"

    # Add the traces for both teams
    fig.add_trace(
        go.Scatterpolar(
            r=stats_league,
            theta=selected_attributes,
            fill="toself",
            name=league_name,
            fillcolor=high_color_rgba,  # Transparent fill (0 alpha value)
            line=dict(color=high_color, width=2),
        )
    )

    if not selected_team1.empty:
        fig.add_trace(
            go.Scatterpolar(
                r=stats_team1,
                theta=selected_attributes,
                fill="toself",
                name=top_club_name,
                fillcolor=medium_color_rgba,  # Transparent blue fill,  # Transparent fill (0 alpha value)
                line=dict(color=medium_color, width=2),
            )
        )

    if not selected_team2.empty:
        fig.add_trace(
            go.Scatterpolar(
                r=stats_team2,
                theta=selected_attributes,
                fill="toself",
                name=main_club_name,
                fillcolor=low_color_rgba,  # Transparent fill (0 alpha value)
                line=dict(color=low_color, width=2),
            )
        )

    # Update layout
    fig.update_layout(
        margin=dict(l=125, r=125, t=75, b=0),
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                tickfont=dict(
                    family="Roboto, Arial, sans-serif",  # Font family for radial axis
                    size=12,  # Font size for radial axis labels
                ),
            ),
            angularaxis=dict(
                tickfont=dict(
                    family="Roboto, Arial, sans-serif",  # Font family for angular axis (attributes)
                    size=16,  # Font size for angular axis labels
                )
            ),
        ),
        width=650,
        height=650,
        title={
            "text": f"Radar Chart: {selected_category}",  # Dynamic title text
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
            orientation="h",  # Horizontal legend
            yanchor="bottom",  # Align legend to the bottom of its box
            y=0.88,  # Place legend above the plot
            xanchor="left",  # Align legend to the left
            x=-0.2,  # Start from the left
            font=dict(
                family="Roboto, Arial, sans-serif",  # Set the font to Roboto
                size=15,  # Increase the font size
            ),
        ),
    )

    return fig
