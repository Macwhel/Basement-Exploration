from cmu_112_graphics import *
from player import *
from map import *
from rectangle import *
from mob import *

def appStarted(app):
    # these are things that'll change depending on difficulty
    app.rows, app.cols = (20, 20)
    numOfMobs = 4

    app.sW = min(app.width / app.rows, app.height / app.rows)

    # initilalize map and then get start locations for player and end goal as
    # well as acceptable mob locations
    '''Adjust maxTuns and maxLen scalings on difficulty'''
    app.gameMap, app.pLoc, app.gLoc, mLocs = createMap(
        (app.rows, app.cols), int(1.2 * (app.rows + app.cols)), app.rows // 2.5)
    app.player = Player(app.pLoc[0], app.pLoc[1], app.sW / 3)
    
    # make a list of unique mob spawning locations
    app.mobListLoc = random.sample(mLocs, numOfMobs)

    # create a list of mob classes
    app.mobList = [Mob(i[1], i[0], app.sW / 3, 10) for i in app.mobListLoc]



    # for bugtesting
    '''for i in app.gameMap:
        print(i)'''

    # initialize mobs in random locations

# this is a little scuffed so change it later to be cleaner

def keyPressed(app, event):
    lastCoords = (app.player.y, app.player.x)

    if (event.key == 'Up'): app.player.y -= 1
    if (event.key == 'Down'): app.player.y += 1
    if (event.key == 'Right'): app.player.x += 1
    if (event.key == 'Left'): app.player.x -= 1

    pY = app.player.getY()
    pX = app.player.getX()

    if (pY not in range(app.rows) or pX not in range(app.cols) or 
        app.gameMap[pY][pX] == 0):
        app.player.setY(lastCoords[0])
        app.player.setX(lastCoords[1])
    
    

def redrawAll(app, canvas):
    for i in range(len(app.gameMap)):
        for j in range(len(app.gameMap[0])):
            cell = Rectangle(i * app.sW, j * app.sW, app.sW)

            if app.gameMap[i][j] == 0:
                cell.setColor('black')
            else:
                if (i, j) == app.gLoc:
                    cell.setColor('green')
                else: 
                    cell.setColor('white')

            canvas.create_rectangle(cell.x, cell.y, cell.x2, cell.y2, fill = 
                                    cell.color, width = 0)

            # coords for player
            x = app.player.x * app.sW + (app.sW / 2)
            y = app.player.y * app.sW + (app.sW / 2)

            # draw player
            canvas.create_oval(
                x - app.player.radius,
                y - app.player.radius,
                x + app.player.radius,
                y + app.player.radius,
                fill = app.player.color)

            # draw mobs
            for mob in app.mobList:
                x = mob.x * app.sW + (app.sW / 2)
                y = mob.y * app.sW + (app.sW / 2)
                canvas.create_oval(
                    x - mob.rad,
                    y - mob.rad,
                    x + mob.rad,
                    y + mob.rad,
                    fill = "red"
                )





if __name__ == "__main__":
    runApp(width = 400, height = 400)
