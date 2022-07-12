from player import Player

class PlayerList:

    def __init__(self):
        self.list_of_players = []

    def add_player(self, name, surname, rating):
        new_player = Player(name, surname, rating)
        self.list_of_players.append(new_player)
        self.sort_player_list()
        starting_number = 1
        for player in self.list_of_players:
            player.starting_number = starting_number
            starting_number += 1

    def sort_player_list(self):
        self.list_of_players.sort(key=lambda player: (player.surname, player.name))
        self.list_of_players.sort(reverse=True, key=lambda player: (player.points, player.sos, player.sosos, player.msos, player.rating))
        current_place = 1
        for player in self.list_of_players:
            player.current_place = current_place
            current_place += 1

    def find_player_by_starting_number(self, number = int):
        index = next((i for i, player in enumerate(self.list_of_players) if player.starting_number == number), -1)
        return index
        

