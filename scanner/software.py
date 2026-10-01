import subprocess

def get_installed_software():
    try:
        result = subprocess.check_output(
            'powershell "Get-ItemProperty HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* | Select-Object DisplayName"',
            shell=True,
            text=True
        )

        software = []

        for line in result.split("\n"):
            line = line.strip()
            if line and "DisplayName" not in line and "---" not in line:
                software.append(line)

        return software[:15]

    except Exception as e:
        return [str(e)]