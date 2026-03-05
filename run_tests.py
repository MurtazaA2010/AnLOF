import subprocess
import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Run tests with the correct working directory to ensure module imports work
subprocess.run(["python", "tests/test_methods.py"], cwd=script_dir)
subprocess.run(["python", "tests/test_forward.py"], cwd=script_dir)
