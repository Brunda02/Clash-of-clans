import colorama
import numpy as np
from colorama import Fore, Back, Style
colorama.init()
import time

#Inheritance-troops, kings from same class

class Character:
    def __init__(self, x, y):
        self._pos_x = x
        self._pos_y = y
        self._hitpoints = 100
        

class PersonKing(Character):
    def __init__(self, x, y):
        self._height = 1
        self._width = 1
        self._char = [['K']]
        self._color = Fore.CYAN + Back.YELLOW
        self._change = 4
        self._damage = 10
        self._attack=0
        self._speed=1
        self._ragespell = 0
        self._healspell = 0
        self._destroy=0
        
        super().__init__(x, y)

    def check_boun(self,limit_x,limit_y):
        if (self._pos_y + self._width - 1 > limit_y) :
            self._pos_y = limit_y - self._width + 1
        if self._pos_y < 0:
            self._pos_y = 0
        if self._pos_x < self._height:
            self._pos_x = self._height 
        if self._pos_x >= limit_x:
            self._pos_x = limit_x-1

    def get_attack(self):
        return self._attack

    def change_attack(self, val):
        self._attack = val           

    def get_posx(self):
        return self._pos_x

    def get_posy(self):
        return self._pos_y             

    def change_life(self,val):
        self._life+=val  

    def get_life(self):
        return self._life        

    def change_posx(self, val):
        self._pos_x += val

    def change_posy(self, val):
        self._pos_y += val

    def put_posx(self, val):
        self._pos_x = val

    def put_posy(self, val):
        self._pos_y = val

    def get_height(self):
        return self._height

    def get_width(self):
        return self._width        

    def get_char(self,i,j):
        return self._char[i][j]

    def change_char(self, val):
        self._char = val 

    def change_val(self, val):
        if(val == 'a' or val == 'A'):
            self._pos_y -= 1
        elif(val == 'd' or val == 'D'):
            self._pos_y += 1
        elif(val == 'w' or val == 'W'):
            self._pos_x -= 1  
        elif(val == 's' or val == 'S'):
            self._pos_x +=1

    def get_damage(self):
        return self._damage
    def change_damage(self,val):
        self._damage=val
    def get_speed(self):
        return self._speed
    def change_speed(self,val):
        self._speed=val 
    def get_destroy(self):
        return self._destroy
    def change_destroy(self):
        self._destroy=1 
    def change_hitpoints(self,val):
        self._hitpoints+=val 
    def get_hitpoints(self):
        x=(int)(self._hitpoints)
        return x
    def put_hitpoints(self,val):
        self._hitpoints=val    

    def ragespell(self):
        if(self._destroy==0 ):
            self._speed=0.5
            self._damage=(self._damage*2)
    
    def healspell(self):
        if(self._destroy==0):
            self._hitpoints = ((self._hitpoints)*150)/100
            if(self._hitpoints>100):
                self._hitpoints = 100     
                                  
                   

class Building:
    def __init__(self, x, y):
        self._pos_x = x
        self._pos_y = y
        self._maxhitpoints = 100
        self._hitpoints = 100
        # self._color = Fore.GREEN+Back.WHITE

class Hut(Building):
    def __init__(self, x, y):
        self._height = 1
        self._width = 1
        self._char = [['H']]
        self._destroy = 0
        self._color = Fore.GREEN+Back.WHITE
        # self._color = Fore.YELLOW+Back.CYAN
        super().__init__(x, y) 

    def get_posx(self):
        return self._pos_x

    def get_posy(self):
        return self._pos_y

    def get_hitpoints(self):
        return self._hitpoints

    def get_color(self):
        return self._color 

    def change_hitpoints(self, val):
        self._hitpoints += val
        # if(self._hitpoints > 20 and self._hitpoints <=50):
        #     self._grid[self._pos_x][self._pos_y] = Fore.YELLOW+'K'+Back.WHITE
        # if(self._hitpoints <= 20 and self._hitpoints >0):
        #     self._grid[self._pos_x][self._pos_y] = Style.RESET_ALL+Fore.RED+'K'+Back.WHITE

    def get_color(self):
        return self._color

    def change_color1(self):
        self._color =  Fore.YELLOW+Back.WHITE
    
    def change_color2(self):
        self._color=   Fore.RED+Back.WHITE

    def get_destroy(self):
        return self._destroy
    def change_destroy(self):
        self._destroy=1  

    def put_posx(self,val):
        self._pos_x=val

    def change_char1(self):
        self._char = [['8']]            

    # def change_color(self):
    #     if(self._hitpoints > 20 and self._hitpoints <=50):
    #         self._color = Fore.YELLOW
    #     if(self._hitpoints <= 20 and self._hitpoints >0):
    #         self._color = Fore.RED
                                 

class TownHall(Building):
    def __init__(self, x, y):
        self._height = 4
        self._width = 3
        self._color = Fore.GREEN+Back.WHITE
        self._char = [['L', 'L', 'L'], ['L', 'L', 'L'], ['L', 'L', 'L'],['L','L','L']]
        self._destroy=0
        super().__init__(x, y) 

    def change_vel(self,val1,val2):
        self._pos_x = val1
        self._pos_y = val2     

    def get_posx(self):
        return self._pos_x

    def get_posy(self):
        return self._pos_y

    def get_hitpoints(self):
        return self._hitpoints

    def get_color(self):
        return self._color 

    def put_posx(self,val):
        self._pos_x=val
    def put_posy(self,val):
        self._pos_y=val         

    def change_hitpoints(self, val):
        self._hitpoints += val
        # if(self._hitpoints > 20 and self._hitpoints <=50):
        #     self._color = Fore.YELLOW + Back.WHITE
        # if(self._hitpoints <= 20 and self._hitpoints >0):
        #     self._color = Fore.RED  + Back.WHITE


    # def change_color(self):
    #     if(self._hitpoints > 20 and self._hitpoints <=50):
    #         self._color = Fore.YELLOW
    #     if(self._hitpoints <= 20 and self._hitpoints >0):
    #         self._color = Fore.RED 
    def get_destroy(self):
        return self._destroy
    def change_destroy(self):
        self._destroy=1  
    def change_color1(self):
        self._color =  Fore.YELLOW+Back.WHITE
    
    def change_color2(self):
        self._color=   Fore.RED+Back.WHITE  

    def change_char1(self):
        self._char = [['8']]         



class cannon:
    def __init__(self, x, y):
        self._pos_x = x
        self._pos_y = y
        self._range = 5
        self._damage = 10
        self._bullets = []
        self._color = Fore.GREEN
        # self.make_arr(x,y)
        self._height = 1
        self._width = 1
        self._char = [['C']]
        self._destroy=0
        self._starttime=time.time()
        self._steps=0
        self._hitpoints = 100

    def get_posx(self):
        return self._pos_x
    def get_posy(self):
        return self._pos_y
    def get_damage(self):
        return self._damage   
    def change_char1(self):
        self._char = [['8']]  
    def get_destroy(self):
        return self._destroy
    def change_destroy(self):
        self._destroy=1 
    def get_starttime(self):
        return self._starttime
    def change_starttime(self):
        self._starttime = time.time()  
    def change_steps(self):
        self._steps+=1
    def get_steps(self):
        return self._steps   
    def change_color1(self):
        self._color =  Fore.YELLOW
    def change_hitpoints(self, val):
        self._hitpoints += val
    def change_color2(self):
        self._color=   Fore.RED   
    def get_hitpoints(self):
        return self._hitpoints            

class Wizard_Tower:
    def __init__(self, x, y):
        self._pos_x = x
        self._pos_y = y
        self._range = 5
        self._damage = 1
        self._bullets = []
        self._color = Fore.MAGENTA
        # self.make_arr(x,y)
        self._height = 1
        self._width = 1
        self._char = [['I']]
        self._destroy=0
        self._starttime=time.time()
        self._steps=0
        self._hitpoints=100

    def get_posx(self):
        return self._pos_x
    def get_posy(self):
        return self._pos_y
    def get_damage(self):
        return self._damage
    def get_destroy(self):
        return self._destroy
    def change_destroy(self):
        self._destroy=1 
    def get_starttime(self):
        return self._starttime
    def change_starttime(self):
        self._starttime = time.time()  
    def change_steps(self):
        self._steps+=1
    def get_steps(self):
        return self._steps 
    def change_char1(self):
        self._char = [['8']] 
    def change_color1(self):
        self._color =  Fore.YELLOW
    def change_hitpoints(self, val):
        self._hitpoints += val
    def change_color2(self):
        self._color=   Fore.RED   
    def get_hitpoints(self):
        return self._hitpoints                      
          
                      

class Bullets:
    def __init__(self, x, y):
        self._pos_x = x
        self._pos_y = y
        # self._range = 6
        self._damage = 5
        self._char = [['-']]
        self._color = Fore.BLUE
        self._starttime=time.time()
        # self.make_arr(x,y)
        self._height = 1
        self._width = 1   
   
class wall:
    def __init__(self, x, y):
        self._pos_x = x
        self._pos_y = y
        self._char = [['W']]
        self._color = Fore.WHITE+Back.GREEN
        # self.make_arr(x,y)
        self._height = 1
        self._width = 1
        self._numattacksbyking = 4
        self._numattaksbytroop = 5
        self._hitpoints=100
        self._destroy=0

    def change_hitpoints(self,val):
        self._hitpoints+=val    
        
    def get_hitpoints(self):
        return self._hitpoints

    def get_posx(self):
        return self._pos_x

    def get_posy(self):
        return self._pos_y
    
    def put_posx(self,val):
        self._pos_x=val
    
    def put_posy(self,val):
        self._pos_y=val

    def change_color1(self):
        self._color =  Fore.WHITE+Back.YELLOW
    
    def change_color2(self):
        self._color=   Fore.WHITE+Back.RED

    def get_destroy(self):
        return self._destroy
    def change_destroy(self):
        self._destroy=1               

class Troops(Character):
    def __init__(self, x, y):
        self._height = 1
        self._width = 1
        self._char = [['T']]
        self._color = Fore.BLUE 
        self._change = 10
        self._speed = 1
        self._damage=5
        self._starttime = time.time()
        self._steps = 0
        self._ragespell = 0
        self._healspell = 0
        self._attackmode = 0
        self._destroy =0
        super().__init__(x, y)

    def check_boun(self,limit_x,limit_y):
        if (self._pos_y + self._width - 1 > limit_y) :
            self._pos_y = limit_y - self._width + 1
        if self._pos_y < 0:
            self._pos_y = 0
        if self._pos_x < self._height:
            self._pos_x = self._height 
        if self._pos_x >= limit_x:
            self._pos_x = limit_x-1
    def change_starttime(self):
        self._starttime = time.time()        

    def change_life(self,val):
        self._life+=val 

    def change_ragespell(self, val):
        self._ragespell = val   

    def change_healspell(self):
        self._healspell = val        
    
    def change_steps(self):
        self._steps+=1

    def get_steps(self):
        return self._steps   

    def get_starttime(self):
        return self._starttime    

    def get_life(self):
        return self._life     #get heal, rage spell         

    def change_posx(self, val):
        self._pos_x += val

    def change_posy(self, val):
        self._pos_y += val

    def put_posx(self, val):
        self._pos_x = val

    def put_posy(self, val):
        self._pos_y = val

    def get_height(self):
        return self._height

    def get_width(self):
        return self._width        

    def get_char(self,i,j):
        return self._char[i][j]

    def get_posx(self):
        return self._pos_x

    def get_posy(self):
        return self._pos_y        

    def change_char(self, val):
        self._char = val

    def change_attackmode(self,val):
        self._attackmode = val

    def get_attackmode(self):
        return self._attackmode         

    def change_vel(self,val1,val2):
        self._pos_x = val1
        self._pos_y = val2 

    def get_damage(self):
        return self._damage
    def change_damage(self,val):
        self._damage=val
    def get_speed(self):
        return self._speed
    def change_speed(self,val):
        self._speed=val  

    def get_destroy(self):
        return self._destroy
    def change_destroy(self):
        self._destroy=1    

    def change_hitpoints(self,val):
        self._hitpoints+=val           

    def get_hitpoints(self):
        return self._hitpoints    

    def ragespell(self):
        if(self._destroy==0 ):
            self._speed=0.5
            self._damage=(self._damage*2)
    
    def healspell(self):
        if(self._destroy==0):
            self._hitpoints = ((self._hitpoints)*150)/100
            if(self._hitpoints>100):
                self._hitpoints = 100 

    def put_hitpoints(self,val):
        self._hitpoints=val


class Archers(Character):
    def __init__(self, x, y):
        self._height = 1
        self._width = 1
        self._char = [['A']]
        self._color = Fore.BLUE 
        self._change = 10
        self._speed = 0.5
        self._damage= 2.5
        self._starttime = time.time()
        self._steps = 0
        self._ragespell = 0
        self._healspell = 0
        self._attackmode = 0
        self._destroy =0
        self._range = 6
        super().__init__(x, y)

    def check_boun(self,limit_x,limit_y):
        if (self._pos_y + self._width - 1 > limit_y) :
            self._pos_y = limit_y - self._width + 1
        if self._pos_y < 0:
            self._pos_y = 0
        if self._pos_x < self._height:
            self._pos_x = self._height 
        if self._pos_x >= limit_x:
            self._pos_x = limit_x-1

    def change_life(self,val):
        self._life+=val 

    def change_ragespell(self, val):
        self._ragespell = val   

    def change_healspell(self):
        self._healspell = val        
    
    def change_steps(self):
        self._steps+=1

    def get_steps(self):
        return self._steps   

    def get_starttime(self):
        return self._starttime    

    def get_life(self):
        return self._life     #get heal, rage spell         

    def change_posx(self, val):
        self._pos_x += val

    def change_posy(self, val):
        self._pos_y += val

    def put_posx(self, val):
        self._pos_x = val

    def put_posy(self, val):
        self._pos_y = val

    def get_height(self):
        return self._height

    def get_width(self):
        return self._width        

    def get_char(self,i,j):
        return self._char[i][j]

    def get_posx(self):
        return self._pos_x

    def get_posy(self):
        return self._pos_y        

    def change_char(self, val):
        self._char = val

    def change_attackmode(self,val):
        self._attackmode = val

    def get_attackmode(self):
        return self._attackmode         

    def change_vel(self,val1,val2):
        self._pos_x = val1
        self._pos_y = val2 

    def get_damage(self):
        return self._damage
    def change_damage(self,val):
        self._damage=val
    def get_speed(self):
        return self._speed
    def change_speed(self,val):
        self._speed=val  

    def get_destroy(self):
        return self._destroy
    def change_destroy(self):
        self._destroy=1    

    def change_hitpoints(self,val):
        self._hitpoints+=val           

    def get_hitpoints(self):
        return self._hitpoints    

    def ragespell(self):
        if(self._destroy==0 ):
            self._speed=0.5
            self._damage=(self._damage*2)
    
    def healspell(self):
        if(self._destroy==0):
            self._hitpoints = ((self._hitpoints)*150)/100
            if(self._hitpoints>100):
                self._hitpoints = 100 

    def put_hitpoints(self,val):
        self._hitpoints=val

    def change_starttime(self):
        self._starttime = time.time()
        
         


class Balloons(Character):
    def __init__(self, x, y):
        self._height = 1
        self._width = 1
        self._char = [['B']]
        self._color = Fore.GREEN+Back.WHITE
        self._change = 10
        self._speed = 1
        self._damage=10
        self._starttime = time.time()
        self._steps = 0
        self._ragespell = 0
        self._healspell = 0
        self._attackmode = 0
        self._destroy =0
        self._prev='B'
        super().__init__(x, y)

    def put_prev(self,val):
        self._prev = val

    def get_prev(self):
        return self._prev    

    # def change_char1(self):
    #     self._char = [['8']]     

    # def change_normal(self):
    #     self._char = [['B']] 
    def change_starttime(self):
        self._starttime = time.time()    

    def check_boun(self,limit_x,limit_y):
        if (self._pos_y + self._width - 1 > limit_y) :
            self._pos_y = limit_y - self._width + 1
        if self._pos_y < 0:
            self._pos_y = 0
        if self._pos_x < self._height:
            self._pos_x = self._height 
        if self._pos_x >= limit_x:
            self._pos_x = limit_x-1

    def change_life(self,val):
        self._life+=val 

    def change_ragespell(self, val):
        self._ragespell = val   

    def change_healspell(self):
        self._healspell = val        
    
    def change_steps(self):
        self._steps+=1

    def get_steps(self):
        return self._steps   

    def get_starttime(self):
        return self._starttime    

    def get_life(self):
        return self._life     #get heal, rage spell         

    def change_posx(self, val):
        self._pos_x += val

    def change_posy(self, val):
        self._pos_y += val

    def put_posx(self, val):
        self._pos_x = val

    def put_posy(self, val):
        self._pos_y = val

    def get_height(self):
        return self._height

    def get_width(self):
        return self._width        

    def get_char(self,i,j):
        return self._char[i][j]

    def get_posx(self):
        return self._pos_x

    def get_posy(self):
        return self._pos_y        

    def change_char(self, val):
        self._char = val

    def change_attackmode(self,val):
        self._attackmode = val

    def get_attackmode(self):
        return self._attackmode         

    def change_vel(self,val1,val2):
        self._pos_x = val1
        self._pos_y = val2 

    def get_damage(self):
        return self._damage
    def change_damage(self,val):
        self._damage=val
    def get_speed(self):
        return self._speed
    def change_speed(self,val):
        self._speed=val  

    def get_destroy(self):
        return self._destroy
    def change_destroy(self):
        self._destroy=1    

    def change_hitpoints(self,val):
        self._hitpoints+=val           

    def get_hitpoints(self):
        return self._hitpoints    

    def put_hitpoints(self,val):
        self._hitpoints=val
    

# class cannon:
#     def __init__(self, x, y):
#         self._pos_x = x
#         self._pos_y = y
#         self._range = 6
#         self._damage = 5
#         self._bullets = []
#         self._color = Fore.MAGENTA
#         # self.make_arr(x,y)
#         self._height = 1
#         self._width = 1
#         self._char = [['W']]

#     def get_posx(self):
#         return self._pos_x
#     def get_posy(self):
#         return self._pos_y
#     def get_damage(self):
#         return self._damage  
#     def change_char1(self):
#         self._char = [['8']]       
                          


class PersonQueen(Character):
    def __init__(self, x, y):
        self._height = 1
        self._width = 1
        self._char = [['Q']]
        self._color = Fore.CYAN + Back.YELLOW
        self._change = 4
        self._damage = 10
        self._attack=0
        self._speed=1
        self._ragespell = 0
        self._healspell = 0
        self._destroy=0
        
        super().__init__(x, y)

    def check_boun(self,limit_x,limit_y):
        if (self._pos_y + self._width - 1 > limit_y) :
            self._pos_y = limit_y - self._width + 1
        if self._pos_y < 0:
            self._pos_y = 0
        if self._pos_x < self._height:
            self._pos_x = self._height 
        if self._pos_x >= limit_x:
            self._pos_x = limit_x-1

    def get_attack(self):
        return self._attack

    def change_attack(self, val):
        self._attack = val           

    def get_posx(self):
        return self._pos_x

    def get_posy(self):
        return self._pos_y             

    def change_life(self,val):
        self._life+=val  

    def get_life(self):
        return self._life        

    def change_posx(self, val):
        self._pos_x += val

    def change_posy(self, val):
        self._pos_y += val

    def put_posx(self, val):
        self._pos_x = val

    def put_posy(self, val):
        self._pos_y = val

    def get_height(self):
        return self._height

    def get_width(self):
        return self._width        

    def get_char(self,i,j):
        return self._char[i][j]

    def change_char(self, val):
        self._char = val 

    def change_val(self, val):
        if(val == 'a' or val == 'A'):
            self._pos_y -= 1
        elif(val == 'd' or val == 'D'):
            self._pos_y += 1
        elif(val == 'w' or val == 'W'):
            self._pos_x -= 1  
        elif(val == 's' or val == 'S'):
            self._pos_x +=1

    def get_damage(self):
        return self._damage
    def change_damage(self,val):
        self._damage=val
    def get_speed(self):
        return self._speed
    def change_speed(self,val):
        self._speed=val 
    def get_destroy(self):
        return self._destroy
    def change_destroy(self):
        self._destroy=1 
    def change_hitpoints(self,val):
        self._hitpoints+=val 
    def get_hitpoints(self):
        return self._hitpoints 
    def put_hitpoints(self,val):
        self._hitpoints=val    

        

                   

