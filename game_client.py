import requests

class Client():
    def __init__(self, host):
        self.host = host

    def join_game(self, game_type, player_name):
        response = requests.get(self.host + "/games?active=false&type=" + game_type)
        response.raise_for_status()
        if len(response.json()) > 0:
            game_id = response.json()[0]['id']
            join_response = requests.put(self.host + "/games/" + str(game_id) + "/join", json={"current_player": player_name})
            if join_response.status_code == 200:
                return {"game_id": game_id, "created": False, "waiting": False, "player_id": "2"}
        # We could not join an existing game. Create a new one and wait for someone else
        # to join.
        create_response = requests.post(self.host + "/games", json={"current_player": player_name, "type": game_type})
        response.raise_for_status()
        game_id = create_response.json()['id']
        return {"game_id": game_id, "created": True, "waiting": True, "player_id": "1"}
    
    def get_game(self, game_id):
        response = requests.get(self.host + "/games/" + str(game_id))
        response.raise_for_status()
        return response
    
    def delete_game(self, game_id):
        response = requests.delete(self.host + "/games/" + str(game_id))
        response.raise_for_status()
    
    def make_move(self, game_id, updated_board):
        response = requests.put(self.host + "/games/" + str(game_id) + "/makeMove", json={"board": updated_board})
        response.raise_for_status()