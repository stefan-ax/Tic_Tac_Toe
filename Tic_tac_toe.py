from numpy import zeros, ndenumerate, count_nonzero, trace
from sys import exit

class Game():
    '''BASE GAME APP
    Call run() method to start the game.
    Dependecies: numpy,sys.'''
    
    __author__ = 'Stefan Obada'
    __title__ = 'Basic TIC-TAC TOE'
    __date__ = '01.06.2019'
    
    def __init__(self):
        self.dimension = 3
        self.turn = 1
        self.win = 0
        self.score = zeros((1,2), dtype = 'int')
        self.table = zeros((self.dimension, self.dimension), dtype = 'int')
        
    def run(self):
        self.menu_start()
        while(True):
            self.draw_grid()
            self.get_key_move()
            if(self.check_win() == 0):
                pass
            else:
                self.menu_exit(self.check_win())
                break
                
        
    def menu_start(self):
        print('Player 1 starts. Place X using numpad.')
    
    def menu_exit(self, winner):
        self.draw_grid()
        if(winner == 1):
            print('Player 1 wins.')
        elif(winner == 2):
            print('Player 2 wins.')
        else:
            print('DRAW.')
            
        print('Exiting game...')
    
    def check_win(self):
        '''
        0 if not
        1 if Player1, 2 if Player2
        3 if draw
        '''
        #Check on line if WIN
        for line in self.table:
            if sum(line) == 3:
                return 1
            elif sum(line) == -3:
                return 2
        #Check on column if WIN
        for line in self.table.T:
            if sum(line) == 3:
                return 1
            elif sum(line) == -3:
                return 2
            
        #Check on diagonal
            if trace(self.table, axis1=0, axis2=1) == 3 or trace(self.table, axis1=1, axis2=0) == 3:
                return 1
            elif trace(self.table, axis1=0, axis2=1) == -3 or trace(self.table, axis1=1, axis2=0) == -3:
                return 2
            
        #Check if draw
        if (count_nonzero(self.table) == 9):
            return 3
        
        #Any other case, return NOT
        return 0
    
    def get_key_move(self):
        player = self.turn % 2
        input_numbers = [7, 8, 9, 4, 5, 6, 1, 2, 3]
        positions = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        moves = {number : position for number, position in zip(input_numbers, positions)}
        try:
            key = int(input(''))
        except:
            key = 0
            pass
        if(key not in input_numbers):
            print('Input a valid number [1-0]')
            self.get_key_move()
        elif(self.table[moves[key]] != 0):
            print('Impossible')
            self.get_key_move()
        else:
            self.table[moves[key]] = 1 if player == 1 else -1
            self.turn += 1
        
    def draw_grid(self):
        print('''          
          ---------
        | {} | {} | {} |
          ---------
        | {} | {} | {} |
          ---------
        | {} | {} | {} |
           ---------    '''.format(*['X' if x == 1 else 'O' if x == -1 else ' ' for x in self.table.flatten()]))
        
if __name__ == '__main__':
    Game().run()