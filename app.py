# from dash.dependencies import Input, Output, State
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

from callbacks import db_interactor, get_callbacks
import app_elements.device_messenger as device_messenger
# import app_elements.experiment_panel as experiment_panel
# import app_elements.imaging_panel as imaging_panel
# import app_elements.livestream_panel as livestream_panel
 

# print(get_all_experiments())

from users import USERNAME_PASSWORD_PAIRS
from users import PISCOPE_BOT_TOKEN

import os

base_path = os.getenv('BASE_PATH', '/device-controllers/')
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], url_base_pathname=base_path)
app.title = 'Braingeneers Control Panel'
# get_callbacks(app)
device_messenger.get_callbacks(app)

auth = dash_auth.BasicAuth(
    app,
    USERNAME_PASSWORD_PAIRS
)

app.layout = html.Div(id='main-div', className='row flex-display', children=[
    
#layout = dbc.Container([

    dcc.Tabs([
        device_messenger.DEVICE_MESSENGER,
    ])
])



if __name__ == "__main__":
    app.run_server(debug=True, host='0.0.0.0', port=8050)
