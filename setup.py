# Check if we have pip installed
import os
import platform


try:

    import pip

except Exception as e:
    # pip is NOT installed so lets install it
    # Check which OS we are running so we can install it

    print(f"{e} No worries we are installing it for you")

    os_pip_command = {
        "Linux": "python3 -m ensurepip --upgrade",
        "Darwin": "python3 -m ensurepip --upgrade",
        "Windows": "py -m ensurepip --upgrade",
    }

    pip_command = os_pip_command[platform.system()]

    os.system(pip_command)

# Now we have to create our env so lets check again that we can or install it needed

try:

    import venv

except Exception as e:
    # Not installed
    print(f"{e} No worries we got you coverd again...")

    os_venv_command = {
        "Linux": "python3 -m ensurepip --upgrade",
        "Darwin": "python3 -m ensurepip --upgrade",
        "Windows": "python -m venv C:\\path\\to\\new\\virtual\\environment",
    }

    venv_command = os_venv_command[platform.system()]

    os.system(venv_command)


# Install our dependencies
os.system("pip install -r requirements.txt")
