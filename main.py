# Imports
from uuid import uuid4
from flask import Flask, jsonify, request
import routes  # Register API routes
app = Flask(__name__)  # Create a new Flask server!

# Save my address to identify myself as a node
node_identifier = str(uuid4()).replace("-", "")

# Create a Blockchain Application
blockchain = Blockchain()

# Arguments for application running
if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    # Usage: python main.py --port <any port number>
    parser.add_argument("-p", "--port", default=3000,
                        type=int, help="port to listen on")

    # Gets arguments from 'python main.py --port <argument>'
    args = parser.parse_args()
    port = args.port  # Save the port value, default 3000

    app.run(host="0.0.0.0", port=port)  # Do the thing!!!
