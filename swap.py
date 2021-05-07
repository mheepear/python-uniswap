from uniswap import Uniswap
from web3 import Web3
import json
import math

infura_url = "https://mainnet.infura.io/v3/1c78a15e3a7d4fe9b732e0abb0c78228"
web3 = Web3(Web3.HTTPProvider(infura_url))
# print(web3.isConnected())
# print(web3.eth.blockNumber)

address = "0x0000000000000000000000000000000000000000" # or "0x0000000000000000000000000000000000000000", if you're not making transactions
private_key = ""  # or None, if you're not going to make transactions
uniswap_wrapper = Uniswap(address, private_key, version=2)  # pass version=2 to use Uniswap v2
eth = "0x0000000000000000000000000000000000000000",


outputTokens = { 
  "dai": "0x6b175474e89094c44da98b954eedeac495271d0f",
  "ankr": "0x8290333cef9e6d528dd5618fb97a76f268f3edd4",
  "usdt": "0xdAC17F958D2ee523a2206206994597C13D831ec7"
}

fAmount = input("Amount of ETH is: ")
fData = input("Put in Output token: ")
fToken = outputTokens[fData]
print(fToken)
x = (uniswap_wrapper.get_eth_token_input_price(Web3.toChecksumAddress(fToken), 1*10**18))

print(x)
tAmount = x/10e+17

print("%.2f" % tAmount)

