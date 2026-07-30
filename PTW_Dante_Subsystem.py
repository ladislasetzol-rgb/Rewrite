import os
import sys
import shutil
import sqlite3
import tempfile
import time
from pathlib import Path
from datetime import datetime

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

class DanteSubsystem:
    def __init__(self):
        self.owr_domains = [
            "reddit.com", "twitter.com", "x.com", "facebook.com", 
            "instagram.com", "tiktok.com", "cnn.com", "foxnews.com", 
            "bbc.com", "nytimes.com", "buzzfeed.com"
        ]
        self.log_file = Path(r"C:\Users\Ladislas.000\Documents\Ray's Sources\PTW_Sovereign_Architecture\dante_observation.log")
        self.chrome_history = Path(os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data\Default\History"))
        
        firefox_profiles = Path(os.path.expandvars(r"%APPDATA%\Mozilla\Firefox\Profiles"))
        self.firefox_history = None
        if firefox_profiles.exists():
            for p in firefox_profiles.iterdir():
                if "default-release" in p.name:
                    db_path = p / "places.sqlite"
                    if db_path.exists():
                        self.firefox_history = db_path
                        break

    def _log_observation(self, url: str, title: str, source: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [DANTE] OBSERVED: {source} | {url[:60]}... | {title[:40]}...\n"
        print(log_entry.strip())
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(log_entry)

    def _query_locked_db(self, db_path: Path, query: str):
        if not db_path or not db_path.exists():
            return []
        
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
        except Exception:
            return []
        finally:
            try:
                temp_file.unlink(missing_ok=True)
            except:
                pass

    def scan_for_friction(self):
        print("="*75)
        print(" [DANTE SUBSYSTEM] INITIATING LETHAL OBSERVATION")
        print(" Target: HJ Friction Domains")
        print("="*75)
        
        # Chrome
        c_query = "SELECT url, title FROM urls ORDER BY last_visit_time DESC LIMIT 20"
        c_results = self._query_locked_db(self.chrome_history, c_query)
        for url, title in c_results:
            for domain in self.owr_domains:
                if domain in url:
                    self._log_observation(url, title if title else "Unknown", "CHROME")

        # Firefox
        f_query = "SELECT url, title FROM moz_places ORDER BY last_visit_date DESC LIMIT 20"
        f_results = self._query_locked_db(self.firefox_history, f_query)
        for url, title in f_results:
            for domain in self.owr_domains:
                if domain in url:
                    self._log_observation(url, title if title else "Unknown", "FIREFOX")

        print("="*75)
        print(" [DANTE SUBSYSTEM] OBSERVATION COMPLETE. HJ NOTED.")
        print("="*75)

if __name__ == "__main__":
    dante = DanteSubsystem()
    dante.scan_for_friction()
