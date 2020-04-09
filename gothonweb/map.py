class Room(object):
    def __init__(self, name, description, attempts):
        self.name = name
        self.description = description
        self.attempts = attempts
        self.paths = {}
        self.right_path = []
        
    def go(self, direction):
        return self.paths.get(direction)
        
        
    def add_paths(self, paths):
        return self.paths.update(paths)
        
    def update_attempts(self, num):
        self.attempts -= num
        
    def add_right_path(self, a_path):
        self.right_path.append(a_path)
        
central_corridor = Room("Central Corridor", 
                        
"""
The Gothon's of Planet Percal #25 have invaded your ship  and
destroyed your entire crew. You are the last surviving member 
and your last mission is to get the neutron destruct bomb from
the Weapons Armory, put it in the bridge, and blow the ship up
after getting into an escape pod

You are running down the central corridor to the Weapons Armory
when a Gothon jumps out, red scaly skin, dark grimy teeth and evil clown costume
flowing around his hate filled body. He's blocking the door to
the Armory and about to pull the weapon to blast you.
What will you do? Shoot? Dodge? Tell a joke?
""",1
)

laser_weapon_armory = Room("Laser Weapon Armory",

"""
Lucky for you they made you learn Gothon insults in the academy.
You tell one Gothon joke you know: Lbhe zbgure vf fb sng, jura fur 
fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr.
The Gothon stops, tries not to laugh, then busts out laughing and 
can't move. While he's laughing you run up and shoot him square in 
the head putting him down, then jump throught the Weapon Armory door.

You do a dive roll into the Weapon Armory, crouch and scan the room
for more Gothons that might be hidding. It's dead quiet, too quiet.
You stand up and run to the far side of the room and find the neutron 
bomb in its container. There's a keypad lock on the box and you need the
code to get the bomb out. If you get the code wrong 10 times then the lock
closes forever and you can't get the bomb. The code is 3 digits (between 1 and 3).
""", 5
)
    
the_bridge = Room("The Bridge", 
                  
"""
The container clicks open and the seal breaks, letting gas out.
You grab the neautron bomb and run as fast as you can to the bridge 
where you must place it in the right spot.

You burst onto the bridge with the neutron destruct bomb under
your arm and surprise 5 Gothons who are trying to take control of the ship.
Each of them has an even uglier clown costume than the last. They haven't
pulled out their weapons yet as they see the active bomb under your arm
and don't want to set it off.

What do you do?

1) Throw the bomb!
2) Slowly place the bomb!
""", 1
)

escape_pod = Room("Escape Pod",
                  
"""
You point your blaster at the bomb under your arm and the 
Gothons put their hands up and start to sweat.
you inch backward to the door, open it, and then carefully place the bomb 
on the floor, pointing your blaster at it.
You then jump back through the door, punch the close button
and blast the lock so the Gothons can't get out. 
Now the bombm is placed you run to the escape pod to get off this tin
can.

Your rush through the ship desperately trying to make it to the
escape pod before the whole ship explodes. It seems like hardly any 
Gothons are on the ship, so your run is clear of interference. You get
to the chamber with the escape pods, and need to pick one to take. Some
of them could be demaged but you don't have time to look. there's 5 pods,
which one do you take?
""", 1
)

the_end_winner = Room("Win",
                      
"""
You jump into pod 2 and hit the eject button.
The pod easily slides out into space heading to the planet 
bellow. As it flies to the planet, you look back and see your ship
implode then explode like a bright star, taking out the Gothon ship
at the same time. You won!
""", 1
)

the_end_loser = Room("The End",
        
"""
You jump into a random pod and hit the eject button.
The pod escapes out in the void of space, then implodes as the
hull ruptures, crushing your body into jam jelly.
""", 1
)

escape_pod.add_paths({
    '2':the_end_winner,
    '*':the_end_loser
})

escape_pod.add_right_path('2')

generic_death = Room("death", "You died", 1)

bridge_death = Room("The End",
"""
In a panic you throw the bomb at the group of Gothons and 
make a leap for the door. Right as you drop it a Gothon shoots you
right in the back killing you. 
As you die you see another Gothon frantically try to disarm the bomb.
You die knowing they will probably blow up when it goes off.
""", 1
)

shoot_death = Room('The End', 
"""   
Quick on the draw you yank out your blaster and fire it at 
the Gothon. His clown costume is flowing  and moving around his body,
which throws off your aim. Your laser hits his costume, but misses 
him entirely. This completely ruins his brand new costume, his mother
bought him, which makes him fly into a rage and blast you repeatedly 
in the face until you  are dead. Then he eats you.
""", 1
)

dodge_death = Room('The End', 

"""    
Like a world class boxer you dodge , weave, slip and side 
right as the Gothon's blaster cranks a laser past your head.In the 
middle of your artful dodge your foot slips and you bang your head 
on the metal wall and pass out. You wake up shortly after only to die 
as the Gothon stomps on your head and eats you.
""", 1
)

armory_death = Room('The End', 
"""   
The lock buzzes one last time and then you hear a 
sickening melting sound as the mechanism is fused together. You 
decide to sit there, and finally the Gothons blow up the ship from 
their ship and you die.
""", 1
)

the_bridge.add_paths({
    'Throw the bomb!': bridge_death,
    'Slowly place the bomb!': escape_pod
})

the_bridge.add_right_path('slowly place the bomb')

laser_weapon_armory.add_paths ({
    '132':the_bridge,
    '*':armory_death
})

laser_weapon_armory.add_right_path('132')

central_corridor.add_paths({
    'shoot!':shoot_death,
    'dodge!':dodge_death,
    'tell a joke!': laser_weapon_armory
})

central_corridor.add_right_path('tell a joke')

START = central_corridor


    #def represent(self):
        #print "The name of this room is %s" % self.name
        #print self.description
        
    #def check_name_lenght(self):
        #lenght = 0
        #for i in self.name:
            #lenght +=1
        #return lenght
    
    #def update_description(self):
        #self.description = self.description + "," + str(self.check_name_lenght())
        #print self.description
    
    
    
            
    
    