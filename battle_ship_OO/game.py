import pprint as pp

class Game:
    def __init__(self):
        self.empty_board = [[ "/","A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
         ["1", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
         ["2", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
         ["3", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
         ["4", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
         ["5", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
         ["6", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
         ["7", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
         ["8", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
         ["9", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
         ["10", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]]
        self.counter = 0
        self.attack_enemie = ""

    def place_hit(self,attack,player_board):
        alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        first_index = attack[0]
        second_index = int(attack[1])
        letter_index = alphabet.index(first_index) + 1
        print(letter_index)
        player_board[second_index][letter_index] = "X"

    def battle(self,board,boat_list,score,player_one_position,hit_board):
        print("This is your board: \n")
        pp.pprint(board)
        print("Hit board: \n")
        pp.pprint(hit_board)
        print(f"Your score is {score}\n")
        print(f"Proposition that as been played {player_one_position}\n")
        self.attack_enemie = input(f"Give me a position to attack (exemple A3)\n")
        player_one_position.append(self.attack_enemie)
        for x in boat_list:
            if self.attack_enemie in x:
                print("You hit one boat and score a point\n")
                x.remove(self.attack_enemie)
                if len(x) == 0:
                    print("YOU KILLED A BOAT\n")
                return True
        
        return False
    
    