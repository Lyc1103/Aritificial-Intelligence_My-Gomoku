from numpy import *
from Graph import *


def myAI(gomoku):
    x = 0
    y = 0
    decision = 0
    for m in range(1, gomoku.block_num + 1):
        for n in range(1, gomoku.block_num + 1):
            if gomoku.positions[m][n] != 0:
                gomoku.steps += 1
    if gomoku.steps == 361:
        print("There is no position to take!")
        x = -1
        y = -1
    elif gomoku.steps == 0:
        InitRate(gomoku)
        while not decision:
            x = int(random.random() * 19) + 1
            y = int(random.random() * 19) + 1
            if ((x < 3) or (x > 17)) and ((y < 3) or (y > 17)):
                # print(
                #     "First step should be The first step must be in the outer two circles."
                # )
                decision = 1
    elif gomoku.steps == 1 or gomoku.steps == 2:
        while not decision:
            tmp_x = 10
            tmp_y = 10
            ran_num = int(random.random() * 97) + 1
            # print(ran_num)
            if ran_num <= 50:
                if gomoku.positions[tmp_y][tmp_x] == 0:
                    x = tmp_x
                    y = tmp_y
                    decision = 1
            elif ran_num <= 75:
                while not decision:
                    ran_num = int(random.random() * 2 * 1 * 4) + 1
                    row = -1
                    col = -1
                    if ran_num > 1:
                        for i in range(1, ran_num):
                            if i < 2 * 1 + 1 or i > 2 * 1 * 4 - (2 * 1 + 1):
                                row += 1
                            else:
                                if ran_num % 2 == 1:
                                    row = -1
                                    col += 1
                                else:
                                    row = 1
                    if (
                        (tmp_y + col < 1)
                        or (tmp_y + col > 19)
                        or (tmp_x + row < 1)
                        or (tmp_x + row > 19)
                    ):
                        continue
                    if gomoku.positions[tmp_y + col][tmp_x + row] == 0:
                        x = tmp_x + row
                        y = tmp_y + col
                        decision = 1
            elif ran_num <= 87:
                while not decision:
                    ran_num = int(random.random() * 2 * 2 * 4) + 1
                    row = -2
                    col = -2
                    if ran_num > 1:
                        for i in range(1, ran_num):
                            if i < 2 * 2 + 1 or i > 2 * 2 * 4 - (2 * 2 + 1):
                                row += 1
                            else:
                                if ran_num % 2 == 1:
                                    row = -1
                                    col += 1
                                else:
                                    row = 1
                    if (
                        (tmp_y + col < 1)
                        or (tmp_y + col > 19)
                        or (tmp_x + row < 1)
                        or (tmp_x + row > 19)
                    ):
                        continue
                    if gomoku.positions[tmp_y + col][tmp_x + row] == 0:
                        x = tmp_x + row
                        y = tmp_y + col
                        decision = 1
            elif ran_num <= 93:
                while not decision:
                    ran_num = int(random.random() * 2 * 3 * 4) + 1
                    row = -3
                    col = -3
                    if ran_num > 1:
                        for i in range(1, ran_num):
                            if i < 2 * 3 + 1 or i > 2 * 3 * 4 - (2 * 3 + 1):
                                row += 1
                            else:
                                if ran_num % 2 == 1:
                                    row = -1
                                    col += 1
                                else:
                                    row = 1
                    if (
                        (tmp_y + col < 1)
                        or (tmp_y + col > 19)
                        or (tmp_x + row < 1)
                        or (tmp_x + row > 19)
                    ):
                        continue
                    if gomoku.positions[tmp_y + col][tmp_x + row] == 0:
                        x = tmp_x + row
                        y = tmp_y + col
                        decision = 1
            elif ran_num <= 96:
                while not decision:
                    ran_num = int(random.random() * 2 * 4 * 4) + 1
                    row = -4
                    col = -4
                    if ran_num > 1:
                        for i in range(1, ran_num):
                            if i < 2 * 4 + 1 or i > 2 * 4 * 4 - (2 * 4 + 1):
                                row += 1
                            else:
                                if ran_num % 2 == 1:
                                    row = -1
                                    col += 1
                                else:
                                    row = 1
                    if (
                        (tmp_y + col < 1)
                        or (tmp_y + col > 19)
                        or (tmp_x + row < 1)
                        or (tmp_x + row > 19)
                    ):
                        continue
                    if gomoku.positions[tmp_y + col][tmp_x + row] == 0:
                        x = tmp_x + row
                        y = tmp_y + col
                        decision = 1
            elif ran_num <= 97:
                while not decision:
                    ran_num = int(random.random() * 2 * 5 * 4) + 1
                    row = -5
                    col = -5
                    if ran_num > 1:
                        for i in range(1, ran_num):
                            if i < 2 * 5 + 1 or i > 2 * 5 * 4 - (2 * 5 + 1):
                                row += 1
                            else:
                                if ran_num % 2 == 1:
                                    row = -1
                                    col += 1
                                else:
                                    row = 1
                    if (
                        (tmp_y + col < 1)
                        or (tmp_y + col > 19)
                        or (tmp_x + row < 1)
                        or (tmp_x + row > 19)
                    ):
                        continue
                    if gomoku.positions[tmp_y + col][tmp_x + row] == 0:
                        x = tmp_x + row
                        y = tmp_y + col
                        decision = 1
    else:
        tmp_x = 0
        tmp_y = 0
        for m in range(1, gomoku.block_num + 1):
            for n in range(1, gomoku.block_num + 1):
                v = gomoku.graph.get_vertex(str(n) + "_" + str(m))
                tmp_v = gomoku.graph.get_vertex(str(n) + "_" + str(m))

                tmp_x, tmp_y = CheckTriple_OneLive(v, tmp_v, gomoku)
                if tmp_x != 0 and tmp_y != 0:
                    x = tmp_x
                    y = tmp_y
                    decision = 1

                tmp_x, tmp_y = CheckBothSide(v, m, n)
                if tmp_x != 0 and tmp_y != 0:
                    x = tmp_x
                    y = tmp_y
                    decision = 1

        for m in range(1, gomoku.block_num + 1):
            for n in range(1, gomoku.block_num + 1):
                v = gomoku.graph.get_vertex(str(n) + "_" + str(m))
                tmp_v = gomoku.graph.get_vertex(str(n) + "_" + str(m))

                tmp_x, tmp_y = CheckTriple_TwoLive(v, tmp_v, gomoku)
                if tmp_x != 0 and tmp_y != 0:
                    x = tmp_x
                    y = tmp_y
                    decision = 1

                tmp_x, tmp_y = CheckQuadra(v, tmp_v)
                if tmp_x != 0 and tmp_y != 0:
                    x = tmp_x
                    y = tmp_y
                    decision = 1
                    break

        v_id = ""
        if gomoku.present == 0:
            v_id = gomoku.graph.black_path.pop()
            gomoku.graph.add_to_black_path(v_id)
        elif gomoku.present == 1:
            v_id = gomoku.graph.white_path.pop()
            gomoku.graph.add_to_white_path(v_id)
        v = gomoku.graph.get_vertex(v_id)
        rate_buffer = zeros((3, 2))
        for i in range(gomoku.block_num ** 2):
            tmp_x = int(i) % 19 + 1
            tmp_y = int((i + 1) / 19) + 1
            # To ensure credibility, we only take positions with denominators greater than 1000 as reference
            if gomoku.positions[tmp_y][tmp_x] == 0 and v.black_rate[i][1] > 1000:
                numerator = v.black_rate[i][0]
                denominator = v.black_rate[i][1]
                rate = 1
                if denominator > 0:
                    rate = numerator / denominator

                if rate > rate_buffer[0][0]:
                    rate_buffer[2][0] = rate_buffer[1][0]
                    rate_buffer[2][1] = rate_buffer[1][1]
                    rate_buffer[1][0] = rate_buffer[0][0]
                    rate_buffer[1][1] = rate_buffer[0][1]
                    rate_buffer[0][0] = rate
                    rate_buffer[0][1] = i + 1
                elif rate > rate_buffer[1][0]:
                    rate_buffer[2][0] = rate_buffer[1][0]
                    rate_buffer[2][1] = rate_buffer[1][1]
                    rate_buffer[1][0] = rate
                    rate_buffer[1][1] = i + 1
                elif rate > rate_buffer[2][0]:
                    rate_buffer[2][0] = rate
                    rate_buffer[2][1] = i + 1

                tmp = int(random.random() * 100) + 1
                if rate == rate_buffer[0][0] and tmp > 50:
                    rate_buffer[2][0] = rate_buffer[1][0]
                    rate_buffer[2][1] = rate_buffer[1][1]
                    rate_buffer[1][0] = rate_buffer[0][0]
                    rate_buffer[1][1] = rate_buffer[0][1]
                    rate_buffer[0][0] = rate
                    rate_buffer[0][1] = i + 1
                elif rate == rate_buffer[1][0] and tmp > 50:
                    rate_buffer[2][0] = rate_buffer[1][0]
                    rate_buffer[2][1] = rate_buffer[1][1]
                    rate_buffer[1][0] = rate
                    rate_buffer[1][1] = i + 1
                elif rate == rate_buffer[2][0] and tmp > 50:
                    rate_buffer[2][0] = rate
                    rate_buffer[2][1] = i + 1
        # If there are any positions meet the above rule, then random to choose one
        if rate_buffer[0][0] != 0:
            rate_0 = (
                100
                * rate_buffer[0][0]
                / (rate_buffer[0][0] + rate_buffer[1][0] + rate_buffer[2][0])
            )
            rate_1 = (
                100
                * rate_buffer[1][0]
                / (rate_buffer[0][0] + rate_buffer[1][0] + rate_buffer[2][0])
            )
            rate_2 = (
                100
                * rate_buffer[2][0]
                / (rate_buffer[0][0] + rate_buffer[1][0] + rate_buffer[2][0])
            )
            ran_num = int(random.random() * 200) + 1
            if ran_num < rate_0:
                x = int(rate_buffer[0][1] - 1) % 19 + 1
                y = int(rate_buffer[0][1] / 19) + 1
                decision = 1
            elif ran_num < rate_0 + rate_1:
                x = int(rate_buffer[1][1] - 1) % 19 + 1
                y = int(rate_buffer[1][1] / 19) + 1
                decision = 1
            elif ran_num < rate_0 + rate_1 + rate_2:
                x = int(rate_buffer[2][1] - 1) % 19 + 1
                y = int(rate_buffer[2][1] / 19) + 1
                decision = 1
            else:
                while not decision:
                    x = int(random.random() * 19) + 1
                    y = int(random.random() * 19) + 1
                    if gomoku.positions[y][x] == 0:
                        decision = 1

        cnt = 0
        while not decision:
            cnt += 1
            if cnt > 100:
                break
            tmp_id = v_id.split("_")
            tmp_x = int(tmp_id[0])
            tmp_y = int(tmp_id[1])
            ran_num = int(random.random() * 97) + 1
            # Take a random number to choose the position around current position
            # raid = 1 circle
            if ran_num <= 50:
                ctr = 0
                while not decision:
                    if ctr > 50:
                        break
                    ran_num = int(random.random() * 2 * 1 * 4) + 1
                    row = -1
                    col = -1
                    if ran_num > 1:
                        for i in range(1, ran_num):
                            if i < 2 * 1 + 1 or i > 2 * 1 * 4 - (2 * 1 + 1):
                                row += 1
                            else:
                                if ran_num % 2 == 1:
                                    row = -1
                                    col += 1
                                else:
                                    row = 1
                    if (
                        (tmp_y + col < 1)
                        or (tmp_y + col > 19)
                        or (tmp_x + row < 1)
                        or (tmp_x + row > 19)
                    ):
                        ctr += 1
                        continue
                    if gomoku.positions[tmp_y + col][tmp_x + row] == 0:
                        x = tmp_x + row
                        y = tmp_y + col
                        decision = 1
                    else:
                        ctr += 1
            # raid = 2 circle
            elif ran_num <= 75:
                ctr = 0
                while not decision:
                    if ctr > 50:
                        break
                    ran_num = int(random.random() * 2 * 2 * 4) + 1
                    row = -2
                    col = -2
                    if ran_num > 1:
                        for i in range(1, ran_num):
                            if i < 2 * 2 + 1 or i > 2 * 2 * 4 - (2 * 2 + 1):
                                row += 1
                            else:
                                if ran_num % 2 == 1:
                                    row = -1
                                    col += 1
                                else:
                                    row = 1
                    if (
                        (tmp_y + col < 1)
                        or (tmp_y + col > 19)
                        or (tmp_x + row < 1)
                        or (tmp_x + row > 19)
                    ):
                        ctr += 1
                        continue
                    if gomoku.positions[tmp_y + col][tmp_x + row] == 0:
                        x = tmp_x + row
                        y = tmp_y + col
                        decision = 1
                    else:
                        ctr += 1
            # raid = 3 circle
            elif ran_num <= 87:
                ctr = 0
                while not decision:
                    if ctr > 50:
                        break
                    ran_num = int(random.random() * 2 * 3 * 4) + 1
                    row = -3
                    col = -3
                    if ran_num > 1:
                        for i in range(1, ran_num):
                            if i < 2 * 3 + 1 or i > 2 * 3 * 4 - (2 * 3 + 1):
                                row += 1
                            else:
                                if ran_num % 2 == 1:
                                    row = -1
                                    col += 1
                                else:
                                    row = 1
                    if (
                        (tmp_y + col < 1)
                        or (tmp_y + col > 19)
                        or (tmp_x + row < 1)
                        or (tmp_x + row > 19)
                    ):
                        ctr += 1
                        continue
                    if gomoku.positions[tmp_y + col][tmp_x + row] == 0:
                        x = tmp_x + row
                        y = tmp_y + col
                        decision = 1
                    else:
                        ctr += 1
            # raid = 4 circle
            elif ran_num <= 93:
                ctr = 0
                while not decision:
                    if ctr > 50:
                        break
                    ran_num = int(random.random() * 2 * 4 * 4) + 1
                    row = -4
                    col = -4
                    if ran_num > 1:
                        for i in range(1, ran_num):
                            if i < 2 * 4 + 1 or i > 2 * 4 * 4 - (2 * 4 + 1):
                                row += 1
                            else:
                                if ran_num % 2 == 1:
                                    row = -1
                                    col += 1
                                else:
                                    row = 1
                    if (
                        (tmp_y + col < 1)
                        or (tmp_y + col > 19)
                        or (tmp_x + row < 1)
                        or (tmp_x + row > 19)
                    ):
                        ctr += 1
                        continue
                    if gomoku.positions[tmp_y + col][tmp_x + row] == 0:
                        x = tmp_x + row
                        y = tmp_y + col
                        decision = 1
                    else:
                        ctr += 1
            # raid = 5 circle
            elif ran_num <= 96:
                ctr = 0
                while not decision:
                    if ctr > 50:
                        break
                    ran_num = int(random.random() * 2 * 5 * 4) + 1
                    row = -5
                    col = -5
                    if ran_num > 1:
                        for i in range(1, ran_num):
                            if i < 2 * 5 + 1 or i > 2 * 5 * 4 - (2 * 5 + 1):
                                row += 1
                            else:
                                if ran_num % 2 == 1:
                                    row = -1
                                    col += 1
                                else:
                                    row = 1
                    if (
                        (tmp_y + col < 1)
                        or (tmp_y + col > 19)
                        or (tmp_x + row < 1)
                        or (tmp_x + row > 19)
                    ):
                        ctr += 1
                        continue
                    if gomoku.positions[tmp_y + col][tmp_x + row] == 0:
                        x = tmp_x + row
                        y = tmp_y + col
                        decision = 1
                    else:
                        ctr += 1
            # raid = 6 circle
            elif ran_num <= 97:
                ctr = 0
                while not decision:
                    if ctr > 50:
                        break
                    ran_num = int(random.random() * 2 * 6 * 4) + 1
                    row = -6
                    col = -6
                    if ran_num > 1:
                        for i in range(1, ran_num):
                            if i < 2 * 6 + 1 or i > 2 * 6 * 4 - (2 * 6 + 1):
                                row += 1
                            else:
                                if ran_num % 2 == 1:
                                    row = -1
                                    col += 1
                                else:
                                    row = 1
                    if (
                        (tmp_y + col < 1)
                        or (tmp_y + col > 19)
                        or (tmp_x + row < 1)
                        or (tmp_x + row > 19)
                    ):
                        ctr += 1
                        continue
                    if gomoku.positions[tmp_y + col][tmp_x + row] == 0:
                        x = tmp_x + row
                        y = tmp_y + col
                        decision = 1
                    else:
                        ctr += 1
        # The last choose to make sure have the next choose
        while not decision:
            x = int(random.random() * 19) + 1
            y = int(random.random() * 19) + 1
            if gomoku.positions[y][x] == 0:
                decision = 1
                break

    # print("x = " + str(x) + ", y = " + str(y))
    return [x, y]


def InitRate(gomoku):
    with open("black.txt", mode="r") as file:
        m = 1
        n = 1
        ctr = 0
        for line in file:
            v = gomoku.graph.get_vertex(str(n) + "_" + str(m))
            integers = line.split()
            for i in range(gomoku.block_num ** 2):
                v.black_rate[i][ctr] = int(integers[i])
            ctr = (ctr + 1) % 2
            if ctr == 0:
                n += 1
            if n == 20:
                m += 1
                n = 1
    with open("white.txt", mode="r") as file:
        m = 1
        n = 1
        ctr = 0
        for line in file:
            v = gomoku.graph.get_vertex(str(n) + "_" + str(m))
            integers = line.split()
            for i in range(gomoku.block_num ** 2):
                v.white_rate[i][ctr] = int(integers[i])
            ctr = (ctr + 1) % 2
            if ctr == 0:
                n += 1
            if n == 20:
                m += 1
                n = 1


def RefreshRate(gomoku, gg):
    if gomoku.player_mode == 2:
        v_child_id = gomoku.graph.black_path.pop()
        v_parent_id = gomoku.graph.black_path.pop()
        while not gomoku.graph.black_path:
            v_parent = gomoku.graph.get_vertex(v_parent_id)
            id = v_child_id.split("_")
            id_x = int(id[0])
            id_y = int(id[1])
            num = (id_y - 1) * 19 + id_x - 1
            v_parent.black_rate[num][1] += 1
            if gg == -1:
                v_parent.black_rate[num][0] += 1
            v_child_id = v_parent
            v_parent_id = gomoku.graph.black_path.pop()
    elif gomoku.player_mode == 3:
        # black
        # print("Black Path:")
        # print(gomoku.graph.black_path)
        v_child_id_b = gomoku.graph.black_path.pop()
        v_parent_id_b = gomoku.graph.black_path.pop()
        while gomoku.graph.black_path:
            v_parent_b = gomoku.graph.get_vertex(v_parent_id_b)
            id = v_child_id_b.split("_")
            id_x = int(id[0])
            id_y = int(id[1])
            num = (id_y - 1) * 19 + id_x - 1
            v_parent_b.black_rate[num][1] = v_parent_b.black_rate[num][1] + 1
            if gg == -1:  # black win, numerator +1
                v_parent_b.black_rate[num][0] = v_parent_b.black_rate[num][0] + 1
            v_child_id_b = v_parent_id_b
            v_parent_id_b = gomoku.graph.black_path.pop()
        # print(gomoku.graph.black_path)
        # white
        # print("White Path:")
        # print(gomoku.graph.white_path)
        v_child_id_w = gomoku.graph.white_path.pop()
        v_parent_id_w = gomoku.graph.white_path.pop()
        while gomoku.graph.white_path:
            v_parent_w = gomoku.graph.get_vertex(v_parent_id_w)
            id = v_child_id_w.split("_")
            id_x = int(id[0])
            id_y = int(id[1])
            num = (id_y - 1) * 19 + id_x - 1
            v_parent_w.white_rate[num][1] = v_parent_w.white_rate[num][1] + 1
            if gg == 1:  # white win, numerator +1
                v_parent_w.white_rate[num][0] = v_parent_w.white_rate[num][0] + 1
            v_child_id_w = v_parent_id_w
            v_parent_id_w = gomoku.graph.white_path.pop()
        # print(gomoku.graph.white_path)


def OutputRate(gomoku):
    if gomoku.player_mode == 2:
        with open("black.txt", mode="w") as file:
            for m in range(1, gomoku.block_num + 1):
                for n in range(1, gomoku.block_num + 1):
                    v = gomoku.graph.get_vertex(str(n) + "_" + str(m))
                    for i in range(gomoku.block_num * gomoku.block_num):
                        file.write(str(int(v.black_rate[i][0])) + " ")
                    file.write("\n")
                    for j in range(gomoku.block_num * gomoku.block_num):
                        file.write(str(int(v.black_rate[j][1])) + " ")
                    file.write("\n")
    if gomoku.player_mode == 3:
        with open("black.txt", mode="w") as file:
            for m in range(1, gomoku.block_num + 1):
                for n in range(1, gomoku.block_num + 1):
                    v = gomoku.graph.get_vertex(str(n) + "_" + str(m))
                    for i in range(gomoku.block_num * gomoku.block_num):
                        file.write(str(int(v.black_rate[i][0])) + " ")
                    file.write("\n")
                    for j in range(gomoku.block_num * gomoku.block_num):
                        file.write(str(int(v.black_rate[j][1])) + " ")
                    file.write("\n")
        with open("white.txt", mode="w") as file:
            for m in range(1, gomoku.block_num + 1):
                for n in range(1, gomoku.block_num + 1):
                    v = gomoku.graph.get_vertex(str(n) + "_" + str(m))
                    for i in range(gomoku.block_num * gomoku.block_num):
                        file.write(str(int(v.white_rate[i][0])) + " ")
                    file.write("\n")
                    for j in range(gomoku.block_num * gomoku.block_num):
                        file.write(str(int(v.white_rate[j][1])) + " ")
                    file.write("\n")


def CheckBothSide(v, m, n):
    x = 0
    y = 0
    if v.BorW == 0:
        if v.N.BorW != 0 and v.N.BorW != -1:
            if v.N.BorW == v.EN.BorW and v.N.link_N_S + v.EN.link_EN_WS >= 3:
                x = n
                y = m
            elif v.N.BorW == v.E.BorW and v.N.link_N_S + v.E.link_E_W >= 3:
                x = n
                y = m
            elif v.N.BorW == v.ES.BorW and v.N.link_N_S + v.ES.link_ES_WN >= 3:
                x = n
                y = m
            elif v.N.BorW == v.S.BorW and v.N.link_N_S + v.S.link_N_S >= 3:
                x = n
                y = m
            elif v.N.BorW == v.WS.BorW and v.N.link_N_S + v.WS.link_EN_WS >= 3:
                x = n
                y = m
            elif v.N.BorW == v.W.BorW and v.N.link_N_S + v.W.link_E_W >= 3:
                x = n
                y = m
            elif v.N.BorW == v.WN.BorW and v.N.link_N_S + v.WN.link_ES_WN >= 3:
                x = n
                y = m
        elif v.EN.BorW != 0 and v.EN.BorW != -1:
            if v.EN.BorW == v.E.BorW and v.EN.link_EN_WS + v.E.link_E_W >= 3:
                x = n
                y = m
            elif v.EN.BorW == v.ES.BorW and v.EN.link_EN_WS + v.ES.link_ES_WN >= 3:
                x = n
                y = m
            elif v.EN.BorW == v.S.BorW and v.EN.link_EN_WS + v.S.link_N_S >= 3:
                x = n
                y = m
            elif v.EN.BorW == v.WS.BorW and v.EN.link_EN_WS + v.WS.link_EN_WS >= 3:
                x = n
                y = m
            elif v.EN.BorW == v.W.BorW and v.EN.link_EN_WS + v.W.link_E_W >= 3:
                x = n
                y = m
            elif v.EN.BorW == v.WN.BorW and v.EN.link_EN_WS + v.WN.link_ES_WN >= 3:
                x = n
                y = m
        elif v.E.BorW != 0 and v.E.BorW != -1:
            if v.E.BorW == v.ES.BorW and v.E.link_E_W + v.ES.link_ES_WN >= 3:
                x = n
                y = m
            elif v.E.BorW == v.S.BorW and v.E.link_E_W + v.S.link_N_S >= 3:
                x = n
                y = m
            elif v.E.BorW == v.WS.BorW and v.E.link_E_W + v.WS.link_EN_WS >= 3:
                x = n
                y = m
            elif v.E.BorW == v.W.BorW and v.E.link_E_W + v.W.link_E_W >= 3:
                x = n
                y = m
            elif v.E.BorW == v.WN.BorW and v.E.link_E_W + v.WN.link_ES_WN >= 3:
                x = n
                y = m
        elif v.ES.BorW != 0 and v.ES.BorW != -1:
            if v.ES.BorW == v.S.BorW and v.ES.link_ES_WN + v.S.link_N_S >= 3:
                x = n
                y = m
            elif v.ES.BorW == v.WS.BorW and v.ES.link_ES_WN + v.WS.link_EN_WS >= 3:
                x = n
                y = m
            elif v.ES.BorW == v.W.BorW and v.ES.link_ES_WN + v.W.link_E_W >= 3:
                x = n
                y = m
            elif v.ES.BorW == v.WN.BorW and v.ES.link_ES_WN + v.WN.link_ES_WN >= 3:
                x = n
                y = m
        elif v.S.BorW != 0 and v.S.BorW != -1:
            if v.S.BorW == v.WS.BorW and v.S.link_N_S + v.WS.link_EN_WS >= 3:
                x = n
                y = m
            elif v.S.BorW == v.W.BorW and v.S.link_N_S + v.W.link_E_W >= 3:
                x = n
                y = m
            elif v.S.BorW == v.WN.BorW and v.S.link_N_S + v.WN.link_ES_WN >= 3:
                x = n
                y = m
        elif v.WS.BorW != 0 and v.WS.BorW != -1:
            if v.WS.BorW == v.W.BorW and v.WS.link_EN_WS + v.W.link_E_W >= 3:
                x = n
                y = m
            elif v.WS.BorW == v.WN.BorW and v.WS.link_EN_WS + v.WN.link_ES_WN >= 3:
                x = n
                y = m
        elif v.W.BorW != 0 and v.W.BorW != -1:
            if v.W.BorW == v.WN.BorW and v.W.link_E_W + v.WN.link_ES_WN >= 3:
                x = n
                y = m

    return [x, y]


def CheckQuadra(v, tmp_v):
    x = 0
    y = 0
    if tmp_v.link_N_S >= 4:
        while tmp_v.N.BorW == v.BorW:
            tmp_v = tmp_v.N
        if tmp_v.N.BorW == 0:
            tmp_id = tmp_v.N.id.split("_")
            x = int(tmp_id[0])
            y = int(tmp_id[1])
            # decision = 1
        else:
            while tmp_v.S.BorW == v.BorW:
                tmp_v = tmp_v.S
            if tmp_v.S.BorW == 0:
                tmp_id = tmp_v.S.id.split("_")
                x = int(tmp_id[0])
                y = int(tmp_id[1])
                # decision = 1
    elif tmp_v.link_EN_WS >= 4:
        while tmp_v.EN.BorW == v.BorW:
            tmp_v = tmp_v.EN
        if tmp_v.EN.BorW == 0:
            tmp_id = tmp_v.EN.id.split("_")
            x = int(tmp_id[0])
            y = int(tmp_id[1])
            # decision = 1
        else:
            while tmp_v.WS.BorW == v.BorW:
                tmp_v = tmp_v.WS
            if tmp_v.WS.BorW == 0:
                tmp_id = tmp_v.WS.id.split("_")
                x = int(tmp_id[0])
                y = int(tmp_id[1])
                # decision = 1
    elif tmp_v.link_E_W >= 4:
        while tmp_v.E.BorW == v.BorW:
            tmp_v = tmp_v.E
        if tmp_v.E.BorW == 0:
            tmp_id = tmp_v.E.id.split("_")
            x = int(tmp_id[0])
            y = int(tmp_id[1])
            # decision = 1
        else:
            while tmp_v.W.BorW == v.BorW:
                tmp_v = tmp_v.W
            if tmp_v.W.BorW == 0:
                tmp_id = tmp_v.W.id.split("_")
                x = int(tmp_id[0])
                y = int(tmp_id[1])
                # decision = 1
    elif tmp_v.link_ES_WN >= 4:
        while tmp_v.ES.BorW == v.BorW:
            tmp_v = tmp_v.ES
        if tmp_v.ES.BorW == 0:
            tmp_id = tmp_v.ES.id.split("_")
            x = int(tmp_id[0])
            y = int(tmp_id[1])
            # decision = 1
        else:
            while tmp_v.WN.BorW == v.BorW:
                tmp_v = tmp_v.WN
            if tmp_v.WN.BorW == 0:
                tmp_id = tmp_v.WN.id.split("_")
                x = int(tmp_id[0])
                y = int(tmp_id[1])
                # decision = 1
    return [x, y]


def CheckTriple_OneLive(v, tmp_v, gomoku):
    x = 0
    y = 0
    if v.BorW == gomoku.present + 1:
        # if 1 == 1:
        buffer = zeros(5)
        if tmp_v.link_N_S >= 3:
            buffer[0] = 1
            buffer[4] = 1
        if tmp_v.link_EN_WS >= 3:
            buffer[1] = 1
            buffer[4] = 1
        if tmp_v.link_E_W >= 3:
            buffer[2] = 1
            buffer[4] = 1
        if tmp_v.link_ES_WN >= 3:
            buffer[3] = 1
            buffer[4] = 1

        if buffer[4] == 1:  # There are some cases are satisfied
            # print("hey")
            ran = int(random.random() * 4)
            while buffer[ran] == 0:
                ran = int(random.random() * 4)

            if ran == 0:
                tmp_ran = int(random.random() * 2)  # random to choose go N or S
                if tmp_ran == 0:
                    while tmp_v.N.BorW == v.BorW:
                        tmp_v = tmp_v.N
                    if tmp_v.N.BorW == 0:
                        tmp_id = tmp_v.N.id.split("_")
                        x = int(tmp_id[0])
                        y = int(tmp_id[1])
                    else:
                        while tmp_v.S.BorW == v.BorW:
                            tmp_v = tmp_v.S
                        if tmp_v.S.BorW == 0:
                            tmp_id = tmp_v.S.id.split("_")
                            x = int(tmp_id[0])
                            y = int(tmp_id[1])
                            # decision = 1
                else:
                    while tmp_v.S.BorW == v.BorW:
                        tmp_v = tmp_v.S
                    if tmp_v.S.BorW == 0:
                        tmp_id = tmp_v.S.id.split("_")
                        x = int(tmp_id[0])
                        y = int(tmp_id[1])
                        # decision = 1
                    else:
                        while tmp_v.N.BorW == v.BorW:
                            tmp_v = tmp_v.N
                        if tmp_v.N.BorW == 0:
                            tmp_id = tmp_v.N.id.split("_")
                            x = int(tmp_id[0])
                            y = int(tmp_id[1])
                            # decision = 1

            elif ran == 1:
                tmp_ran = int(random.random() * 2)  # random to choose go EN or WS
                if tmp_ran == 0:
                    while tmp_v.EN.BorW == v.BorW:
                        tmp_v = tmp_v.EN
                    if tmp_v.EN.BorW == 0:
                        tmp_id = tmp_v.EN.id.split("_")
                        x = int(tmp_id[0])
                        y = int(tmp_id[1])
                    else:
                        while tmp_v.WS.BorW == v.BorW:
                            tmp_v = tmp_v.WS
                        if tmp_v.WS.BorW == 0:
                            tmp_id = tmp_v.WS.id.split("_")
                            x = int(tmp_id[0])
                            y = int(tmp_id[1])
                else:
                    while tmp_v.WS.BorW == v.BorW:
                        tmp_v = tmp_v.WS
                    if tmp_v.WS.BorW == 0:
                        tmp_id = tmp_v.WS.id.split("_")
                        x = int(tmp_id[0])
                        y = int(tmp_id[1])
                    else:
                        while tmp_v.EN.BorW == v.BorW:
                            tmp_v = tmp_v.EN
                        if tmp_v.EN.BorW == 0:
                            tmp_id = tmp_v.EN.id.split("_")
                            x = int(tmp_id[0])
                            y = int(tmp_id[1])

            elif ran == 2:
                tmp_ran = int(random.random() * 2)  # random to choose go E or W
                if tmp_ran == 0:
                    while tmp_v.E.BorW == v.BorW:
                        tmp_v = tmp_v.E
                    if tmp_v.E.BorW == 0:
                        tmp_id = tmp_v.E.id.split("_")
                        x = int(tmp_id[0])
                        y = int(tmp_id[1])
                    else:
                        while tmp_v.W.BorW == v.BorW:
                            tmp_v = tmp_v.W
                        if tmp_v.W.BorW == 0:
                            tmp_id = tmp_v.W.id.split("_")
                            x = int(tmp_id[0])
                            y = int(tmp_id[1])
                else:
                    while tmp_v.W.BorW == v.BorW:
                        tmp_v = tmp_v.W
                    if tmp_v.W.BorW == 0:
                        tmp_id = tmp_v.W.id.split("_")
                        x = int(tmp_id[0])
                        y = int(tmp_id[1])
                    else:
                        while tmp_v.E.BorW == v.BorW:
                            tmp_v = tmp_v.E
                        if tmp_v.E.BorW == 0:
                            tmp_id = tmp_v.E.id.split("_")
                            x = int(tmp_id[0])
                            y = int(tmp_id[1])

            elif ran == 3:
                tmp_ran = int(random.random() * 2)  # random to choose go ES or WN
                if tmp_ran == 0:
                    while tmp_v.ES.BorW == v.BorW:
                        tmp_v = tmp_v.ES
                    if tmp_v.ES.BorW == 0:
                        tmp_id = tmp_v.ES.id.split("_")
                        x = int(tmp_id[0])
                        y = int(tmp_id[1])
                    else:
                        while tmp_v.WN.BorW == v.BorW:
                            tmp_v = tmp_v.WN
                        if tmp_v.WN.BorW == 0:
                            tmp_id = tmp_v.WN.id.split("_")
                            x = int(tmp_id[0])
                            y = int(tmp_id[1])
                else:
                    while tmp_v.WN.BorW == v.BorW:
                        tmp_v = tmp_v.WN
                    if tmp_v.WN.BorW == 0:
                        tmp_id = tmp_v.WN.id.split("_")
                        x = int(tmp_id[0])
                        y = int(tmp_id[1])
                    else:
                        while tmp_v.ES.BorW == v.BorW:
                            tmp_v = tmp_v.ES
                        if tmp_v.ES.BorW == 0:
                            tmp_id = tmp_v.ES.id.split("_")
                            x = int(tmp_id[0])
                            y = int(tmp_id[1])
    return [x, y]


def CheckTriple_TwoLive(v, tmp_v, gomoku):
    reverse_present = zeros(3)
    reverse_present[2] = 1
    reverse_present[1] = 2
    x = 0
    y = 0
    if v.BorW == reverse_present[gomoku.present + 1]:
        # print("here2")
        tmp_tmp_v = tmp_v

        if tmp_v.link_N_S >= 3:
            # random to choose go N or S
            tmp_ran = int(random.random() * 2)
            tmp_v = tmp_tmp_v
            if tmp_ran == 0:
                while tmp_v.N.BorW == v.BorW:
                    tmp_v = tmp_v.N
                if tmp_v.N.BorW == 0:
                    while tmp_v.S.BorW == v.BorW:
                        tmp_v = tmp_v.S
                    if tmp_v.S.BorW == 0:
                        tmp_id = tmp_v.S.id.split("_")
                        x = int(tmp_id[0])
                        y = int(tmp_id[1])
            else:
                while tmp_v.S.BorW == v.BorW:
                    tmp_v = tmp_v.S
                if tmp_v.S.BorW == 0:
                    while tmp_v.N.BorW == v.BorW:
                        tmp_v = tmp_v.N
                    if tmp_v.N.BorW == 0:
                        tmp_id = tmp_v.N.id.split("_")
                        x = int(tmp_id[0])
                        y = int(tmp_id[1])
        if tmp_v.link_EN_WS >= 3:
            # random to choose go EN or WS
            tmp_ran = int(random.random() * 2)
            tmp_v = tmp_tmp_v
            if tmp_ran == 0:
                while tmp_v.EN.BorW == v.BorW:
                    tmp_v = tmp_v.EN
                if tmp_v.EN.BorW == 0:
                    while tmp_v.WS.BorW == v.BorW:
                        tmp_v = tmp_v.WS
                    if tmp_v.WS.BorW == 0:
                        tmp_id = tmp_v.WS.id.split("_")
                        x = int(tmp_id[0])
                        y = int(tmp_id[1])
            else:
                while tmp_v.WS.BorW == v.BorW:
                    tmp_v = tmp_v.WS
                if tmp_v.WS.BorW == 0:
                    while tmp_v.EN.BorW == v.BorW:
                        tmp_v = tmp_v.EN
                    if tmp_v.EN.BorW == 0:
                        tmp_id = tmp_v.EN.id.split("_")
                        x = int(tmp_id[0])
                        y = int(tmp_id[1])
        if tmp_v.link_E_W >= 3:
            # random to choose go E or W
            tmp_ran = int(random.random() * 2)
            tmp_v = tmp_tmp_v
            if tmp_ran == 0:
                while tmp_v.E.BorW == v.BorW:
                    tmp_v = tmp_v.E
                if tmp_v.E.BorW == 0:
                    while tmp_v.W.BorW == v.BorW:
                        tmp_v = tmp_v.W
                    if tmp_v.W.BorW == 0:
                        tmp_id = tmp_v.W.id.split("_")
                        x = int(tmp_id[0])
                        y = int(tmp_id[1])
            else:
                while tmp_v.W.BorW == v.BorW:
                    tmp_v = tmp_v.W
                if tmp_v.W.BorW == 0:
                    while tmp_v.E.BorW == v.BorW:
                        tmp_v = tmp_v.E
                    if tmp_v.E.BorW == 0:
                        tmp_id = tmp_v.E.id.split("_")
                        x = int(tmp_id[0])
                        y = int(tmp_id[1])
        if tmp_v.link_ES_WN >= 3:
            # random to choose go ES or WN
            tmp_ran = int(random.random() * 2)
            tmp_v = tmp_tmp_v
            if tmp_ran == 0:
                while tmp_v.ES.BorW == v.BorW:
                    tmp_v = tmp_v.ES
                if tmp_v.ES.BorW == 0:
                    while tmp_v.WN.BorW == v.BorW:
                        tmp_v = tmp_v.WN
                    if tmp_v.WN.BorW == 0:
                        tmp_id = tmp_v.WN.id.split("_")
                        x = int(tmp_id[0])
                        y = int(tmp_id[1])
            else:
                while tmp_v.WN.BorW == v.BorW:
                    tmp_v = tmp_v.WN
                if tmp_v.WN.BorW == 0:
                    while tmp_v.ES.BorW == v.BorW:
                        tmp_v = tmp_v.ES
                    if tmp_v.ES.BorW == 0:
                        tmp_id = tmp_v.ES.id.split("_")
                        x = int(tmp_id[0])
                        y = int(tmp_id[1])

    return [x, y]
