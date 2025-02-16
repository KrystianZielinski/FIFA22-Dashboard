import pandas as pd
import plotly.express as px


def create_violin_plot_empty(selected_category):
    data = pd.DataFrame(columns=[selected_category])  # Create empty DataFrame

    # Create an empty violin plot
    fig = px.violin(
        data, y=selected_category, title="Violin Plot: No Data", box=True, points="all"
    )  # Keep structure intact

    # Add annotation to indicate no data
    fig.add_annotation(
        x=0.5,
        y=0.5,
        text="No data",
        showarrow=False,
        font=dict(size=16),
        xref="paper",
        yref="paper",  # Center annotation
    )

    # Update layout
    fig.update_layout(
        title={
            "text": "Violin Plot: No Data",  # Dynamic title text
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
        height=575,
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
        margin=dict(t=110, r=200),
    )

    return fig
