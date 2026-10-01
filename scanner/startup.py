import subprocess

def get_startup_programs():
    try:
        result = subprocess.check_output(
            'powershell "Get-CimInstance Win32_StartupCommand | Select-Object Name"',
            shell=True,
            text=True
        )

        startup = []

        for line in result.split("\n"):
            line = line.strip()
            if line and "Name" not in line and "---" not in line:
                startup.append(line)

        return startup[:5]

    except Exception:
        return ["Unable to Detect"]