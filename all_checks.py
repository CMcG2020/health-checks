import os
import shutil
import sys

def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_gb, min_percent):
    """Returns true if there isn't enough disk space, false otherwise"""
    du = shutil.disk_usage(disk)
    #Calculates the percentage of free space
    percentage_free = 100* du.free / du.total
    #Calculates how many free gigabytes
    gigabytes_free = du.free / 2**30
    if gigabytes_free < min_gb or percentage_free < min_percent:
        return True
    return false

def check_root_full():
    """ Returns true if the root partition is full, otherwise fales"""
    return check_disk_full (disk="/", min_gb=2, min_percent=10)

def main():
    checks= [
        (check_reboot, "Pending Reboot"),
        (check_root_full, "Root partition full")

    ]
    for check, msg in checks:
        if check():
            print(msg)
            sys.exit(1)
    
    print("Everything ok.")
    sys.exit(0)
    
main()
