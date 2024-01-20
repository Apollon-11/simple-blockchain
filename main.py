from blockchain import Block
from blockchain import Blockchain
from time import time

JeChain = Blockchain()


JeChain.addBlock(Block(str(int(time())), ({"from": "Nikolay", "to": "Alexey", "amount": 1000000})))

print(JeChain)