import numpy as np

class Table(object):
    def __init__(self, size = (1024, 1024)):
        self.size = size
        self.table = np.zeros((size[0], size[1], 3))
        self.table.fill(255)

        for i in range(0, size[0]):
            for j in range(0, size[1]):
                if ((i + j) % 2):
                    self.setPointType(i, j, True)

    def getPointType(self, x, y):
        return False if ((x + y) % 2) else True

    def setPointType(self, x, y, type):
        if self.isOutOfBounds(x, y):
            return False
    
        self.table[x, y] = [0, 0, 0] if type else [255, 255, 255]

    def isOutOfBounds(self, x, y):
        return True if (x >= self.size[0] or y >= self.size[1]) else False
    
    def getNextPointByDirection(self, positionX, positionY, direction, step = 1):
        movements = {
            360: (0,  1),   # up
            270: (-1, 0),   # left
            180: (0, -1),   # down
            90:  (1,  0)    # right
        }

        dx, dy = movements.get(direction, (0, 0))
        _positionX = positionX + dx * step
        _positionY = positionY + dy * step
        
        if self.isOutOfBounds(_positionX, _positionY):
            return False
        
        return (_positionX, _positionY)

    def getTable(self):
        return self.table