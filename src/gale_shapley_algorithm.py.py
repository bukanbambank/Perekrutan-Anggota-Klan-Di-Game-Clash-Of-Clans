def gale_shapley(players, clans):
    free_players = list(players.keys())
    matches = {clan: None for clan in clans}
    
    player_preferences = {p: sorted(clans.keys(), key=lambda c: players[p]['preferences'][c], reverse=True) for p in players}
    clan_preferences = {c: sorted(players.keys(), key=lambda p: clans[c]['preferences'][p], reverse=True) for c in clans}
    
    while free_players:
        player = free_players.pop(0)
        player_pref_list = player_preferences[player]
        
        for clan in player_pref_list:
            if matches[clan] is None:
                matches[clan] = player
                break
            else:
                current_player = matches[clan]
                if clan_preferences[clan].index(player) < clan_preferences[clan].index(current_player):
                    matches[clan] = player
                    free_players.append(current_player)
                    break
    
    return matches

def calculate_preference_score(preferences, characteristics):
    return sum(preferences[characteristic] * characteristics[characteristic] for characteristic in preferences)

def input_player_data():
    players = {}
    num_players = int(input("Masukkan jumlah pemain: "))
    
    for _ in range(num_players):
        player_id = input("Masukkan ID pemain: ")
        trophy = int(input(f"Masukkan jumlah trophy untuk {player_id}: "))
        war_stars = int(input(f"Masukkan jumlah bintang war untuk {player_id}: "))
        donation_count = int(input(f"Masukkan jumlah donasi untuk {player_id}: "))
        
        print(f"Masukkan preferensi {player_id} terhadap karakteristik clan (1 untuk prioritas tertinggi, 3 untuk terendah):")
        level_pref = int(input("Level clan: "))
        total_trophy_pref = int(input("Total trophy clan: "))
        war_wins_pref = int(input("Jumlah kemenangan war clan: "))
        
        preferences = {
            'level': level_pref,
            'total_trophy': total_trophy_pref,
            'war_wins': war_wins_pref
        }
        
        players[player_id] = {
            'trophy': trophy,
            'war_stars': war_stars,
            'donation_count': donation_count,
            'preferences': preferences
        }
    
    return players

def input_clan_data():
    clans = {}
    num_clans = int(input("Masukkan jumlah clan: "))
    
    for _ in range(num_clans):
        clan_id = input("Masukkan ID clan: ")
        clan_level = int(input(f"Masukkan level untuk clan {clan_id}: "))
        total_trophy = int(input(f"Masukkan total trophy untuk clan {clan_id}: "))
        war_wins = int(input(f"Masukkan jumlah kemenangan war untuk clan {clan_id}: "))
        
        print(f"Masukkan preferensi clan {clan_id} terhadap karakteristik pemain (pilih salah satu: trophy, war_stars, donation_count):")
        preference = input("Karakteristik preferensi: ")
        
        clans[clan_id] = {
            'level': clan_level,
            'total_trophy': total_trophy,
            'war_wins': war_wins,
            'preference': preference
        }
    
    return clans

def main():
    print("Input data pemain:")
    players = input_player_data()
    
    print("\nInput data clan:")
    clans = input_clan_data()
    
    # Calculate preference scores for matching
    for player in players:
        players[player]['preferences'] = {clan: calculate_preference_score(players[player]['preferences'], clans[clan]) for clan in clans}
    
    for clan in clans:
        clans[clan]['preferences'] = {player: players[player][clans[clan]['preference']] for player in players}
    
    matches = gale_shapley(players, clans)
    print("\nHasil Pencocokan:")
    for clan, player in matches.items():
        print(f"Clan {clan} dipasangkan dengan Pemain {player}")

if __name__ == "__main__":
    main()
