import os
import subprocess

from config import DevelopmentConfig
from flask import Flask, render_template, request, session
from flask_assets import Bundle, Environment

# from models import Model
from utils import log, opendnd, sassfilter

# from webassets.filter import register_filter
# from webassets.filter.sass import DartSass


def create_app():
    app = Flask(os.getenv("APP_NAME", __name__))
    app.config.from_object(DevelopmentConfig)
    #################################################################
    #                             Extensions                        #
    #################################################################
    # app.wsgi_app = SassMiddleware(
    #     app.wsgi_app,
    #     {
    #         os.getenv("APP_NAME", __name__): (
    #             "static/style/sass",
    #             "static/style",
    #             "/static/style",
    #         )
    #     },
    # )
    assets = Environment(app)

    assets.register(
        "js",
        Bundle(
            "js/main.js",
            "js/base.js",
            "js/widgets.js",
            filters="jsmin",
            output="main.js",
        ),
    )

    # assets.register(
    #     "dartscss",
    #     Bundle(
    #         "sass/main.scss",
    #         filters=(sassfilter.dartsass),  # ("dartsass",),
    #         output="style.css",
    #     ),
    # )
    app.before_first_request(lambda: sassfilter.dartsass())

    #################################################################
    #                             ROUTES                            #
    #################################################################
    @app.route("/", methods=["GET", "POST"])
    def index():
        log(request.form)
        if request.form.get("number", session.get("number")):
            session.update(request.form)
            # log(session)
            session["monsters"] = opendnd.OpenDnD.get_monsters(**session)
            log(request.form)
        return render_template("index.html")

    return app
