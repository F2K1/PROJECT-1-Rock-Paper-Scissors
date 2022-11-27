from tkinter import *
from rps import *


class Controller:
    def __init__(self):
        self.window = App(self)
        self.rps = RPS()

    def showFrame(self, frame_id):
        self.window.showFrame(frame_id)

    def updateNickname(self, name):
        self.rps.registerPlayer(name)
    
    def updateChoice(self, choice):
        list = self.rps.game(choice)
        self.window.endgame_frame.getResult(list[0], list[1], list[2])

class App(Tk):
    def __init__(self, controller):
        super(App, self).__init__()
        
        self.controller = controller

        self.cont = Frame(self)
        self.cont.pack()
        self.cont.rowconfigure(0, weight=1)
        self.cont.columnconfigure(0, weight=1)

        self.geometry("400x400")

        self.intro_frame = IntroFrame(self.cont, self.controller)
        self.intro_frame.grid(row=0, column=0, sticky="nsew")
        
        self.game_frame = GameFrame(self.cont, self.controller)
        self.game_frame.grid(row=0, column=0, sticky="nsew")
        
        self.endgame_frame = EndgameFrame(self.cont, controller)
        self.endgame_frame.grid(row=0, column=0, sticky="nsew")

        self.intro_frame.tkraise()
    
    def showFrame(self, frame_id):
        if frame_id == 0:
            self.intro_frame.tkraise()
        elif frame_id == 1:
            self.game_frame.tkraise()
        elif frame_id == 2:
            self.endgame_frame.tkraise()

    def submitNickname(self):
        return self.intro_frame.getNickname()

class IntroFrame(Frame):
    def __init__(self, parent, controller: Controller):
        super(IntroFrame, self).__init__(parent)
        self.controller = controller
        
        label = Label(self, text="Insert Nickname")
        label.pack()
        
        self.nickname = StringVar()
        entry = Entry(self, textvariable=self.nickname)
        entry.pack()

        button = Button(self, text="Submit", command=self.button_action)
        button.pack()

    def button_action(self):
        self.getNickname()
        controller.showFrame(1)
    
    def getNickname(self):
        self.controller.updateNickname(self.nickname.get())

class GameFrame(Frame):
    def __init__(self, parent, controller: Controller):
        super(GameFrame, self).__init__(parent)
        self.controller = controller

        label = Label(self, text="Choose Your Weapon!")
        label.grid(row=0, column=1)

        button1 = Button(self, text="rock", command=lambda: [self.getChoice("rock"), controller.showFrame(2)])
        button1.grid(row=1, column=0)

        button2 = Button(self, text="paper", command=lambda: [self.getChoice("paper"), controller.showFrame(2)])
        button2.grid(row=1, column=1)

        button3 = Button(self, text="scissors", command=lambda: [self.getChoice("scissors"), controller.showFrame(2)])
        button3.grid(row=1, column=2)

    def getChoice(self, button):
        if button == "rock":
            self.controller.updateChoice("rock")
        elif button == "paper":
            self.controller.updateChoice("paper")
        elif button == "scissors":
            self.controller.updateChoice("scissors")

class EndgameFrame(Frame):
    def __init__(self, parent, controller: Controller):
        super(EndgameFrame, self).__init__(parent)
        self.controller = controller

        label = Label(self, text="Game Over!")
        label.grid(row=0, column=1)

        button1 = Button(self, text="Exit", command=lambda: [controller.rps.saveGame(), controller.window.destroy()])
        button1.grid(row=1, column=0)
        
        button2 = Button(self, text="Restart", command=lambda: [controller.rps.restartGame(), controller.showFrame(1)])
        button2.grid(row=1, column=2)
        
        self.choice = StringVar()
        self.label2 = Label(self, text=self.choice.get())
        self.label2.grid(row=1, column=1)

        self.comp_choice = StringVar()
        self.label3 = Label(self, text=self.comp_choice.get())
        self.label3.grid(row=2, column=1)

        self.message =  StringVar()
        self.label4 = Label(self, text=self.message.get())
        self.label4.grid(row=3, column=1)

    def getResult(self, choice, comp_choice, message):
        self.choice.set("Your Choice: " + choice)
        self.comp_choice.set("Computer's Choice: " + comp_choice)
        self.message.set(message)

        self.label2.config(text=self.choice.get())
        self.label3.config(text=self.comp_choice.get())
        self.label4.config(text=self.message.get())


if __name__ == "__main__":
    controller = Controller()
    controller.window.mainloop()