import random

class NBA:
    #Class Attributes (Apply to all instances of the class)
    ball_size = 29.5
    ball_type = 'Wilson'
    name = 'National Basketball Association'

    def __init__(self, player, city, mascot, pos):
        #Instance Attributes (Different for every instance, but every instance has to have these)
        self.player = player
        self.city = city
        self.mascot = mascot
        self.pos= pos

#Making a new object from a class (Instantiating)
P1 = NBA('Demar DeRozan', 'Chicago', 'Bulls','SF')
P2 = NBA('LeBron James', 'LA', 'Lakers', 'PF')
P3 = NBA('John Wall', 'Houston','Rockets','PG')
P4 = NBA('Russel Westbrook', 'LA', 'Lakers', 'PG')
P5 = NBA('Steph Curry', 'Golden State', 'Warriors', 'PG')

value = [P1, P2, P3, P4, P5]

play = random.choice(value)

gChoice = [1,2,3]
g= random.choice(gChoice)

while input() != play.player:
    if g == 1:
        print('He plays in ' + play.city)
        g=2
    elif g ==2:
        print('The mascot of his team is ' + play.mascot) 
        g=3
    elif g ==3 :
        print ('His position is '+ play.pos)
        g=1
else:
    print('Correct!')



        

  
