import pprint as pp

class Boat:
    def __init__(self):
        self.board = [[ "/","A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
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
        self.boat_position_list = []
        
    def place_boat(self,place_boat_choice,player_placement_front,player_placement_back,player_board,boat_position_list):
        if len(player_placement_front) == 2:
            front_col = player_placement_front[0]
            front_row = int(player_placement_front[1])
        else:
            front_col = player_placement_front[0]
            front_row = int(player_placement_front[-2:])
            
        if len(player_placement_back) == 2:
            back_col = player_placement_back[0]
            back_row = int(player_placement_back[1])
        else:
            back_col = player_placement_back[0]
            back_row = int(player_placement_back[-2:])
            
        alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        front_col_index = None
        back_col_index = None
        alphatbet_front_col_index = alphabet.index(front_col)

        if front_col in player_board[0]:
            front_col_index = player_board[0].index(front_col)
        if back_col in player_board[0]:
            back_col_index = player_board[0].index(back_col)

        if place_boat_choice == "2":
            player_board[front_row][front_col_index] = "2"
            player_board[back_row][back_col_index] = "2"
            boat_position_list.append([player_placement_front,player_placement_back])
        elif place_boat_choice == "3":
            if front_col == back_col:
                player_board[front_row][front_col_index] = "3"
                player_board[back_row][back_col_index] = "3"
                player_board[front_row + 1][front_col_index] = "3"
                boat_position_list.append([player_placement_front,str(front_col) + str(front_row + 1),player_placement_back])
            elif front_row == back_row:
                player_board[front_row][front_col_index] = "3"
                player_board[back_row][back_col_index] = "3"
                player_board[front_row][front_col_index + 1] = "3"
                boat_position_list.append([player_placement_front,str(alphabet[alphatbet_front_col_index + 1]) + str(front_row),player_placement_back])
        elif place_boat_choice == "4":
            if front_col == back_col:
                player_board[front_row][front_col_index] = "4"
                player_board[back_row][back_col_index] = "4"
                player_board[front_row + 1][front_col_index] = "4"
                player_board[front_row + 2][front_col_index] = "4"
                boat_position_list.append([player_placement_front,str(front_col) + str(front_row + 1),str(front_col) + str(front_row + 2),player_placement_back])
            elif front_row == back_row:
                player_board[front_row][front_col_index] = "4"
                player_board[back_row][back_col_index] = "4"
                player_board[front_row][front_col_index + 1] = "4"
                player_board[front_row][front_col_index + 2] = "4"
                boat_position_list.append([player_placement_front,str(alphabet[alphatbet_front_col_index + 1]) + str(front_row),str(alphabet[alphatbet_front_col_index + 2]) + str(front_row),player_placement_back])
        
        print(boat_position_list)
        pp.pprint(player_board)