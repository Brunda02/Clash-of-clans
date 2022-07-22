Notes
--> followed OOP in building this game we've different classes where each of them represents --buildings --kings --canons --barbarian --archers --balloons etc --> here few classes are inherited from parent classes example: hut class is inherited from building class, king is child class of person (parent class) etc

-->each of classes have different methods and constructors for example:

def __init__(self):

    self.hit_pts=1
    
    self.damage=2
    
    self.health=30
    
this is constructor for person's class
Encapsulation:
it is a way where we bundle data and methods together. we've bundled attributes and methods in a class. so, we've used encapsulation

Polymorphism
it is about having different interfaces for same function. for example if we want to calculate addition of 2 numbers. now we can write different functions with same name where one of it taes integers, other takes decimals etc.

Execution
run python3 game.py

enter 'K' for choosing king and 'Q' for choosing queen

use -A for moving king to left

-D -->move king to right

-S -->move king down

-W --> move king up

spacebar -->to attack huts/townhalls

G,P,I--> create barbarian

J,K,L---> creates balloons

M,N,O-->creates archers

-Q-->quit game