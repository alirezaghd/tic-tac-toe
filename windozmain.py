# This Python file uses the following encoding: utf-8
import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow,QMessageBox

from PySide6.QtUiTools import QUiLoader



class windozmain(QMainWindow):
    def __init__(self):
        super(windozmain, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load("form.ui")
        self.game = [[None for i in range(3)] for j in range(3)]
        self.game[0][0] = self.ui.btn_00
        self.game[0][1] = self.ui.btn_01
        self.game[0][2] = self.ui.btn_02
        self.game[1][0] = self.ui.btn_10
        self.game[1][1] = self.ui.btn_11
        self.game[1][2] = self.ui.btn_12
        self.game[2][0] = self.ui.btn_20
        self.game[2][1] = self.ui.btn_21
        self.game[2][2] = self.ui.btn_22
        self.ui.show()
        self.player = 1
        self.player1_win = 0
        self.player2_win = 0
        self.draw = 0
        for i in  range(3):
            for j in range(3):
                self.game[i][j].clicked.connect(partial(self.play, i, j))


    def play(self,i,j):
        if self.game[i][j].text() == '':
            if self.player == 1:
                self.game[i][j].setText('X')
                self.game[i][j].setStyleSheet('color: red')
                self.player = 2

                if self.player == 2 and self.ui.rb_pvc.isChecked():
                    while True:
                        row = random.randint(0, 2)
                        col = random.randint(0, 2)
                        if self.game[row][col].text() == '':
                            self.game[row][col].setText('O')
                            self.game[row][col].setStyleSheet('color: blue')
                            self.player = 1
                            break
            elif self.player == 2 and self.ui.rb_pvp.isChecked():

                self.game[i][j].setText('O')
                self.game[i][j].setStyleSheet('color: blue')
                self.player = 1


        self.check()

    def clear(self):
        for i in range(3):
            for j in range(3):
                self.game[i][j].setText("")

    def check(self):
        for j in range(3):
                #if self.game[0][0] == 'x' and self.game[0][0] and self.game[0][0]
                if all(self.game[j][i].text() == 'X' for i in range(3)):
                    self.player1_win += 1
                    self.ui.lbl_s1.setText(str(self.player1_win))
                    msgbox = QMessageBox()
                    msgbox.setText('بازیکن 1 برنده')
                    msgbox.exec_()
                    self.clear()

                elif all(self.game[i][j].text() == 'X' for i in range(3)):
                    self.player1_win += 1
                    self.ui.lbl_s1.setText(str(self.player1_win))
                    msgbox = QMessageBox()
                    msgbox.setText('بازیکن 1 برنده')
                    msgbox.exec_()
                    self.clear()

                if all(self.game[j][i].text() == 'O' for i in range(3)):
                    self.player2_win += 1
                    self.ui.lbl_s2.setText(str(self.player2_win))
                    msgbox = QMessageBox()
                    msgbox.setText('بازیکن 2 برنده')
                    msgbox.exec_()
                    self.clear()

                elif all(self.game[i][j].text() == 'O' for i in range(3)):
                    self.player2_win += 1
                    self.ui.lbl_s2.setText(str(self.player2_win))
                    msgbox = QMessageBox()
                    msgbox.setText('بازیکن 2 برنده')
                    msgbox.exec_()
                    self.clear()

                if self.game[0][0].text() == 'X' and self.game[1][1].text() == 'X' and self.game[2][2].text() == 'X' or self.game[0][2].text() == 'X' and self.game[1][1].text() == 'X' and self.game[2][0].text() == 'X':
                    self.player1_win += 1
                    self.ui.lbl_s1.setText(str(self.player1_win))
                    msgbox = QMessageBox()
                    msgbox.setText('بازیکن 1 برنده')
                    msgbox.exec_()
                    self.clear()

                if self.game[0][0].text() == 'O' and self.game[1][1].text() == 'O' and self.game[2][2].text() == 'O' or self.game[0][2].text() == 'O' and self.game[1][1].text() == 'O' and self.game[2][0].text() == 'O':
                    self.player2_win += 1
                    self.ui.lbl_s2.setText(str(self.player2_win))
                    msgbox = QMessageBox()
                    msgbox.setText('بازیکن 2 برنده')
                    msgbox.exec_()
                    self.clear()



if __name__ == "__main__":
    app = QApplication([])
    window = windozmain()
    sys.exit(app.exec_())
