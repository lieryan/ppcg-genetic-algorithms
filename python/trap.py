import coordinates
from sys import version_info

if version_info >= (3,):
    xrange = range

class Trap(object):
    possible_directions = []
    max_traps = 4

    def __init__(self, board, direction):
        self.board = board
        self.direction = direction

    def turn(self, coordinate):
        pass

    def moved_to(self, coordinate, origin):
        pass

    def color(self):
        return self.color


class DeathTrap(Trap):
    possible_directions = coordinates.directions

    def turn(self, coordinate):
        self.board.specimens.pop(coordinate, 0)


class TeleportationTrap(Trap):
    possible_directions = [coordinates.Coordinate(x,y) for x in xrange(-5, 6)
                           for y in xrange(-5, 6) if x != 0 or y != 0]

    def moved_to(self, coordinate, origin):
        if coordinate+self.direction in self.board.next_specimens:
            self.board.next_specimens[coordinate+self.direction].extend(
                self.board.next_specimens[coordinate])
        else:
            self.board.next_specimens[coordinate+self.direction] = \
                self.board.next_specimens[coordinate]
        del self.board.next_specimens[coordinate]


class WallTrap(Trap):
    possible_directions = [coordinates.Coordinate(0, 0)]*4
    def moved_to(self, coordinate, origin):
        if origin in self.board.next_specimens:
            self.board.next_specimens[origin].extend(
                self.board.next_specimens[coordinate])
        else:
            self.board.next_specimens[origin] = \
                self.board.next_specimens[coordinate]
        del self.board.next_specimens[coordinate]


trap_types = DeathTrap, TeleportationTrap, WallTrap