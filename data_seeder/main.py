"""
Main script to generate and seed data
"""

# Import necessary libraries
import subprocess

# Generate fake data
subprocess.run(["python", "data_generator.py"])

# Seed fake data
subprocess.run(["python", "seeder.py"])
