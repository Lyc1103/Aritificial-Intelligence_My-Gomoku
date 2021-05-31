# reference : https://blog.csdn.net/qq_44731019/article/details/111330958
from __future__ import with_statement
from tkinter import *
import tkinter.messagebox
import numpy as np
from numpy.core.numeric import outer
from MyAI import *
from Graph import *
import time
import sys
import platform

sys.setrecursionlimit(1000000)
sysstr = platform.system()

# Global variables/settings
global block_num, steps, _text_
_text_ = "ABCDEFGHIJKLMNOPQRS"
block_num = 19
firat_step = 1
taichi_x = 625
taichi_y = 260
taichi_w_calibration = 9
taichi_b_calibration = 11
plate_edge_x = 165
plate_edge_y = 33.77777777777777
player = ["Black", "White"]
loop_times = 10

# colors
board_bg = "gray10"
board_fg = "white"
board_right = "sky blue"
board_left = "spring green"
button_color = "gray20"  # "alice blue"
button_fg = "gray"
active_fg = "white"
font_style = "Helvetica"


class MyGo(Tk):
    def __init__(self, my_block_num=19):
        Tk.__init__(self)
        self.sys = sysstr

        # for AI
        self.AIx = 0
        self.AIy = 0
        self.steps = 0
        self.eve_loop_times = loop_times

        self.block_num = my_block_num
        self.size = 1.8
        self.dd = 360 * self.size / (self.block_num - 1)
        self.p = 4 / 9
        self.x = 0
        self.y = 0

        # Set Plate and Graph
        self.positions = np.zeros((self.block_num + 2, self.block_num + 2))  # [
        self.graph = Graph()
        self.init_plategraph()

        self.cross_last = None
        # Black player go first, 0: black, 1: white
        self.present = 0
        # stop = None then start the game
        self.stop = True
        # Create the frame
        self.geometry(str(int(700 * self.size)) + "x" + str(int(400 * self.size)))
        self.canvas_bottom = Canvas(
            self, bg="white", bd=0, width=700 * self.size, height=400 * self.size
        )
        self.canvas_bottom.place(x=0, y=0)
        self.gg = Label(
            self,
            text="Press Start to get start.",
            fg=board_fg,
            bg=board_bg,
            font=(font_style, 40),
        )
        self.gg.place(x=350 * self.size, y=200 * self.size, anchor=CENTER)

        # Labels
        self.label()
        # Several buttons
        self.bottoms()
        # draw board
        self.mid_board()
        self.right_board()
        self.left_board()

        # Load some photos in need
        self.PhotoWellcome = PhotoImage(file="./Pictures/Title.png")
        self.photoW = PhotoImage(file="./Pictures/W.png")
        self.photoB = PhotoImage(file="./Pictures/B.png")
        self.nap = PhotoImage(file="./Pictures/cat.png")
        self.photoWD = PhotoImage(file="./Pictures/WD.png")
        self.photoBD = PhotoImage(file="./Pictures/BD.png")
        self.photoWU = PhotoImage(file="./Pictures/WU.png")
        self.photoBU = PhotoImage(file="./Pictures/BU.png")
        self.photoWBU_list = [self.photoBU, self.photoWU]
        self.photoWBD_list = [self.photoBD, self.photoWD]
        self.beautification()
        self.canvas_bottom.bind("<Motion>", self.shadow)
        self.canvas_bottom.bind("<Button-1>", self.getDown)
        self.bind("<Control-KeyPress-d>", self.keyboardQuit)

    def init_plategraph(self):
        for m in range(self.block_num + 2):
            for n in range(self.block_num + 2):
                if m * n == 0 or m == self.block_num + 1 or n == self.block_num + 1:
                    self.positions[m][n] = -1

        for m in range(1, self.block_num + 1):
            for n in range(1, self.block_num + 1):
                # print("N")
                self.graph.add_edge(
                    str(n) + "_" + str(m), str(n) + "_" + str(m - 1), "N"
                )
                if self.positions[m - 1][n] == -1:
                    tmp = self.graph.get_vertex(str(n) + "_" + str(m - 1))
                    tmp.BorW = -1

                # print("EN")
                self.graph.add_edge(
                    str(n) + "_" + str(m), str(n + 1) + "_" + str(m - 1), "EN"
                )
                if self.positions[m - 1][n + 1] == -1:
                    tmp = self.graph.get_vertex(str(n + 1) + "_" + str(m - 1))
                    tmp.BorW = -1

                # print("E")
                self.graph.add_edge(
                    str(n) + "_" + str(m), str(n + 1) + "_" + str(m), "E"
                )
                if self.positions[m][n + 1] == -1:
                    tmp = self.graph.get_vertex(str(n + 1) + "_" + str(m))
                    tmp.BorW = -1

                # print("ES")
                self.graph.add_edge(
                    str(n) + "_" + str(m), str(n + 1) + "_" + str(m + 1), "ES"
                )
                if self.positions[m + 1][n + 1] == -1:
                    tmp = self.graph.get_vertex(str(n + 1) + "_" + str(m + 1))
                    tmp.BorW = -1

                # print("S")
                self.graph.add_edge(
                    str(n) + "_" + str(m), str(n) + "_" + str(m + 1), "S"
                )
                if self.positions[m + 1][n] == -1:
                    tmp = self.graph.get_vertex(str(n) + "_" + str(m + 1))
                    tmp.BorW = -1

                # print("WS")
                self.graph.add_edge(
                    str(n) + "_" + str(m), str(n - 1) + "_" + str(m + 1), "WS"
                )
                if self.positions[m + 1][n - 1] == -1:
                    tmp = self.graph.get_vertex(str(n - 1) + "_" + str(m + 1))
                    tmp.BorW = -1

                # print("W")
                self.graph.add_edge(
                    str(n) + "_" + str(m), str(n - 1) + "_" + str(m), "W"
                )
                if self.positions[m][n - 1] == -1:
                    tmp = self.graph.get_vertex(str(n - 1) + "_" + str(m))
                    tmp.BorW = -1

                # print("WN")
                self.graph.add_edge(
                    str(n) + "_" + str(m), str(n - 1) + "_" + str(m - 1), "WN"
                )
                if self.positions[m - 1][n - 1] == -1:
                    tmp = self.graph.get_vertex(str(n - 1) + "_" + str(m - 1))
                    tmp.BorW = -1
        # print(self.graph.num_vertices)
        # tmp = self.graph.get_vertex("19_19")
        # print(tmp.BorW)
        # print(tmp.N.BorW)
        # print(tmp.EN.BorW)
        # print(tmp.E.BorW)
        # print(tmp.ES.BorW)
        # print(tmp.S.BorW)
        # print(tmp.WS.BorW)
        # print(tmp.W.BorW)
        # print(tmp.WN.BorW)
        # print(self.positions[20][20])

    def bottoms(self):
        self.startButton = Button(
            self,
            text="S",
            fg=button_fg,
            bg=button_color,
            font=(font_style, 20),
            # height=2,
            # width=5,
            highlightthickness=0,
            borderwidth=0,
            activebackground=button_color,
            activeforeground=active_fg,
            command=self.start,
        )
        self.startButton.place(x=35 * self.size, y=257 * self.size, anchor=CENTER)
        self.stopButton = Button(
            self,
            text="T",
            fg=button_fg,
            background=button_color,
            font=(font_style, 20),
            highlightthickness=0,
            borderwidth=0,
            activebackground=button_color,
            activeforeground=active_fg,
            command=self.stop_button,
        )
        self.stopButton.place(x=75 * self.size, y=217 * self.size, anchor=CENTER)
        self.replayButton = Button(
            self,
            text="R",
            fg=button_fg,
            bg=button_color,
            font=(font_style, 20),
            # height=2,
            # width=5,
            highlightthickness=0,
            borderwidth=0,
            activebackground=button_color,
            activeforeground=active_fg,
            command=self.reload,
        )
        self.replayButton.place(x=115 * self.size, y=257 * self.size, anchor=CENTER)
        self.quitButton = Button(
            self,
            text="E",
            fg=button_fg,
            bg=button_color,
            font=(font_style, 20),
            highlightthickness=0,
            borderwidth=0,
            activebackground=button_color,
            activeforeground=active_fg,
            command=self.quit,
        )
        self.quitButton.place(x=75 * self.size, y=297 * self.size, anchor=CENTER)
        self.player_mode = 1
        self.PvPButton = Button(
            self,
            text="X",
            fg=button_fg,
            bg=button_color,
            font=(font_style, 20),
            highlightthickness=0,
            borderwidth=0,
            activebackground=button_color,
            activeforeground=active_fg,
            command=self.bonus,  #########################################
        )
        self.PvPButton.place(x=625 * self.size, y=87 * self.size, anchor=CENTER)
        self.player_mode = 1
        self.PvPButton = Button(
            self,
            text="Y",
            fg=button_fg,
            bg=button_color,
            font=(font_style, 20),
            highlightthickness=0,
            borderwidth=0,
            activebackground=button_color,
            activeforeground=active_fg,
            command=self.PvP,
        )
        self.PvPButton.place(x=585 * self.size, y=127 * self.size, anchor=CENTER)
        self.PvEButton = Button(
            self,
            text="A",
            fg=button_fg,
            bg=button_color,
            font=(font_style, 20),
            highlightthickness=0,
            borderwidth=0,
            activebackground=button_color,
            activeforeground=active_fg,
            command=self.AvA,
        )
        self.PvEButton.place(x=665 * self.size, y=127 * self.size, anchor=CENTER)
        self.EvEButton = Button(
            self,
            text="B",
            fg=button_fg,
            bg=button_color,
            font=(font_style, 20),
            highlightthickness=0,
            borderwidth=0,
            activebackground=button_color,
            activeforeground=active_fg,
            command=self.PvA,
        )
        self.EvEButton.place(x=625 * self.size, y=167 * self.size, anchor=CENTER)

    def label(self):

        self.mode_label = Label(
            self, text="current mode = PvP", bg=board_right, font=(font_style, 10)
        )
        self.mode_label.place(x=625 * self.size, y=25 * self.size, anchor=CENTER)
        print("Current mode is PvP ( player1 v.s. player2 )")
        self.bonus_pic = Label(text="", bg="white")
        self.bonus_pic.place(x=0, y=0)
        self.bonus_txt = Label(text="", bg="white")
        self.bonus_txt.place(x=0, y=0)
        self.menu = Label(
            text="S:Start,  T:Stop,  R:Reload,  E:Exit,  Y:PvP,  A:AvA,  B:PvA",
            fg=board_fg,
            bg=board_bg,
            font=(font_style, 10),
        )
        self.menu.place(x=350 * self.size, y=395 * self.size, anchor=CENTER)

    def mid_board(self):
        for i in range(19):
            Label(self, text=_text_[i], fg=board_fg, bg=board_bg, font=("", 12)).place(
                x=plate_edge_x * self.size + 36 * i, y=2
            )
            if i < 9:
                Label(
                    self, text=str(i + 1), fg=board_fg, bg=board_bg, font=("", 12)
                ).place(x=150 * self.size + 10, y=plate_edge_y - 15 + 36 * i)
            else:
                Label(
                    self, text=str(i + 1), fg=board_fg, bg=board_bg, font=("", 12)
                ).place(x=150 * self.size + 5, y=plate_edge_y - 15 + 36 * i)
        self.canvas_bottom.create_rectangle(
            150 * self.size,
            0 * self.size,
            550 * self.size,
            400 * self.size,
            fill=board_bg,
        )
        self.canvas_bottom.create_rectangle(
            170 * self.size,
            20 * self.size,
            530 * self.size,
            380 * self.size,
            width=3,
            outline="gray",
        )

        for i in range(1, self.block_num - 1):
            # row
            self.canvas_bottom.create_line(
                170 * self.size,
                i * self.dd + 20 * self.size,
                530 * self.size,
                i * self.dd + 20 * self.size,
                width=2,
                fill="gray",
            )
            # column
            self.canvas_bottom.create_line(
                i * self.dd + 170 * self.size,
                20 * self.size,
                i * self.dd + 170 * self.size,
                380 * self.size,
                width=2,
                fill="gray",
            )
        for m in range(-1, 2):
            for n in range(-1, 2):
                self.canvas_bottom.create_oval(
                    350 * self.size + 120 * m * self.size - self.size * 2,
                    200 * self.size + 120 * n * self.size - self.size * 2,
                    350 * self.size + 120 * m * self.size + self.size * 2,
                    200 * self.size + 120 * n * self.size + self.size * 2,
                    fill="white",
                )

    def right_board(self):
        self.canvas_bottom.create_oval(
            600 * self.size,
            0 * self.size,
            700 * self.size,
            100 * self.size,
            fill=board_right,
        )
        self.canvas_bottom.create_oval(
            600 * self.size,
            300 * self.size,
            700 * self.size,
            400 * self.size,
            fill=board_right,
        )
        self.canvas_bottom.create_rectangle(
            550 * self.size,
            0 * self.size,
            650 * self.size,
            400 * self.size,
            fill=board_right,
            outline=board_right,
        )
        self.canvas_bottom.create_rectangle(
            650 * self.size,
            50 * self.size,
            700 * self.size,
            350 * self.size,
            fill=board_right,
            outline=board_right,
        )

        # X
        self.canvas_bottom.create_oval(
            605 * self.size,
            65 * self.size,
            645 * self.size,
            105 * self.size,
            fill=button_color,
            outline=board_right,
        )
        # Y
        self.canvas_bottom.create_oval(
            565 * self.size,
            105 * self.size,
            605 * self.size,
            145 * self.size,
            fill=button_color,
            outline=board_right,
        )
        # A
        self.canvas_bottom.create_oval(
            645 * self.size,
            105 * self.size,
            685 * self.size,
            145 * self.size,
            fill=button_color,
            outline=board_right,
        )
        # B
        self.canvas_bottom.create_oval(
            605 * self.size,
            145 * self.size,
            645 * self.size,
            185 * self.size,
            fill=button_color,
            outline=board_right,
        )

    def left_board(self):
        self.canvas_bottom.create_oval(
            0 * self.size,
            0 * self.size,
            100 * self.size,
            100 * self.size,
            fill=board_left,
        )
        self.canvas_bottom.create_oval(
            0 * self.size,
            300 * self.size,
            100 * self.size,
            400 * self.size,
            fill=board_left,
        )
        self.canvas_bottom.create_rectangle(
            50 * self.size,
            0 * self.size,
            150 * self.size,
            400 * self.size,
            fill=board_left,
            outline=board_left,
        )
        self.canvas_bottom.create_rectangle(
            0 * self.size,
            50 * self.size,
            50 * self.size,
            350 * self.size,
            fill=board_left,
            outline=board_left,
        )
        # S
        self.canvas_bottom.create_oval(
            15 * self.size,
            235 * self.size,
            55 * self.size,
            275 * self.size,
            fill=button_color,
            outline=board_left,
        )
        # T
        self.canvas_bottom.create_oval(
            55 * self.size,
            195 * self.size,
            95 * self.size,
            235 * self.size,
            fill=button_color,
            outline=board_left,
        )
        # R
        self.canvas_bottom.create_oval(
            95 * self.size,
            235 * self.size,
            135 * self.size,
            275 * self.size,
            fill=button_color,
            outline=board_left,
        )
        # E
        self.canvas_bottom.create_oval(
            55 * self.size,
            275 * self.size,
            95 * self.size,
            315 * self.size,
            fill=button_color,
            outline=board_left,
        )

    def beautification(self):
        self.wellcome = self.canvas_bottom.create_image(
            75 * self.size, 100 * self.size, image=self.PhotoWellcome
        )
        self.pW = self.canvas_bottom.create_image(
            taichi_x * self.size + taichi_w_calibration,
            taichi_y * self.size,
            image=self.photoW,
        )
        self.pB = self.canvas_bottom.create_image(
            taichi_x * self.size + taichi_b_calibration,
            taichi_y * self.size,
            image=self.photoB,
        )
        self.canvas_bottom.addtag_withtag("image", self.pW)
        self.canvas_bottom.addtag_withtag("image", self.pB)
        self.leftedge = self.canvas_bottom.create_rectangle(
            145 * self.size,
            0,
            150 * self.size,
            400 * self.size,
            fill="gray",
            outline="gray",
        )
        self.leftedge = self.canvas_bottom.create_rectangle(
            550 * self.size,
            0,
            555 * self.size,
            400 * self.size,
            fill="gray",
            outline="gray",
        )

    def start(self):
        self.gg.after(1000, self.gg.destroy)
        self.bonus_pic.after(1000, self.bonus_pic.destroy)
        self.bonus_txt.after(1000, self.bonus_txt.destroy)
        if self.stop:
            # self.reload()
            self.canvas_bottom.delete(self.pW)
            self.canvas_bottom.delete(self.pB)

            if self.present == 0:
                self.create_pB()
                self.del_pW()
            else:
                self.create_pW()
                self.del_pB()
            self.stop = None
            if self.player_mode == 3:
                print("////////  Count Backwards: " + str(self.eve_loop_times))
                gg = self.getDown(self)
                while gg == None:
                    gg = self.getDown(self)
                self.end_game(gg)

    def stop_button(self):
        print("Stop")
        self.stop = True

    def create_pW(self):
        self.pW = self.canvas_bottom.create_image(
            taichi_x * self.size + taichi_w_calibration,
            taichi_y * self.size,
            image=self.photoW,
        )
        self.canvas_bottom.addtag_withtag("image", self.pW)

    def create_pB(self):
        self.pB = self.canvas_bottom.create_image(
            taichi_x * self.size + taichi_b_calibration,
            taichi_y * self.size,
            image=self.photoB,
        )
        self.canvas_bottom.addtag_withtag("image", self.pB)

    def del_pW(self):
        self.canvas_bottom.delete(self.pW)

    def del_pB(self):
        self.canvas_bottom.delete(self.pB)

    def PvP(self):
        self.stop = True
        self.player_mode = 1
        self.mode_label = Label(
            self, text="current mode = PvP", bg=board_right, font=(font_style, 10)
        )
        self.mode_label.place(x=625 * self.size, y=25 * self.size, anchor=CENTER)
        print("Current mode is PvP ( player1 v.s. player2 )")
        self.reload()

    def PvA(self):
        self.stop = True
        self.player_mode = 2
        self.mode_label = Label(
            self, text="current mode = PvA", bg=board_right, font=(font_style, 10)
        )
        self.mode_label.place(x=625 * self.size, y=25 * self.size, anchor=CENTER)
        print("Current mode is PvA ( player v.s. AI )")
        self.reload()

    def AvA(self):
        self.stop = True
        self.player_mode = 3
        self.mode_label = Label(
            self, text="current mode = AvA", bg=board_right, font=(font_style, 10)
        )
        self.mode_label.place(x=625 * self.size, y=25 * self.size, anchor=CENTER)
        print("Current mode is AvA ( AI1 v.s. AI2 )")
        self.reload()

    def reload(self):
        self.canvas_bottom.delete("image")
        self.present = 0
        self.steps = 0
        self.create_pB()
        self.reset_plategraph()
        print("Reloaded...")

    def reset_plategraph(self):
        for m in range(1, self.block_num + 1):
            for n in range(1, self.block_num + 1):
                self.positions[m][n] = 0
                v = self.graph.get_vertex(str(n) + "_" + str(m))
                v.reset()

    def shadow(self, event):
        if not self.stop:
            if self.player_mode == 1:
                if (170 * self.size < event.x < 530 * self.size) and (
                    20 * self.size < event.y < 380 * self.size
                ):
                    dx = (event.x - 10 * self.size) % self.dd
                    dy = (event.y - 20 * self.size) % self.dd
                    self.cross = self.canvas_bottom.create_image(
                        event.x - dx + round(dx / self.dd) * self.dd,
                        event.y - dy + round(dy / self.dd) * self.dd,
                        image=self.photoWBU_list[self.present],
                    )
                    self.canvas_bottom.addtag_withtag("image", self.cross)
                    if self.cross_last != None:
                        self.canvas_bottom.delete(self.cross_last)
                    self.cross_last = self.cross
            elif self.player_mode == 2:
                if self.present == 0:
                    self.AIx, self.AIy = myAI(self)
                    if self.AIx == -1 and self.AIy == -1:
                        self.end_game(2)
                    else:
                        self.getDown(self)
                    # self.steps = 0
                else:
                    if (170 * self.size < event.x < 530 * self.size) and (
                        20 * self.size < event.y < 380 * self.size
                    ):
                        dx = (event.x - 10 * self.size) % self.dd
                        dy = (event.y - 20 * self.size) % self.dd
                        self.cross = self.canvas_bottom.create_image(
                            event.x - dx + round(dx / self.dd) * self.dd,
                            event.y - dy + round(dy / self.dd) * self.dd,
                            image=self.photoWBU_list[self.present],
                        )
                        self.canvas_bottom.addtag_withtag("image", self.cross)
                        if self.cross_last != None:
                            self.canvas_bottom.delete(self.cross_last)
                        self.cross_last = self.cross

    def getDown(self, event):
        if not self.stop:
            self.canvas_bottom.delete(self.pW)
            self.canvas_bottom.delete(self.pB)
            if self.present == 1:
                self.create_pB()
                self.del_pW()
            else:
                self.create_pW()
                self.del_pB()

            if self.player_mode == 1:
                if (
                    170 * self.size - self.dd * 0.4
                    < event.x
                    < self.dd * 0.4 + 530 * self.size
                ) and (
                    20 * self.size - self.dd * 0.4
                    < event.y
                    < self.dd * 0.4 + 380 * self.size
                ):
                    dx = (event.x - 10 * self.size) % self.dd
                    dy = (event.y - 20 * self.size) % self.dd
                    self.x = int(
                        (event.x - 170 * self.size - dx) / self.dd
                        + round(dx / self.dd)
                        + 1
                    )
                    self.y = int(
                        (event.y - 20 * self.size - dy) / self.dd
                        + round(dy / self.dd)
                        + 1
                    )
                    if self.positions[self.y][self.x] == 0:
                        self.positions[self.y][self.x] = self.present + 1
                        gg = FlagInGraph(self, self.x, self.y, self.present + 1)
                        self.image_added = self.canvas_bottom.create_image(
                            event.x - dx + round(dx / self.dd) * self.dd + 4 * self.p,
                            event.y - dy + round(dy / self.dd) * self.dd - 5 * self.p,
                            image=self.photoWBD_list[self.present],
                        )
                        self.canvas_bottom.addtag_withtag("image", self.image_added)
                        print(
                            "Player "
                            + player[self.present]
                            + " got position (x, y) = ("
                            + _text_[self.x - 1]
                            + ", "
                            + str(self.y)
                            + ")"
                        )
                        self.present = (self.present + 1) % 2
                        if (gg == 1) or (gg == -1):
                            self.end_game(gg)
                    else:
                        self.bell()
                else:
                    self.bell()
            elif self.player_mode == 2:
                if self.present == 0:
                    self.positions[self.AIy][self.AIx] = self.present + 1
                    gg = FlagInGraph(self, self.AIx, self.AIy, self.present + 1)
                    self.image_added = self.canvas_bottom.create_image(
                        plate_edge_x + (self.AIx - 1) * 36 + 80 * self.size,
                        plate_edge_y + (self.AIy - 1) * 36,
                        image=self.photoWBD_list[self.present],
                    )
                    self.canvas_bottom.addtag_withtag("image", self.image_added)
                    self.graph.add_to_black_path(str(self.AIx) + "_" + str(self.AIy))
                    print(
                        "AI got position (x, y) = ("
                        + _text_[self.AIx - 1]
                        + ", "
                        + str(self.AIy)
                        + ")"
                    )
                    self.present = (self.present + 1) % 2
                    if (gg == 1) or (gg == -1):
                        self.end_game(gg)
                else:
                    if (
                        170 * self.size - self.dd * 0.4
                        < event.x
                        < self.dd * 0.4 + 530 * self.size
                    ) and (
                        20 * self.size - self.dd * 0.4
                        < event.y
                        < self.dd * 0.4 + 380 * self.size
                    ):
                        dx = (event.x - 10 * self.size) % self.dd
                        dy = (event.y - 20 * self.size) % self.dd
                        self.x = int(
                            (event.x - 170 * self.size - dx) / self.dd
                            + round(dx / self.dd)
                            + 1
                        )
                        self.y = int(
                            (event.y - 20 * self.size - dy) / self.dd
                            + round(dy / self.dd)
                            + 1
                        )
                        # print('ex = '+str(event.x-dx+round(dx/self.dd)*self.dd+4*self.p)+', ey = '+str(event.y-dy+round(dy/self.dd)*self.dd-5*self.p))
                        # print('x = '+str(self.x)+', y = '+str(self.y))
                        # print(self.positions)
                        if self.positions[self.y][self.x] == 0:
                            self.positions[self.y][self.x] = self.present + 1
                            gg = FlagInGraph(self, self.x, self.y, self.present + 1)
                            self.image_added = self.canvas_bottom.create_image(
                                event.x
                                - dx
                                + round(dx / self.dd) * self.dd
                                + 4 * self.p,
                                event.y
                                - dy
                                + round(dy / self.dd) * self.dd
                                - 5 * self.p,
                                image=self.photoWBD_list[self.present],
                            )
                            self.canvas_bottom.addtag_withtag("image", self.image_added)
                            print(
                                "You got position (x, y) = ("
                                + _text_[self.x - 1]
                                + ", "
                                + str(self.y)
                                + ")"
                            )
                            self.present = (self.present + 1) % 2
                            if (gg == 1) or (gg == -1):
                                self.end_game(gg)
                        else:
                            self.bell()
                    else:
                        self.bell()
            elif self.player_mode == 3:
                self.AIx, self.AIy = myAI(self)
                if self.AIx == -1 and self.AIy == -1:
                    self.end_game(2)
                else:
                    self.positions[self.AIy][self.AIx] = self.present + 1
                    gg = FlagInGraph(self, self.AIx, self.AIy, self.present + 1)
                    self.image_added = self.canvas_bottom.create_image(
                        plate_edge_x + (self.AIx - 1) * 36 + 80 * self.size,
                        plate_edge_y + (self.AIy - 1) * 36,
                        image=self.photoWBD_list[self.present],
                    )
                    self.canvas_bottom.addtag_withtag("image", self.image_added)
                    if self.present == 0:
                        self.graph.add_to_black_path(
                            str(self.AIx) + "_" + str(self.AIy)
                        )
                    elif self.present == 1:
                        self.graph.add_to_white_path(
                            str(self.AIx) + "_" + str(self.AIy)
                        )
                    # print(
                    #     "AI "
                    #     + player[self.present]
                    #     + " got position (x, y) = ("
                    #     + _text_[self.AIx - 1]
                    #     + ", "
                    #     + str(self.AIy)
                    #     + ")"
                    # )
                    self.present = (self.present + 1) % 2
                    if (gg == 1) or (gg == -1):
                        return gg
                        # self.end_game(gg)

    def end_game(self, gg):
        if gg == 2:
            self.gg = Label(
                self,
                text="Tie!",
                fg="red",
                bg=board_left,
                font=(font_style, 20),
            )
            self.gg.place(x=75 * self.size, y=160 * self.size, anchor=CENTER)
            print("Tie!")
        elif self.player_mode == 1:
            if gg == 1:
                self.gg = Label(
                    self,
                    text="Player White Win!",
                    fg="red",
                    bg=board_left,
                    font=(font_style, 20),
                )
                self.gg.place(x=75 * self.size, y=160 * self.size, anchor=CENTER)
                print("Player White Win!")
            elif gg == -1:
                self.gg = Label(
                    self,
                    text="Player Black Win!",
                    fg="red",
                    bg=board_left,
                    font=(font_style, 20),
                )
                self.gg.place(x=75 * self.size, y=160 * self.size, anchor=CENTER)
                print("Player Black Win!")
        elif self.player_mode == 2:
            if gg == 1:
                self.gg = Label(
                    self,
                    text="Congratulation!\nYou Win",
                    fg="red",
                    bg=board_left,
                    font=(font_style, 20),
                )
                self.gg.place(x=75 * self.size, y=160 * self.size, anchor=CENTER)
                print("You Win!")
                # refresh black path rate
                RefreshRate(self, gg)
                OutputRate(self)
            elif gg == -1:
                self.gg = Label(
                    self,
                    text="You Loss...\nPress\nRelaod and Start\nto try again.",
                    fg="red",
                    bg=board_left,
                    font=(font_style, 20),
                )
                self.gg.place(x=75 * self.size, y=170 * self.size, anchor=CENTER)
                print("You Loss...")
        elif self.player_mode == 3:
            # time.sleep(0.001)
            if gg == 1:
                self.gg = Label(
                    self,
                    text="AI White Win!",
                    fg="red",
                    bg=board_left,
                    font=(font_style, 20),
                )
                self.gg.place(x=75 * self.size, y=160 * self.size, anchor=CENTER)
                print("AI White Win!")
                # refresh path rate
                RefreshRate(self, gg)
                OutputRate(self)
            elif gg == -1:
                self.gg = Label(
                    self,
                    text="AI Black Win!",
                    fg="red",
                    bg=board_left,
                    font=(font_style, 20),
                )
                self.gg.place(x=75 * self.size, y=160 * self.size, anchor=CENTER)
                print("AI Black Win!")
                # refresh path rate
                RefreshRate(self, gg)
                OutputRate(self)
            # loop to get data
            # time.sleep(0.001)
            self.stop = True
            self.eve_loop_times -= 1
            if self.eve_loop_times > 0:
                self.reload()
                self.start()
        if self.eve_loop_times <= 0:
            self.eve_loop_times = loop_times
        self.stop = True

    def showwarningbox(self, title, message):
        self.canvas_bottom.delete(self.cross)
        tkinter.messagebox.showwarning(title, message)

    def keyboardQuit(self, event):
        self.quit()

    def bonus(self):
        self.bonus_pic = Label(image=self.nap)
        self.bonus_pic.place(x=350 * self.size, y=200 * self.size, anchor=CENTER)
        self.bonus_txt = Label(
            text="Meowwwwwww....", font=(font_style, 30), fg=board_fg, bg=board_bg
        )
        self.bonus_txt.place(x=350 * self.size, y=325 * self.size, anchor=CENTER)
