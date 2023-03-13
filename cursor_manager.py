import ctypes
import sys

# Hide the cursor
def hide_cursor():
    if sys.platform.startswith('win'):
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleCursorInfo(kernel32.GetStdHandle(-11), ctypes.c_long(100))
    elif sys.platform.startswith('linux'):
        print("\033[?25l", end="", flush=True)
    elif sys.platform.startswith('darwin'):
        print("\033[?25l", end="", flush=True)
    else:
        print("\033[?25l", end="", flush=True)

# Show the cursor
def show_cursor():
    if sys.platform.startswith('win'):
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleCursorInfo(kernel32.GetStdHandle(-11), ctypes.c_long(20))
    elif sys.platform.startswith('linux'):
        print("\033[?25h", end="", flush=True)
    elif sys.platform.startswith('darwin'):
        print("\033[?25h", end="", flush=True)
    else:
        print("\033[?25h", end="", flush=True)
