import colorama
from colorama import Fore, Back, Style
import time
from src.objects import *
from src.config import *
from src.village import village
import random
import numpy as np
colorama.init()

def check_destroyed4(a_huts,townhall):
    p=0
    for i in range(0,5):
        if(a_huts[i].get_destroy()==1):
            p+=1
    if(townhall.get_destroy()==1):
        p+=1        
    if(p==6):
        return 1
    else:
        return 0

def clearobj4(iiith,varia2):
    if(varia2.get_hitpoints()<=0):
        iiith.clear(varia2)
        varia2.change_destroy()

def changecolour4(iiith,varia2):
    if(varia2.get_hitpoints()> 20 and varia2.get_hitpoints() <=50):
        varia2.change_color1()
        iiith.objectc(varia2)
    if(varia2.get_hitpoints()<= 20 and varia2.get_hitpoints() >0):
        varia2.change_color2()
        iiith.objectc(varia2)
    if(varia2.get_hitpoints()<=0):
        iiith.clear(varia2)
        varia2.change_destroy()

def check_inbetween3(tempo2, iiith, nodes, node):
    x_coor = [1, 1, -1, -1, 1, 0, -1, 0]
    y_coor = [1, -1, 1, -1, 0, 1, 0, -1]
    letter = ["RU", "RD", "LU", "LD", "R", "U", "L", "D"]
    arr = [x_coor, y_coor]
    arr2 = np.asarray(arr)
    arr3 = arr2 + node
    distance = []
    nodest = np.transpose(nodes)
    tempii=np.asarray([-30,-90])
    # for i in range(0, 8):
    #     # p=(arr3[:,i] in nodest.tolist())
    #     # if(p!=True):
    #       if(iiith.get_char(arr3[0][i], arr3[1][i]) != ' ' ):
    #         arr3[:, i] = tempii
        #   if(iiith.get_char(arr3[0][i], arr3[1][i]) != ' ' and iiith.get_char(arr3[0][i], arr3[1][i]) == 'W'):
            
             

    arr4 = np.sum((arr3-tempo2)**2, axis=0)
    # print(arr4)
    minElement = np.amin(arr4)
    result = np.where(arr4 == np.amin(arr4))
    # print(result)
    temp = arr3[:, result[0][0]]
    return temp    


def closest_node3(node, nodes):
    # nodes = np.asarray(nodes)
    dist = np.sum((nodes - node)**2, axis=0)
    # print(dist)
    minElement = np.amin(dist)
    # print(minElement)
    result = np.where(dist == np.amin(dist))
    temp = result[0]
    # print(temp)
    return temp[0]

def write_all_cooraaa2(iiith, d_huts,d_walls,townhall):
    xco = []
    yco = []
    for key,value in d_huts.items():
        xco.append(value[0])
        yco.append(value[1])
    
    # for key,value in d_walls.items():
    #     xco.append(value[0])
    #     yco.append(value[1])
    if(townhall.get_destroy()!=1):
     xco.append(townhall.get_posx())
     yco.append(townhall.get_posy())
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


def write_all_cooraaa3(iiith, d_huts,d_walls,d_all,townhall,d_all3):
    xco = []
    yco = []
    for key,value in d_all3.items():
        xco.append(value[0])
        yco.append(value[1])
    
    # for key,value in d_walls.items():
    #     xco.append(value[0])
    #     yco.append(value[1])
    
    # xco.append(townhall.get_posx())
    # yco.append(townhall.get_posy())
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

# def check_neigh2(troopsee, iiith):
#     print("z")
#     ran = -1
#     # nodes = write_all_coor3(iiith, x_cor, y_cor)
#     node = np.array([[troopsee.get_posx(), troopsee.get_posy()]]).T
#     x_coor = [1, 1, -1, -1, 1, 0, -1, 0]
#     y_coor = [1, -1, 1, -1, 0, 1, 0, -1]
#     # letter = ["RU","RD","LU","LD","R","U","L","D"]
#     arr = [x_coor, y_coor]
#     arr2 = np.asarray(arr)
#     arr3 = arr2 + node
#     distance = []
#     # nodest = np.transpose(nodes)
#     for i in range(0, 8):
#         # p=(arr3[:,i] in nodest.tolist())
#         # result = np.where((nodest == arr3[:, i]).all(axis=1))
#         # if(len(result[0]) != 0):
#           if(iiith.get_char(arr3[0][i], arr3[1][i]) == 'H' or iiith.get_char(arr3[0][i], arr3[1][i]) == 'L' or iiith.get_char(arr3[0][i], arr3[1][i]) == 'W'):
#             # troopsee.change_attackmode()
#             ran = 1
#     if(ran==1):
#         troopsee.change_attackmode(0)

def check_neigh3(troopsee, iiith):
    # print("z")
    ran = -1
    node = [troopsee.get_posx(), troopsee.get_posy()]
    # for i in range(0, 6):
    #     for j in range(0,6):
    if(node[0] >=1 and node[0] <=28 and node[1] >=0 and node[1] <=89):   
        if(iiith.get_char(node[0], node[1]) == 'H' or iiith.get_char(node[0], node[1]) == 'L' or iiith.get_char(node[0], node[1]) == 'W' or iiith.get_char(node[0], node[1])=='8'):
            # troopsee.change_attackmode()
            ran = 1
    if(ran==1):
        troopsee.change_attackmode(0)        


def attack_balloons2(troopsee, iiith, d_huts,d_walls,d_all,townhall,d_all3):
    # print("y")
    ran = -1
    nodes = write_all_cooraaa3(iiith, d_huts,d_walls,d_all,townhall,d_all3)
    x_a=troopsee.get_posx()
    y_a=troopsee.get_posy()
    # mini=-10000
    arra2=[0,0]
    
    bb2 = -1
    nodest = np.transpose(nodes)
    for key,value in d_all3.items():
        x_i=value[0]
        y_i=value[1]
        if(x_i == x_a and y_i == y_a):
            bb2=key
            
    return bb2




def final_step3(arr,iiith, king,d_huts,d_walls,d_balloons,d_all,d_all3,townhall,a_huts,a_walls,a_balloons,a_all3,num_cann,num_tower,d_all2):
    for key,value in d_balloons.items():
        i=key
        if(a_balloons[i].get_destroy()!=1):
        #   print("x")
          var=a_balloons[i]
          var2 = time.time() - (var.get_starttime() + var.get_steps())
        #   print(var2)
          if(var2 >= var.get_speed() and var2< 2*(var.get_speed())):
            var=a_balloons[i]
            result=attack_balloons2(var,iiith,d_huts,d_walls,d_all,townhall,d_all3)
            # print(result)
            if(result>=0 and result<num_cann):
                var.change_attackmode(1)
                # var.change_char1()
                # var.put_prev()
                bru2=a_all3[result]
                bru2.change_char1()
                # var.put_prev(iiith.get_char(d_all3[result][0],d_all3[result][1]))
                bru2.change_hitpoints(-1*var.get_damage())
                changecolour4(iiith,bru2)              
                if(bru2.get_hitpoints()<=0):
                    d_all3.pop(result)
                    iiith.clear(bru2)
                    var.change_attackmode(0)    
                #    print(result)
            if(result>=num_cann and result<num_cann+num_tower):
                var.change_attackmode(1)
                bru2=a_all3[result]
                bru2.change_char1()
                bru2.change_hitpoints(-1*var.get_damage())
                changecolour4(iiith,bru2)             
                if(bru2.get_hitpoints()<=0):
                    d_all3.pop(result)
                    iiith.clear(bru2)
                    var.change_attackmode(0) 
            if(var.get_attackmode()==0):  
             iiith.clear(var)
             var.change_vel(arr[i][0],arr[i][1])
             d_balloons[i]=arr[i]
             d_all2[i+9]=arr[i]
            if(var.get_destroy()==0):    
             iiith.objectc(var)           
          check_neigh3(var, iiith)    

def Balloons_movement2(iiith, king,d_huts,d_walls,d_balloons,d_all,d_all3,townhall,a_huts,a_walls,a_balloons,a_all3,num_cann,num_tower,d_all2):
    nodes = write_all_cooraaa3(iiith, d_huts,d_walls,d_all,townhall,d_all3)
    arr = {}
    # print(len(d_balloons))
    for key,value in d_balloons.items():
        node = np.array([[value[0],value[1]]]).T
        print(nodes)
        tempo = closest_node3(node, nodes)
        tempo2 = np.array([[nodes[0][tempo], nodes[1][tempo]]]).T
        tempo3 = check_inbetween3(tempo2, iiith, nodes, node)
        # print(tempo3)
        arr[key]=tempo3
        # print(arr[key])
    final_step3(arr,iiith, king,d_huts,d_walls,d_balloons,d_all,d_all3,townhall,a_huts,a_walls,a_balloons,a_all3,num_cann,num_tower,d_all2)


    