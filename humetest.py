from hume import HumeBatchClient
from hume.models.config import FaceConfig
import time
from pprint import pprint

client = HumeBatchClient("hojgeK2bEEC09H9EiQkY5zewiN8Y5qo8qqaSP4z4RWG2mZO5")
urls = ["https://as2.ftcdn.net/v2/jpg/00/88/53/89/1000_F_88538986_5Bi4eJ667pocsO3BIlbN4fHKz8yUFSuA.jpg"]
config = FaceConfig()
job = client.submit_job(urls, [config])

status = job.get_status()
print(f"Job status: {status}")
time.sleep(3)
details = job.get_details()
run_time_ms = details.get_run_time_ms()
print(f"Job ran for {run_time_ms} milliseconds")

predictions = job.get_predictions()
pprint(predictions)


import random
import spotipy
from spotipy.oauth2 import SpotifyOAuth
# Spotify API Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="b41d53920ebe4048bf3ead7aa5cb0171",
                                               client_secret="d15daad23d904ba3aab7a6332735be14",
                                               redirect_uri="https://arizonamillay.com/fireboa/spotify",
                                               scope="user-library-read"))

# Fetch user's playlists
playlists = sp.current_user_playlists()["items"]

# Randomly select a playlist
selected_playlist = random.choice(playlists)
playlist_tracks = sp.playlist_items(selected_playlist["id"])["items"]

# Randomly select a track from the playlist
selected_track = random.choice(playlist_tracks)["track"]["uri"]

# Play the track as an alarm (this is a placeholder, you'd need to integrate with an actual alarm or player)
print(f"Playing track: {selected_track}")
