import plotly.graph_objs as go
from utils import football_pitch_positions, positions_category
import mplsoccer
import io
import base64

# Define your player positions and labels
player_positions = football_pitch_positions()


# Function to create the pitch figure
def create_pitch():
    pitch = mplsoccer.VerticalPitch(
        pitch_type="statsbomb",
        half=False,
        pitch_color="#333333",
        line_color="white",
        corner_arcs=True,
    )

    fig, ax = pitch.draw(figsize=(12, 8))
    fig.patch.set_facecolor("none")  # Transparent background
    ax.set_facecolor("none")  # Set axes background to transparent

    # Save the pitch to a buffer (no file save, only in-memory)
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=600, bbox_inches="tight", transparent=True)
    buf.seek(0)

    # Encode the image in base64
    img_str = base64.b64encode(buf.read()).decode("utf-8")

    # Close the buffer
    buf.close()

    return img_str


# Step 2: Convert the base64 image into a Plotly figure
def create_pitch_figure(selected_players):
    img_str = create_pitch()

    # Create the Plotly figure
    fig = go.Figure()

    # Add the pitch image as a background in Plotly
    fig.add_layout_image(
        dict(
            source=f"data:image/png;base64,{img_str}",
            xref="paper",  # Use paper coordinates (0 to 1 scale)
            yref="paper",  # Use paper coordinates (0 to 1 scale)
            x=0.5,  # Position of the image at the center of the plot (50%)
            y=0.5,  # Position of the image at the center of the plot (50%)
            sizex=1,
            sizey=1,
            xanchor="center",  # Align the image to the center horizontally
            yanchor="middle",  # Align the image to the middle vertically
            layer="below",
        )
    )

    position_hover_map = {
        "GK": "Goalkeeper",
        "LB": "Left Back",
        "CB": "Center Back",
        "RB": "Right Back",
        "LWB": "Left Wing Back",
        "CDM": "Defensive Midfielder",
        "RWB": "Right Wing Back",
        "LM": "Left Midfielder",
        "CM": "Center Midfielder",
        "RM": "Right Midfielder",
        "LW": "Left Winger",
        "CAM": "Attacking Midfielder",
        "RW": "Right Winger",
        "ST": "Striker",
        "CF": "Center Forward",
    }

    fig.add_trace(
        go.Scatter(
            x=[x for label, (x, y) in player_positions.items()],
            y=[y + 0.5 for label, (x, y) in player_positions.items()],
            mode="markers+text",
            marker=dict(
                size=22,
                color="rgba(0, 0, 0, 0)",  # Fully transparent color (black with 0 alpha)
                symbol="circle",
                opacity=0,  # Make the marker fully transparent
            ),
            text=[label for label, (x, y) in player_positions.items()],
            textposition="top center",
            hoverinfo="text",
            hovertext=[
                f"{label} - {position_hover_map.get(label, 'Unknown')}"
                for label, (x, y) in player_positions.items()
            ],
            textfont=dict(
                color=[
                    "white" if label in selected_players else "gray"
                    for label, (x, y) in player_positions.items()
                ],
                size=16,  # Adjust font size if needed
            ),
        )
    )

    shirt_gk_image_path = "images/shirt_gk.png"
    shirt_def_image_path = "images/shirt_def.png"
    shirt_mid_image_path = "images/shirt_mid.png"
    shirt_atk_image_path = "images/shirt_atk.png"
    shirt_unselected_image_path = "images/shirt_unselected.png"

    # Read and encode the image file to base64
    with open(shirt_gk_image_path, "rb") as img_file:
        shirt_gk_image_path_encoded = base64.b64encode(img_file.read()).decode("utf-8")
    with open(shirt_def_image_path, "rb") as img_file:
        shirt_def_image_path_encoded = base64.b64encode(img_file.read()).decode("utf-8")
    with open(shirt_mid_image_path, "rb") as img_file:
        shirt_mid_image_path_encoded = base64.b64encode(img_file.read()).decode("utf-8")
    with open(shirt_atk_image_path, "rb") as img_file:
        shirt_atk_image_path_encoded = base64.b64encode(img_file.read()).decode("utf-8")

    with open(shirt_unselected_image_path, "rb") as img_file:
        shirt_unselected_image_path_encoded = base64.b64encode(img_file.read()).decode(
            "utf-8"
        )

    positions_cat = positions_category()
    # Define position hover text mapping

    for label, (x, y) in player_positions.items():
        if label in selected_players:
            if label == "GK":
                image_source = f"data:image/png;base64,{shirt_gk_image_path_encoded}"  # Use the first base64 image
            elif label in positions_cat["DEF"]:
                image_source = f"data:image/png;base64,{shirt_def_image_path_encoded}"  # Use the first base64 image
            elif label in positions_cat["MID"]:
                image_source = f"data:image/png;base64,{shirt_mid_image_path_encoded}"  # Use the first base64 image
            elif label in positions_cat["ATK"]:
                image_source = f"data:image/png;base64,{shirt_atk_image_path_encoded}"  # Use the first base64 image

        else:
            image_source = f"data:image/png;base64,{shirt_unselected_image_path_encoded}"  # Use the second base64 image

        fig.add_layout_image(
            dict(
                source=image_source,  # Embed base64 encoded image
                x=x,
                y=y,
                xref="x",
                yref="y",
                sizex=5,
                sizey=5,  # Adjust icon size
                xanchor="center",
                yanchor="middle",
                layer="above",  # Ensure it appears above the pitch
            )
        )

    fig.update_xaxes(range=[20, 80])  # Adjust x-axis range
    fig.update_yaxes(range=[-30, 20])  # Adjust y-axis range
    fig.update_layout(yaxis=dict(scaleanchor="x"))  # Keep proper aspect ratio

    # Set layout options for the plot (no grid, transparent background)
    fig.update_layout(
        width=475,
        height=600,
        xaxis=dict(
            scaleanchor="y", showgrid=False, zeroline=False, showticklabels=False
        ),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        plot_bgcolor="rgba(0,0,0,0)",  # Transparent background
        margin=dict(l=0, r=0, b=0, t=0),
        clickmode="event",
        dragmode=False,
    )

    return fig
