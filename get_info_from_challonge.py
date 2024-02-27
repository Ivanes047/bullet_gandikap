import challonge
                
def get_info_about_tournament(username, api_key, id):
    partii = {}
    players = {}
    challonge.set_credentials(username, api_key)
    tournament = challonge.tournaments.show(id)
    participants = challonge.participants.index(tournament["id"])
    count_partiy = len(participants)//2
    for participant in participants:
        player = participant['name'].split()
        raiting = int(player[-1])
        player.pop()
        name = " ".join(player)
        players[participant['id']] = [name, raiting]
    matches = challonge.matches.index(tournament["id"])
    for match in matches:
        if (match["round"] not in partii):
            partii[match["round"]] = []
        partii[match["round"]].append([match["player1_id"], match["player2_id"], match["winner_id"]])
    return partii, players

if __name__ == "__main__":
    print(get_info_about_tournament())