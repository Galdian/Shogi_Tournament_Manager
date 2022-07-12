from player_list import PlayerList
from pairing import round_pairing


test_list = PlayerList()

test_list.add_player("Krzysztof", "Sieja", 1800)
test_list.add_player("Miłosz", "Roman", 1750)
test_list.add_player("Teścik2", "Teścik2", 0)
test_list.add_player("Grzegorz", "Adaszewski", 1600)
test_list.add_player("Teścik3", "Teścik3", 0)
test_list.add_player("Adam", "Dziwoki", 1900)
test_list.add_player("Teścik", "Teścik", 0)
test_list.add_player("Anatol", "Bardyła", 0)
test_list.add_player("Artek", "BarK", 0)
# print(test_list.find_player_by_starting_number(3))


round_pairing(test_list)

test_list.list_of_players[0].points = 6
test_list.list_of_players[1].points = 6
test_list.list_of_players[2].points = 6
test_list.list_of_players[3].points = 5
test_list.list_of_players[4].points = 5
test_list.list_of_players[5].points = 4
test_list.list_of_players[6].points = 4
test_list.list_of_players[7].points = 2
test_list.list_of_players[8].points = 1

round_pairing(test_list)
round_pairing(test_list)
round_pairing(test_list)
round_pairing(test_list)

for player in test_list.list_of_players:
    print(player.current_place, player.starting_number, player.name, player.surname, player.rating, player.points, player.got_bye, player.tier_group)

