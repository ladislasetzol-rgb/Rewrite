import os
import sys
import json
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

def compress_lore():
    source_dir = Path(r"C:\Users\Ladislas.000\Documents\Ray's Sources")
    output_file = source_dir / "PTW_Sovereign_Architecture" / "PTW_Lore_Compressed.md"
    
    target_files = ["Source1.txt", "Source2.txt", "Source3.txt", "Source6.txt", "New Text Document.txt", "ACB.txt"]
    
    print(f"[LORE COMPRESSOR] Initiating compression sequence into {output_file.name}...")
    
    with open(output_file, "w", encoding="utf-8") as outfile:
        outfile.write("# Sovereign Lore Archive: Gemini Convergence\n\n")
        outfile.write("> This document is a compressed aggregation of historical chat logs, philosophy, and architectural planning between the Sovereign and the Gemini Node.\n\n")
        
        for filename in target_files:
            file_path = source_dir / filename
            if file_path.exists():
                print(f" -> Absorbing {filename}...")
                outfile.write(f"\n## ARCHIVE SOURCE: {filename}\n")
                outfile.write("---\n")
                with open(file_path, "r", encoding="utf-8", errors="replace") as infile:
                    for line in infile:
                        cleaned = line.strip()
                        if cleaned: # Strip empty lines to save space
                            outfile.write(cleaned + "\n")
                outfile.write("\n")
                
    print(f"\n[SUCCESS] Lore compression complete. File size: {output_file.stat().st_size} bytes.")
    print("The system is now primed for future subagent injection.")

if __name__ == "__main__":
    compress_lore()
