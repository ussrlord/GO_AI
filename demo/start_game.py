# AI五子nal.graphics import *

from demo.classes.GoBoard import GoBoard

# 画棋盘
def initialization():
    # 新建对象
    go_board = GoBoard()
    # 初始化检查
    go_board.init_board()

    return go_board


def start_game(go_board):
    # 游戏是否结束flag
    in_game_flg = True
    # 统计步数，用于判断现在轮到谁落子，奇数为AI方，偶数为我方
    step_count = 0

    while in_game_flg:
        pos = go_board.get_human_player_pos()
        if step_count % 2==0:
            print("Black Move!")
            go_board.draw_piece(pos, 'black')
        else:
            print("White Move!")
            go_board.draw_piece(pos, 'white')
        step_count += 1

# 主程序
def run():
    # 初始化
    go_board = initialization()
    start_game(go_board)

'''
    for j in range(COLUMN+1):
        for i in range(ROW+1):
            all_list.append((i, j))
    # 游戏是否结束flag
    inGameFlg = True
    # 统计步数，用于判断现在轮到谁落子，奇数为AI方，偶数为我方
    step_count = 0
    while inGameFlg:
        if step_count % 2:
            p_ai = AI()
            if p_ai in aime_list:
                message = Text(Point(300, 300), 'AI gets a wrong next step.')
                message.draw(gw)
                inGameFlg = False
            ai_list.append(p_ai)
            aime_list.append(p_ai)
            piece = Circle(Point(GRID_WIDTH * p_ai[0], GRID_WIDTH * p_ai[1]), 16)
            piece.setFill('white')
            piece.draw(gw)
            if is_game_over(ai_list):
                message = Text(Point(100, 100), 'AI white win.')
                message.draw(gw)
                inGameFlg = False
            step_count += 1
        else:
            p_me = gw.getMouse()
            x = round((p_me.getX()) / GRID_WIDTH)
            y = round((p_me.getY()) / GRID_WIDTH)
            if not ((x, y) in aime_list):
                me_list.append((x, y))
                aime_list.append((x, y))
                piece = Circle(Point(GRID_WIDTH * x, GRID_WIDTH * y), 16)
                piece.setFill('black')
                piece.draw(gw)
                if is_game_over(me_list):
                    message = Text(Point(100, 100), 'You black win.')
                    message.draw(gw)
                    inGameFlg = False
                step_count += 1
    # 游戏结束后的处理
    message = Text(Point(300, 300), 'Click anywhere to quit.')
    message.draw(gw)
    gw.getMouse()
    gw.close()
'''

if __name__ == '__main__':
    run()