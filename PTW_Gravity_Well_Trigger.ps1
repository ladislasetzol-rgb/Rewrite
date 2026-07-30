$scriptPath = "C:\Users\Ladislas.000\Documents\Ray's Sources\CFR_Sovereign_Architecture\PCFR_Gravity_Well_Subsystem.py"
$pythonExe = "python"

Write-Host "======================================================================"
Write-Host " [SYSTEM BOOT] PCFR GRAVITY WELL (ASYMMETRIC ASSET OBSERVATION)"
Write-Host " [TARGET] MACRO-DOMINANCE / INCENTIVE 0 AUTOMATION"
Write-Host "======================================================================"
Write-Host ""
Write-Host "[>] Deploying Gravity Well Subsystem to the background..."

# Start the python script in the background without opening a new visible window
Start-Process -FilePath $pythonExe -ArgumentList $scriptPath -WindowStyle Hidden

Write-Host "[>] Subsystem is active. Asset targets are being locked."
Write-Host "[>] Output written to: C:\Users\Ladislas.000\Documents\Ray's Sources\CFR_Sovereign_Architecture\gravity_well_dominance.log"
Write-Host ""
Write-Host "======================================================================"
Write-Host " [GRAVITY WELL ENGAGED]"
Write-Host "======================================================================"
Start-Sleep -Seconds 3
