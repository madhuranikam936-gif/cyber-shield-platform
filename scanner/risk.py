def calculate_risk_score(firewall, ports, password, startup):

    score = 100

    # Firewall
    if firewall != "Enabled":
        score -= 20

    # Open Ports
    if len(ports) > 5:
        score -= 20

    # Password Policy
    if "Weak" in password:
        score -= 20

    # Startup Programs
    if len(startup) > 10:
        score -= 20

    # Minimum Score
    if score < 0:
        score = 0

    return score