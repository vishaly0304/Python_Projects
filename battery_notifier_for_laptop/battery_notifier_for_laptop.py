# Import necessary modules
import time
import psutil
from plyer import notification


# Infinite loop to continuously check the battery percentage
while True:
    # Get battery information using psutil
    battery = psutil.sensors_battery()
    
    # Extract the battery percentage
    percent = battery.percent
    
    # Determine the message based on the battery percentage
    if percent <= 10:
        message = "Battery low, plug in charger!"
    elif percent == 100:
        message = "Battery fully charged, unplug your charger!"
    else:
        message = f"{percent}% Battery remaining"
    
    # Send the notification with the appropriate message
    notification.notify(
        title="Battery Status",
        message=message,
        timeout=10
    )
    
    # Wait for 60 minutes before checking the battery percentage again
    time.sleep(60 * 60)