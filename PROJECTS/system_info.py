import platform
import datetime

print("="*50)
print("SYSTEM INFORMATION REPORT")
print("="*50)

print(f"Computer Name:{platform.node()}")
print(f"Operating System:{platform.system()}")
print(f"OS Version:{platform.version()}")
print(f"Proccesor:{platform.processor()}")
print(f"Python Version:{platform.python_version()}")
print()
print("="*50)
print("Day 1 of DevOps Journey - Complete!")
