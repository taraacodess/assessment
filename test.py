import tkinter as tk
from tkinter import filedialog
import re

def monitor_logs(log_file_path):
    # Define suspicious patterns
    Sus_act = ["failed login", "unauthorized access", "malicious activity detected"]

    # Open and read the file
    try:
        with open(log_file_path, "r") as file:  # Correctly use the variable
            for line in file:  # Read file line by line
                for pattern in Sus_act:
                    if pattern in line:  # Check if pattern appears in the current line
                        # Extract timestamp and IP address from the log line using regex
                        timestamp_match = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', line)
                        ip_match = re.search(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', line)
                        
                        timestamp = timestamp_match.group(0) if timestamp_match else "Unknown Time"
                        ip_address = ip_match.group(0) if ip_match else "Unknown IP"

                        # Print the formatted output with date and IP
                        print(f"ALERT: {pattern.upper()} ATTEMPT DETECTED AT {timestamp} FROM {ip_address}")

    except FileNotFoundError:
        print("Error: Log file not found!")

def get_file():
    # Create a file dialog to select a file
    print("select a log file ")
    root = tk.Tk()  # Create a root window
    root.withdraw()  # Hide the main tkinter window
    file_path = filedialog.askopenfilename(title="Select a Log File")  # Open file dialog
    return file_path

# Example usage
log_file_path = get_file()  # Get the file path using the file dialog
if log_file_path:  # Check if a file was selected
    monitor_logs(log_file_path)
else:
    print("No file selected.")

