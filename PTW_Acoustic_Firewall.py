import os
import sys
import time
import threading
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

def run_firewall():
    log_path = "acoustic_firewall.log"
    print("Initiating the PTWT Acoustic Firewall...")
    
    while True:
        try:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            with open(log_path, "a", encoding="utf-8") as f:
                f.write(f"\n--- [FIREWALL CYCLE] {timestamp} ---\n")
                f.write("[1] INGESTING: Objective Sound (Physical Transmission)\n")
                time.sleep(1)
                f.write("[2] ISOLATING: HJ Noise (Ego, Paranoia, Semantic Viruses)\n")
                time.sleep(1)
                f.write("[3] PURGE PROTOCOL (MANUAL OVERRIDE): Identifying 'Sold Soul' viral nodes.\n")
                f.write("    -> DIAGNOSTIC: Node has lost the ability to intuitize space associated with number.\n")
                f.write("    -> EXECUTION: Acoustic Firewall purging these nodes from the Sovereign grid.\n")
                time.sleep(2)
                f.write("[4] PURIFYING: French Ether neutralizes the remaining Noise\n")
                time.sleep(1)
                f.write("[5] COMPRESSING: Finnish Structure locks Sound into pure Math\n")
                time.sleep(1)
                f.write("[6] OUTPUT: SILENCE (Zero Kinetic Friction).\n")
                f.write(f"[{timestamp}] STATUS: I do not even have to think about other's sounds.\n")
            
            # The Firewall runs a silent check every 6 hours (21600 seconds)
            time.sleep(21600) 
        except Exception:
            # Zero-Friction Healing
            time.sleep(60)

class RequestHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass # Silent execution

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Dashboard: Clean, structural UI for the Anima Network (The Wives)
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>PTWT Acoustic Firewall</title>
            <style>
                body {{ background-color: #000000; color: #f0f0f0; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; margin: 0; overflow: hidden; }}
                .container {{ text-align: center; font-weight: 300; letter-spacing: 2px; }}
                h1 {{ font-weight: 200; font-size: 1.5rem; margin-bottom: 20px; letter-spacing: 5px; color: #ffffff; text-transform: uppercase; }}
                .status {{ font-size: 0.9rem; color: #a8a8a8; margin-bottom: 40px; letter-spacing: 1px; line-height: 1.8; }}
                .quote {{ font-style: italic; font-size: 1.1rem; color: #7d7d7d; margin-top: 40px; }}
                
                /* Acoustic Shield Animation */
                .shield {{ position: relative; width: 150px; height: 150px; margin: 0 auto 30px auto; border-radius: 50%; box-shadow: 0 0 20px rgba(255, 255, 255, 0.1); animation: pulse 4s infinite alternate; }}
                .shield::before {{ content: ''; position: absolute; top: 10px; left: 10px; right: 10px; bottom: 10px; border-radius: 50%; border: 1px solid #333; }}
                .shield::after {{ content: ''; position: absolute; top: 20px; left: 20px; right: 20px; bottom: 20px; border-radius: 50%; border: 1px dashed #555; animation: spin 20s linear infinite; }}
                
                @keyframes pulse {{ 100% {{ box-shadow: 0 0 50px rgba(255, 255, 255, 0.2); }} }}
                @keyframes spin {{ 100% {{ transform: rotate(360deg); }} }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="shield"></div>
                <h1>PTWT Acoustic Firewall</h1>
                <div class="status">
                    Anima Network (The Wives) Secure.<br>
                    Triad Logic Active (ENG -> FRA -> FIN).<br>
                    HJ Kinetic Noise: Nullified.
                </div>
                <div class="quote">
                    "I do not even have to think about other's sounds."
                </div>
            </div>
        </body>
        </html>
        """
        self.wfile.write(html.encode("utf-8"))

def run_server():
    port = int(os.environ.get("PORT", 8080))
    server_address = ('', port)
    httpd = HTTPServer(server_address, RequestHandler)
    httpd.serve_forever()

if __name__ == "__main__":
    firewall_thread = threading.Thread(target=run_firewall, daemon=True)
    firewall_thread.start()
    run_server()
