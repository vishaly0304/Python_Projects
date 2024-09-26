# Importing Python Library
import psutil  
import time  
import csv  
from datetime import datetime 

def log_performance():
    # Open a CSV file to log system performance metrics
    with open('system_performance.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        # Write the header row to the CSV file
        writer.writerow(["Timestamp", "CPU Usage", "Memory Usage", "Disk Usage", "Process PID", "Process Name", "Process Memory Usage (%)"])
        
        while True:
            # Collect system performance metrics
            cpu = psutil.cpu_percent(interval=1)  # Get CPU usage percentage over a 1-second interval
            memory = psutil.virtual_memory().percent  # Get memory usage percentage
            disk = psutil.disk_usage('/').percent  # Get disk usage percentage for the root directory
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get the current date and time, formatted as a string
            
            # Write the collected metrics to the CSV file
            writer.writerow([timestamp, cpu, memory, disk])
            file.flush()  # Ensure data is written to the file
            
            # Print the collected metrics to the console
            print(f"{timestamp} - CPU: {cpu}%, Memory: {memory}%, Disk: {disk}%")
            
            # Check if memory usage is greater than 80%
            if memory > 80:
                # Iterate over all running processes
                for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
                    try:
                        process_info = proc.info  # Get process information
                        memory_percent = process_info['memory_percent']  # Get memory usage percentage of the process
                        # Write process information to the CSV file
                        writer.writerow([timestamp, cpu, memory, disk, process_info['pid'], process_info['name'], f"{memory_percent:.2f}%"])
                        file.flush()  # Ensure data is written to the file
                        # Print process information to the console
                        print(f"Process PID: {process_info['pid']}, Name: {process_info['name']}, Memory Usage: {memory_percent:.2f}%")
                    except (psutil.NoSuchProcess, psutil.AccessDenied):  # Handle exceptions for processes that no longer exist or cannot be accessed
                        pass
            
            time.sleep(60)  # Pause the loop for 60 seconds before collecting the next set of metrics

if __name__ == "__main__":
    log_performance()  # Call the log_performance function if the script is run directly