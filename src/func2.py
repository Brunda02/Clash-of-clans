
import colorama
from colorama import Fore, Back, Style
import time
from src.objects import *
from src.config import *
from src.village import village
import random
import numpy as np
# from src.input import input
colorama.init()

# Keys to spawn troops, ballons, archers

# Keys are G,P,I----> Troops
# J,K,L ---> Archers
# M,N,O ---> Balloons


def changecoloru(iiith,varia2):
    if(varia2.get_hitpoints()> 20 and varia2.get_hitpoints() <=50):
        # print("x")
        varia2.change_color1()
        iiith.objectc(varia2)
    if(varia2.get_hitpoints()<= 20 and varia2.get_hitpoints() >0):
        # print("y")
        varia2.change_color2()
        iiith.objectc(varia2)
    if(varia2.get_hitpoints()<=0):
        # print("z")
        iiith.clear(varia2)
        varia2.change_destroy()

def check_inbetweena(tempo2, iiith, nodes, node):
    x_coor = [1, 1, -1, -1, 1, 0, -1, 0]
    y_coor = [1, -1, 1, -1, 0, 1, 0, -1]
    letter = ["RU", "RD", "LU", "LD", "R", "U", "L", "D"]
    arr = [x_coor, y_coor]
    arr2 = np.asarray(arr)
    arr3 = arr2 + node
    distance = []
    nodest = np.transpose(nodes)
    for i in range(0, 8):
        # p=(arr3[:,i] in nodest.tolist())
        # if(p!=True):
          if(iiith.get_char(arr3[0][i], arr3[1][i]) != ' ' and iiith.get_char(arr3[0][i], arr3[1][i]) != 'W'):
            arr3[:, i] = node.T
        #   if(iiith.get_char(arr3[0][i], arr3[1][i]) != ' ' and iiith.get_char(arr3[0][i], arr3[1][i]) == 'W'):
            
             

    arr4 = np.sum((arr3-tempo2)**2, axis=0)
    # print(arr4)
    minElement = np.amin(arr4)
    result = np.where(arr4 == np.amin(arr4))
    # print(result)
    temp = arr3[:, result[0][0]]
    return temp


def closest_nodea(node, nodes):
    # nodes = np.asarray(nodes)
    dist = np.sum((nodes - node)**2, axis=0)
    # print(dist)
    minElement = np.amin(dist)
    # print(minElement)
    result = np.where(dist == np.amin(dist))
    temp = result[0]
    # print(temp)
    return temp[0]


def write_all_coora(iiith, x_cor, y_cor,x_t,y_t):
    xco = []
    yco = []
    for i in range(0, 5):
        xco.append(x_cor[i])
        yco.append(y_cor[i])
    xco.append(x_t)
    yco.append(y_t)
    n = []
    n.append(xco)
    n.append(yco)
    # print(n)
    nodes = np.asarray(n)
    # nodes=nodes.transpose()
    # nodes = nodes[~np.all(nodes == 0, axis=1)]
    # nodes=nodes.transpose()
    # print(nodes)
    return nodes

def write_all_coora2(iiith, x_cor, y_cor,x_t,y_t):
    xco = []
    yco = []
    for i in range(0, 5):
        xco.append(x_cor[i])
        yco.append(y_cor[i])
    for i in range(0, 8):
        xco.append(x_cor[i+12])
        yco.append(y_cor[i+12])    
    xco.append(x_t)
    yco.append(y_t)
    n = []
    n.append(xco)
    n.append(yco)
    # print(n)
    nodes = np.asarray(n)
    # nodes=nodes.transpose()
    # nodes = nodes[~np.all(nodes == 0, axis=1)]
    # nodes=nodes.transpose()
    # print(nodes)
    return nodes    


def Archers_movement(x_cor, y_cor, iiith, king,x_t,y_t,x_cor2,y_cor2):
    nodes = write_all_coora(iiith, x_cor, y_cor,x_t,y_t)
    arr = []
    for i in range(0, 4):
        node = np.array([[x_cor2[i], y_cor2[i]]]).T
        # print(node)
        tempo = closest_nodea(node, nodes)
        tempo2 = np.array([[nodes[0][tempo], nodes[1][tempo]]]).T
        tempo3 = check_inbetweena(tempo2, iiith, nodes, node)
        # print(tempo3)
        arr.append(tempo3)
    return arr
    
   # get hut positions check nearest manhattan position 

def attack_archers(troopsee, iiith, x_cor, y_cor,x_t,y_t,a_huts, a_walls, townhall):
    ran = -1
    nodes = write_all_coora2(iiith, x_cor, y_cor)
    x_a=troopsee.get_posx()
    y_a=troopsee.get_posy()
    mini=10000
    # x_coor = [1, 1, -1, -1, 1, 0, -1, 0]
    # y_coor = [1, -1, 1, -1, 0, 1, 0, -1]
    # letter = ["RU","RD","LU","LD","R","U","L","D"]
    # arr = [x_coor, y_coor]
    # arr2 = np.asarray(arr)
    # arr3 = arr2 + node
    distance = []
    nodest = np.transpose(nodes)
    for i in range(0, len(nodes)):
        # p=(arr3[:,i] in nodest.tolist())
        x_i=node[i][0]
        y_i=node[i][1]
        tempuu=min(abs(x_i-x_a),abs(y_i-y_a))
        if(tempuu< mini and tempuu<=6):
            mini=tempuu
            ran=i
    if(ran>=0 and ran<=4):
                    # print(a_huts[ans].get_hitpoints())
        a_huts[ans].change_hitpoints(-1*troopsee.get_damage())  
        objectu=a_huts[ans]
        changecoloru(iiith,objectu)     
    if(ran>=5 and ran<=12):
                    # print(a_walls[ans-5].get_hitpoints())
        a_walls[ans-5].change_hitpoints(-troopsee*king.get_damage())
        objectu=a_walls[ans-5]
        changecoloru(iiith,objectu)
    if(ran==13):
                    # print(townhall.get_hitpoints()) 
        townhall.change_hitpoints(-1*troopsee.get_damage())
        objectu=townhall
        changecoloru(iiith,objectu)       
          
     
    #  min(abs(x_i-x_a),abs(y_i-y_a))


    

def user_controlled():
    print("Which Character U want to play(K/Q):")
    val=input()
    if(val=="K"):
        return 0
    if(val=="Q"):
        return 1  

def getattack(iiith,x_cor,y_cor,x_t,y_t,node,a_huts,a_walls,townhall):
    ans=-1
    nodes=write_all_coora2(iiith, x_cor, y_cor,x_t,y_t)
    nodest=np.transpose(nodes)
    result = np.where((nodest == node).all(axis=1))
    if(len(result[0])!=0):
     ans=result[0][0]
    #  if(ans<4):
         
    #  if(ans>=4 and ans<12):
    #  if(ans==13):        
    return ans 


def archerqueen(iiith,king,val,x_cor,y_cor,x_t,y_t,a_huts,a_walls,townhall):
    x_temp=0
    y_temp=0
    print(val)
    if(val=='W' or val=='w'): 
        x_temp=-1
    if(val=='S' or val=='s'): 
        x_temp=1
    if(val=='A' or val=='a'): 
        y_temp=-1
    if(val=='D' or val=='d'): 
        y_temp=1
    x_pos = king.get_posx()+8*x_temp
    y_pos = king.get_posy()+8*y_temp
    # print(x_pos,y_pos)
    for i in range(-2,3):
        for j in range(-2,3):
            if(x_pos+i<=28 and x_pos+i>=1 and y_pos+j<=90 and y_pos+j>=0):
             node = np.asarray([x_pos+i,y_pos+j])   
             c=iiith.get_char(x_pos+i, y_pos+j)
            #  print(c)
             if(c=='H' or c=='L' or c=='W'):
                ans=getattack(iiith,x_cor,y_cor,x_t,y_t,node,a_huts,a_walls,townhall)
                # print(ans)
                if(ans>=0 and ans<=4):
                    # print(a_huts[ans].get_hitpoints())
                    a_huts[ans].change_hitpoints(-1*king.get_damage())  
                    objectu=a_huts[ans]
                    changecoloru(iiith,objectu)     
                if(ans>=5 and ans<=12):
                    # print(a_walls[ans-5].get_hitpoints())
                    a_walls[ans-5].change_hitpoints(-1*king.get_damage())
                    objectu=a_walls[ans-5]
                    changecoloru(iiith,objectu)
                if(ans==13):
                    # print(townhall.get_hitpoints()) 
                    townhall.change_hitpoints(-1*king.get_damage())
                    objectu=townhall
                    changecoloru(iiith,objectu)

def check_destroyed(a_huts,a_walls,townhall):
    for i in range(0,5):
        if(a_huts[i].get_destroy==1):
            x_cor



def moove(a_archers,iiith,x_cor,y_cor,king,x_t,y_t,a_huts,a_walls,townhall):
        for i in range(0,4):
            x_cor2.append(a_archers[i].get_posx[i])
            y_cor2.append(a_archers[i].get_posy[i])
        arr=Archers_movement(x_cor,y_cor,iiith,king,x_t,y_t,x_cor2,y_cor2)    
        
        for i in range(0,4):
          var=a_archers[i]
          var2 = time.time() - (var.get_starttime() + var.get_steps())
        #   print(var2)
          if(var2 >= var.get_speed() and var2< 2*(var.get_speed())):
            var=a_archers[i]
            attack_archers(var,iiith,x_cor,y_cor,x_t,y_t,a_huts, a_walls, townhall)
            # print(result)
               
            var.change_steps() 
            if(var.get_attackmode()==0):  
             iiith.clear(var)
             var.change_vel(arr[i][0],arr[i][1])
            #  x_cor[i]=arr[i][0]
            #  y_cor[i+7]=arr[i][1]
            if(var.get_destroy()==0): 
             iiith.objectc(var)
          check_neigh(var, iiith, x_cor2, y_cor2)


def check_gameoveru(a_all2,a_all,a_all3,m,n,p,q,u):
    w=0
    l=0
    ret=-1
    for i in a_all:
        if(i.get_destroy()==1):
            w+=1
    for i in a_all3:
        if(i.get_destroy()==1):
            w+=1  
    for i in a_all2:
        if(i.get_destroy()==1):
            l+=1
    c=14-((5-m)+(4-n)+(4-p))
    if(l==14):
        print("YOU LOSE")
        ret=0
    if(w==6+q+u):
        print("YOU WIN") 
        ret=1           

    return ret                 

