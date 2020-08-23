#!/usr/bin/env python3

# Imports
import flask


def main():
    app = flask.Flask(__name__)
    app.config["DEBUG"] = True


    # API Functions
    @app.route("/", methods=['GET'])
    def home():
        # Setup the webpage for app's frontend
        html_str = "<h1>Hello World</h1>"

        return html_str

    app.run()





if __name__ == '__main__':
    main()

'''
PreReq
0. Make sure python and pip are installed using
python --version
pip --version

1. Install pip using
pip install flask



How to run
1. Go to command line and type this:
python Server.py

2. Go to 127.0.0.1:5000 on browser
'''