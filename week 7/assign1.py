def move_player(ladders,snakes,current_position,die_roll):
    player_moved = current_position + die_roll
    if player_moved in ladders:
        return 1
    elif player_moved in snakes:
        return -1
    else:
        return 0
    
ladders = list(map(int,input().split()))
snakes = list(map(int,input().split()))
current_position = int(input())
die_roll = int(input())
print(move_player(ladders,snakes,current_position,die_roll))