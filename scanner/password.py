import subprocess

def check_weak_password():
    try:
        result = subprocess.check_output(
            'net accounts',
            shell=True,
            text=True
        )

        if "Minimum password length" in result:
            for line in result.split("\n"):
                if "Minimum password length" in line:
                    length = int(line.split()[-1])

                    if length >= 8:
                        return "Strong Password Policy ✅"
                    else:
                        return "Weak Password Policy ⚠️"

        return "Unable to Detect"

    except Exception:
        return "Unable to Detect"