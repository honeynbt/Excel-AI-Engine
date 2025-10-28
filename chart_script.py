import plotly.graph_objects as go

# Define the components with improved positioning for better flow
components = [
    {"name": "User", "x": 4, "y": 9, "width": 1.8, "height": 0.8},
    {"name": "REST API<br>(FastAPI)", "x": 4, "y": 7.8, "width": 1.8, "height": 0.8},
    {"name": "File Upload<br>Handler", "x": 4, "y": 6.6, "width": 1.8, "height": 0.8},
    {"name": "Excel Reader<br>(openpyxl/pandas)", "x": 4, "y": 5.4, "width": 1.8, "height": 0.8},
    {"name": "LLM Query<br>Processor<br>(LangChain)", "x": 4, "y": 4.2, "width": 1.8, "height": 0.8},
    {"name": "OpenAI LLM", "x": 4, "y": 3, "width": 1.8, "height": 0.8},
    {"name": "Data Operations<br>Engine<br>(pandas)", "x": 4, "y": 1.8, "width": 1.8, "height": 0.8},
    {"name": "Result<br>Formatter", "x": 4, "y": 0.6, "width": 1.8, "height": 0.8},
    {"name": "Response to<br>User", "x": 4, "y": -0.6, "width": 1.8, "height": 0.8}
]

# Define arrows with better positioning to avoid overlap
arrows = [
    {"from": (4, 8.6), "to": (4, 8.2)},     # User -> REST API
    {"from": (4, 7.4), "to": (4, 7.0)},     # REST API -> File Upload Handler
    {"from": (4, 6.2), "to": (4, 5.8)},     # File Upload Handler -> Excel Reader
    {"from": (4, 5.0), "to": (4, 4.6)},     # Excel Reader -> LLM Query Processor
    {"from": (4, 3.8), "to": (4, 3.4)},     # LLM Query Processor -> OpenAI LLM
    {"from": (4, 2.6), "to": (4, 2.2)},     # OpenAI LLM -> Data Operations Engine
    {"from": (4, 1.4), "to": (4, 1.0)},     # Data Operations Engine -> Result Formatter
    {"from": (4, 0.2), "to": (4, -0.2)}     # Result Formatter -> Response to User
]

# Create the figure
fig = go.Figure()

# Color palette with better contrast
colors = ['#1FB8CD', '#DB4545', '#2E8B57', '#5D878F', '#D2BA4C', 
          '#B4413C', '#964325', '#944454', '#13343B']

# Add rectangles for components
for i, comp in enumerate(components):
    color = colors[i % len(colors)]
    
    # Add rectangle with rounded corners effect
    fig.add_shape(
        type="rect",
        x0=comp["x"] - comp["width"]/2,
        y0=comp["y"] - comp["height"]/2,
        x1=comp["x"] + comp["width"]/2,
        y1=comp["y"] + comp["height"]/2,
        fillcolor=color,
        line=dict(color="#333333", width=2),
        opacity=0.9
    )
    
    # Add text with better contrast
    fig.add_annotation(
        x=comp["x"],
        y=comp["y"],
        text=comp["name"],
        showarrow=False,
        font=dict(color="white", size=11, family="Arial Black"),
        align="center"
    )

# Add arrows with proper arrowheads
for arrow in arrows:
    fig.add_annotation(
        x=arrow["to"][0],
        y=arrow["to"][1],
        ax=arrow["from"][0],
        ay=arrow["from"][1],
        xref="x",
        yref="y",
        axref="x",
        ayref="y",
        showarrow=True,
        arrowhead=2,
        arrowsize=1.8,
        arrowwidth=4,
        arrowcolor="#333333"
    )

# Update layout with clean appearance
fig.update_layout(
    title="Excel AI Engine Architecture",
    xaxis=dict(
        range=[1, 7],
        showgrid=False,
        showticklabels=False,
        zeroline=False,
        visible=False
    ),
    yaxis=dict(
        range=[-1.5, 10],
        showgrid=False,
        showticklabels=False,
        zeroline=False,
        visible=False
    ),
    plot_bgcolor="white",
    paper_bgcolor="white",
    showlegend=False
)

# Save the chart as both PNG and SVG
fig.write_image("excel_ai_architecture.png")
fig.write_image("excel_ai_architecture.svg", format="svg")

print("Improved system architecture diagram created successfully!")