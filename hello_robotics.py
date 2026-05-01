# hello_robotics.py
"""My first robotics learning script"""

from logging import config
import random

def sensor_simulator():
    """Simulate a robot temperature sensor"""
    temperature = random.uniform(20, 100)
    return temperature

if __name__ == "__main__":
    reading = sensor_simulator()
    print(f"🤖 Robot sensor reading: {reading:.2f}°C")
    print("✅ Congratulations! Your first Python script works!")
