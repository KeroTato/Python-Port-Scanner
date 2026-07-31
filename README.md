# 🔍 Simple Port Scanner

A simple Python tool for scanning open ports on a target host, built using the core socket library with no external dependencies.

---

⚠️ Important Note

This project is still a Work in Progress. It was built mainly as a learning exercise while studying Python for Cybersecurity. The goal is to understand how a port scanner works under the hood (TCP Connect Scan), not to provide a production-ready tool for real-world use.

The tool still needs a lot of improvements in terms of performance, robustness, and additional features (see the Roadmap section below).

---

✨ Current Features

- Scan a range of ports (start to end) on a given target IP.
- Perform a TCP Connect Scan to verify whether a port is actually open.
- Attempt to identify the service name associated with each open port.
- Attempt to grab the banner (if the service responds with data upon connection).
- Display a final report with all open ports and their details.

---

🛠️ Usage

Run the script with: python3 scanner.py

You will then be prompted to enter:
- Target IP → the IP address of the host you want to scan.
- Start Port → the first port in the scan range.
- End Port → the last port in the scan range.

---

🚧 Roadmap

- Add multithreading to speed up scanning.
- Support scanning multiple IPs or a full network range (CIDR).
- Add a user-configurable timeout.
- Save scan results to a file (TXT / JSON / CSV).
- Add a command-line interface using argparse.
- Improve error handling.

---

📌 Disclaimer

This tool was built for educational purposes only. Do not use it against any host or network without explicit permission to scan it. Scanning systems without authorization may be illegal in your country.

---

👨‍💻 About This Project

This project is part of my journey learning Python and its applications in Cybersecurity, and I'll keep improving it as I learn more.

This project was built for learning Python programming and Offensive Security.
