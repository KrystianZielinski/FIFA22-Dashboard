import plotly.graph_objects as go
from utils import get_attributes


def create_radar_chart_empty(selected_category):
    all_attributes = get_attributes()
    # Get the selected attributes for the category
    selected_attributes = all_attributes[selected_category]

    fig = go.Figure()  # Create an empty figure
    fig.add_trace(
        go.Scatterpolar(
            r=[0, 0, 0, 0, 0],  # Placeholder radial values
            theta=selected_attributes,  # Placeholder labels
            fill="toself",
            name="No Data",
            line=dict(
                color="lightgray", dash="dash"
            ),  # Light gray dashed line for visibility
        )
    )

    fig.update_layout(
        title={
            "text": "Radar Chart: No Data",  # Indicate no data
            "x": 0.5,
            "xanchor": "center",
            "yanchor": "top",
            "y": 0.96,
        },
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),  # Keep axes visible
        width=625,
        height=625,
        margin=dict(l=125, r=125, t=75, b=0),
        hovermode="closest",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=0.88,
            xanchor="left",
            x=-0.2,
            font=dict(family="Roboto, Arial, sans-serif", size=22, weight="bold"),
        ),
    )

    return fig
