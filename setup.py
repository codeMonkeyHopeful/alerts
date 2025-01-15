# Check if we have pip installed
import os
import platform

try:

    import pip

except:
    # pip is NOT installed so lets install it
    # Check which OS we are running so we can install it
    os_pip_command = {
        "Linux": "python3 -m ensurepip --upgrade",
        "Darwin": "python3 -m ensurepip --upgrade",
        "Windows": "py -m ensurepip --upgrade",
    }

    pip_command = os_pip_command[platform.system()]

    os.system(pip_command)
