from dash import dcc, html
# import dash_core_components as dcc
# import dash_html_components as html
import dash_bootstrap_components as dbc
import dash.exceptions
import numpy as np
import itertools
import time
import plotly.subplots
import plotly.graph_objects as go
# import braingeneers.utils.messaging as messaging
import uuid
import threading
# import json
import datetime
# import pytz
import dash_auth
# from github import Github
import re
import sqlite3
        
DEVICE_MESSENGER = dcc.Tab(label='Device-Messenger', children=[
                    html.Div(id='device-div-2', className='six columns pretty_container', children=[
                            dbc.Button(id='show-device-button', children='Refresh', color="primary", n_clicks=0),
                            html.H4(id='device-list-header', children='Devices:'),
                            dcc.Dropdown(
                                    id="Devices-List",
                                    options=[],
                                ),
                            html.Div(
                                [
                                    dbc.Checklist(
                                        options=[
                                            {"label": "show only active experiments", "value": True},
                                        ],
                                        value=[True],
                                        id="show-only-1",
                                        switch=True,
                                    ),
                                ]),
                            dcc.Loading(children=[
                                html.Pre(id="Device-Info",
                                       className="info__container"),
                                # toggle switch for experiment active
                                html.Div(
                                [
                                    dbc.Checklist(
                                        options=[
                                            {"label": "Active", "value": True},

                                            # {"label": "Disabled Option", "value": 3, "disabled": True},
                                        ],
                                        value=[True],
                                        id="switches-input-2",
                                        switch=True,
                                    ),
                                ]),
                                ],
                                type="dot",
                            ),
                    ]),

                ])


from callbacks import *

def get_callbacks(app):
    """
        def update_device_list()

        populate the dropdown list of devices, optional filter for active devices

    """    
    @app.callback(
        Output('Devices-List', 'options'),
        Output('Devices-List', 'value'),
        Input('show-device-button', 'n_clicks'),
        Input('show-only-1', 'value'),
    )
    def update_device_list(clicks, show_only_active):
        #weird hack to get bool from toggle switch
        show_only_active = True in show_only_active

        if show_only_active:
            devices = db_interactor.list_objects_with_name_and_id("interaction-things","?filters[active][$eq]=true")
        else:
            devices = db_interactor.list_objects_with_name_and_id("interaction-things")
        return devices, devices[0]["value"]

    """
        def populate_device_info()

    """
    @app.callback(
        Output('Device-Info', 'children'),
        Input('Devices-List', 'value'),
        Input('show-device-button', 'n_clicks')
    )
    def populate_device_info(device_id, clicks):
        device = db_interactor.get_device(device_id)
        return json.dumps(device.to_json(), indent=4)
