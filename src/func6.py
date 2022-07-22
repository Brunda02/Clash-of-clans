import colorama
from colorama import Fore, Back, Style
import time
from src.objects import *
from src.config import *
from src.village import village
import random
import numpy as np
colorama.init()

def check_destroyed6(a_all2):
    r=1
    for v in a_all2:
        if(v.get_destroy()==0):
            r=0
            break
    return r    

def clearobj8(iiith,varia2,d_all2,r,d_troops,d_archers,d_balloons):
    print(r)
    if(varia2.get_hitpoints()<=0):
        if(r>=0 and r<=4):
         d_troops.pop(r)
        #  iiith.clear(varia2)
        if(r>=5 and r<=8):

         d_archers.pop(r-5)
        #  iiith.clear(varia2)
        if(r>=9 and r<=12):
        #  d_balloons.pop(r-9)
        #  a_all2[r].set_colour()
        #  iiith.clear(varia2)
         d_balloons.pop(r-9)
        iiith.clear(varia2) 
        d_all2.pop(r)
        varia2.change_destroy()
           


def closest_nodex(node, nodes):
    # nodes = np.asarray(nodes)
    dist = np.sum((nodes - node)**2, axis=0)
    # print(dist)
    minElement = np.amin(dist)
    # print(minElement)
    result = np.where(dist == np.amin(dist))
    temp = result[0]
    # print(temp)
    return temp[0]

def check_r(node,value):
    xo=max(abs(node[0]-value[0]),abs(node[1]-value[1])) 
    # print(xo)
    if(xo<=6):
        return 1
    else:
        return 0       

def write_all_coord2(iiith, d_all2,king,node):
    xco = []
    yco = []
    for key,value in d_all2.items():
       if(check_r(node,value)==1): 
        xco.append(value[0])
        yco.append(value[1])
    
    # for key,value in d_walls.items():
    #     xco.append(value[0])
    #     yco.append(value[1])
    # value=[king.get_posx(),king.get_posy()]
    # if(king.get_destroy()==0 and check_r(node,value)==1):
    #  xco.append(king.get_posx())
    #  yco.append(king.get_posy())
    n = []
    n.append(xco)
    n.append(yco)
    # print(n)
    nodes = np.asarray(n)
    # print(nodes)
    # nodes=nodes.transpose()
    # nodes = nodes[~np.all(nodes == 0, axis=1)]
    # nodes=nodes.transpose()
    # print(nodes)
    return nodes

def write_all_coord3(iiith, d_all2,king,node):
    xco = []
    yco = []
    for key,value in d_all2.items():
       if(check_r(node,value)==1 and (key<=8 or key==13)): 
        xco.append(value[0])
        yco.append(value[1])
    
    # for key,value in d_walls.items():
    #     xco.append(value[0])
    #     yco.append(value[1])
    # value=[king.get_posx(),king.get_posy()]
    # if(king.get_destroy()==0 and check_r(node,value)==1):
    #  xco.append(king.get_posx())
    #  yco.append(king.get_posy())
    n = []
    n.append(xco)
    n.append(yco)
    # print(n)
    nodes = np.asarray(n)
    # print(nodes)
    # nodes=nodes.transpose()
    # nodes = nodes[~np.all(nodes == 0, axis=1)]
    # nodes=nodes.transpose()
    # print(nodes)
    return nodes    

def check_nei(iiith,d_all2,r,a_all2,d,d_troops,d_archers,d_balloons):
    x_a=d_all2[r][0]
    y_a=d_all2[r][1]
    ar=[]
    print(d_all2)
    for key,value in d_all2.items():
        xo=max(abs(d_all2[r][0]-value[0]),abs(d_all2[r][1]-value[1]))
        # print(xo) 
        if(xo<=1):
         a_all2[key].change_hitpoints(-1*d)
        #  print(key)
         ar.append(key)
    for c in ar:     
         clearobj8(iiith,a_all2[c],d_all2,c,d_troops,d_archers,d_balloons)

# def check_nei2(iiith,d_all2,r,a_all2,d):
#     x_a=d_all2[r][0]
#     y_a=d_all2[r][1]
#     ar=[]
#     for key,value in d_all2.items():
#         xo=max(abs(d_all2[r][0]-value[0]),abs(d_all2[r][1]-value[1])) 
#         if(xo==0):
#          a_all2[key].change_hitpoints(-1*d)
#         #  print(key)
#          ar.append(key)
#         #  print(ar)
#     for c in ar:     
#          clearobj8(iiith,a_all2[c],d_all2,c)


def attack_tower(iiith,d_all2,king,d_towers,a_all2,a_towers,d_troops,d_archers,d_balloons,b_time3):
    # nodes = write_all_coord2(iiith, d_all,king)
    arr = {}
    # print(len(d_archers))
    for key,value in d_towers.items():
       varii= time.time()-(a_towers[key].get_starttime()+a_towers[key].get_steps())
    #    varii=time.time()-b_time3
    #    print(varii)
       if(varii>=1 and varii<2):
        # print(varii)
        # print('y')   
        node2=[value[0],value[1]]
        nodes = write_all_coord2(iiith, d_all2,king,node2)
        node = np.array([[value[0],value[1]]]).T
        # print(nodes)
        # print(node)
        if(len(nodes[0])!=0):
         tempo = closest_nodex(node, nodes)
         tempo2 = [nodes[0][tempo], nodes[1][tempo]]
         bb=[key2 for key2, value2 in d_all2.items() if value2[0] == tempo2[0] and value2[1]==tempo2[1]]
         r=bb[0]
        #  print(r)
         d=a_towers[key].get_damage()
        #  a_all2[r].change_hitpoints(-1*a_towers[key].get_damage())
         check_nei(iiith,d_all2,r,a_all2,d,d_troops,d_archers,d_balloons)
        #  clearobj8(iiith,all2[r],d_all2,r)
        a_towers[key].change_steps()
    #    a_towers[key].change_steps()  


        # tempo3 = check_inbetween2(tempo2, iiith, nodes, node)
        # print(tempo3)
        # arr[key]=tempo3

def attack_cannons(iiith,d_all2,king,d_towers,a_all2,a_towers,d_troops,d_archers,d_balloons,b_time4):
    # nodes = write_all_coord2(iiith, d_all,king)
    arr = {}
    # print(len(d_archers))
    for key,value in d_towers.items():
       varii= time.time()-(a_towers[key].get_starttime()+a_towers[key].get_steps())
    #    print(varii)
    #    varii = time.time()-b_time4
    #    print(varii)
    #    print("x")
       if(varii>=1 and varii<=2):
        # print('y')   
        node2=[value[0],value[1]]
        nodes = write_all_coord3(iiith, d_all2,king,node2)
        node = np.array([[value[0],value[1]]]).T
        # print(nodes)
        if(len(nodes[0])!=0):
         tempo = closest_nodex(node, nodes)
         tempo2 = [nodes[0][tempo], nodes[1][tempo]]
         bb=[key2 for key2, value2 in d_all2.items() if value2[0] == tempo2[0] and value2[1]==tempo2[1]]
         r=bb[0]
        #  print(r)
         d=a_towers[key].get_damage()
        #  a_all2[r].change_hitpoints(-1*a_towers[key].get_damage())
         a_all2[r].change_hitpoints(-1*d)
         clearobj8(iiith,a_all2[r],d_all2,r,d_troops,d_archers,d_balloons)
        #  clearobj8(iiith,all2[r],d_all2,r)
        a_towers[key].change_steps()

