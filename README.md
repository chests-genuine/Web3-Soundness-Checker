# Web3 Soundness Checker

## Overview
This repository contains a simple script **app.py** that checks the "soundness" of a smart contract by reading its bytecode and calculating its hash using **web3.py**.  
It is compatible with projects related to **Aztec**, **Zama**, **Ethereum**, and other zero-knowledge or web3-based ecosystems where code integrity verification is important.

## Installation
1. Install Python 3.10+  
2. Install dependencies:  
   pip install web3  
3. In `app.py`, replace `your_api_key` with your own Infura API key or RPC node URL.

## Usage
   python3 app.py

## Expected Output
The script will connect to the RPC endpoint, fetch the smart contract bytecode, and calculate its hash.  
If the code exists, it will display a success message confirming the contract’s soundness.

Example output:
🔧 Web3 Soundness Checker (Aztec/Zama compatible)  
🔍 Contract Address: 0x00000000219ab540356cBB839Cbe05303d7705Fa  
Code Hash: 0x8a8a9b6c7f3f6c9b44a99a9d5e41ab8bb5d66a3a5e04afcb9e8c9e7776e2b3d9  
✅ Contract soundness verified (code present)

## Notes
- You can use any RPC endpoint, including private ones (e.g., for Aztec or Zama networks).  
- For stricter validation, compare the hash with a known reference hash from a trusted source.  
