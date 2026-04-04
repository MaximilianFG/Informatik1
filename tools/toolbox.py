import subprocess
import sys
import threading

"""
Utility tool functions to keep instructional demo programs simpler.

2025-03-09 | swiest | 1.0 | Initial version.
2025-04-24 | swiest | 1.0 | Adds typed input functions.
"""

#############################################################################
# Simple, cross-platform audio playback.
#
# Requires ffmpeg (https://www.ffmpeg.org/) to be installed locally.
#############################################################################


def play_audio(audio_file):
    """Function to play audio synchronously"""
    try:
        subprocess.run(
            ["ffplay", "-nodisp", "-autoexit", "-loglevel", "quiet", audio_file],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except FileNotFoundError:
        # If ffplay cannot be found or is not installed, ignore audio output silently (pun intended).
        pass


def play_audio_async(audio_file):
    """Function to play audio asynchronously"""
    # Create a thread for asynchronous playback
    play_thread = threading.Thread(target=play_audio, args=(audio_file,))
    play_thread.start()


#############################################################################
# Wraps input to produce colored user input.
#############################################################################


def wrap_input(original_input):
    def wrapper(prompt):
        # Display input in green
        print(prompt + "\033[0;32m", end="", flush=True)
        text = original_input()
        print("\033[0m", end="", flush=True)
        return text

    return wrapper


def wrap_stderr_write(original_write):
    def wrapper(text):
        # Display errors in red
        original_write("\033[0;31m" + text + "\033[0m")

    return wrapper


def wrap_stdout_write(original_write):
    is_first_call = True

    def wrapper(text):
        nonlocal is_first_call
        # Clear screen on first call
        original_write("\033[2J\033[3J\033[H" + text if is_first_call else text)
        is_first_call = False

    return wrapper


input = wrap_input(input)
sys.stderr.write = wrap_stderr_write(sys.stderr.write)  # type: ignore
sys.stdout.write = wrap_stdout_write(sys.stdout.write)  # type: ignore

#############################################################################
# Typed input functions
#############################################################################


def inputFloat(prompt):
    return float(input(prompt))


def inputInteger(prompt):
    return int(input(prompt))


def inputBoolean(prompt):
    return True if input(prompt).lower() in ["yes", "ja", "true", "y", "j"] else False


#############################################################################
# Demo showcasing the toolbox.
#############################################################################


if __name__ == "__main__":
    name = input("Enter your name: ")
    print(f"Hello, {name} on stdout!")
    print("This is a message on stderr.", file=sys.stderr)
    print(f"Hello again on stdout, {name}!")
    f = inputFloat("Gleitkommazahl eingeben: ")
    print(f"Eingabe  * 2.5 = {f * 2.5}")
