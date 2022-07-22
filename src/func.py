import colorama
from colorama import Fore, Back, Style
import time
from src.objects import *
from src.config import *
from src.village import village
import random
import numpy as np
colorama.init()

def check_gameover(king,troop0,troop1,troop2,troop3,troop4,hut0,hut1,hut2,hut3,hut4,townhall):
    l=0
    w=0
    arr=[]
    if(king.get_destroy()==1):
         l+=1
    if(troop0.get_destroy()==1):
         l+=1
    if(troop1.get_destroy()==1):
         l+=1
    if(troop2.get_destroy()==1):
         l+=1
    if(troop3.get_destroy()==1):
         l+=1
    if(troop4.get_destroy()==1):
         l+=1
    if(hut0.get_destroy()==1):
         w+=1
    if(hut1.get_destroy()==1):
         w+=1
    if(hut2.get_destroy()==1):
         w+=1
    if(hut3.get_destroy()==1):
         w+=1
    if(hut4.get_destroy()==1):
         w+=1
    if(townhall.get_destroy()==1):
         w+=1     
    arr.append(l)
    arr.append(w)
    return arr  


def clearobj(iiith,varia2):
    if(varia2.get_hitpoints()<=0):
        iiith.clear(varia2)
        varia2.change_destroy()

def changecolour(iiith,varia2):
    if(varia2.get_hitpoints()> 20 and varia2.get_hitpoints() <=50):
        varia2.change_color1()
        iiith.objectc(varia2)
    if(varia2.get_hitpoints()<= 20 and varia2.get_hitpoints() >0):
        varia2.change_color2()
        iiith.objectc(varia2)
    if(varia2.get_hitpoints()<=0):
        iiith.clear(varia2)
        varia2.change_destroy()

def check_inbetween(tempo2, iiith, nodes, node):
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


def closest_node(node, nodes):
    # nodes = np.asarray(nodes)
    dist = np.sum((nodes - node)**2, axis=0)
    # print(dist)
    minElement = np.amin(dist)
    # print(minElement)
    result = np.where(dist == np.amin(dist))
    temp = result[0]
    # print(temp)
    return temp[0]


def write_all_coor(iiith, x_cor, y_cor):
    xco = []
    yco = []
    for i in range(0, 5):
        xco.append(x_cor[i])
        yco.append(y_cor[i])

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


def Troops_movement(x_cor, y_cor, iiith, king,x_t,y_t):
    nodes = write_all_coor(iiith, x_cor, y_cor)
    arr = []
    for i in range(0, 5):
        node = np.array([[x_cor[i+7], y_cor[i+7]]]).T
        # print(node)
        tempo = closest_node(node, nodes)
        tempo2 = np.array([[nodes[0][tempo], nodes[1][tempo]]]).T
        tempo3 = check_inbetween(tempo2, iiith, nodes, node)
        # print(tempo3)
        arr.append(tempo3)
    return arr


def attack_troops(troopsee, iiith, x_cor, y_cor,x_t,y_t):
    ran = -1
    nodes = write_all_coor(iiith, x_cor, y_cor)
    node = np.array([[troopsee.get_posx(), troopsee.get_posy()]]).T
    x_coor = [1, 1, -1, -1, 1, 0, -1, 0]
    y_coor = [1, -1, 1, -1, 0, 1, 0, -1]
    # letter = ["RU","RD","LU","LD","R","U","L","D"]
    arr = [x_coor, y_coor]
    arr2 = np.asarray(arr)
    arr3 = arr2 + node
    distance = []
    nodest = np.transpose(nodes)
    for i in range(0, 8):
        # p=(arr3[:,i] in nodest.tolist())
        result = np.where((nodest == arr3[:, i]).all(axis=1))
        if(len(result[0]) != 0):
          if(iiith.get_char(arr3[0][i], arr3[1][i]) == 'H'):
            # troopsee.change_attackmode()
            ran = (result[0][0])
        #   if(iiith.get_char(arr3[0][i], arr3[1][i]) == 'L'):
        #     # troopsee.change_attackmode()
        #     ran = 5  
    return ran

def write_all_coor3(iiith, x_cor, y_cor):
    xco = []
    yco = []
    for i in range(0, 8):
        xco.append(x_cor[i+12])
        yco.append(y_cor[i+12])

    n = []
    n.append(xco)
    n.append(yco)
    # print(n)
    nodes = np.asarray(n)
    # print(nodes)
    return nodes

def write_all_coor4(iiith, x_cor, y_cor, x_t,y_t):
    xco = []
    yco = []
    for i in range(0, 5):
        xco.append(x_cor[i])
        yco.append(y_cor[i])

    for i in range(0,3):
        for j in range(0,3):
           xco.append(x_t+i)  
           yco.append(y_t+j)

    n = []
    n.append(xco)
    n.append(yco)
    # print(n)
    nodes = np.asarray(n)
    # print(nodes)
    return nodes    
   

def check_neigh(troopsee, iiith, x_cor, y_cor):
    ran = -1
    # nodes = write_all_coor3(iiith, x_cor, y_cor)
    node = np.array([[troopsee.get_posx(), troopsee.get_posy()]]).T
    x_coor = [1, 1, -1, -1, 1, 0, -1, 0]
    y_coor = [1, -1, 1, -1, 0, 1, 0, -1]
    # letter = ["RU","RD","LU","LD","R","U","L","D"]
    arr = [x_coor, y_coor]
    arr2 = np.asarray(arr)
    arr3 = arr2 + node
    distance = []
    # nodest = np.transpose(nodes)
    for i in range(0, 8):
        # p=(arr3[:,i] in nodest.tolist())
        # result = np.where((nodest == arr3[:, i]).all(axis=1))
        # if(len(result[0]) != 0):
          if(iiith.get_char(arr3[0][i], arr3[1][i]) == 'H'):
            # troopsee.change_attackmode()
            ran = 1
    if(ran==1):
        troopsee.change_attackmode(0)

def check_inrange(tempo2, iiith, cannon1):
    x_pos=cannon1.get_posx()
    y_pos=cannon1.get_posy()
    inrange=0
    if(tempo2[0]<=x_pos+5 and tempo2[0]>=x_pos-5 and tempo2[1]<=y_pos+5 and tempo2[1]>=y_pos-5):
        inrange=1 
    return inrange


def write_all_coor2(iiith, x_cor, y_cor, king):
    xco = []
    yco = []
    for i in range(7, 12):
        xco.append(x_cor[i])
        yco.append(y_cor[i])
    xco.append(king.get_posx())
    yco.append(king.get_posy())
    n = []
    n.append(xco)
    n.append(yco)
    # print(n)
    nodes = np.asarray(n)
    # print(nodes)
    return nodes

def fire_bullets(iiith,x1,y1,x2,y2,cannon1):
    n=x2-x1
    bullet=Bullets(x1,y1)
    for i in range(1,n+1):
     iiith.objectc(bullet)   
     x=x1+i   
     y= y1+int(((y2-y1)*n)/(x2-x1))
     bullet=Bullets(x,y)
     iiith.objectc(bullet)    

    #  iiith.clear(bullet)
    #  iiith.objectc(bullet)
    #getnearest king or troop , check whether they are in the range, fire the bullet along shortest path...
    

def cannon_attack(iiith, cannon1, x_cor, y_cor, king, cannon2):
    nodes = write_all_coor2(iiith, x_cor, y_cor,king)
    arr = []
    for i in range(0, 2):
        node = np.array([[x_cor[i+5], y_cor[i+5]]]).T
        # print(node)
        tempo = closest_node(node, nodes)
        # tempo2 gives nearest king or node array position
        tempo2 = np.array([nodes[0][tempo], nodes[1][tempo]])
        if(i==0):
         tempo3 = check_inrange(tempo2, iiith, cannon1)
        if(i==1):
         tempo3 = check_inrange(tempo2, iiith, cannon2)   
        arr.append(tempo)
        # print(tempo)
        if(tempo3==0):
            # print(cannon1.get_posx(),cannon1.get_posy(),nodes[0][tempo],nodes[1][tempo])
            # fire_bullets(iiith,cannon1.get_posx(),cannon1.get_posy(),nodes[0][tempo],nodes[1][tempo],cannon1)
            arr[i]=-1
    return arr        
    


# def fire_bullets(cannon1,king,x_cor,y_cor):
#     #getnearest king or troop , check whether they are in the range, fire the bullet along shortest path...
#     pass

# get position of attack and find whose position it is, change its hitpoinrs
def getpositionofattack(iiith, king,nodes):
    x_coor = [1, 1, -1, -1, 1, 0, -1, 0]
    y_coor = [1, -1, 1, -1, 0, 1, 0, -1]
    letter = ["RU", "RD", "LU", "LD", "R", "U", "L", "D"]
    l = -1
    arr = [x_coor, y_coor]
    arr2 = np.asarray(arr)
    node = np.array([[king.get_posx(), king.get_posy()]]).T
    arr3 = arr2 + node
    # for i in range(0,5):
    #     nodes.append(arr3[:,i])
    nodest = np.asarray(nodes).T
    for i in range(0, 8):
        # print(arr3)
        # print(str(iiith.get_char(0, 1)))
        li = np.where((nodest == arr3[:, i]).all(axis=1))
        if(len(li[0])!=0):
          if(iiith.get_char(arr3[0][i], arr3[1][i]) == 'H'):
        #    li = np.where((nodest == arr3[:, i]).all(axis=1))
        #    if(len(li[0])!=0):
            l=li[0][0]
          if(iiith.get_char(arr3[0][i], arr3[1][i]) == 'L'):
            l=5
    return l           
