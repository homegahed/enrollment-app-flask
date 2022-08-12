import dash

from flask import redirect

from dash import Dash, html, dcc, Output, Input
import numpy as np
import plotly.express as px

from application import app


dash_app_2 = Dash(__name__, server = app, url_base_pathname='/dash2/')



x_label = [f'label_{x}' for x in range(50)]
x = [np.random.rand() for x in range(50)]
y = [np.random.rand() * 5 + x for x in range(50)]


fig1 = px.scatter(x = x, y = y)
fig2 = px.line(x = x_label, y = y)
fig3 = px.bar(x = x_label, y = x)





dash_app_2.layout = html.Div(children= [
    html.H1('Hello from dash app number 2'),
    html.A("Home", href= "/") , html.Br(), html.Br(),
    dcc.RadioItems(['Scatter', 'Line', 'Bar'], 'Line', id='radio_btn'),
    dcc.Graph(id='graph_1')
    ])


@dash_app_2.callback(
    Output('graph_1', 'figure'),
    Input('radio_btn', 'value'))
def update_graph(v):
    if v == 'Scatter':
        return fig1

    elif v == 'Line':        
        return fig2
    
    else:
        return fig3


