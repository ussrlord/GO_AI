# -*- coding: utf-8 -*-
"""
@author: Junxiao Song
"""

from AlphaZeroModule.constants import *
from original.graphics import *
import numpy as np

class GoBoard(object):
    """board for the game"""

    #初始化棋盘
    def __init__(self, **kwargs):
        self.width = int(kwargs.get('width', CONSTANT_GO_BOARD_WIDTH))
        self.height = int(kwargs.get('height', CONSTANT_GO_BOARD_HEIGHT))

        self.gw = GraphWin(
                            'AI Go Test',
                           GRID_WIDTH* (CONSTANT_GO_BOARD_HEIGHT+2), GRID_WIDTH* (CONSTANT_GO_BOARD_HEIGHT+2)
                           )

        self.states = {}
        # need how many pieces in a row to win
        self.n_in_row = int(kwargs.get('n_in_row', 5))
        self.players = [1, 2]  # player1 and player2

    #校验和初始化棋盘
    def init_board(self, start_player: object = 0) -> object:
        if self.width < self.n_in_row or self.height < self.n_in_row:
            raise Exception('board width and height can not be '
                            'less than {}'.format(self.n_in_row))
        self.current_player = self.players[start_player]  # start player
        # keep available moves in a list
        self.availables = list(range(self.width * self.height))
        self.states = {}
        self.last_move = -1
        self.draw_board()

    #绘制棋盘格
    def draw_board(self):
        self.gw.setBackground('#554E44')  # 054E9F
        for j in range(1, self.width + 2):
            l = Line(Point( GRID_WIDTH*j, GRID_WIDTH), Point(GRID_WIDTH*j, GRID_WIDTH * (self.width+1)))
            l.draw(self.gw)
        for j in range(1, self.width + 2):
            l = Line(Point( GRID_WIDTH, GRID_WIDTH*j), Point(GRID_WIDTH * (self.width+1), GRID_WIDTH*j))
            l.draw(self.gw)

    #校验落子坐标
    def check_location_to_move(self, location):
        print("location:"+ str(location))
        if len(location) != 2:
            print("location length error")
            return False
        if location[0] not in range(self.width) or location[0] not in range(self.height) :
            return False
        return True

    #返回用户坐标
    def get_human_player_pos(self):
        check_flg = False
        while check_flg==False:
            tmp_loc = self.gw.getMouse()
            tmp_x = round((tmp_loc.getX()) / GRID_WIDTH)
            tmp_y = round((tmp_loc.getY()) / GRID_WIDTH)
            location = (tmp_x, tmp_y)
            check_flg = self.check_location_to_move(location)

        return (tmp_x-1,tmp_y-1)


    def draw_piece(self, location, color='black'):
        piece = Circle(Point(GRID_WIDTH * (location[0]+1), GRID_WIDTH * (location[1]+1)), 16)
        piece.setFill(color)
        piece.draw(self.gw)
    '''
    
    def current_state(self):
        """return the board state from the perspective of the current player.
        state shape: 4*width*height
        """

        square_state = np.zeros((4, self.width, self.height))
        if self.states:
            moves, players = np.array(list(zip(*self.states.items())))
            move_curr = moves[players == self.current_player]
            move_oppo = moves[players != self.current_player]
            square_state[0][move_curr // self.width,
                            move_curr % self.height] = 1.0
            square_state[1][move_oppo // self.width,
                            move_oppo % self.height] = 1.0
            # indicate the last move location
            square_state[2][self.last_move // self.width,
                            self.last_move % self.height] = 1.0
        if len(self.states) % 2 == 0:
            square_state[3][:, :] = 1.0  # indicate the colour to play
        return square_state[:, ::-1, :]

    def do_move(self, move):
        self.states[move] = self.current_player
        self.availables.remove(move)
        self.current_player = (
            self.players[0] if self.current_player == self.players[1]
            else self.players[1]
        )
        self.last_move = move

    def has_a_winner(self):
        width = self.width
        height = self.height
        states = self.states
        n = self.n_in_row

        moved = list(set(range(width * height)) - set(self.availables))
        if len(moved) < self.n_in_row *2-1:
            return False, -1

        for m in moved:
            h = m // width
            w = m % width
            player = states[m]

            if (w in range(width - n + 1) and
                    len(set(states.get(i, -1) for i in range(m, m + n))) == 1):
                return True, player

            if (h in range(height - n + 1) and
                    len(set(states.get(i, -1) for i in range(m, m + n * width, width))) == 1):
                return True, player

            if (w in range(width - n + 1) and h in range(height - n + 1) and
                    len(set(states.get(i, -1) for i in range(m, m + n * (width + 1), width + 1))) == 1):
                return True, player

            if (w in range(n - 1, width) and h in range(height - n + 1) and
                    len(set(states.get(i, -1) for i in range(m, m + n * (width - 1), width - 1))) == 1):
                return True, player

        return False, -1

    # 结束当前游戏
    def game_end(self):
        """Check whether the game is ended or not"""
        win, winner = self.has_a_winner()
        if win:
            return True, winner
        elif not len(self.availables):
            return True, -1
        return False, -1

    #获取当前玩家
    def get_current_player(self):
        return self.current_player

    '''
