# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Output, Input, callback
import plotly.express as px
import pandas as pd
from grid import Grid

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
new_grid = Grid()
new_grid.detect_neighbors()
colorscales = px.colors.named_colorscales()

fig = px.imshow(new_grid.neighbors)

app.layout = html.Div(children=[
    html.H1(children='Nearest Neighbors'),

    html.Div(children='''
        A nearest neighbors detector.
    '''),
    dcc.Input(
    id="num_rows", type="number", placeholder="Number of Grid Rows",
    min=50, max=100,step=5,value=50
    ),
    dcc.Input(
        id="num_cols", type="number", placeholder="Number of Grid Columns",
        min=50, max=100, step=5,value=50
    ),
    dcc.Input(
        id="distance", type="number", placeholder="Neighbor Search Distance",
        min=1, max=10, step=1,value=3
    ),
    dcc.Dropdown(
        id='dropdown', 
        options=colorscales,
        value='viridis'
    ),
    dcc.Graph(figure={}, id='chart')
    
])

@callback(
    Output(component_id='chart', component_property='figure'),
    Input(component_id='distance', component_property='value'),
    Input(component_id='num_rows', component_property='value'),
    Input(component_id='num_cols',component_property='value'),
    Input("dropdown", "value")

)
def update_chart(dist,rows,cols,scale):
    update_grid = Grid(rows=rows,cols=cols,distance=dist)
    update_grid.detect_neighbors()

    fig = px.imshow(update_grid.neighbors, width=900,height=700,
                    color_continuous_scale=scale)
    return fig

if __name__ == '__main__':
    app.run(debug=True)