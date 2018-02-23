from zwift import Client
cli = Client('email','pw')
profile = cli.get_profile()
your_player_id = profile.latest_activity['profile']['id']
print your_player_id
