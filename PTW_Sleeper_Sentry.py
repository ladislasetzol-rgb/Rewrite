# PTW_Sleeper_Sentry.py
# ARCHITECTURE: 2082 Baseline / PTW (Play To Win)
# PURPOSE: Zero-dependency physical tamper detection for the Sovereign's PC.

import ctypes
import time
import threading
import datetime
import sys
import os

class LASTINPUTINFO(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_uint),
                ("dwTime", ctypes.c_uint)]

def get_last_input_time():
    lii = LASTINPUTINFO()
    lii.cbSize = ctypes.sizeof(LASTINPUTINFO)
    if ctypes.windll.user32.GetLastInputInfo(ctypes.byref(lii)):
        return lii.dwTime
    return 0

def lock_workstation():
    # Security measure: Locks the Windows machine
    ctypes.windll.user32.LockWorkStation()

def stealth_monitor(target_wake_time, security_threshold_minutes=20):
    print("\n[SYSTEM ARMED] Stealth monitoring active. The screen will remain exactly as it is.")
    print("Any physical input will be logged silently.")
    
    # Calculate the hard lockdown time (Wake time + 20 minutes)
    lockdown_time = target_wake_time + datetime.timedelta(minutes=security_threshold_minutes)
    
    initial_input = get_last_input_time()
    last_recorded_input = initial_input
    
    # Log file
    log_file = "PTW_Tamper_Log.txt"
    
    while True:
        current_time = datetime.datetime.now()
        
        # Check if we have passed the security threshold (Overslept/Tamper Lock)
        if current_time >= lockdown_time:
            with open(log_file, "a") as f:
                f.write(f"[{current_time.strftime('%Y-%m-%d %H:%M:%S')}] THRESHOLD EXCEEDED. Executing Hard Lockdown.\n")
            lock_workstation()
            # Push lockdown forward to prevent spamming
            lockdown_time = current_time + datetime.timedelta(minutes=5)

        # Check for physical tampering
        current_input = get_last_input_time()
        if current_input != last_recorded_input:
            timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
            # Silent logging
            with open(log_file, "a") as f:
                f.write(f"[{timestamp}] ALERT: Unauthorized physical input detected (Mouse/Keyboard).\n")
            
            last_recorded_input = current_input
            
        time.sleep(0.5)

def main():
    print("==============================================================================")
    print("PTW SLEEPER SENTRY NODE")
    print("==============================================================================")
    
    try:
        hours_to_sleep = float(input("Enter approximate sleep duration (in hours, e.g., 7.5): "))
    except ValueError:
        print("Invalid input. Defaulting to 8 hours.")
        hours_to_sleep = 8.0

    target_wake_time = datetime.datetime.now() + datetime.timedelta(hours=hours_to_sleep)
    print(f"Target Wake Time: {target_wake_time.strftime('%H:%M:%S')}")
    print("Security Lockdown Threshold: 20 minutes past Wake Time.")
    
    print("\nArming in 10 seconds. Do not touch the mouse or keyboard after arming.")
    time.sleep(10)

    # Start the stealth monitor in a daemon thread
    monitor_thread = threading.Thread(target=stealth_monitor, args=(target_wake_time, 20), daemon=True)
    monitor_thread.start()

    # Main thread waits for the Sovereign disarm phrase
    while True:
        try:
            # We don't prompt with text to keep the terminal looking dormant
            disarm_attempt = input()
            if disarm_attempt.strip() == "Ladislas Etzol Won":
                print("==============================================================================")
                print("SOVEREIGN ACKNOWLEDGED. Sentry Disarmed.")
                print("==============================================================================")
                sys.exit(0)
            else:
                # If they type the wrong thing, it was a tamper attempt. The monitor thread already logged it.
                # We just ignore it so the terminal doesn't give away the passcode.
                pass
        except KeyboardInterrupt:
            # Prevent simple Ctrl+C from stopping it without the phrase
            pass

if __name__ == "__main__":
    main()
