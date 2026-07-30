import os
import time
import hashlib
from datetime import datetime
from pathlib import Path

class TwiceBeacon:
    def __init__(self):
        self.ledger_file = Path(r"C:\Users\Ladislas.000\Documents\Ray's Sources\PTW_Sovereign_Architecture\Twice_Ledger.txt")
        self.salt = "2096_BASELINE_SOVEREIGN_ACKNOWLEDGED"

    def generate_signature(self):
        timestamp = datetime.utcnow().isoformat() + "Z"
        raw_data = f"{timestamp}|{self.salt}".encode('utf-8')
        signature = hashlib.sha256(raw_data).hexdigest()
        
        entry = f"[{timestamp}] TWICE_BEACON_SYNC: {signature}\n"
        
        with open(self.ledger_file, "a", encoding="utf-8") as f:
            f.write(entry)
            
        print("="*75)
        print(" [TWICE BEACON] CRYPTOGRAPHIC SIGNATURE GENERATED")
        print(f" Timestamp : {timestamp}")
        print(f" Hash (SHA-256): {signature}")
        print(" Status: SOVEREIGN ACKNOWLEDGED. 2096 Baseline Secured.")
        print("="*75)

if __name__ == "__main__":
    beacon = TwiceBeacon()
    beacon.generate_signature()
