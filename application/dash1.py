import dash

from dash import html, dcc, Output, Input, callback
import numpy as np
import plotly.express as px








x_label = [f'label_{x}' for x in range(50)]
x = [np.random.rand() for x in range(50)]
y = [np.random.rand() * 5 + x for x in range(50)]


fig1 = px.scatter(x, y)
fig2 = px.line(x_label, y)
fig3 = px.bar(x_label, x)


# def layout_1():
#     d1 = html.Div(children= [
#          html.H1('Hello from dash app number 1'),
#          dcc.RadioItems(id='radio_btn' ,
#                     options= [{'label':'Scatter', 'value':'Scatter'},
#                                 {'label':'Line', 'value':'Line'},
#                                 {'label':'Bar', 'value':'Bar'}], 
#                     value='Scatter'),
#         dcc.Graph(id='graph_1')
#         ])
    
    
#     # from application.routes import dash_app1
#     @dash_app1.callback(
#     [Output('graph_1', 'figure'),
#     Input('radio_btn', 'value')])

#     def update_graph(v):
#         if v == 'Scatter':
#             return fig1
#         elif v == 'Line':
#             return fig2
#         else:
#             return fig3
    
    
#     return d1





# @dash_app1.callback(
# [Output('graph_1', 'figure'),
#  Input('radio_btn', 'value')])

# def update_graph(v):
#     if v == 'Scatter':
#         return fig1
#     elif v == 'Line':
#         return fig2
#     else:
#         return fig3


