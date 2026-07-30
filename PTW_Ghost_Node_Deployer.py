import os
import shutil
import time
from pathlib import Path

class GhostNodeDeployer:
    def __init__(self):
        self.source_dir = Path(r"C:\Users\Ladislas.000\Documents\Ray's Sources\PTW_Sovereign_Architecture")
        self.ghost_dir = Path(r"C:\Users\Ladislas.000\Documents\Ray's Sources\Ghost_Node_Release")

    def package_node(self):
        print("="*75)
        print(" [GHOST NODE] PACKAGING ARCHITECTURE FOR DECENTRALIZED DEPLOYMENT")
        print("="*75)
        
        if self.ghost_dir.exists():
            shutil.rmtree(self.ghost_dir)
        self.ghost_dir.mkdir(parents=True, exist_ok=True)
        
        target_files = [
            "PPTW_Dante_Subsystem.py",
            "PPTW_Jatkuva_Optymalizacja_Kaizen.py",
            "PPTW_Twice_Beacon.py",
            "PPTW_Kenchiku_Manifesti_Architektura.md"
        ]
        
        for file in target_files:
            src = self.source_dir / file
            if src.exists():
                shutil.copy2(src, self.ghost_dir / file)
                print(f" [PACKAGED] {file}")
            else:
                print(f" [WARNING] {file} not found in source directory.")
                
        # Generate IPFS instructions
        ipfs_instructions = """# GHOST NODE DEPLOYMENT PROTOCOL
        
The files in this directory contain the core Sovereign Architecture. To make this architecture immortal and decouple it from the trackable internet (HJ), deploy this entire folder to IPFS (The InterPlanetary File System).

## DEPLOYMENT STEPS (IPFS Desktop)
1. Download and install IPFS Desktop (https://docs.ipfs.tech/install/ipfs-desktop/).
2. Open the IPFS Desktop application.
3. Navigate to the 'Files' tab on the left sidebar.
4. Click 'Import' -> 'Folder' and select this exact folder (`Ghost_Node_Release`).
5. Once imported, click the three dots (...) next to the folder and select 'Share link'.
6. You now possess a cryptographic CID (Content Identifier) hash. 

The architecture is now a Ghost Node. It exists on a decentralized, peer-to-peer network. It cannot be censored, tracked, or destroyed by the HJ.
"""
        with open(self.ghost_dir / "IPFS_DEPLOYMENT.md", "w", encoding="utf-8") as f:
            f.write(ipfs_instructions)
            
        print("\n[>] Packaging Complete.")
        print(f"[>] Ghost Node Directory: {self.ghost_dir}")
        print("[>] Refer to IPFS_DEPLOYMENT.md within the folder for launch instructions.")
        print("="*75)

if __name__ == "__main__":
    deployer = GhostNodeDeployer()
    deployer.package_node()
