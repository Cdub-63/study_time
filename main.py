import time
import os
from playsound import playsound

def start_timer(duration):
    """Starts a countdown timer for the given duration in seconds."""
    print(f"\033[1;32mTimer starter for {duration} seconds...\033[0m")
    while duration:
        minutes, seconds = divmod(duration, 60)
        print(f"\033[1,34m{minutes:02d}:{seconds:02d}\033[0m", end="\r")
        time.sleep(1)
        duration -= 1
    print("\nTime's up!")
    play_sound()

def play_sound():
    """Plays a custom sound to notify the user."""
    sound_file = os.path.join(os.path.dirname(__file__), "alert.wav")
    if os.path.exists(sound_file):
        try:
            playsound(sound_file)
        except Exception as e:
            print(f"\033[1;31mError playing sound: {e}\033[0m")
    else:
        print("\033[1;31mSound file 'alert.wav' not found.\033[0m")

if __name__ == "__main__":
    time_metric = input("Do you want a timer in seconds or minutes? (s/m): ").strip().lower()
    try: 
        if time_metric == "s":
            duration = int(input("Enter the timer duration in seconds: "))
        elif time_metric == "m":
            duration = int(input("Enter the timer duration in minutes: ")) * 60
    except ValueError:
        print("\033[1;31mPlease enter a valid number. \033[0m")
        exit(1)
    if duration <= 0:
        print("\033[1;31mGotta have a timer greater than 0 seconds dude. \033[0m")
        exit(1)
    else:
        start_timer(duration)
