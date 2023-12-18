import matplotlib.pyplot as plt
from tableModel import Table

# util function
def setDirection(direction):
    if ((direction) < 0):
        direction = 270
    elif ((direction) > 360):
        direction = 90

    return direction

# create world
table = Table((1024, 1024))

# set ant start params
startX = 512
startY = 512
direction = 360

while(True):
    nextPos = table.getNextPointByDirection(startX, startY, direction)
    if (not nextPos):
        break

    if (table.getPointType(nextPos[0], nextPos[1])):
        direction = setDirection(direction - 90)
        table.setPointType(nextPos[0], nextPos[1], not table.getPointType(nextPos[0], nextPos[1]))
    
    else:
        direction = setDirection(direction + 90)
        table.setPointType(nextPos[0], nextPos[1], table.getPointType(nextPos[0], nextPos[1]))

    startX = nextPos[0]
    startY = nextPos[1]


# Output
result = table.getTable()
plt.imshow(result)
plt.show()