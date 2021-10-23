import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
import numpy as np

app = dash.Dash()
np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

app.layout = html.Div([
    dcc.Graph(id='scatterplot',
              figure={'data':[
                  go.Scatter(
                      x=random_x,
                      y=random_y,
                      mode='markers'
                  )],
              'layout':go.Layout(title='My Scatterplot')}
              ),
    dcc.Graph(id='scatterplot2',
              figure={'data': [
                  go.Scatter(
                      x=random_x,
                      y=random_y,
                      mode='markers'
                  )],
                  'layout': go.Layout(title='My Scatterplot2    ')}
              )
])

if __name__ =='__main__':
    app.run_server()