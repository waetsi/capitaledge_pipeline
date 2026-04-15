import subprocess
import sys

print("Starting pipeline...")

# Use the current Python interpreter (your .venv)
python_executable = sys.executable

subprocess.run([python_executable, "scripts/extract.py"])
subprocess.run([python_executable, "scripts/transform.py"])

print("Pipeline completed successfully ✅")