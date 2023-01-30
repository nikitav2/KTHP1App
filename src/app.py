import dash


# use a scatter po6

# import dash_core_components as dcc
# import dash_html_components as html
# import plotly.graph_objs as go
import pandas as pd
from dash import Dash, dcc, html, Input, Output
from dash.exceptions import PreventUpdate


# mgr_options = df["About"].unique()
# #
# app = dash.Dash()
#
# app.layout = html.Div([
#     html.H2("Sales Funnel Report"),
#     html.Div(
#         [
#             dcc.Dropdown(
#                 id="Manager",
#                 options=[{
#                     'label': i,
#                     'value': i
#                 } for i in mgr_options],
#                 value='All Managers'),
#         dcc.Graph(id='funnel-graph'),
#         ],
#         style={'width': '25%',
#                'display': 'inline-block', 'text-align': 'center'}),
# ])
#
# #
# # @app.callback(
# #     dash.dependencies.Output("graph", "figure"),
# #     dash.dependencies.Input("medals", "value"))
# # def filter_heatmap(cols):
# #     df = go.data.medals_wide(indexed=True) # replace with your own data source
# #     fig = go.imshow(df[cols])
# #     return fig
#
# # app.layout = html.Div([
# #     html.H4('Olympic medals won by countries'),
# #     dcc.Graph(id="graph"),
# #     html.P("Medals included:"),
# #     dcc.Checklist(
# #         id='medals',
# #         options=["gold", "silver", "bronze"],
# #         values=["gold", "silver"],
# #     ),
# # ])
# #
# #
# # @app.callback(
# #     dash.dependencies.Output("graph", "figure"),
# #     [dash.dependencies.Input("medals", "values")])
# # def filter_heatmap(cols):
# #     df = go.data # replace with your own data source
# #     fig = go.imshow(df[cols])
# #     return fig
# # @app.callback(
# #     dash.dependencies.Output('funnel-graph', 'figure'),
# #     [dash.dependencies.Input('Manager', 'value')])
# # def update_graph(Manager):
# #     if Manager == "All Managers":
# #         df_plot = df.copy()
# #     else:
# #         df_plot = df[df['About'] == Manager]
# #
# #     # x = ['A', 'B', 'C', 'D']
# #
# #     plot = go.Figure(data=[go.Bar(
# #         name='Data 1',
# #         x=df_plot,
# #         y=[100, 200, 500, 673]
# #     ),
# #         go.Bar(
# #             name='Data 2',
# #             x=df_plot,
# #             y=[56, 123, 982, 213]
# #         )
# #     ])
# #
# #     # trace1 = go.Bar(x=pv.index, y=pv[('Quantity', 'declined')], name='Declined')
# #     # trace2 = go.Bar(x=pv.index, y=pv[('Quantity', 'pending')], name='Pending')
# #     # trace3 = go.Bar(x=pv.index, y=pv[('Quantity', 'presented')], name='Presented')
# #     # trace4 = go.Bar(x=pv.index, y=pv[('Quantity', 'won')], name='Won')
# #
# #     return {
# #         # 'data': [trace1, trace2, trace3, trace4],
# #
# #         'layout':
# #         go.Layout(
# #             title='Customer Order Status for {}'.format(Manager),
# #             barmode='stack')
# #     }
# #
#
# if __name__ == '__main__':
#     app.run_server(debug=True)


import dash
# from dash import dcc,html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.express as px
print(pd.__version__)
app = dash.Dash(__name__)
server = app.server
df_bar = pd.read_csv("src/data.csv")
columns = df_bar.columns.tolist()
df = pd.read_csv("src/data2.csv")
app.layout = html.Div(children=[
   # elements from the top of the page
   html.Div([
      html.H1(children='Information Visualization Project 1', style={'textAlign': 'center'}),
        html.H2(children='By Nikita Volynskiy', style={'textAlign': 'center'}),
       dcc.Dropdown(
           id="dropdown",
           options=[
               {'label': "All", 'value': "All"},
               {'label': "Artistic", 'value': "Artistic"},
               {'label': "Collaboration", 'value': "Collaboration"},
               {'label': "Communication", 'value': "Communication"},
               {'label' : "Computer", 'value' : "Computer"} ,
               {'label': "Evaluation", 'value': "Evaluation"},
                {'label': "Graphics", 'value': "Graphics"},
               {'label': "Human-computer", 'value': "Human-computer"},
               {'label' : "Mathematics", 'value' : "Mathematics"},
               {'label': "Programming", 'value': "Programming"},
               {'label': "Repository", 'value': "Repository"},
               {'label': "Statistical", 'value': "Statistical"},
               {'label' : "Visualization", 'value' : "Visualization"},],
           multi=True,
           placeholder="Select The Traits That You Want To Compare Between The Group",
           # value = 'Mathematics'
       ),


      dcc.Graph(
         id='graph1',

      ),  html.H4(children='Sort graph By: ', style={'textAlign': 'center'}),
dcc.RadioItems(
    options=[
        {'label': 'Ascending', 'value': 'Ascending'},
        {'label': 'Descending', 'value': 'Descending'},
        {'label': 'Alphabetical', 'value': 'Alphabetical'},
{'label': 'None', 'value': 'None'}
    ], value='None',id = "Radio", labelClassName = 'Buttons',style=dict(display='flex', justifyContent='center'),
),

dcc.Dropdown(
           df["Alias"].unique(),
           id="dropdown2"
           ,

           multi=True,
           placeholder="Remove the Students You Do Not Think Would be a Good Match For Your Group",
           # value = 'Mathematics'
       ),

   ]),
html.Div([]),
   # New Div for all elements in the new 'row' of the page
   html.Div([
      html.H1(children='Students Grouped By Interests and Their Skill Ranking', style={'textAlign': 'center'}),

        #  dcc.Dropdown(
        #     id="dropdown",
        #     options=["Mathematics", "Computer", "Programming"],
        #     value="Fri",
        #     clearable=False,
        #      multi = True
        # ),
      dcc.Graph(
         id='graph2',
          # figure = fig2
      ),

       dcc.Dropdown(
           df["Alias"].unique(),
           id="dropdown3"
           ,

           multi=True,
           placeholder="Add Up To 5 students That Will Make the Most Optimal Group",
           # value = 'Mathematics'
       ),html.H1(children='Students That Share the Same Interests', style={'textAlign': 'center'}),
        dcc.Graph(
         id='graph4',
          # figure = fig2
      ), html.H1(children='Strengths of The Group Compared To Each Other Strength', style={'textAlign': 'center'}),dcc.Graph(
         id='graph3',
          # figure = fig2
      ),

   ]),


])

@app.callback(
    Output('graph1', 'figure'), Output('graph2', 'figure'),  Output('graph3', 'figure'),Output('graph4', 'figure'),
    [Input('dropdown', 'value'), Input('Radio', 'value'), Input('dropdown2', 'value'), Input('dropdown3', 'value')])
def update_graph(value,  value2, value3, value4):
    if value is None:
        raise PreventUpdate
    df_plot = df_bar.copy()
    df_plot['Alias'] = df_plot['Alias'].str.lower()
    print(value3)
    if (value[0] != 'All'):
        fig = px.bar(df_plot, x='Alias', y=value, labels={"Alias": "Alias",
                                                      "Ranking (Out of 10 for each Category)": "Ranking (Out of 10 for each Category)",
                                                      })
    else:
        print("here")
        value.remove('All')
        value = ["Visualization","Statistical","Mathematics","Artistic","Computer","Programming","Graphics","Human-computer","Evaluation","Communication","Collaboration","Repository"]
        # print(value)
        fig = px.bar(df_plot, x='Alias', y=value, labels={"Alias": "Alias",
                                                          "Ranking (Out of 10 for each Category)": "Ranking (Out of 10 for each Category)",

                                                          })
    df_plot['Sum'] = df_plot[[col for col in value]].sum(axis=1)
    print(value[0], value)

    # fig.update_yaxes(visible=True, showticklabels=True)
    if (value2 == "None"):
        print(value3)
        fig = px.bar(df_plot, x='Alias', y=value, labels = {                     "Aliases": "Aliases",
                     "Ranking (Out of 10 for each Category)": "Ranking (Out of 10 for each Category)",
})
    elif (value2 == "Ascending"):
        df_plot = df_plot.sort_values(by = 'Sum')
        fig = px.bar(df_plot, x='Alias', y=value, labels={"Aliases": "Aliases",
                                                          "Ranking (Out of 10 for each Category)": "Ranking (Out of 10 for each Category)",
                                                          })
    elif (value2 == "Descending"):
        df_plot = df_plot.sort_values(by='Sum', ascending=False)
        fig = px.bar(df_plot, x='Alias', y=value, labels={"Aliases": "Aliases",
                                                          "Ranking (Out of 10 for each Category)": "Ranking (Out of 10 for each Category)",
                                                          })
    elif (value2 == "Alphabetical"):
        df_plot = df_plot.sort_values(by='Alias')
        fig = px.bar(df_plot, x='Alias', y=value, labels={"Aliases": "Aliases",
                                                          "Ranking (Out of 10 for each Category)": "Ranking (Out of 10 for each Category)",

                                                          })
    fig.update_layout(
        title="Participants Rankings of Their Skills" ,title_x=0.5,
        xaxis_title="Alias",
        yaxis_title="Ranking (Each Category Out of 10)",
        legend_title="Legend",
    )
    d = df.copy().fillna(0)
    d['Total Sum of All Skills'] = d[[col for col in ['Visualization','Statistical','Mathematics','Artistic','Computer','Programming','Graphics','Human-computer','Evaluation','Communication','Collaboration','Repository']]].sum(axis=1)
    fig2 = px.treemap(d, path=[px.Constant('world'), 'About', 'Alias', "Visualization"],
                      color='Total Sum of All Skills')
    if value3 != None:

        for i in value3:
            d= d[d.Alias != i]
        fig2 = px.treemap(d, path=[px.Constant('Different Group Interests'), 'About', 'Alias', 'Total Sum of All Skills'],

                          color='Total Sum of All Skills')
    d2 = d.copy()
    fig3 = px.scatter_matrix(d2, dimensions=['Visualization', 'Statistical', 'Mathematics', 'Artistic', 'Computer',
                                             'Programming', 'Graphics', 'Human-computer', 'Evaluation', 'Communication',
                                             'Collaboration', 'Repository'],
                             color="Alias")
    fig4 =  px.sunburst(d2, path=['About', 'Alias'])
    if value4 != None:

        d2 = d2[d2['Alias'].isin(value4)]
        fig3 = px.scatter_matrix(d2, dimensions=['Visualization','Statistical','Mathematics','Artistic','Computer','Programming','Graphics','Human-computer','Evaluation','Communication','Collaboration','Repository'],
                                color="Alias")
        fig4 = px.sunburst(d2, path=['About', 'Alias'])
    fig3.update_layout(title="Fake Islands Populations")
    fig3.update_layout(
                      dragmode='select',
                      width=1500,
                      height=1800,
                      hovermode='closest',
    )
    return fig,fig2, fig3, fig4


# fig.update_layout(
#     updatemenus=[
#         dict(
#             active=0,
#             buttons=list([
#                 dict(label="None",
#                      method="update",
#                      args=[{"visible": [True, False, True, False]},
#                            {"title": "Yahoo",
#                             "annotations": []}]),
#                 dict(label="High",
#                      method="update",
#                      args=[{"visible": [True, True, False, False]},
#                            {"title": "Yahoo High",
#                             }]),
#                 dict(label="Low",
#                      method="update",
#                      args=[{"visible": [False, False, True, True]},
#                            {"title": "Yahoo Low",
#                             }]),
#                 dict(label="Both",
#                      method="update",
#                      args=[{"visible": [True, True, True, True]},
#                            {"title": "Yahoo",
#                             }]),
#             ]),
#         )
#     ])

if __name__ == '__main__':
    app.run_server(debug=True)