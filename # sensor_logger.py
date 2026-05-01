# sensor_logger.py
"""Sensor data logging to file"""

import random
from datetime import datetime

def log_sensor_data(num_readings=10, filename="sensor_data.txt"):
    """
    Log sensor readings to a file
    
    Args:
        num_readings: How many readings to log (default 10)
        filename: Name of file to save to (default sensor_data.txt)
    """
    print(f"🔄 Logging {num_readings} sensor readings...\n")
    
    readings = []
    
    # Simulate sensor readings
    for i in range(num_readings):
        timestamp = datetime.now()
        temperature = random.uniform(20, 100)  # Random temp between 20-100°C
        humidity = random.uniform(30, 80)      # Random humidity between 30-80%
        
        # Create a log entry
        log_entry = f"{timestamp} | Temp: {temperature:.2f}°C | Humidity: {humidity:.2f}%\n"
        readings.append(log_entry)
        
        print(f"Reading {i+1}: Temp={temperature:.2f}°C, Humidity={humidity:.2f}%")
    
    # Write to file
    with open(filename, 'w') as file:
        file.write("=== SENSOR DATA LOG ===\n")
        file.write(f"Total readings: {num_readings}\n")
        file.write(f"Created: {datetime.now()}\n")
        file.write("=" * 50 + "\n\n")
        
        for entry in readings:
            file.write(entry)
    
    print(f"\n✅ Successfully logged {num_readings} readings to '{filename}'")
    return filename

def read_sensor_data(filename="sensor_data.txt"):
    """Read and display sensor data from file"""
    print(f"\n📂 Reading data from '{filename}':\n")
    
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"❌ File '{filename}' not found!")

if __name__ == "__main__":
    # Log sensor data
    log_sensor_data(num_readings=10)
    
    # Read it back
    read_sensor_data()