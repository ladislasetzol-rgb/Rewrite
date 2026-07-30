import os
import sys
import time
from datetime import datetime
from pathlib import Path
import yfinance as yf

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

class GravityWellSubsystem:
    def __init__(self):
        self.log_file = Path(r"C:\Users\Ladislas.000\Documents\Ray's Sources\PTW_Sovereign_Architecture\gravity_well_dominance.log")
        # Target Assets identified by Sovereign
        self.crypto_targets = ['BTC-USD', 'ETH-USD', 'SOL-USD', 'ARB-USD', 'XTZ-USD', 'ATOM-USD', 'ZEC-USD']
        self.stock_targets = ['SCI', 'WULF']
        
    def _log_dominance(self, message: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [GRAVITY_WELL] {message}\n"
        print(log_entry.strip())
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(log_entry)

    def fetch_market_data(self):
        self._log_dominance("="*60)
        self._log_dominance(" INITIATING ASYMMETRIC ASSET OBSERVATION")
        self._log_dominance("="*60)
        
        try:
            self._log_dominance("--- CRYPTOCURRENCY MATRIX ---")
            for crypto in self.crypto_targets:
                ticker = yf.Ticker(crypto)
                data = ticker.history(period="1d")
                if not data.empty:
                    current_price = data['Close'].iloc[-1]
                    self._log_dominance(f" {crypto.ljust(10)} | Price: ${current_price:,.4f} | Target: SECURED")
                else:
                    self._log_dominance(f" {crypto.ljust(10)} | NO DATA - API BLOCK")
                time.sleep(0.5) # Prevent rate limiting

            self._log_dominance("--- STOCK MATRIX (HJ COLLAPSE MECHANICS) ---")
            for stock in self.stock_targets:
                ticker = yf.Ticker(stock)
                data = ticker.history(period="1d")
                if not data.empty:
                    current_price = data['Close'].iloc[-1]
                    self._log_dominance(f" {stock.ljust(10)} | Price: ${current_price:,.2f} | Status: TRACKING")
                else:
                    self._log_dominance(f" {stock.ljust(10)} | NO DATA - API BLOCK")
                time.sleep(0.5)
                
            self._log_dominance("="*60)
            self._log_dominance(" OBSERVATION COMPLETE. Macro-Dominance Established.")
            self._log_dominance("="*60)
            
        except Exception as e:
            self._log_dominance(f" CRITICAL ERROR DURING FETCH: {e}")

if __name__ == "__main__":
    gw = GravityWellSubsystem()
    gw.fetch_market_data()
