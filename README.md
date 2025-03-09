This script monitors log files for suspicious activity such as failed login attempts, unauthorized access, or malicious activity. It scans logs line by line, extracts timestamps and IP addresses, and alerts the user when suspicious patterns are detected.

Features

Detects Suspicious Activity: Scans logs for failed logins, unauthorized access, and malicious activity.

Extracts Key Information: Uses regex to extract timestamps and IP addresses from log entries.

User-Friendly File Selection: Provides a graphical file selection dialog using Tkinter.

Real-Time Alerts: Displays alerts when suspicious patterns are found in the log file.

Installation

Prerequisites

Python 3.x

Required libraries:

tkinter (included with Python)

re (regular expressions, included with Python)

Setup

Clone the repository:

git clone https://github.com/yourusername/log-monitor.git
cd log-monitor

Install dependencies (if needed):

pip install tk

Usage

Run the script and select a log file when prompted:

python log_monitor.py

Example Output:

Select a log file
ALERT: FAILED LOGIN ATTEMPT DETECTED AT 2025-03-09 12:30:45 FROM 192.168.1.10
ALERT: UNAUTHORIZED ACCESS ATTEMPT DETECTED AT 2025-03-09 14:15:22 FROM 10.0.0.5

Assumptions & Limitations

The script does not modify log files; it only scans and reports.

It relies on predefined suspicious patterns; additional patterns may need to be added manually.

The log format must contain timestamps and IP addresses for accurate detection.
