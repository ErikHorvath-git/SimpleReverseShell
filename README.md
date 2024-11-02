Simple Reverse Shell
This repository contains a basic Python-based reverse shell script. The script allows an attacker to remotely execute commands on a compromised machine by connecting back to a designated IP and port on the attacker's machine.

⚠️ Disclaimer: This code is for educational purposes only. Unauthorized use of this tool is illegal and unethical. Always have permission before using it in any environment.

How It Works
The reverse shell script, reverseSH.py, is designed to:

Establish a connection to a remote attacker’s machine (specified by IP and port).
Receive commands from the attacker, execute them on the compromised machine, and send the results back.
Maintain this command-execution loop until the attacker sends an exit command, which terminates the connection.
Script Overview
Socket Communication: The script uses Python's socket module to create a connection to the attacker's machine.
Command Execution: Received commands are executed using Python's subprocess module, and the output (including errors) is sent back to the attacker.
Usage
Configuration:

Modify REMOTE_HOST and REMOTE_PORT in reverseSH.py to specify the attacker's IP address and port number.
Running the Script:

On the target machine, run reverseSH.py to initiate the reverse shell connection.
Attacker’s Machine:

The attacker must have a listener running on the specified IP and port to receive the incoming connection and commands.
Example
In reverseSH.py, replace:

python
Copy code
REMOTE_HOST = "127.0.0.1"
REMOTE_PORT = 443
with the actual IP and port.

Requirements
Python 3.x installed on the target machine.
Disclaimer
This tool should only be used with explicit permission in a controlled environment for ethical hacking and cybersecurity research purposes. Unauthorized use is illegal and could result in severe penalties.
