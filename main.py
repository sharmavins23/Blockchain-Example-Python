# Imports
from argparse import ArgumentParser
from flask import Flask, jsonify, request, abort
import routes  # Register API routes
from blockchain import Blockchain  # Load our blockchain class

app = Flask(__name__)  # Create a new Flask server!

# Create a Blockchain Application
blockchain = Blockchain()


def startServer():  # Function to run server application
    # Arguments for application running
    parser = ArgumentParser()
    # Usage: python main.py --port <any port number>
    parser.add_argument("-p", "--port", default=3000,
                        type=int, help="port to listen on")

    # Gets arguments from 'python main.py --port <argument>'
    args = parser.parse_args()
    port = args.port  # Save the port value, default 3000

    app.run(host="0.0.0.0", port=port)  # Do the thing!!!
