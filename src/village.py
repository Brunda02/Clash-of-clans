import numpy as np
import random
import colorama
from colorama import Fore, Back, Style
from src.config import *
colorama.init()

class village:
    def __init__(self, player, rows, cols, frames):
       self._rows = rows
       self._cols = cols*frames
       self._grid = ([[Back.BLACK + Fore.BLACK + ' ' for col in range(self._cols)]
                       for row in range(self._rows)])
       self._char = ([[' ' for col in range(self._cols)]
                       for row in range(self._rows)]) 
       self._Spawning_points =  [[23, 56],[15,78],[2,6]]    

       for i in range(0,3):
            temp= self._Spawning_points[i][0]
            temp1= self._Spawning_points[i][1]
            self._grid[temp][temp1]= Fore.MAGENTA + Back.BLUE + 'S'
            # self._char[temp][temp1]= 'S'

       for val in range(self._cols):
        self._grid[0][val] = Fore.WHITE + 'X'
        self._grid[self._rows - 1][val] = Fore.GREEN + 'X' 
        self._char[0][val] =  'X'
        self._char[self._rows - 1][val] =  'X' 

    def object(self, object):
        for x in range(0, object._height):
            for y in range(0, object._width):
                self._char[object._pos_x - x][object._pos_y + y] = object._char[object._height - 1 - x][y]
                self._grid[object._pos_x - x][object._pos_y + y] = object._color + object._char[object._height - 1 - x][y]

    def objectc(self, object):
        for x in range(0, object._height):
            for y in range(0, object._width):
                self._char[object._pos_x - x][object._pos_y + y] = object._char[object._height - 1 - x][y]
                self._grid[object._pos_x - x][object._pos_y + y] = object._color + object._char[object._height - 1 - x][y]

    def clear(self, object):
        for x in range(0, object._height):
            for y in range(0, object._width):
                self._char[object._pos_x - x][object._pos_y + y] = ' '
                self._grid[object._pos_x - x][object._pos_y + y] = Back.BLACK + Fore.BLACK + ' '  

    def check_present(self,object,val):
        ret=1
        if(val == 'W' or val == 'w'):
            if(self._char[object._pos_x-1][object._pos_y]!=' ' ):
            #    print(self._char[object._pos_x-object._height][object._pos_y+1]) 
               ret=0
        if(val == 'S' or val == 's'):
            if(self._char[object._pos_x+1][object._pos_y]!=' '  ):
            #    print(self._char[object._pos_x+1][object._pos_y], self._char[object._pos_x+1][object._pos_y+2])
               ret=0
        if(val == 'A' or val == 'a'):
            if(self._char[object._pos_x][object._pos_y-1]!=' ' ):
            #    print(self._char[object._pos_x][object._pos_y-1], self._char[object._pos_x-1][object._pos_y-1],self._char[object._pos_x-2][object._pos_y]) 
               ret=0
        if(val == 'D' or val == 'd'):  
            if(self._char[object._pos_x][object._pos_y+1]!=' '):
            #    print(self._char[object._pos_x][object._pos_y+3], self._char[object._pos_x-1][object._pos_y+3]) 
               ret=0
        # print(ret)
        return ret

    def print_spawn(self):
        for i in range(0,3):
            temp= self._Spawning_points[i][0]
            temp1= self._Spawning_points[i][1]
            self._grid[temp][temp1]= Fore.MAGENTA + Back.BLUE + 'S'

    
    # def spell(self,object,val):
    #   if(val=='R'):
    #     if(object._destroy==0 ):
    #         object._speed=0.5
    #         object._damage=(object.damage*2)
    #   if(val=='H'):
    #     if(object._destroy==0):
    #         object._hitpoints = ((object._hitpoints)*150)/100
    #         if(object._hitpoints>100):
    #             object._hitpoints = 100                                                             

    def get_grid(self,i,j):
        return self._grid[i][j]                     

    def change_grid(self,i,j,val):
        self._grid[i][j]=val

    def get_char(self,i,j):
        return self._char[i][j]                     

    def change_char(self,i,j,val):
        self._char[i][j]=val 

    def get_rows(self):
        return self._rows

    def printvillage(self):
        for i in range(self._rows):
            for j in range(self._cols):
                print(self._char[i][j])

    def get_spawn(self):
        # xi=random.randint(0,2)
        return self._Spawning_points                 