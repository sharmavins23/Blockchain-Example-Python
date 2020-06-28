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
    def register_node(self, address):
        parsed_url = urlparse(address)  # Parse value into usable format

        if parsed_url.netloc:  # If there is a specific net domain, e.g. "example.com"
            self.nodes.add(parsed_url.netloc)  # Add the net location
        elif parsed_url.path:  # If URL has 'IP address' schema, e.g. "192.168.1.1:3000"
            self.nodes.add(parsed_url.path)  # Add the IP path
        else:  # If no URL provided
            raise ValueError("Invalid address")

    # Function to check if a chain is valid
    def valid_chain(self, chain):
        last_block = chain[0]  # We'll iterate through all blocks
        current_index = 1
        # Normally, we should be checking all of the proofs of work.
        # But instead we're going to check the hash values lining up

        while current_index < len(chain):
            block = chain[current_index]  # Temp. store current block
            last_block_hash = self.hash(last_block)  # Store last hash

            # If hash pointer is wrong, it's not a valid chain.
            if block["previous_hash"] != last_block_hash:
                return False

            last_block = block  # Iterate to next block in chain
            current_index += 1

        # At this point, all of the blocks have been checked and are NOT INvalid
        return True

    # Function to resolve conflicts between neighbors' chains
    def resolve_conflicts(self):
        neighbors = self.nodes  # Load address book into mutable temp. store
        new_chain = None  # Temp. store for neighbors' chains

        max_length = len(self.chain)

        for node in neighbors:  # Get all chains from all neighbor servers
            response = requests.get(f"http://{node}/chain")

            if response.status_code == 200:  # OK status
                length = response.json()["length"]
                chain = response.json()["chain"]

                # The longest chain is going to be the correct one, for this example
                if length > max_length and self.valid_chain(chain):
                    max_length = length
                    new_chain = chain

        # At this point, if a new chain has not been found, the new_chain will still have None from initialization
        # None always coerces to False. But any other value will coerce to True
        if new_chain:
            self.chain = new_chain  # Replace the chain
            return True

        return False  # The chain wasn't replaced

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

    # Function to create the proof of work of a block
    def proof_of_work(self, last_block):
        last_proof = last_block["proof"]  # Last proof of work
        last_hash = self.hash(last_block)  # Recalc last hash

        proof = 0
        # Don't actually do this... This is for simplification purposes.
        while self.valid_proof(last_proof, proof, last_hash) is False:
            proof += 1  # Iterates proof values instead of calculating
            # Will keep iterating until a proof works and is valid
            # Which means this could theoretically take infinite time

        return proof

    # Function to check if a proof of work is valid
    @staticmethod
    def valid_proof(last_proof, proof, last_hash):
        # Create a proof based on these encoded values
        guess = f"{last_proof}{proof}{last_hash}".encode()
        guess_hash = hashlib.sha256(guess).hexdigest()

        # A valid proof will have first four bits zeroes, and return True
        return guess_hash[:4] == "0000"
