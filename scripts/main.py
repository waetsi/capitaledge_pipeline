import subprocess
import sys

print("Starting pipeline...")

python_executable = sys.executable

extract_result = subprocess.run([python_executable, "scripts/extract.py"])
if extract_result.returncode != 0:
    print("Extraction step failed ❌")
    sys.exit(1)

transform_result = subprocess.run([python_executable, "scripts/transform.py"])
if transform_result.returncode != 0:
    print("Transformation step failed ❌")
    sys.exit(1)

print("Pipeline completed successfully ✅")