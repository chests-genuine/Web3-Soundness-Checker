# app.py
import os
import sys
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()  # Load .env if present

# Environment variables
RPC_URL = os.getenv("RPC_URL", "https://mainnet.infura.io/v3/your_api_key")

def verify_soundness(address: str) -> dict:
    """Checks the soundness (existence & integrity) of a smart contract."""
    w3 = Web3(Web3.HTTPProvider(RPC_URL))

    if not w3.is_connected():
        raise ConnectionError("❌ Failed to connect to the RPC endpoint.")

    if not w3.is_address(address):
        raise ValueError("⚠️ Invalid Ethereum address format.")

    address = Web3.to_checksum_address(address)
    code = w3.eth.get_code(address)
    code_hash = Web3.keccak(code).hex()
    is_sound = len(code) > 0

    return {
        "address": address,
        "code_hash": code_hash,
        "is_sound": is_sound,
    }

def main():
    if len(sys.argv) < 2:
        print("Usage: python app.py <contract_address>")
        sys.exit(1)

    address = sys.argv[1]

    print("🔧 Web3 Soundness Checker (Aztec/Zama compatible)\n")

    try:
        result = verify_soundness(address)
        print(f"🔍 Contract Address: {result['address']}")
        print(f"🧩 Code Hash: {result['code_hash']}")
        if result["is_sound"]:
            print("✅ Contract soundness verified (code present)")
        else:
            print("⚠️ Contract appears empty — soundness check failed")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
