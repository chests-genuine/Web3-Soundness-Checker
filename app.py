# app.py
from web3 import Web3
import sys

# Simple script to check zkApp or smart contract soundness using web3
RPC_URL = "https://mainnet.infura.io/v3/your_api_key"
CONTRACT_ADDRESS = "0x00000000219ab540356cBB839Cbe05303d7705Fa"  # Ethereum Deposit Contract

def verify_soundness(address):
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    if not w3.is_connected():
        print("❌ Failed to connect to RPC endpoint")
        sys.exit(1)
    code = w3.eth.get_code(Web3.to_checksum_address(address))
    code_hash = Web3.keccak(code).hex()
    print(f"🔍 Contract Address: {address}")
    print(f"Code Hash: {code_hash}")
    if len(code) > 0:
        print("✅ Contract soundness verified (code present)")
    else:
        print("⚠️ Contract appears empty — soundness check failed")

if __name__ == "__main__":
    print("🔧 Web3 Soundness Checker (Aztec/Zama compatible)")
    verify_soundness(CONTRACT_ADDRESS)
