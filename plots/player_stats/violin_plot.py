import plotly.graph_objects as go
from plots.player_stats.violin_plot_empty import create_violin_plot_empty
from utils import colors


def create_violin_plot(league_teams, selected_team1, selected_team2, selected_category):
    if league_teams.empty:
        fig = create_violin_plot_empty(selected_category)
        return fig

    # Get club names
    league_teams_name = league_teams["Club"].iloc[0]
    if not selected_team1.empty:
        top_club_name = selected_team1["Club"].iloc[0]
    if not selected_team2.empty:
        main_club_name = selected_team2["Club"].iloc[0]

    fig = go.Figure()

    low_color, medium_color, high_color = colors()

    if selected_team2.empty:
        # Only one group if selected_team2 is missing
        fig.add_trace(
            go.Violin(
                x=["League vs Best Team"] * len(league_teams[selected_category]),
                y=league_teams[selected_category],
                legendgroup=league_teams_name,
                scalegroup="League vs Best Team",
                name=f"{league_teams_name}",
                side="negative",
                box_visible=True,
                meanline_visible=True,
                points="all",
                line_color=high_color,
            )
        )

        if not selected_team1.empty:
            fig.add_trace(
                go.Violin(
                    x=["League vs Best Team"] * len(selected_team1[selected_category]),
                    y=selected_team1[selected_category],
                    legendgroup=top_club_name,
                    scalegroup="League vs Best Team",
                    name=f"{top_club_name}",
                    side="positive",
                    box_visible=True,
                    meanline_visible=True,
                    points="all",
                    line_color=medium_color,
                )
            )
    else:
        fig.add_trace(
            go.Violin(
                x=["Selected Team vs League"] * len(league_teams[selected_category]),
                y=league_teams[selected_category],
                legendgroup=league_teams_name,
                scalegroup="Selected Team vs League",
                name=f"{league_teams_name}",
                side="positive",
                box_visible=True,
                meanline_visible=True,
                points="all",
                line_color=high_color,
            )
        )

        fig.add_trace(
            go.Violin(
                x=["Selected Team vs League"] * len(selected_team2[selected_category]),
                y=selected_team2[selected_category],
                legendgroup=main_club_name,
                scalegroup="Selected Team vs League",
                name=f"{main_club_name}",
                side="negative",
                box_visible=True,
                meanline_visible=True,
                points="all",
                line_color=low_color,
            )
        )

        fig.add_trace(
            go.Violin(
                x=["Selected Team vs Best Team"]
                * len(selected_team1[selected_category]),
                y=selected_team1[selected_category],
                legendgroup=top_club_name,
                scalegroup="Selected Team vs Best Team",
                name=f"{top_club_name}",
                side="positive",
                box_visible=True,
                meanline_visible=True,
                points="all",
                line_color=medium_color,
            )
        )

        fig.add_trace(
            go.Violin(
                x=["Selected Team vs Best Team"]
                * len(selected_team2[selected_category]),
                y=selected_team2[selected_category],
                showlegend=False,
                scalegroup="Selected Team vs Best Team",
                side="negative",
                box_visible=True,
                meanline_visible=True,
                points="all",
                line_color=low_color,  # Default Plotly blue
            )
        )

    # Update layout
    fig.update_layout(
        title={
            "text": f"Violin Plot: {selected_category}",  # Dynamic title text
            "x": 0.5,  # Centers title horizontally
            "xanchor": "center",  # Ensures proper centering
            "yanchor": "top",  # Keeps title anchored at the top
            "y": 0.95,
        },  # Moves title slightly higher
        title_font=dict(
            family="Roboto, Arial, sans-serif",  # Font family
            size=22,  # Font size
            weight="bold",
        ),
        yaxis_title=f"{selected_category}",
        violingap=0.2,
        violinmode="overlay",
        width=1025,
        height=525,
        xaxis_title="",
        showlegend=True,
        legend=dict(
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
        margin=dict(t=110, r=200, b=20),
    )

    return fig
