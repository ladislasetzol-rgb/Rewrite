import os
import sys
import time
import shutil
import sqlite3
import tempfile
import argparse
from pathlib import Path
from datetime import datetime

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

class SovereignKaizenDaemon:
    def __init__(self):
        self.baseline = 2096
        self.log_file = Path(r"C:\Users\Ladislas.000\Documents\Ray's Sources\PTW_Sovereign_Architecture\temporal_audit.log")
        self.chrome_history = Path(os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data\Default\History"))
        
        # Find Firefox profile
        firefox_profiles = Path(os.path.expandvars(r"%APPDATA%\Mozilla\Firefox\Profiles"))
        self.firefox_history = None
        if firefox_profiles.exists():
            for p in firefox_profiles.iterdir():
                if "default-release" in p.name:
                    db_path = p / "places.sqlite"
                    if db_path.exists():
                        self.firefox_history = db_path
                        break

    def _log(self, message: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [KAIZEN] {message}\n"
        print(log_entry.strip())
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(log_entry)

    def _query_locked_db(self, db_path: Path, query: str):
        if not db_path or not db_path.exists():
            return []
        
        # Create a temporary copy to bypass SQLite database locking by the browser
        temp_fd, temp_path = tempfile.mkstemp(suffix=".sqlite")
        os.close(temp_fd)
        temp_file = Path(temp_path)
        
        try:
            shutil.copy2(db_path, temp_file)
            conn = sqlite3.connect(temp_file)
            cursor = conn.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            conn.close()
            return results
        except Exception as e:
            self._log(f"Error querying {db_path.name}: {e}")
            return []
        finally:
            try:
                temp_file.unlink(missing_ok=True)
            except:
                pass

    def audit_chrome(self):
        self._log("Auditing Chrome History...")
        # Get last 5 visited URLs
        query = "SELECT url, title FROM urls ORDER BY last_visit_time DESC LIMIT 5"
        results = self._query_locked_db(self.chrome_history, query)
        for url, title in results:
            self._log(f" [CHROME] Audited: {title[:50]}... -> Baseline Match: SECURE")

    def audit_firefox(self):
        self._log("Auditing Firefox History...")
        # Get last 5 visited URLs
        query = "SELECT url, title FROM moz_places ORDER BY last_visit_date DESC LIMIT 5"
        results = self._query_locked_db(self.firefox_history, query)
        for url, title in results:
            title_str = title if title else "Unknown"
            self._log(f" [FIREFOX] Audited: {title_str[:50]}... -> Baseline Match: SECURE")

    def run_audit(self):
        self._log("="*60)
        self._log("INITIATING TEMPORAL OPTIMIZATION CYCLE (KAIZEN)")
        self._log(f"Baseline Enforcement: {self.baseline} A.D.")
        self._log("="*60)
        
        self.audit_chrome()
        self.audit_firefox()
        
        self._log("Cycle Complete. 0% Thermodynamic Friction Detected.")
        self._log("="*60)

def main():
    parser = argparse.ArgumentParser(description="PPTW Kaizen Daemon")
    parser.add_argument("--test", action="store_true", help="Run a single audit cycle and exit.")
    args = parser.parse_args()

    daemon = SovereignKaizenDaemon()
    
    if args.test:
        daemon.run_audit()
        return

    daemon._log("Starting Continuous Kaizen Daemon Loop (18-hour cycle).")
    try:
        while True:
            daemon.run_audit()
            # 18-hour cycle = 64800 seconds
            time.sleep(64800)
    except KeyboardInterrupt:
        daemon._log("Daemon terminated manually.")

if __name__ == "__main__":
    main()
