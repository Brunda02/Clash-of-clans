import colorama
from colorama import Fore, Back, Style
from src.input import input
import termios
import subprocess as sp
import time
import tty
import sys
import os
from src.objects import *
from src.config import *
from src.func3 import *
from src.func2 import *
from src.func7 import *
from src.func8 import *
from src.func6 import *
from src.village import village
import random
import json


colorama.init()


if __name__ == "__main__":
   orig_settings = termios.tcgetattr(sys.stdin)
   tty.setcbreak(sys.stdin)
   input = input()
   input.hide_cursor()
   brunda=0
   mat=[[3,3],[4,4],[5,5]]
   for suma in range(0,3):
    yesh=-1
    orig_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin)
    x_t=random.randint(4,rows-2)
    y_t=random.randint(0,columns-5)
    num_tower = mat[suma][0]
    num_cann = mat[suma][1]
    num=20+num_tower
    
    # x_cor = random.sample(range(1,rows-2),20)
    # y_cor = random.sample(range(0,columns-1),20)
    x_cor=[]
    y_cor=[]
    p=0
    Archer_num=0
    Troop_num=0
    Balloon_num=0
    # x_t=0
    # y_t=0
    while(p!=num):
        x_temp=random.randint(1,rows-2)
        y_temp=random.randint(0,columns-1)
        if((x_temp<x_t-3 or x_temp>x_t) and (y_temp<y_t-3 or y_temp>y_t)):
            x_cor.append(x_temp)
            y_cor.append(y_temp)
            p+=1
    # x1_cor = random.sample(range(4,rows-2),2)
    # y1_cor = random.sample(range(0,columns-9),2)
    array=[]
    # king = PersonKing(28, 1)
    # input = input()
    # input.hide_cursor()

    inu=user_controlled()
    if(inu==0):
        king = PersonKing(28, 1)
    else:
        king = PersonQueen(28,1)    
    iiith = village(king, rows, columns, frames)
    iiith.objectc(king)
    townhall=TownHall(x_t,y_t)
    iiith.objectc(townhall)
    spx1=iiith.get_spawn()[0][0]
    spx2=iiith.get_spawn()[1][0]
    spx3=iiith.get_spawn()[2][0]
    spy1=iiith.get_spawn()[0][1]
    spy2=iiith.get_spawn()[1][1]
    spy3=iiith.get_spawn()[2][1]
 
    names_huts=[]
    for i in range(0,5):
        var="hut"+str(i)
        names_huts.append(var)

    for i in range(0,5):
        locals()[names_huts[i]] = Hut(x_cor[i],y_cor[i])
        iiith.objectc(locals()[names_huts[i]])
 
    names_cannons=[]
    a_cannons=[]
    for i in range(0,num_cann):
        var="cannon"+str(i)
        names_cannons.append(var)


    for i in range(0,num_cann):
        locals()[names_cannons[i]] = cannon(x_cor[i+5],y_cor[i+5])
        a_cannons.append(locals()[names_cannons[i]])
        iiith.objectc(locals()[names_cannons[i]])

    names_troops=[]
    for i in range(0,5):
        var="troop"+str(i)
        names_troops.append(var)

    for i in range(0,5):
        locals()[names_troops[i]] = Troops(x_cor[i+7],y_cor[i+7])
        # iiith.objectc(locals()[names_troops[i]])

    names_walls=[]
    for i in range(0,8):
        var="wall"+str(i)
        names_walls.append(var)

    names_archers=[]
    for i in range(0,4):
        var="archer"+str(i)
        names_archers.append(var) 

    for i in range(0,4):
        # var11 = iiith.get_spawn()
        # varx=var11[0]
        # vary=var11[1]
        locals()[names_archers[i]] = Archers(spx1,spy1)
        # iiith.objectc(locals()[names_archers[i]])    
    
    names_balloons=[]
    for i in range(0,4):
        var="balloon"+str(i)
        names_balloons.append(var) 

    for i in range(0,4):
        # var11 = iiith.get_spawn()
        # varx=var11[0]
        # vary=var11[1]
        locals()[names_balloons[i]] = Balloons(spx1,spy1)
        # iiith.objectc(locals()[names_archers[i]])
                  
    
    for i in range(0,8):
        locals()[names_walls[i]] = wall(x_cor[i+12],y_cor[i+12])
        iiith.objectc(locals()[names_walls[i]])

    names_towers=[]
    a_towers=[]
    for i in range(0,5):
        var="tower"+str(i)
        names_towers.append(var)

    for i in range(0,num_tower):
        locals()[names_towers[i]] = Wizard_Tower(x_cor[(num-(i+num_tower))],y_cor[(num-(i+num_tower))])
        a_towers.append(locals()[names_towers[i]])
        iiith.objectc(locals()[names_towers[i]])    
    
    start_time = time.time()
    # global_time = time.time()
    gtime = time.time()
    # brunda=0
    persons=[king,troop0,troop1,troop2,troop3,troop4]
    a_troops=[troop0,troop1,troop2,troop3,troop4]
    a_archers=[archer0,archer1,archer2,archer3]
    a_balloons=[balloon0,balloon1,balloon2,balloon3]
    a_huts=[hut0,hut1,hut2,hut3,hut4]
    a_walls=[wall0,wall1,wall2,wall3,wall4,wall5,wall6,wall7]
    d_huts={}
    d_troops={}
    d_archers={}
    d_balloons={}
    d_walls={}
    d_all={}
    d_all2={}
    d_towers={}
    d_cannons={}
    d_all3={}
    a_all2=a_troops+a_archers+a_balloons+[king]
    a_all3=a_cannons+a_towers
    a_all=a_huts+[townhall]
    for i in range(0,5):
        d_huts[i]=np.asarray([x_cor[i],y_cor[i]])
    # for i in range(0,5):
    #     d_troops[i]=np.asarray([x_cor[i+7],y_cor[i+7]])    
    for i in range(0,8):
        d_walls[i]=np.asarray([x_cor[i+12],y_cor[i+12]])
    for i in range(0,5):
        d_all[i]=np.asarray([x_cor[i],y_cor[i]])   
    for i in range(0,8):
        d_all[i+5]=np.asarray([x_cor[i+12],y_cor[i+12]])  
    for i in range(0,num_tower):
        d_towers[i]=np.asarray([x_cor[(num-(i+num_tower))],y_cor[num-(i+num_tower)]])
    for i in range(0,num_cann):
        d_cannons[i]=np.asarray([x_cor[i+5],y_cor[i+5]])
    for i in range(0,num_cann+num_tower):
       if(i<num_cann): 
        d_all3[i]=d_cannons[i]
       else :
        d_all3[i]=d_towers[i-num_cann]   

    

    kq=0    
    for i in range(0,3):
        for j in range(0,3):
            d_all[kq+13]=np.asarray([x_t+i,y_t+j])
            kq+=1
    prev='D'

    global_time = time.time()
    e_time=0

    while(1):
        # if(king.get_life()>=0):
        #     king.change_life(-10)
        output_str=""    
        for row in range(rows):
                for col in range(columns):
                    output_str += iiith.get_grid(row, col)
                output_str += '\n'
        string=""
        for i in range(0,6):
            if(persons[i].get_hitpoints()<=0 or persons[i].get_destroy()==1):
                persons[i].put_hitpoints(0)
        # print(king.get_hitpoints())
        # print(king.get_destroy())
        for i in range(0,king.get_hitpoints()):
            string+='*' 
        for i in range(king.get_hitpoints(),100):
            string+=' '      
        string+="\n" 
        output_str=output_str+string        
        print('\033[H' + output_str)
        array.append(output_str)
        brunda+=1
        d_all2[13]=[king.get_posx(),king.get_posy()]
        # break

        # print(iiith.printvillage())
        if(inu==0):
        #  print("x")   
         if input.kbhit():
            val = input.getch()
            val = val.upper()
            # print(val)
            if(val==' '):
               nodes=write_all_coor4(iiith,x_cor,y_cor,x_t,y_t) 
               p=getpositionofattack(iiith,king,nodes)
               if(p!=-1 and p!=5):
                varia="hut"+str(p)
                varia2=locals()[varia]
                varia2.change_hitpoints(-1*king.get_damage())
                changecolour(iiith,varia2)
               if(p!=-1 and p==5):
                townhall.change_hitpoints(-1*king.get_damage())
                changecolour(iiith,townhall)
            if(val=='R'):
                for i in range(0,6):
                    persons[i].ragespell()
            if(val=='H'):
                for i in range(0,6):
                    persons[i].healspell() 
            if(val=='W' or val=='A' or val=='S' or val == 'D'):                            
             if(iiith.check_present(king,val)!=0):
              iiith.clear(king)
              king.change_val(val)
              king.check_boun(limit_x,limit_y)
             if(king.get_hitpoints()>0):
              d_all2[13]=[king.get_posx(),king.get_posy()] 
            #   print(d_all2[13])  
              iiith.objectc(king)
            if(val=='G' and Troop_num<5): 
              a_troops[Troop_num].change_vel(spx1,spy1)
              a_troops[Troop_num].change_starttime()
              iiith.objectc(a_troops[Troop_num])
              d_troops[Troop_num]=[spx1,spy1]
              d_all2[Troop_num] = [spx1,spy1]
              Troop_num+=1
            if(val=='P' and Troop_num<5): 
              a_troops[Troop_num].change_vel(spx2,spy2)
              a_troops[Troop_num].change_starttime()
              iiith.objectc(a_troops[Troop_num])
              d_troops[Troop_num]=[spx2,spy2]
              d_all2[Troop_num] = [spx2,spy2]
              Troop_num+=1
            if(val=='I' and Troop_num<5): 
              a_troops[Troop_num].change_vel(spx3,spy3)
              a_troops[Troop_num].change_starttime()
              iiith.objectc(a_troops[Troop_num])
              d_troops[Troop_num]=[spx3,spy3]
              d_all2[Troop_num] = [spx3,spy3]
              Troop_num+=1  
            if(val=='J' and Archer_num<4):
            #   print("x")  
              a_archers[Archer_num].change_vel(spx1,spy1)
              a_archers[Archer_num].change_starttime()
              iiith.objectc(a_archers[Archer_num])
              d_archers[Archer_num]=[spx1,spy1]
              d_all2[Archer_num+5] = [spx1,spy1]
              Archer_num+=1
            if(val=='K' and Archer_num<4):
              a_archers[Archer_num].change_vel(spx2,spy2)
              a_archers[Archer_num].change_starttime()
              iiith.objectc(a_archers[Archer_num]) 
              d_archers[Archer_num]=[spx2,spy2]
              d_all2[Archer_num+5] = [spx2,spy2]
              Archer_num+=1     
            if(val=='L' and Archer_num<4):
              a_archers[Archer_num].change_vel(spx3,spy3)
              a_archers[Archer_num].change_starttime()
              iiith.objectc(a_archers[Archer_num])
              d_archers[Archer_num]=[spx3,spy3]
              d_all2[Archer_num+5] = [spx3,spy3]
              Archer_num+=1
            if(val=='M' and Balloon_num<4): 
              a_balloons[Balloon_num].change_vel(spx1,spy1)
              a_balloons[Balloon_num].change_starttime()
              iiith.objectc(a_balloons[Balloon_num])
              d_balloons[Balloon_num]=[spx1,spy1]
              d_all2[Balloon_num+9] = [spx1,spy1]
              Balloon_num+=1
            if(val=='N' and Balloon_num<4):
              a_balloons[Balloon_num].change_vel(spx2,spy2)
              a_balloons[Balloon_num].change_starttime()
              iiith.objectc(a_balloons[Balloon_num]) 
              d_balloons[Balloon_num]=[spx2,spy2]
              d_all2[Balloon_num+9] = [spx2,spy2]
              Balloon_num+=1     
            if(val=='O' and Balloon_num<4):
              a_balloons[Balloon_num].change_vel(spx3,spy3)
              a_balloons[Balloon_num].change_starttime()
              iiith.objectc(a_balloons[Balloon_num])
              d_balloons[Balloon_num]=[spx3,spy3]
              d_all2[Balloon_num+9] = [spx3,spy3]
              Balloon_num+=1  
               
        
        if(inu==1):
        #    prev='D'
           if input.kbhit():
            val = input.getch()
            val= val.upper()
            # prev=val
            # print(prev)
            # print(val)
            if(val==' '):
                archerqueen(iiith,king,prev,x_cor,y_cor,x_t,y_t,a_huts,a_walls,townhall)
            if(val=='R'):
                for i in range(0,6):
                    persons[i].ragespell()
            if(val=='H'):
                for i in range(0,6):
                    persons[i].healspell() 
            if(val=='W' or val=='A' or val=='S' or val == 'D'):                            
             if(iiith.check_present(king,val)!=0):
              iiith.clear(king)
              king.change_val(val)
              king.check_boun(limit_x,limit_y)
             if(king.get_hitpoints()>0):
              iiith.objectc(king)
              d_all2[13]=[king.get_posx(),king.get_posy()]
             prev=val 
            if(val=='G' and Troop_num<5): 
              a_troops[Troop_num].change_vel(spx1,spy1)
              a_troops[Troop_num].change_starttime()
              iiith.objectc(a_troops[Troop_num])
              d_troops[Troop_num]=[spx1,spy1]
              d_all2[Troop_num] = [spx1,spy1]
              Troop_num+=1
            if(val=='P' and Troop_num<5): 
              a_troops[Troop_num].change_vel(spx2,spy2)
              a_troops[Troop_num].change_starttime()
              iiith.objectc(a_troops[Troop_num])
              d_troops[Troop_num]=[spx2,spy2]
              d_all2[Troop_num] = [spx2,spy2]
              Troop_num+=1
            if(val=='I' and Troop_num<5): 
              a_troops[Troop_num].change_vel(spx3,spy3)
              a_troops[Troop_num].change_starttime()
              iiith.objectc(a_troops[Troop_num])
              d_troops[Troop_num]=[spx3,spy3]
              d_all2[Troop_num] = [spx3,spy3]
              Troop_num+=1   
            if(val=='J' and Archer_num<4):
              a_archers[Archer_num].change_vel(spx1,spy1)
              iiith.objectc(a_archers[Archer_num])
              d_archers[Archer_num]=[spx1,spy1]
              a_archers[Archer_num].change_starttime()
              d_all2[Archer_num+5] = [spx1,spy1]
              Archer_num+=1
            if(val=='K' and Archer_num<4):
              a_archers[Archer_num].change_vel(spx2,spy2)
              iiith.objectc(a_archers[Archer_num]) 
              d_archers[Archer_num]=[spx2,spy2]
              a_archers[Archer_num].change_starttime()
              d_all2[Archer_num+5] = [spx2,spy2]
              Archer_num+=1    
            if(val=='L' and Archer_num<4):
              a_archers[Archer_num].change_vel(spx3,spy3)
              iiith.objectc(a_archers[Archer_num])
              d_archers[Archer_num]=[spx3,spy3]
              a_archers[Archer_num].change_starttime()
              d_all2[Archer_num+5] = [spx3,spy3]
              Archer_num+=1
            if(val=='M' and Balloon_num<4): 
              a_balloons[Balloon_num].change_vel(spx1,spy1)
              a_balloons[Balloon_num].change_starttime()
              iiith.objectc(a_balloons[Balloon_num])
              d_balloons[Balloon_num]=[spx1,spy1]
              d_all2[Balloon_num+9] = [spx1,spy1]
              Balloon_num+=1
            if(val=='N' and Balloon_num<4):
              a_balloons[Balloon_num].change_vel(spx2,spy2)
              a_balloons[Balloon_num].change_starttime()
              iiith.objectc(a_balloons[Balloon_num]) 
              d_balloons[Balloon_num]=[spx2,spy2]
              d_all2[Balloon_num+9] = [spx2,spy2]
              Balloon_num+=1     
            if(val=='O' and Balloon_num<4):
              a_balloons[Balloon_num].change_vel(spx3,spy3)
              a_balloons[Balloon_num].change_starttime()
              iiith.objectc(a_balloons[Balloon_num])
              d_balloons[Balloon_num]=[spx3,spy3]
              d_all2[Balloon_num+9] = [spx3,spy3]
              Balloon_num+=1  
             


        b_time1=time.time()-e_time
        if(check_destroyed3(a_huts,townhall)==0):
            Archers_movement2(iiith, king,d_huts,d_walls,d_archers,d_all,townhall,a_huts,a_walls,a_archers,d_all3,d_towers,d_cannons,a_all3,d_all2)   
        b_time2=time.time()-e_time      
        if(check_destroyed2(a_huts)==0):
         arr=Troops_movement(iiith,king,d_huts,d_walls,d_troops,d_all,townhall,a_huts,a_walls,a_troops,d_all2)
        b_time3=time.time()
        if(check_destroyed6(a_all2)==0):
            attack_tower(iiith,d_all2,king,d_towers,a_all2,a_towers,d_troops,d_archers,d_balloons,b_time3)
        b_time4=time.time()       
        attack_cannons(iiith,d_all2,king,d_cannons,a_all2,a_cannons,d_troops,d_archers,d_balloons,b_time4)
        b_time5=time.time()-e_time
        # Balloons_movement2(iiith, king,d_huts,d_walls,d_balloons,d_all,d_all3,townhall,a_huts,a_walls,a_balloons,a_all3,num_cann,num_tower,d_all2)
        Archers_movement9(iiith, king,d_huts,d_walls,d_balloons,d_all,townhall,a_huts,a_walls,a_balloons,d_all3,d_towers,d_cannons,a_all3,d_all2)   
        iiith.print_spawn()
  
        ii=0
        for cv in a_all2:
            if(ii>=5 and ii<9):
             print(cv.get_hitpoints())
            ii+=1
        e_time=time.time()  
        yesh=check_gameoveru(a_all2,a_all,a_all3,Troop_num,Archer_num,Balloon_num,num_cann,num_tower)
        if(yesh==0 or yesh==1):
            break
    if(yesh==0):
        break

                
    # with open("temp2.json", "r+") as file:
    #   data = json.load(file)
    #   data["games"].append(array)
    #   file.seek(0)
    #   file.close()

    # with open("temp2.json", "w") as file:

    #   json.dump(data, file)
    #   file.close()    


        
             
        

