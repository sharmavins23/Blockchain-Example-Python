from flask import Flask, jsonify, request, abort
from uuid import uuid4
import os
from win32api import GenerateConsoleCtrlEvent

from main import app, blockchain, startServer


# Save my address to identify myself as a node
node_identifier = str(uuid4()).replace("-", "")


# Route to brew coffee.
@app.route("/brew", methods=["GET"])
def teapot():
    response = {
        'message': 'I cannot brew coffee for you.',
        'why': 'Because I\'m a teapot.'
    }

    return jsonify(response), 418


# Route to 'mine' (post) a new block
@app.route('/mine', methods=['POST'])
def mine():
    last_block = blockchain.last_block
    proof = blockchain.proof_of_work(last_block)

    blockchain.new_transaction(
        sender="0",  # Server
        recipient=node_identifier,
        amount=1
    )

    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': 'New Block Forged!',
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']
    }

    return jsonify(response), 201


# Route to post a new transaction


# Route to create a new chain
@app.route("/chain", methods=["GET"])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }

    return jsonify(response), 200


# Route to register (post) a new neighbor
@app.route("/nodes/register", methods=["POST"])
def register_nodes():
    values = request.get_json()

    # Testing purposes
    # print(values)

    nodes = values.get("nodes")

    if nodes is None:
        return "Error: Please supply a valid list of nodes", 400

    for node in nodes:
        blockchain.register_node(node)

    response = {
        "message": "New nodes have been added",
        "total_nodes": list(blockchain.nodes)
    }

    return jsonify(response), 201


# Route to resolve neighboring chains (get the longest one from friends)
@app.route("/nodes/resolve", methods=["POST"])
def consensus():
    # Takes all nodes and resolves all conflicts
    replaced = blockchain.resolve_conflicts()

    if replaced:
        response = {
            "message": "Our chain was replaced",
            "new_chain": blockchain.chain
        }
    else:
        response = {
            "message": "Our chain was not replaced",
            "new_chain": blockchain.chain
        }

    return jsonify(response), 200


# Route to shut down our server (don't put these on actual applications, please)
@app.route("/terminate", methods=["POST"])
def shutdown_server():
    try:
        # Emulate a CTRL+C event to stop code function
        CTRL_C_EVENT = 0  # Value storage
        GenerateConsoleCtrlEvent(CTRL_C_EVENT, 0)  # Uses pywin32 library
        return "Worked"
    except Exception as e:
        # In case of failure, make the operating system shut things down
        os._exit(0)  # This will probably throw a nasty error, but it WILL work
        return e


startServer()
