import os
import sys
import platform

# Wichtig (nur Windows): Dieser Pfad darf keine Leerzeichen haben!
windowsSparkPath = "C:/spark"

if platform.platform()[:7] == "Windows":
    if not os.path.isdir(windowsSparkPath):
        print("FEHLER: Spark wurde nicht nach " + windowsSparkPath + " verschoben.")
    os.environ["SPARK_HOME"] = windowsSparkPath
    os.environ["PYSPARK_PYTHON"] = sys.executable
    os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable
else:
    os.environ["SPARK_HOME"] = os.path.realpath(".") + "/spark"
    os.environ["PYSPARK_PYTHON"] = sys.executable
    os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable