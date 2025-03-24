###################################################################
# IMPORT SECTION
from webhook_handler import start_server, start_ngrok
import threading
import signal
import sys
###################################################################
# MAIN FUNCTION

# Function to handle interrupt signal
def signal_handler(_sig, _frame):
    print("\nInterrupt received! Exiting...")
    sys.exit(0)

if __name__ == '__main__':
    try:
        # Start ngrok service in a separate thread as a daemon
        ngrok_thread = threading.Thread(target=start_ngrok, daemon=True)
        ngrok_thread.start()
        print("ngrok thread started.")

        # Start the server in a separate thread as a daemon
        server_thread = threading.Thread(target=start_server, daemon=True)
        server_thread.start()
        print("Server thread started.")

        # Join threads
        ngrok_thread.join()
        server_thread.join()

        # Register the signal handler
        signal.signal(signal.SIGINT, signal_handler)

        # Keep the main thread alive while daemon threads run.
        # When CTRL+C is pressed, the signal_handler will be invoked,
        # exiting the main thread (which terminates daemon threads).
        signal.pause()

    except KeyboardInterrupt:
        signal_handler(None, None)

###################################################################
# END OF FILE
