import tkinter as tk
from tkinter import filedialog

def monitor_logs(log_file_path):
    # Define suspicious patterns
    Sus_act = ["failed login", "unauthorized access", "malicious activity detected"]

    # Open and read the file
    try:
        with open(log_file_path, "r") as file:  # Correctly use the variable
            for line in file:  # Read file line by line
                for pattern in Sus_act:
                    if pattern in line:  # Check if pattern appears in the current line
                        print(f"ALERT: {pattern} attempt detected! At: {line.strip()}")

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

