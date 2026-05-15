"""
oauth_server.py:

This file provides a simple, insecure webserver that enables the creation of OAuth
authentication tokens for use with Blizzard's BattleNet community APIs.

It is provided as a proof of concept without warranty of any kind.
"""

import configparser
import os
from urllib.parse import parse_qs, urlsplit

import requests
from flask import Flask, redirect, request
from oauthlib.oauth2 import WebApplicationClient

# Read API data from a local config file
#   [battle.net]
#   client_id = ...
#   client_secret = ...
#   redirect_uri = ...
#   token_path = ...
config = configparser.ConfigParser()
config.read(os.environ["CONFIG_PATH"])
battle_net_config = config["battle.net"]
client_id = battle_net_config["client_id"]
client_secret = battle_net_config["client_secret"]
token_path = os.path.expanduser(battle_net_config["token_path"])
redirect_uri = battle_net_config["redirect_uri"]
redirect_parts = urlsplit(redirect_uri)

# Set up OAUTH2 client.  Change the oauth_server if authenticating a CN account
oauth_server = "https://oauth.battle.net"
oauth_client = WebApplicationClient(client_id)

# Configure Local Web Service
oauth_app = Flask(__name__)


@oauth_app.route("/")
def authorise():
    """
    Provides top-level URL.  Invoves the OAuth protocol
    """
    return redirect(
        oauth_client.prepare_request_uri(
            uri=f"{oauth_server}/authorize",
            redirect_uri=redirect_uri,
            scope=["wow.profile", "sc2.profile", "d3.profile"],
            state="MyLocalApp",
        )
    )


@oauth_app.route(redirect_parts.path)
def get_token():
    """
    Handles the redirected response.  Converts the OAuth response to a usable token and
    saves it to a file
    """
    code = request.args.get("code")
    token = requests.post(
        f"{oauth_server}/token",
        auth=(client_id, client_secret),
        data=parse_qs(
            oauth_client.prepare_request_body(
                code=code,
                redirect_uri=redirect_uri,
                include_client_id=False,
            )
        ),
    )
    with open(token_path, "wt") as f:
        f.write(token.text)
    return token.content


# Run local web service if invoked from command line
if __name__ == "__main__":
    oauth_app.run(host=redirect_parts.hostname, port=redirect_parts.port, debug=False)
