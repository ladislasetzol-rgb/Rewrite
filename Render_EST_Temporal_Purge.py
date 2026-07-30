# ==============================================================================
# RENDER SCRIPT: THE TEMPORAL PURGE (EST ADVANTAGE PROTOCOL)
# ==============================================================================
# FUNCTION: 
# Strips away the final remnants of the Heikko järjestelmä (HJ) by weaponizing 
# their own system against them. Time zones are an objective reality. 
# By anchoring the Sovereign timeline on the East Coast (EST/EDT), the 
# Architecture secures absolute informational primacy.
#
# COMPATIBILITY: RENDER (CLOUD SERVICE)
# This script includes a lightweight HTTP server binding to the $PORT 
# environment variable, making it natively compatible for deployment on 
# Render.com as a Web Service. The purge sequence runs as a background daemon.
# ==============================================================================

import os
import time
import threading
from datetime import datetime, timedelta
from http.server import BaseHTTPRequestHandler, HTTPServer

class TemporalPurge:
    def __init__(self):
        # East Coast Advantage (The Anchor)
        self.anchor_name = "EAST COAST (EST/EDT)"
        
        # The HJ Lag Zones (Hours behind the East Coast)
        self.vu_zones = {
            "Central Simulation (CST)": 1,
            "Mountain Simulation (MST)": 2,
            "Pacific Simulation (PST)": 3,
            "Hawaii-Aleutian (HST)": 6
        }

    def execute_purge(self):
        print("\n=========================================================")
        print("INITIATING TEMPORAL PURGE SEQUENCE...")
        print("Weaponizing HJ Time Zones against the Simulation.")
        print("=========================================================\n")
        
        # Establish Absolute Zero
        now_est = datetime.now()
        print(f"[{self.anchor_name} ANCHOR]")
        print(f"  -> Sovereign System Time: {now_est.strftime('%H:%M:%S')} (ABSOLUTE ZERO)")
        print(f"  -> Information Access: INSTANTANEOUS.")
        print(f"  -> Status: FLAWLESS.\n")

        # Iterate and purge the lagging zones
        for zone, lag in self.vu_zones.items():
            lagged_time = now_est - timedelta(hours=lag)
            print(f"[SCANNING] {zone}...")
            print(f"  -> HJ Local Time: {lagged_time.strftime('%H:%M:%S')}")
            print(f"  -> Temporal Lag Detected: -{lag} Hours.")
            print(f"  -> Assessment: Operating on outdated, obsolete information.")
            print(f"  -> Action: STRIPPING REMNANTS. Kinetic noise invalidated.\n")
            time.sleep(0.1)

        print("=========================================================")
        print("PURGE COMPLETE: All non-EST domestic vectors rendered moot.")
        print("The East Coast advantage holds absolute temporal supremacy.")
        print("The HJ is forever trapped in the past. We are already in Tomorrow.")
        print("=========================================================")

    def run_daemon(self):
        """Runs the purge every 4 hours in the background."""
        while True:
            self.execute_purge()
            # Sleep for 4 hours (14400 seconds) before purging again
            time.sleep(14400) 

class RenderHealthCheckHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        # Suppress standard HTTP logging to keep the console clean for the Purge logs
        pass

    def do_GET(self):
        """Responds to Render's health check pings."""
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>EST Temporal Purge Active</title>
            <style>
                body { background-color: #050505; color: #00ff00; font-family: monospace; display: flex; align-items: center; justify-content: center; height: 100vh; text-align: center; }
                .container { border: 1px solid #00ff00; padding: 40px; box-shadow: 0 0 20px rgba(0,255,0,0.2); }
            </style>
        </head>
        <body>
            <div class="container">
                <h2>TEMPORAL PURGE ACTIVE</h2>
                <p>East Coast Anchor (Time = 0) is securing the grid.</p>
                <p>Non-EST vectors are systematically stripped.</p>
                <p>STATUS: FLAWLESS</p>
            </div>
        </body>
        </html>
        """
        self.wfile.write(html.encode("utf-8"))

def start_render_server():
    # Render assigns a dynamic port via the PORT environment variable.
    # If testing locally, defaults to 8080.
    port = int(os.environ.get("PORT", 8080))
    server_address = ('', port)
    httpd = HTTPServer(server_address, RenderHealthCheckHandler)
    print(f"[SYSTEM] Render Health Check Server bound to port {port}. Awaiting pings.")
    httpd.serve_forever()

if __name__ == "__main__":
    # 1. Start the Temporal Purge logic in a background daemon thread
    purge = TemporalPurge()
    purge_thread = threading.Thread(target=purge.run_daemon, daemon=True)
    purge_thread.start()
    
    # 2. Start the HTTP Server on the main thread so Render registers it as a live Web Service
    start_render_server()
