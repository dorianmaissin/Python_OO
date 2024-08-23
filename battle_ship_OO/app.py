from player import Player
from game import Game
from colorama import Fore

player1 = Player([2,2], 'Dorian')
player2 = Player([2,2], 'Alex')
player1.ask_for_position()
player2.ask_for_position()

game = Game()

def run_game():
    if (player1.score < 3) and (player2.score < 3):
        if game.counter % 2 > 0:
            print(Fore.GREEN + f"------------------>>>>>>>>>>>>>>>> {player1.name} turn <<<<<<<<<<<<<<<<<-------------------------------\n")
            battle = game.battle(player1.boat.board,player2.boat.boat_position_list,player1.score,player1.score_position,player1.empty_board)
            if battle:
                player1.score += 1
                print(player1.score)
                game.place_hit(game.attack_enemie,player1.empty_board)
                run_game()
            else:
                print("You missed the boat")
            game.counter += 1
            run_game()
        else:
            print(Fore.BLUE + f"------------------>>>>>>>>>>>>>>>> {player2.name} turn <<<<<<<<<<<<<<<<<-------------------------------\n")
            battle_two = game.battle(player2.boat.board,player1.boat.boat_position_list,player2.score,player2.score_position,player2.empty_board)
            if battle_two:
                player2.score += 1
                print(player2.score)
                game.place_hit(game.attack_enemie,player2.empty_board)
                run_game()
            else:
                print("You missed the boat")
            game.counter += 1
            run_game()
    else:
        if player1.score > player2.score:
            print(f"{player1.name} WIN THE GAME")
        else:
            print(f"{player2.name}PLAYER ONE WIN THE GAME")

run_game()