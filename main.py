import sys
from MyGomoku import MyGo
from MyAI import myAI
import numpy as np
import platform

Black_Plate = np.zeros((19, 19))

if __name__ == "__main__":
    sysstr = platform.system()
    if sysstr == "Windows":
        print("Windows Environment")
    elif sysstr == "Linux":
        print("Linux Environment")
    else:
        print("Other System Environment")
        print("Some background in this game does not support this system!")
        sysstr = input("Do you still want to run it? [Y/N] ")
    if sysstr == "Windows" or sysstr == "Linux" or sysstr == "Y" or sysstr == "y":
        while True:
            newGame = False
            block_num = 19
            game = MyGo(block_num)
            game.title("PlayGo")
            game.mainloop()
            if newGame:
                game.destroy()
            else:
                break

    print("Good Bye~")

    # with open("black.txt", mode="w") as file:
    #     for m in range(game.block_num):
    #         for n in range(game.block_num):
    #             for i in range(game.block_num * game.block_num):
    #                 file.write("0 ")
    #             file.write("\n")
    #             for j in range(game.block_num * game.block_num):
    #                 file.write("0 ")
    #             file.write("\n")
    # with open("white.txt", mode="w") as file:
    #     for m in range(game.block_num):
    #         for n in range(game.block_num):
    #             for i in range(game.block_num * game.block_num):
    #                 file.write("0 ")
    #             file.write("\n")
    #             for j in range(game.block_num * game.block_num):
    #                 file.write("0 ")
    #             file.write("\n")
