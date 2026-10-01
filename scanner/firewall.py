import subprocess

def get_firewall_status():
    try:
        result = subprocess.check_output(
            "netsh advfirewall show allprofiles",
            shell=True,
            text=True
        )

        if "ON" in result:
            return "Enabled"
        else:
            return "Disabled"

    except Exception:
        return "Unable to Detect"