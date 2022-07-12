from player_list import PlayerList
from player import Player
from pair import Pair

current_bye = int

def give_bye(PlayerList):
    global current_bye
    for player in reversed(PlayerList.list_of_players):
        if player.got_bye == False:
            player.got_bye = True
            player.played_versus.append(0)
            player.results_in_order.append(1)
            current_bye = player.current_place-1
            break


def round_pairing(PlayerList):
    pair_list = []
    for player in PlayerList.list_of_players:
        player.is_paired = False
    if not len(PlayerList.list_of_players) % 2 == 0:
        give_bye(PlayerList)
        PlayerList.list_of_players[current_bye].tier_group = 0
        # PlayerList.list_of_players[current_bye].is_paired = True

    groups_properly_set = False
    tier_group = 1
    points_required = 0
    group_pairity = 0
    while not groups_properly_set:
        for player in PlayerList.list_of_players:
            if player.tier_group == None and player.points >= points_required:
                player.tier_group = tier_group
                points_required = player.points
                group_pairity += 1
            elif player.tier_group == None and player.points < points_required:
                if not group_pairity % 2 == 0:
                    player.tier_group = tier_group
                    points_required = 0
                    group_pairity = 0
                    tier_group += 1
                else:
                    tier_group += 1
                    player.tier_group = tier_group
                    group_pairity = 1
        
        groups_properly_set = True
        for player in PlayerList.list_of_players:
            if player.tier_group == None:
                groups_properly_set = False

    temp_tier_group = 0
    pairing_complete = False
    while not pairing_complete:
        temp_tier_group += 1
        players_in_tier = []
        for player in PlayerList.list_of_players:
            if player.tier_group == temp_tier_group:
                players_in_tier.append(player.starting_number)
        try_to_pair_tier(PlayerList, players_in_tier)
        pairing_complete = True

    for player in PlayerList.list_of_players:
        player.tier_group = None

def try_to_pair_tier(PlayerList, players_in_tier):
    temporary_list = players_in_tier.copy()
    while len(players_in_tier) > 0:
        player_tested = players_in_tier[int(len(players_in_tier)/2)]
        if not played_before_test(PlayerList, players_in_tier[0], player_tested):
            new_pair = Pair(players_in_tier[0], player_tested)
            print(f"para: {players_in_tier[0]} vs {player_tested}")
            players_in_tier.remove(player_tested)
            players_in_tier.remove(players_in_tier[0])
        print(len(players_in_tier), players_in_tier)



def played_before_test(PlayerList, player1, player2):
    index = PlayerList.find_player_by_starting_number(player1)
    if player2 in PlayerList.list_of_players[index].played_versus:
        return True
    else:
        return False


    
    


    

