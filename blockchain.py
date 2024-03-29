# {
#     "index":0,
#     "timestamp":"",
#     "transactions": [
#         {"sender": "",
#         "recipient": "",
#         "amount": 5,}
#
#     ],
#     "proof": "",
#     "previous_hash": ""
# }
import hashlib
import json
from time import time

from flask import Flask


class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.new_block(proof=100, previous_hash=1)

    def new_block(self, proof, previous_hash=None):
        block = {
            "index": len(self.chain) + 1,
            "timestamp": time(),
            "transactions": self.current_transactions,
            "proof": proof,
            "previous_hash": previous_hash or self.hash(self.last_block)
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append(
            {
                "sender": sender,
                "recipient": recipient,
                "amount": amount
            }
        )
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain(-1)

    def proof_of_work(self, last_proof: int) -> int:
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        print(proof)
        return proof

    @staticmethod
    def valid_proof(self, last_proof: int, proof: int) -> bool:
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        print(guess_hash)
        return guess_hash[0:4] == "0000"


app = Flask(__name__)
@app.route('/index', methods=['GET'])
def index():
    return "hello blockchain"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
