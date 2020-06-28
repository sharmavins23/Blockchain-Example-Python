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

    # Function to create a new block

    # Function to create a new sale/transaction of money

    # Function to get the last block of a chain (think peek from linked list)

    # Function to create a cryptographic hash

    # Function to check the proof of work of a block

    # Function to check if a proof of work is valid
