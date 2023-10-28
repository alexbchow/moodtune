import random
import spotipy
import time
import threading
import tkinter as tk
from tkinter import simpledialog, messagebox
from spotipy.oauth2 import SpotifyOAuth
import webbrowser

# Spotify API Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="b41d53920ebe4048bf3ead7aa5cb0171",
                                               client_secret="d15daad23d904ba3aab7a6332735be14",
                                               redirect_uri="https://arizonamillay.com/fireboa/spotify",
                                               scope="user-library-read"))

def fetch_random_song():
    # Fetch user's playlists
    playlists = sp.current_user_playlists()["items"]

    # Randomly select a playlist
    selected_playlist = random.choice(playlists)
    playlist_tracks = sp.playlist_items(selected_playlist["id"])["items"]

    # Randomly select a track from the playlist
    selected_track = random.choice(playlist_tracks)["track"]["uri"]

    return selected_track

def set_alarm():
    time_string = simpledialog.askstring("Input", "Set alarm time (HH:MM):")
    # Start the alarm function in a separate thread
    threading.Thread(target=alarm, args=(time_string,)).start()

def alarm(time_string):
    # Convert the time_string (HH:MM) to hours and minutes
    alarm_hour, alarm_minute = map(int, time_string.split(":"))

    while True:
        # Get the current time
        current_time = time.localtime()
        current_hour = current_time.tm_hour
        current_minute = current_time.tm_min

        # Check if the current time matches the alarm time
        if current_hour == alarm_hour and current_minute == alarm_minute:
            play_song()
            break

        # Sleep for a minute before checking again
        time.sleep(60)

def play_song():
    song = fetch_random_song()
    song_url = 'https://open.spotify.com/track/6zvqq50PL7io0rprbkrYc9?si=48a53610d5a24134'
    webbrowser.open(song_url)
    # Logic to play the song goes here
    # For demonstration purposes, we'll just print the song
    print(f"Playing song: {song}")
    
# Create the main window
root = tk.Tk()
root.title("Spotify Alarm")

# Create a button to set the alarm
set_alarm_button = tk.Button(root, text="Set Alarm", command=set_alarm)
set_alarm_button.pack(pady=20)

root.mainloop()