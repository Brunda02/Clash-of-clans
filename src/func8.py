import colorama
from colorama import Fore, Back, Style
import time
from src.objects import *
from src.config import *
from src.village import village
import random
import numpy as np
colorama.init()

def bhutan(a_all3):
    bn=0
    for u in a_all3:
        if(u.get_destroy()==1):
            bn+=1
    if(bn==len(a_all3)):
        return 1
    else:
        return 0

def check_destroyed9(a_huts,townhall):
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

def clearobj9(iiith,varia2):
    if(varia2.get_hitpoints()<=0):
        iiith.clear(varia2)
        varia2.change_destroy()

def changecolour9(iiith,varia2):
    if(varia2.get_hitpoints()> 20 and varia2.get_hitpoints() <=50):
        varia2.change_color1()
        iiith.objectc(varia2)
    if(varia2.get_hitpoints()<= 20 and varia2.get_hitpoints() >0):
        varia2.change_color2()
        iiith.objectc(varia2)
    if(varia2.get_hitpoints()<=0):
        iiith.clear(varia2)
        varia2.change_destroy()

def check_inbetween9(tempo2, iiith, nodes, node):
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


def closest_node9(node, nodes):
    # nodes = np.asarray(nodes)
    dist = np.sum((nodes - node)**2, axis=0)
    # print(dist)
    minElement = np.amin(dist)
    # print(minElement)
    result = np.where(dist == np.amin(dist))
    temp = result[0]
    # print(temp)
    return temp[0]

def write_all_cooraal(iiith, d_huts,d_walls,townhall,d_all):
    xco = []
    yco = []
    # for key,value in d_all.items():
    #     xco.append(value[0])
    #     yco.append(value[1])
    for key,value in d_all.items():
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


def write_all_cooraa9(iiith, d_huts,d_walls,townhall,d_all3):
    xco = []
    yco = []
    # for key,value in d_all.items():
    #     xco.append(value[0])
    #     yco.append(value[1])
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

def check_neigh9(troopsee, iiith):
    # print("z")
    ran = -1
    node = [troopsee.get_posx(), troopsee.get_posy()]
    # for i in range(0, 6):
    #     for j in range(0,6):
    if(node[0] >=1 and node[0] <=28 and node[1] >=0 and node[1] <=89):   
          if(iiith.get_char(node[0], node[1]) == 'H' or iiith.get_char(node[0], node[1]) == 'L' or iiith.get_char(node[0], node[1]) == 'W'):
            # troopsee.change_attackmode()
            ran = 1
    if(ran==1):
        troopsee.change_attackmode(0)        


def attack_archers9(troopsee, iiith, d_huts,d_walls,d_all,townhall,d_all3,a_all3):
    # print("y")
    if(bhutan(a_all3)==0):
        nodes = write_all_cooraa9(iiith, d_huts,d_walls,townhall,d_all3)
        bbn=22
    else:
        nodes = write_all_cooraal(iiith, d_huts,d_walls,townhall,d_all)
        bbn=0
    x_a=troopsee.get_posx()
    y_a=troopsee.get_posy()
    # mini=-10000
    arra2=[0,0]
    
    bb2 = -23
    nodest = np.transpose(nodes)
    for key,value in d_all3.items():
        x_i=value[0]
        y_i=value[1]
        if(x_i == x_a and y_i == y_a):
            bb2=key
            
    return bb2+bbn

def checki(iiith,arr):
    if(iiith.get_char(arr[0],arr[1])=='H'  or iiith.get_char(arr[0],arr[1])=='W' or iiith.get_char(arr[0],arr[1])=='L' or iiith.get_char(arr[0],arr[1])!='T' or iiith.get_char(arr[0],arr[1])!='A ' or iiith.get_char(arr[0],arr[1])!='K' or iiith.get_char(arr[0],arr[1])!='Q'):
        return 1
    else:
        return 0     




def final_step9(arr,iiith, king,d_huts,d_walls,d_archers,d_all,townhall,a_huts,a_walls,a_archers,d_all3,d_towers,d_cannons,a_all3,d_all2):
    for key,value in d_archers.items():
        i=key
        # print(i)
        if(a_archers[i].get_destroy()!=1):
        #   print("x")
          var=a_archers[i]
          var2 = time.time() - (var.get_starttime() + var.get_steps())
        #   print(var2)
          if(var2 >= var.get_speed() and var2< 2*(var.get_speed())):
            var=a_archers[i]
            result=attack_archers9(var,iiith,d_huts,d_walls,d_all,townhall,d_all3,a_all3)
            # print(result)
            # for result in result2:
            if(result>=0 and result<=4):
                var.change_attackmode(1)
                # bru="hut"+str(result)
                bru2=a_huts[result]
                # bru2=locals()[bru]
                bru2.change_hitpoints(-1*var.get_damage())
                changecolour9(iiith,bru2)
                
                if(bru2.get_hitpoints()<=0):
                    d_huts.pop(result)
                    d_all.pop(result)
                    iiith.clear(bru2)
                   
                #    x_cor[result]=-30
                #    y_cor[result]=-90
                    var.change_attackmode(0)    
                #    print(result)
            if(result>=5 and result<=12):
                var.change_attackmode(1)
                # bru2.change_char1()
                # bru="hut"+str(result)
                bru2=a_walls[result-5]
                # bru2=locals()[bru]
                bru2.change_hitpoints(-1*var.get_damage())
                changecolour9(iiith,bru2)
                
                if(bru2.get_hitpoints()<=0):
                    d_walls.pop(result-5)
                    d_all.pop(result)
                    iiith.clear(bru2)
                    
                   
                #    x_cor[result]=-30
                #    y_cor[result]=-90
                    var.change_attackmode(0)    
            if(result>=13 and result<=21):
                var.change_attackmode(1)
                # bru2.change_char1()
                townhall.change_hitpoints(-4)
                changecolour9(iiith,townhall)
                if(townhall.get_hitpoints()<=0):
                # iiith.clear(bru2)
                    for ini in range(13,22):
                     d_all.pop(ini)
                    iiith.clear(townhall)
                    var.change_attackmode(0) 
            if(result>=22 and result<=24):
                var.change_attackmode(1)
                # var.change_attackmode(1)
                # bru="hut"+str(result)
                bru2=a_all3[result-22]
                # bru2.change_char1()
                bru2.change_hitpoints(-1*var.get_damage())
                changecolour9(iiith,bru2)
                
                if(bru2.get_hitpoints()<=0):
                    d_cannons.pop(result-22)
                    d_all3.pop(result-22)
                    iiith.clear(bru2)
                   
                #    x_cor[result]=-30
                #    y_cor[result]=-90
                    var.change_attackmode(0)
                
            if(result>=25 and result<=27):
                var.change_attackmode(1)
                # var.change_attackmode(1)
                # bru="hut"+str(result)
                bru2=a_all3[result-22]
                # bru2.change_char1()
                # bru2=locals()[bru]
                bru2.change_hitpoints(-1*var.get_damage())
                changecolour9(iiith,bru2)
                
                if(bru2.get_hitpoints()<=0):
                    d_towers.pop(result-25)
                    d_all3.pop(result-22)
                    iiith.clear(bru2)
                   
                #    x_cor[result]=-30
                #    y_cor[result]=-90
                    var.change_attackmode(0)            
            var.change_steps() 
            if(var.get_attackmode()==0):  
             iiith.clear(var)
            #  print(arr[i][0])
            #  xi=arr[i]
             var.change_vel(arr[i][0],arr[i][1])
            #  x_cor[i+7]=arr[i][0]
            #  y_cor[i+7]=arr[i][1]
             d_archers[i]=arr[i]
             d_all2[i+9]=arr[i]
            if(var.get_destroy()==0 and var.get_attackmode()==0 and checki(iiith,arr[i])==1): 
             iiith.objectc(var)
          check_neigh9(var, iiith)    

    

def Archers_movement9(iiith, king,d_huts,d_walls,d_archers,d_all,townhall,a_huts,a_walls,a_archers,d_all3,d_towers,d_cannons,a_all3,d_all2):
    if(bhutan(a_all3)!=1):
        nodes = write_all_cooraa9(iiith, d_huts,d_walls,townhall,d_all3)
    else:
        nodes= write_all_cooraal(iiith, d_huts,d_walls,townhall,d_all)

    arr = {}
    # print(len(d_archers))
    for key,value in d_archers.items():
        node = np.array([[value[0],value[1]]]).T
        # print(node)
        tempo = closest_node9(node, nodes)
        tempo2 = np.array([[nodes[0][tempo], nodes[1][tempo]]]).T
        tempo3 = check_inbetween9(tempo2, iiith, nodes, node)
        # print(tempo3)
        arr[key]=tempo3
        # print(arr[key])
    final_step9(arr,iiith, king,d_huts,d_walls,d_archers,d_all,townhall,a_huts,a_walls,a_archers,d_all3,d_towers,d_cannons,a_all3,d_all2)


    