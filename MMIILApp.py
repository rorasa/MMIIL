import kivy

from kivy.app import App
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

import mmiil

class NumberBlock(Button):
    def update(self, value):
        self.text = str(value)

    def clear(self):
        self.text = ''

class MMIILGame(BoxLayout):
    button0 = ObjectProperty(None)
    button1 = ObjectProperty(None)
    button2 = ObjectProperty(None)
    button3 = ObjectProperty(None)
    button4 = ObjectProperty(None)
    button5 = ObjectProperty(None)
    button6 = ObjectProperty(None)
    button7 = ObjectProperty(None)
    button8 = ObjectProperty(None)
    button9 = ObjectProperty(None)
    button10= ObjectProperty(None)
    button11= ObjectProperty(None)
    button12= ObjectProperty(None)
    button13= ObjectProperty(None)
    button14= ObjectProperty(None)
    button15= ObjectProperty(None)
    scoreLabel = ObjectProperty(None)
    statusBar = ObjectProperty(None)

    def start(self):
        self.game = mmiil.Game()

        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):

        if not self.game.won:
            if keycode[1] == 'w':
                self.game.move('up')
                self.update()
            elif keycode[1] == 's':
                self.game.move('down')
                self.update()
            elif keycode[1] == 'a':
                self.game.move('left')
                self.update()
            elif keycode[1] == 'd':
                self.game.move('right')
                self.update()

        return True

    def update(self):
        # 0,0
        if self.game.board.board[0][0] == None:
            self.button0.clear()
        else:
            self.button0.update(self.game.board.board[0][0].value)

        # 0,1
        if self.game.board.board[0][1] == None:
            self.button1.clear()
        else:
            self.button1.update(self.game.board.board[0][1].value)

        # 0,2
        if self.game.board.board[0][2] == None:
            self.button2.clear()
        else:
            self.button2.update(self.game.board.board[0][2].value)

        # 0,3
        if self.game.board.board[0][3] == None:
            self.button3.clear()
        else:
            self.button3.update(self.game.board.board[0][3].value)

        # 1,0
        if self.game.board.board[1][0] == None:
            self.button4.clear()
        else:
            self.button4.update(self.game.board.board[1][0].value)

        # 1,1
        if self.game.board.board[1][1] == None:
            self.button5.clear()
        else:
            self.button5.update(self.game.board.board[1][1].value)

        # 1,2
        if self.game.board.board[1][2] == None:
            self.button6.clear()
        else:
            self.button6.update(self.game.board.board[1][2].value)

        # 1,3
        if self.game.board.board[1][3] == None:
            self.button7.clear()
        else:
            self.button7.update(self.game.board.board[1][3].value)

        # 2,0
        if self.game.board.board[2][0] == None:
            self.button8.clear()
        else:
            self.button8.update(self.game.board.board[2][0].value)

        # 2,1
        if self.game.board.board[2][1] == None:
            self.button9.clear()
        else:
            self.button9.update(self.game.board.board[2][1].value)

        # 2,2
        if self.game.board.board[2][2] == None:
            self.button10.clear()
        else:
            self.button10.update(self.game.board.board[2][2].value)

        # 2,3
        if self.game.board.board[2][3] == None:
            self.button11.clear()
        else:
            self.button11.update(self.game.board.board[2][3].value)

        # 3,0
        if self.game.board.board[3][0] == None:
            self.button12.clear()
        else:
            self.button12.update(self.game.board.board[3][0].value)

        # 3,1
        if self.game.board.board[3][1] == None:
            self.button13.clear()
        else:
            self.button13.update(self.game.board.board[3][1].value)

        # 3,2
        if self.game.board.board[3][2] == None:
            self.button14.clear()
        else:
            self.button14.update(self.game.board.board[3][2].value)

        # 3,3
        if self.game.board.board[3][3] == None:
            self.button15.clear()
        else:
            self.button15.update(self.game.board.board[3][3].value)

        self.scoreLabel.text = "Turns taken: "+str(self.game.turns)

        if self.game.won:
            self.statusBar.text = "Congratulations!"


class MMIILApp(App):
    def build(self):
        Window.size = (420,600)
        game = MMIILGame()
        game.start()
        game.update()
        return game

if __name__=='__main__':
    MMIILApp().run()
