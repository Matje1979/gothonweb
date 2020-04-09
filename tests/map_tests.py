from nose.tools import *
from gothonweb.map import *



def test_room():
    gold = Room("GoldRoom",
                """
                This room has gold in it you can grab. There's a door to the 
                north.""", 1)
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths,{})
    
def test_room_paths():
    center = Room("Center", "Test the room in the center.", 1)
    north = Room("North", "Test the room in the north.", 1)
    south = Room("South", "Test the room in the south.", 1)
    
    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)
    
def test_map():
    start = Room("Start", "You can go west and down a hole.", 1)
    west = Room("Trees", "There are trees here, you can go east.", 1)
    down = Room("Dungeon", "It's dark down here, you can go up.", 1)

    start.add_paths({"west": west, "down": down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})
    
    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)
    
def test_gothon_game_map():
    assert_equal(START.go('shoot!'), shoot_death)
    assert_equal(START.go('dodge!'), dodge_death)
    
    room = START.go('tell a joke')
    assert_equal(room, laser_weapon_armory)
    

    
    