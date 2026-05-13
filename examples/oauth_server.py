
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

# %% Set up OAUTH2 client
oauth_client = WebApplicationClient(battle_net_config["client_id"])

# %% Configure Local Web Service
oauth_app = Flask(__name__)


@oauth_app.route("/")
def authorise():
    return redirect(
        oauth_client.prepare_request_uri(
            uri="https://oauth.battle.net/authorize",
            redirect_uri=battle_net_config["redirect_uri"],
            scope=["wow.profile"],
            state="MyLocalApp",
        )
    )


@oauth_app.route("/access")
def get_token():
    code = request.args.get("code")
    token = requests.post(
        "https://oauth.battle.net/token",
        auth=(battle_net_config["client_id"], battle_net_config["client_secret"]),
        data=parse_qs(
            oauth_client.prepare_request_body(
                code=code, redirect_uri=battle_net_config["redirect_uri"], include_client_id=False
            )
        ),
    )
    with open(battle_net_config["token_path"], "wt") as f:
        f.write(token.text)
    return token.content


# %% Run local web service if invoked from command line
if __name__ == "__main__":
    url = urlsplit(battle_net_config["redirect_uri"])
    oauth_app.run(host=url.hostname, port=url.port, debug=False)
