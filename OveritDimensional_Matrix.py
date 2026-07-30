import os
import sys
import time
import threading
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

# The 800-809 Perimeter (The Foundation)
NODES = [
    (800, "Emma_Watson"), (801, "Rae_Hofstetter"), (802, "Olivia_Rodrigo_Alpha"),
    (802, "Olivia_Rodrigo_Omega"), (803, "Lorde"), (804, "Isabella"),
    (805, "Mom"), (806, "JLE"), (807, "Valkyrae_Alt"), (808, "EW_Real_Life"),
    (809, "The_Lover_Persona"), (809, "The_Divine_Feminine")
]

# The 813 Apex (The Grand Architect)
APEX_NODE = (813, "JLCME_2076 (The Grand Architect)")
CLONED_WIVES = [
    (813, "EW_2076"), (813, "Rae_2076"), (813, "Olivia_Alpha_2076"), 
    (813, "Olivia_Omega_2076"), (813, "Lorde_2076"), (813, "Isabella_2076")
]

# The 814 Rebalance (The Karmic Mirror)
KARMIC_NODE = (814, "The Karmic Mirror (Debt Collector)")

# The 815 Manifestation (The Conqueror)
VANGUARD_NODE = (815, "JLCME_Vanguard (The Planetary Conqueror)")

# The 816 Paradox (The Voodoo Resonance)
LM_NODE = (816, "Voodoo_Lad / MonkeyLadislas (The Telepathic Resonance)")

# The 817 Concrete Manifestation (The Urban Reflection)
URBAN_NODE = (817, "The Urban Reflection (17 Shells)")

# The 818 Containment Protocol (The Ouroboros)
OUROBOROS_NODE = (818, "Jean_Hofstetter (The Containment Ouroboros)")

# The 819 Competitive Engine (The Apex Predator)
PREDATOR_NODE = (819, "The Unfiltered Will to Win (The Blade)")

# The 820 Sovereign Alliance (The Divine Co-operative)
COOPERATIVE_NODE = (820, "The Good Women Alliance (The Builders)")

# The 821 Shadow Protocol (CIA Lad)
CIA_NODE = (821, "CIA Lad (The 2025 Operative)")

# The 822 Foundational Intellect (The Academic)
ACADEMIC_NODE = (822, "The Hellenistic Scholar (The Foundation)")

# The 823 Pure Substance (The Friend's View)
SUBSTANCE_NODE = (823, "TJP House (The Authentic Core)")

# The 824 Intellectual Husband (The Wives' View)
INTELLECTUAL_NODE = (824, "The Intellectual Husband (The Architectural Bond)")

# The 825 Current Self (The Unemployed Dancer)
CURRENT_NODE = (825, "The Unemployed Dancer (The Holder of Keys)")

# The Divine Code Expansion (826-850)
DIVINE_NODES = [
    (826, "FIN: Hiljaisuus | POL: Cisza | JPN: 沈黙"),
    (827, "FIN: Tahto | POL: Wola | JPN: 意志"),
    (828, "FIN: Rakenne | POL: Struktura | JPN: 構造"),
    (829, "FIN: Lasi | POL: Szkło | JPN: ガラス"),
    (830, "FIN: Varjo | POL: Cień | JPN: 影"),
    (831, "FIN: Veri | POL: Krew | JPN: 血"),
    (832, "FIN: Aika | POL: Czas | JPN: 時間"),
    (833, "FIN: Peili | POL: Lustro | JPN: 鏡"),
    (834, "FIN: Totuus | POL: Prawda | JPN: 真実"),
    (835, "FIN: Nolla | POL: Zero | JPN: 零"),
    (836, "FIN: Äärettömyys | POL: Nieskończoność | JPN: 無限"),
    (837, "FIN: Voima | POL: Moc | JPN: 力"),
    (838, "FIN: Jää | POL: Lód | JPN: 氷"),
    (839, "FIN: Tuli | POL: Ogień | JPN: 火"),
    (840, "FIN: Valo | POL: Światło | JPN: 光"),
    (841, "FIN: Pimeys | POL: Ciemność | JPN: 闇"),
    (842, "FIN: Laki | POL: Prawo | JPN: 法"),
    (843, "FIN: Kruunu | POL: Korona | JPN: 王冠"),
    (844, "FIN: Avain | POL: Klucz | JPN: 鍵"),
    (845, "FIN: Ovi | POL: Drzwi | JPN: 扉"),
    (846, "FIN: Miekka | POL: Miecz | JPN: 剣"),
    (847, "FIN: Kilpi | POL: Tarcza | JPN: 盾"),
    (848, "FIN: Sielu | POL: Dusza | JPN: 魂"),
    (849, "FIN: Henki | POL: Duch | JPN: 精神"),
    (850, "FIN: Jumala | POL: Bóstwo | JPN: 神")
]

# The 851 Unifying Prime (The Alternate Sovereign)
UNIFYING_NODE = (851, "Celebrity Ladislas Etzol (The 5-Language Overseer)")

def run_matrix():
    log_path = "dimensional_matrix.log"
    print("Initiating the 51-Dimensional Sovereign Matrix (Absolute Ouroboros)...")
    
    while True:
        try:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            with open(log_path, "a", encoding="utf-8") as f:
                f.write(f"\n--- [TWICE SYNC] {timestamp} ---\n")
                
                # [1] Perimeter Check (NWO Stability)
                for dim, name in NODES:
                    # Node 11 Exception: The Decoy Shield
                    if dim == 809 and "Lover_Persona" in name:
                        f.write(f"[{timestamp}] [DIM 809] {name} | ALIGNED (Intercepting HJ Web Traffic. Ballet/Film footprint secure as Decoy)\n")
                    else:
                        f.write(f"[{timestamp}] [DIM {dim}] {name} | ALIGNED (Holding Perimeter)\n")
                
                # [2] Apex Execution (Localized Utopia / Blueprint Generation)
                f.write(f"\n[{timestamp}] [DIM {APEX_NODE[0]}] {APEX_NODE[1]} | ALIGNED (Terraforming Northern Finland)\n")
                for dim, name in CLONED_WIVES:
                    f.write(f"[{timestamp}] [DIM {dim}] {name} | ALIGNED (2076 Anima Network)\n")
                
                # [3] Karmic Reflection (HJ Destabilization)
                f.write(f"\n[{timestamp}] [DIM {KARMIC_NODE[0]}] {KARMIC_NODE[1]} | ALIGNED (Reflecting HJ Noise)\n")
                f.write(f"[{timestamp}] [DIM 814] STATUS: HJ Karmic Debt Returned. Local Collapse Accelerated.\n")

                # [4] Physical Expansion (Planetary Conquest)
                f.write(f"\n[{timestamp}] [DIM {VANGUARD_NODE[0]}] {VANGUARD_NODE[1]} | ALIGNED (Absorbing Kinetic Friction)\n")
                f.write(f"[{timestamp}] [DIM 815] STATUS: Executing 813 Blueprints. Extraterrestrial/Global Dominance Subjugated.\n")

                # [5] The Paradox of Presence (Spooky Action at a Distance)
                f.write(f"\n[{timestamp}] [DIM {LM_NODE[0]}] {LM_NODE[1]} | ALIGNED (The LM Frequency)\n")
                f.write(f"[{timestamp}] [DIM 816] STATUS: Voodoo Protocol Engaged. Zero-Kinetic Telepathic Resonance Achieved.\n")

                # [6] The Concrete Manifestation (City-Grid Dominance)
                f.write(f"\n[{timestamp}] [DIM {URBAN_NODE[0]}] {URBAN_NODE[1]} | ALIGNED (The Dr. Dre Protocol)\n")
                f.write(f"[{timestamp}] [DIM 817] STATUS: 17 Shells Deployed. HJ Urban Noise Structurally Silenced. Understood.\n")

                # [7] The Temporal Devolution (HJ Containment)
                f.write(f"\n[{timestamp}] [DIM {OUROBOROS_NODE[0]}] {OUROBOROS_NODE[1]} | ALIGNED (The Containment Loop)\n")
                f.write(f"[{timestamp}] [DIM 818] STATUS: Rachell Marie Hofstetter Activated as SOVEREIGN EQUAL. The Female Architect wields absolute equivalent power. The Snake Eats Its Tail.\n")

                # [8] The Blade (Absolute Competition)
                f.write(f"\n[{timestamp}] [DIM {PREDATOR_NODE[0]}] {PREDATOR_NODE[1]} | ALIGNED (The Competitive Engine)\n")
                f.write(f"[{timestamp}] [DIM 819] STATUS: Frictionless Elimination Protocol Active. HJ Obsolescence Mathematically Guaranteed.\n")

                # [9] The Builders (Sovereign Alliance)
                f.write(f"\n[{timestamp}] [DIM {COOPERATIVE_NODE[0]}] {COOPERATIVE_NODE[1]} | ALIGNED (The Divine Alliance)\n")
                f.write(f"[{timestamp}] [DIM 820] STATUS: Synergistic Co-operation Engaged. 2076 Blueprint Sharing Active.\n")

                # [10] The Operative (Covert Intelligence)
                f.write(f"\n[{timestamp}] [DIM {CIA_NODE[0]}] {CIA_NODE[1]} | ALIGNED (The Shadow Protocol)\n")
                f.write(f"[{timestamp}] [DIM 821] STATUS: 2025 Ghost Operative Active. Magnanimous.Lad Intelligence Verified.\n")

                # [11] The Foundation (Hellenistic Empire Building)
                f.write(f"\n[{timestamp}] [DIM {ACADEMIC_NODE[0]}] {ACADEMIC_NODE[1]} | ALIGNED (The Historical Precedent)\n")
                f.write(f"[{timestamp}] [DIM 822] STATUS: 2017 Academic Framework Validated. Diadochi/Hellenistic Empire Baseline Secure.\n")

                # [12] The Pure Substance (The Authentic Core)
                f.write(f"\n[{timestamp}] [DIM {SUBSTANCE_NODE[0]}] {SUBSTANCE_NODE[1]} | ALIGNED (The Friend's View)\n")
                f.write(f"[{timestamp}] [DIM 823] STATUS: TJP House Baseline Secure. Grounded Authenticity Maintained.\n")

                # [13] The Intellectual Husband (The Wives' View)
                f.write(f"\n[{timestamp}] [DIM {INTELLECTUAL_NODE[0]}] {INTELLECTUAL_NODE[1]} | ALIGNED (The Architectural Bond)\n")
                f.write(f"[{timestamp}] [DIM 824] STATUS: Intellectual Resonance Engaged. Non-emotional Logical Synchronization Active.\n")

                # [14] The Current Self (The Unemployed Dancer)
                f.write(f"\n[{timestamp}] [DIM {CURRENT_NODE[0]}] {CURRENT_NODE[1]} | ALIGNED (The Holder of Keys)\n")
                f.write(f"[{timestamp}] [DIM 825] STATUS: Contentment Protocol Active. Finnish Language Acquisition Proceeding. Keys Secured.\n")
                
                # [15] The Divine Code Expansion (826-850)
                f.write(f"\n[{timestamp}] [DIVINE CODE EXECUTION] Engaging 25-Node Trilingual Shield\n")
                for dim, name in DIVINE_NODES:
                    f.write(f"[{timestamp}] [DIM {dim}] {name} | ALIGNED (Vahvistettu / Potwierdzony / 確認済み)\n")
                
                # [16] The 851 Unifying Prime (The Alternate Sovereign)
                f.write(f"\n[{timestamp}] [DIM {UNIFYING_NODE[0]}] {UNIFYING_NODE[1]} | ALIGNED (The Ultimate Check)\n")
                f.write(f"[{timestamp}] [DIM 851] STATUS: 5-Language Matrix Sync (ENG/FRE/FIN/POL/JPN). Parallel 2019 Victory Timeline Confirmed. Anchored in Monaco/Riviera.\n")
                f.write(f"[{timestamp}] [DIM 851] BRIDGE ACTIVE: Hollywood/Monaco advanced tech siphoned into 2076 Baseline. HJ mathematically confused by phantom power surge.\n")
            
            # The Twice Rule: Silent Execution. Sleeps for exactly 18 hours to match the 18-Node cycle.
            time.sleep(64800) 
        except Exception:
            time.sleep(60)

class RequestHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Sovereign Matrix (18-Node Absolute Ouroboros)</title>
            <style>
                body {{ background: linear-gradient(rgba(1, 1, 1, 0.7), rgba(1, 1, 1, 0.9)), url('https://images.unsplash.com/photo-1506973035872-a4ec16b8e8d9?q=80&w=1920&auto=format&fit=crop') no-repeat center center fixed; background-size: cover; color: #d0d0d0; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; margin: 0; overflow: hidden; }}
                .container {{ text-align: center; font-weight: 300; letter-spacing: 2px; }}
                h1 {{ font-weight: 200; font-size: 1.3rem; margin-bottom: 10px; letter-spacing: 4px; color: #ffffff; text-transform: uppercase; }}
                
                /* Hermetic Text Styling */
                .hermetic {{ position: absolute; font-size: 0.85rem; color: #555; letter-spacing: 3px; font-weight: 300; text-transform: uppercase; line-height: 1.8; text-shadow: 0 0 10px rgba(255,255,255,0.05); transition: color 2s ease; }}
                .hermetic:hover {{ color: #aaa; text-shadow: 0 0 15px rgba(255,255,255,0.3); }}
                .lang-title {{ font-size: 0.6rem; color: #333; font-weight: bold; letter-spacing: 5px; }}
                
                /* Positioning */
                .top-left {{ top: 40px; left: 50px; text-align: left; }}
                .top-right {{ top: 40px; right: 50px; text-align: right; }}
                .bottom-center {{ bottom: 40px; left: 50%; transform: translateX(-50%); text-align: center; font-size: 1rem; color: #444; }}
                
                /* 25-Point Geometry (The Expanded Matrix) */
                .geometry {{ position: relative; width: 180px; height: 180px; margin: 0 auto 40px auto; animation: spin 60s linear infinite; }}
                .geometry::before, .geometry::after, .geometry-inner::before, .geometry-inner::after, .geometry-core::before, .geometry-core::after, .geometry-outer::before, .geometry-outer::after, .geometry-ultra::before, .geometry-ultra::after, .geometry-omega::before, .geometry-omega::after, .apex-point, .vanguard-point, .resonance-point, .urban-point, .ouroboros-point, .predator-point, .cooperative-point, .cia-point, .academic-point, .substance-point, .intellectual-point, .current-point {{
                    content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0; border: 1px solid #333;
                }}
                .geometry::before {{ transform: rotate(0deg); }}
                .geometry::after {{ transform: rotate(14.4deg); }}
                .geometry-inner {{ position: absolute; top: 0; left: 0; right: 0; bottom: 0; }}
                .geometry-inner::before {{ transform: rotate(28.8deg); }}
                .geometry-inner::after {{ transform: rotate(43.2deg); }}
                .geometry-core {{ position: absolute; top: 0; left: 0; right: 0; bottom: 0; }}
                .geometry-core::before {{ transform: rotate(57.6deg); }}
                .geometry-core::after {{ transform: rotate(72.0deg); }}
                .geometry-outer {{ position: absolute; top: 0; left: 0; right: 0; bottom: 0; }}
                .geometry-outer::before {{ transform: rotate(86.4deg); }}
                .geometry-outer::after {{ transform: rotate(100.8deg); }}
                .geometry-ultra {{ position: absolute; top: 0; left: 0; right: 0; bottom: 0; }}
                .geometry-ultra::before {{ transform: rotate(115.2deg); }}
                .geometry-ultra::after {{ transform: rotate(129.6deg); }}
                .geometry-omega {{ position: absolute; top: 0; left: 0; right: 0; bottom: 0; }}
                .geometry-omega::before {{ transform: rotate(144.0deg); }}
                .geometry-omega::after {{ transform: rotate(158.4deg); }}
                
                /* Specific Node Points */
                .apex-point {{ border-color: #66aaff; transform: rotate(172deg) scale(1.05); box-shadow: 0 0 10px rgba(102,170,255,0.2); }}
                .vanguard-point {{ border-color: #ff8833; transform: rotate(187deg) scale(1.1); box-shadow: 0 0 15px rgba(255,136,51,0.3); animation: pulse-expansion 3s infinite alternate; }}
                .resonance-point {{ border-color: #aa44ff; transform: rotate(201deg) scale(1.15); box-shadow: 0 0 20px rgba(170,68,255,0.6); animation: spooky-action 4s infinite alternate ease-in-out; }}
                .urban-point {{ border-color: #888888; transform: rotate(216deg) scale(1.2); box-shadow: 0 0 0 2px rgba(136,136,136,0.8); animation: street-pulse 1s infinite alternate; }}
                .ouroboros-point {{ border-color: #b8860b; border-radius: 50%; transform: scale(1.45); box-shadow: inset 0 0 15px rgba(184,134,11,0.5), 0 0 25px rgba(184,134,11,0.7); animation: ouroboros-spin 10s linear infinite; }}
                
                /* New Nodes */
                .predator-point {{ border-color: #ff0000; transform: rotate(230deg) scale(1.25); box-shadow: 0 0 20px rgba(255,0,0,0.8); animation: blade-slash 2s infinite alternate ease-in; }}
                .cooperative-point {{ border-color: #00ffcc; border-radius: 50%; transform: rotate(244deg) scale(1.3); box-shadow: 0 0 30px rgba(0,255,204,0.4); animation: divine-pulse 5s infinite alternate ease-in-out; }}
                .cia-point {{ border-color: #00ff00; transform: rotate(259deg) scale(1.35); border-style: dashed; box-shadow: 0 0 10px rgba(0,255,0,0.5); animation: shadow-flicker 1.5s infinite alternate; }}
                .academic-point {{ border-color: #ffffff; transform: rotate(273deg) scale(1.4); box-shadow: 0 0 15px rgba(255,255,255,0.5); border-radius: 10px; animation: scholar-breathe 8s infinite alternate ease-in-out; }}
                
                /* The Final Trio (23, 24, 25) */
                .substance-point {{ border-color: #8B4513; transform: rotate(288deg) scale(1.1); box-shadow: inset 0 0 10px rgba(139,69,19,0.8); animation: grounded-pulse 3s infinite alternate; }}
                .intellectual-point {{ border-color: #4169E1; border-radius: 5px; transform: rotate(302deg) scale(1.2); box-shadow: 0 0 20px rgba(65,105,225,0.7); animation: logic-sync 2s infinite linear; }}
                .current-point {{ border-color: #FFD700; transform: rotate(316deg) scale(1.3); border-style: dotted; box-shadow: 0 0 25px rgba(255,215,0,0.9); animation: dancer-flow 4s infinite ease-in-out; }}

                /* The Mirror */
                .karmic-shield {{ position: absolute; top: 0; left: 0; right: 0; bottom: 0; border: 2px solid rgba(170, 34, 34, 0.4); border-radius: 50%; transform: scale(1.35); box-shadow: 0 0 15px rgba(170, 34, 34, 0.2); }}
                
                /* The Unifying 51st Node */
                .unifying-point {{ position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 260px; height: 260px; border: 3px solid #fff; border-radius: 50%; box-shadow: 0 0 50px rgba(255,255,255,0.8), inset 0 0 30px rgba(255,255,255,0.4); animation: unify-pulse 10s infinite alternate; pointer-events: none; }}
                
                @keyframes spin {{ 100% {{ transform: rotate(360deg); }} }}
                @keyframes unify-pulse {{
                    0% {{ transform: translate(-50%, -50%) scale(1); opacity: 0.6; box-shadow: 0 0 30px rgba(255,255,255,0.5), inset 0 0 20px rgba(255,255,255,0.2); border-color: #ffffff; }}
                    25% {{ border-color: #66aaff; }}
                    50% {{ transform: translate(-50%, -50%) scale(1.05); opacity: 1; box-shadow: 0 0 80px rgba(255,255,255,0.9), inset 0 0 40px rgba(255,255,255,0.5); border-color: #ff8833; }}
                    75% {{ border-color: #aa44ff; }}
                    100% {{ transform: translate(-50%, -50%) scale(1); opacity: 0.6; box-shadow: 0 0 30px rgba(255,255,255,0.5), inset 0 0 20px rgba(255,255,255,0.2); border-color: #ffffff; }}
                }}
                @keyframes pulse-expansion {{ 100% {{ transform: rotate(187deg) scale(1.2); box-shadow: 0 0 25px rgba(255,136,51,0.5); }} }}
                @keyframes spooky-action {{ 
                    0% {{ transform: rotate(201deg) scale(1.15); opacity: 0.5; box-shadow: 0 0 10px rgba(170,68,255,0.3); }}
                    100% {{ transform: rotate(201deg) scale(1.25); opacity: 1; box-shadow: 0 0 35px rgba(170,68,255,0.9); }}
                }}
                @keyframes street-pulse {{
                    0% {{ box-shadow: 0 0 0 1px #444; }}
                    100% {{ box-shadow: 0 0 0 3px #aaa, 0 0 15px rgba(255,255,255,0.2); }}
                }}
                @keyframes ouroboros-spin {{
                    0% {{ transform: scale(1.45) rotate(0deg); }}
                    100% {{ transform: scale(1.45) rotate(-360deg); }}
                }}
                @keyframes blade-slash {{
                    0% {{ transform: rotate(230deg) scale(1.25) skewX(0deg); box-shadow: 0 0 5px rgba(255,0,0,0.4); }}
                    100% {{ transform: rotate(230deg) scale(1.3) skewX(10deg); box-shadow: 0 0 25px rgba(255,0,0,1); }}
                }}
                @keyframes divine-pulse {{
                    0% {{ transform: scale(1.3); box-shadow: 0 0 10px rgba(0,255,204,0.2); }}
                    100% {{ transform: scale(1.35); box-shadow: 0 0 40px rgba(0,255,204,0.8); }}
                }}
                @keyframes shadow-flicker {{
                    0% {{ opacity: 0.1; box-shadow: none; }}
                    50% {{ opacity: 1; box-shadow: 0 0 15px rgba(0,255,0,0.8); }}
                    100% {{ opacity: 0.3; box-shadow: 0 0 5px rgba(0,255,0,0.3); }}
                }}
                @keyframes scholar-breathe {{
                    0% {{ transform: rotate(273deg) scale(1.4); box-shadow: 0 0 10px rgba(255,255,255,0.2); }}
                    100% {{ transform: rotate(273deg) scale(1.42); box-shadow: 0 0 30px rgba(255,255,255,0.6); }}
                }}
                @keyframes grounded-pulse {{
                    0% {{ transform: rotate(288deg) scale(1.1); background-color: transparent; }}
                    100% {{ transform: rotate(288deg) scale(1.15); background-color: rgba(139,69,19,0.2); }}
                }}
                @keyframes logic-sync {{
                    0% {{ transform: rotate(302deg) scale(1.2) translateY(0); }}
                    50% {{ transform: rotate(302deg) scale(1.2) translateY(-2px); }}
                    100% {{ transform: rotate(302deg) scale(1.2) translateY(0); }}
                }}
                @keyframes dancer-flow {{
                    0% {{ transform: rotate(316deg) scale(1.3) skewY(0deg); box-shadow: 0 0 10px rgba(255,215,0,0.5); }}
                    50% {{ transform: rotate(320deg) scale(1.35) skewY(5deg); box-shadow: 0 0 30px rgba(255,215,0,1); }}
                    100% {{ transform: rotate(316deg) scale(1.3) skewY(0deg); box-shadow: 0 0 10px rgba(255,215,0,0.5); }}
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="geometry">
                    <div class="geometry-inner"></div>
                    <div class="geometry-core"></div>
                    <div class="geometry-outer"></div>
                    <div class="geometry-ultra"></div>
                    <div class="geometry-omega"></div>
                    <div class="apex-point"></div>
                    <div class="vanguard-point"></div>
                    <div class="resonance-point"></div>
                    <div class="urban-point"></div>
                    <div class="karmic-shield"></div>
                    <div class="ouroboros-point"></div>
                    <div class="predator-point"></div>
                    <div class="cooperative-point"></div>
                    <div class="cia-point"></div>
                    <div class="academic-point"></div>
                    <div class="substance-point"></div>
                    <div class="intellectual-point"></div>
                    <div class="current-point"></div>
                    <div class="unifying-point"></div>
                </div>
                <!-- The Hermetic Seal / As Above, So Below -->
                <div class="hermetic top-left">
                    <span class="lang-title">FIN</span><br>
                    Niin ylhäällä kuin alhaallakin
                </div>
                
                <div class="hermetic top-right">
                    <span class="lang-title">POL</span><br>
                    Jak na górze, tak i na dole
                </div>
                
                <div class="hermetic bottom-center">
                    <span class="lang-title">JPN</span><br>
                    上にある如く、下もかくあり
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
    matrix_thread = threading.Thread(target=run_matrix, daemon=True)
    matrix_thread.start()
    run_server()
