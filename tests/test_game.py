import pytest
from src.tictactoe import TicTacToe

obj_empty = TicTacToe()

obj_notEmpty = TicTacToe()
obj_notEmpty.board[0] = 'X'
obj_notEmpty.board[5] = 'O'

obj_winner = TicTacToe()
obj_winner.board[0] = 'X'
obj_winner.board[1] = 'X'
obj_winner.board[2] = 'X'
obj_winner.current_winner = 'X'


# with empty object
def test_make_board():
    assert obj_empty.make_board() == [' ',' ',' ',' ',' ',' ',' ',' ',' '] 

@pytest.mark.parametrize("statement, game", [(True, obj_empty), (True, obj_notEmpty)])
def test_empty_squares(statement, game):
    assert game.empty_squares() == statement

@pytest.mark.parametrize("num, game", [(9, obj_empty), (7, obj_notEmpty)])
def test_num_empty_squares(num, game):
    assert game.num_empty_squares() == num

@pytest.mark.parametrize("num_list, game", [([0,1,2,3,4,5,6,7,8], obj_empty), ([1,2,3,4,6,7,8], obj_notEmpty), ([3,4,5,6,7,8], obj_winner)])
def test_available_moves(num_list, game):
    assert game.available_moves() == num_list

@pytest.mark.parametrize("game, index, player, statement", [(obj_empty, 5, 'O', True), (obj_notEmpty, 3, 'X', True), (obj_notEmpty, 5, 'O', False)])
def test_make_move(game, index, player, statement):
    assert game.make_move(index, player) == statement

@pytest.mark.parametrize("statement, game, index, player", [(True, obj_winner, 2, 'X'), (False, obj_winner, 2, 'O'), (False, obj_winner, 5, 'X')])
def test_winner(statement, game, index, player):
    assert game.winner(index, player) == statement 

"""


import pytest
from src.tictactoe import TicTacToe, play

obj_empty = TicTacToe()

obj_notEmpty = TicTacToe()
obj_notEmpty.board[0] = 'X'
obj_notEmpty.board[5] = 'O'

obj_winner = TicTacToe()
obj_winner.board[0] = 'X'
obj_winner.board[1] = 'X'
obj_winner.board[2] = 'X'
obj_winner.current_winner = 'X'


# with empty object
# board creating test
def test_make_board():
    assert [' ',' ',' ',' ',' ',' ',' ',' ',' '] == obj_empty.make_board()

# is board blank?
def test_empty_squares():
    assert True == obj_empty.empty_squares()
    assert True == obj_notEmpty.empty_squares()

# how many blanks?
def test_num_empty_squares():
    assert 9 == obj_empty.num_empty_squares()
    assert 7 == obj_notEmpty.num_empty_squares()

# blank indexes
def test_available_moves():
    assert [0,1,2,3,4,5,6,7,8] == obj_empty.available_moves()
    assert [1,2,3,4,6,7,8] == obj_notEmpty.available_moves()
    assert [3,4,5,6,7,8] == obj_winner.available_moves()

# tests parameters
@pytest.mark.parametrize("game, index, player", [(obj_empty, 5, 'O'), (obj_notEmpty, 3, 'X')])
def test_make_move(game, index, player):
    assert True == game.make_move(index, player)


# test last move for winner
def test_winner():
    assert True == obj_winner.winner(2, 'X')
    assert False == obj_winner.winner(2, 'O')
    assert False == obj_winner.winner(5, 'X')
    
    """
    