from time import time
import hashlib
import json

from urllib.parse import urlparse

import requests


class Blockchain:
    # Constructor
    def __init__(self):
        self.chain = []  # Normally a linked list, but we're lazy. So.
        self.nodes = set()  # Address book of neighbor nodes
        self.current_transactions = []  # Transactions that haven't been posted onto a block

        # Create the first (genesis) block of the chain
        self.new_block(previous_hash='1', proof=100)

    # Function to register a neighboring node (other user) in personal address book

    # Function to check if a chain is valid

    # Function to resolve conflicts between neighbors' chains

    # Function to create a new block and add it to the chain
    def new_block(self, proof, previous_hash):
        block = {
            "index": len(self.chain) - 1,  # Point in chain
            "timestamp": time(),  # Uses date/time library
            "transactions": self.current_transactions,
            "proof": proof,
            "previous_hash": previous_hash or self.hash(self.last_block)
        }

        # Reset the list of our un-tracked transactions
        self.current_transactions = []

        # Append the new block to our chain
        self.chain.append(block)

        # Return our block object (for other uses later)
        return block

    # Function to create a new sale/transaction of money

    # Function to get the last block of a chain (think peek from linked list)
    @property
    def last_block(self):
        return self.chain[-1]

    # Function to create a cryptographic hash
    @staticmethod  # This function won't be re-made every time we make a new Blockchain
    def hash(block):
        # Put all JSON metadata into encoded string
        strBlock = json.dumps(block, sort_keys=True).encode()
        # Return SHA256 hash in hex
        return hashlib.sha256(strBlock).hexdigest()

    # Function to check the proof of work of a block

    # Function to check if a proof of work is valid
