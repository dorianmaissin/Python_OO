from boat import Boat

class Player:
    def __init__(self, boat_list, player_name):
        self.place_boat_choice = ""
        self.player_placement_front = ""
        self.player_placement_back = ""
        self.boat_list = boat_list
        self.name = player_name
        self.score = 0
        self.score_position = []
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
        self.boat = Boat()

    def ask_user_input(self):
        self.place_boat_choice = input(f"Choose between witch boat you want to place from the list {self.boat_list}\n")
        if len(self.place_boat_choice)  > 1 or int(self.place_boat_choice) not in self.boat_list:
            print("This boat does not exist in the list try again")
            self.ask_for_position()
        elif int(self.place_boat_choice) in self.boat_list:
            self.boat_list.remove(int(self.place_boat_choice))
            self.player_placement_front = input(f"tell me the front position for the boat {self.place_boat_choice}: (exemple A3)\n")
            self.player_placement_back = input(f"tell me the back position for the boat {self.place_boat_choice}: (exemple B3)\n")

    def is_move_valid(self, place_boat_choice,player_placement_front,player_placement_back):
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
        
        if front_col == back_col:
            if front_row - back_row == int(place_boat_choice) - 1:
                return True
            elif back_row - front_row == int(place_boat_choice) - 1 :
                return True
            else:
                return False
        elif front_row == back_row:
            if ord(front_col) - ord(back_col) == int(place_boat_choice) - 1:
                return True
            elif ord(back_col) - ord(front_col) == int(place_boat_choice) - 1:
                return True
            else:
                return False
        else :
            return False
        
    def ask_for_position(self):
        print(self.boat_list)
        if len(self.boat_list) > 0:
            print(f"{self.name} Please Position Your Boats")
            # display_bord(board_one)
            self.ask_user_input()
            if  self.is_move_valid(self.place_boat_choice,self.player_placement_front,self.player_placement_back):
                print("valide position")
                self.boat.place_boat(self.place_boat_choice, self.player_placement_front, self.player_placement_back, self.boat.board, self.boat.boat_position_list)
                self.ask_for_position()
            else:
                print("Invalide position")
                self.boat_list.append(int(self.place_boat_choice))
                self.boat_list.sort()
                self.ask_for_position()
                # position_boat()
        else: 
            print("All your boat have been placed")
            return False    