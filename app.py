
from flask import Flask, render_template

from scanner.processes import get_running_processes
from scanner.ports import get_open_ports
from scanner.firewall import get_firewall_status
from scanner.software import get_installed_software
from scanner.password import check_weak_password
from scanner.startup import get_startup_programs
from scanner.risk import calculate_risk_score
from datetime import datetime


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("system_security.html")

@app.route("/scan")
def scan():
    processes = get_running_processes()
    ports = get_open_ports()
    firewall = get_firewall_status()
    software = get_installed_software()
    password = check_weak_password()
    startup = get_startup_programs()
    risk = calculate_risk_score(firewall, ports, password, startup)
    scan_time = datetime.now().strftime("%d-%m-%Y %I:%M %p")
    
    if risk >= 80:
        risk_level = "🟢 Low Risk"
    elif risk >= 50:
        risk_level = "🟡 Medium Risk"
    else:
        risk_level = "🔴 High Risk"
    
    recommendations = []

    if firewall != "Enabled":
        recommendations.append("Enable Windows Firewall")

    if len(ports) > 5:
        recommendations.append("Close unnecessary open ports")

    if "Weak" in password:
        recommendations.append("Use a strong password policy")

    if len(startup) > 10:
        recommendations.append("Disable unnecessary startup programs")

    return render_template("system_security.html",
    processes=processes,ports=ports,firewall=firewall,software=software,password=password,
    startup=startup,risk=risk,risk_level=risk_level,recommendations=recommendations,scan_time=scan_time)

if __name__ == "__main__":
    app.run(debug=True) 
