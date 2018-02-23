from zwift import Client
cli = Client('drazen@kanjuh.de','Tr1athl0n1970')
profile = cli.get_profile()
your_player_id = profile.latest_activity['profile']['id']
print your_player_id
