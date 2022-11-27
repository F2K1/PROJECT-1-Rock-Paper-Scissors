import csv
import copy
import datetime
import random
from player import Player


class RPS:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.players_list = []
        self.current_player = None

        with open("players.csv", "r") as file:
            reader = csv.DictReader(file, delimiter=',')
            for row in reader:
                player = Player(row["Name"], row["Date"], row["Points"], row["Comp Points"])
                self.players_list.append(copy.copy(player))
        
        for i in self.players_list:
            print(i.name + ": " + i.points + "/" + i.comp_points)

    def registerPlayer(self, nickname):
        self.nickname = nickname

        for player in self.players_list:
            if self.nickname == player.name:
                self.current_player = copy.copy(player)
                break
            else:
                pass

        if self.current_player == None:
            self.current_player = Player(self.nickname, self.getCurrentDate(), "0", "0")
        else:
            pass
    
    def getCurrentDate(self):
        self.date = datetime.datetime.now().strftime("%d/%m/%Y")
        return self.date

    def game(self, choice):
        self.choice = choice
        self.comp_choice = self.choices[random.randint(0, len(self.choices)-1)]
        
        if (self.choice == "rock" and self.comp_choice == "scissors") or (self.choice == "paper" and self.comp_choice == "rock") or (self.choice == "scissors" and self.comp_choice == "paper"):
            self.current_player.points = str(int(self.current_player.points) + 1)
            return [self.choice, self.comp_choice, "You Win!", self.current_player.points]
        elif (self.comp_choice == "rock" and self.choice == "scissors") or (self.comp_choice == "paper" and self.choice == "rock") or (self.comp_choice == "scissors" and self.choice == "paper"):
            self.current_player.comp_points = str(int(self.current_player.comp_points) + 1)
            return [self.choice, self.comp_choice, "Computer Wins!", self.current_player.points]
        elif (self.comp_choice == "rock" and self.choice == "rock") or (self.comp_choice == "paper" and self.choice == "paper") or (self.comp_choice == "scissors" and self.choice == "scissors"):
            return [self.choice, self.comp_choice, "Draw!", self.current_player.points]
        
    def saveGame(self):
        for player in self.players_list:
            if self.current_player.name == player.name:
                self.players_list.remove(player)
                self.current_player.date = self.getCurrentDate()
                self.players_list.append(self.current_player)
                self.current_player = None
                break
            else:
                pass
        
        if self.current_player != None:
            self.players_list.append(self.current_player)
        
        with open("players.csv", "w") as file:
            file.write("Name,Date,Points,Comp Points\n")
            for player in self.players_list:
                file.write(player.name + "," + player.date + "," + player.points + "," + player.comp_points + "\n")

    def restartGame(self):        
        for player in self.players_list:
            if self.current_player.name == player.name:
                print("DEBUG player.points/player.comp_points: " + player.points + "/" + player.comp_points)
                self.current_player.points = player.points
                self.current_player.comp_points = player.comp_points
                break
            else:
                self.current_player.points = "0"
                self.current_player.comp_points = "0"
