import plotly.graph_objects as go

# Create a flowchart using plotly with shapes and annotations
fig = go.Figure()

# Define positions for flowchart elements
positions = {
    'A': (1, 10),    # User sends request
    'B': (1, 9),     # FastAPI receives request
    'C': (1, 8),     # Decision: Upload or Analyze?
    'D': (0, 7),     # Save file (Upload path)
    'E': (0, 6),     # Extract metadata
    'F': (0, 5),     # Return file info
    'G': (2, 7),     # Load Excel file (Analyze path)
    'H': (2, 6),     # Initialize LangChain agent
    'I': (2, 5),     # Process with GPT-4
    'J': (2, 4),     # Execute pandas operations
    'K': (2, 3),     # Format results
    'L': (2, 2),     # Return response
}

# Define node labels (keeping under 15 chars)
labels = {
    'A': 'User sends req',
    'B': 'FastAPI recv req',
    'C': 'Upload or Analyze?',
    'D': 'Save file',
    'E': 'Extract metadata',
    'F': 'Return file info',
    'G': 'Load Excel file',
    'H': 'Init LangChain',
    'I': 'Process w/ GPT-4',
    'J': 'Execute pandas',
    'K': 'Format results',
    'L': 'Return response'
}

# Add rectangles for process nodes
process_nodes = ['A', 'B', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
for node in process_nodes:
    x, y = positions[node]
    fig.add_shape(
        type="rect",
        x0=x-0.4, y0=y-0.2, x1=x+0.4, y1=y+0.2,
        line=dict(color="#21808d", width=2),
        fillcolor="#e8f4f5"
    )

# Add diamond for decision node
x, y = positions['C']
fig.add_shape(
    type="path",
    path=f"M {x-0.4} {y} L {x} {y+0.3} L {x+0.4} {y} L {x} {y-0.3} Z",
    line=dict(color="#21808d", width=2),
    fillcolor="#f3f3ee"
)

# Add connecting lines (no arrows to avoid annotation issues)
connections = [
    ('A', 'B'), ('B', 'C'), 
    ('C', 'D'), ('D', 'E'), ('E', 'F'),  # Upload path
    ('C', 'G'), ('G', 'H'), ('H', 'I'), ('I', 'J'), ('J', 'K'), ('K', 'L')  # Analyze path
]

for start, end in connections:
    x1, y1 = positions[start]
    x2, y2 = positions[end]
    
    # Adjust line endpoints to avoid overlapping shapes
    if y1 > y2:  # downward arrow
        y1_adj = y1 - 0.2
        y2_adj = y2 + 0.2
    else:
        y1_adj = y1 + 0.2
        y2_adj = y2 - 0.2
        
    fig.add_shape(
        type="line",
        x0=x1, y0=y1_adj, x1=x2, y1=y2_adj,
        line=dict(color="#333333", width=2)
    )

# Add text labels for all nodes without using annotations
for node, label in labels.items():
    x, y = positions[node]
    fig.add_trace(go.Scatter(
        x=[x], y=[y],
        text=[label],
        mode='text',
        textfont=dict(size=10, color="#13343b"),
        showlegend=False,
        hoverinfo='skip'
    ))

# Add path labels
fig.add_trace(go.Scatter(
    x=[-0.2], y=[7.5],
    text=["Upload"],
    mode='text',
    textfont=dict(size=9, color="#21808d"),
    showlegend=False,
    hoverinfo='skip'
))

fig.add_trace(go.Scatter(
    x=[2.2], y=[7.5],
    text=["Analyze"],
    mode='text', 
    textfont=dict(size=9, color="#21808d"),
    showlegend=False,
    hoverinfo='skip'
))

# Update layout
fig.update_layout(
    title="Excel AI Engine API Request Flow",
    showlegend=False,
    xaxis=dict(visible=False, range=[-1, 3]),
    yaxis=dict(visible=False, range=[1, 11]),
    plot_bgcolor='white',
    paper_bgcolor='white'
)

# Save the chart
fig.write_image("excel_ai_flowchart.png")
fig.write_image("excel_ai_flowchart.svg", format="svg")

print("Flowchart created successfully using Plotly")
print("Files saved: excel_ai_flowchart.png and excel_ai_flowchart.svg")