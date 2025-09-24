def setup():
    size(700, 700)
    background(0)
    
    stroke(255)
    for x in range(1, 11):
        for y in range(1,11):
            index = int(random(6))
            if index == 0:
                drawShapeOne(x * 50 + 10 * x, y * 50 + 10 * y)
            elif index == 1:
                drawShapeTwo(x * 50 + 10 * x, y * 50 + 10 * y)
            elif index == 2:
                drawShapeThree(x * 50 + 10 * x, y * 50 + 10 * y)
            elif index == 3:
                drawShapeFour(x * 50 + 10 * x, y * 50 + 10 * y)
            elif index == 4:
                drawShapeFive(x * 50 + 10 * x, y * 50 + 10 * y)
            elif index == 5:
                drawShapeSix(x * 50 + 10 * x, y * 50 + 10 * y)
    
def drawShapeOne(x, y):
    stroke(255)
    line(x, y, x + 50, y)
    line(x, y + 50, x + 50, y + 50)

def drawShapeTwo(x, y):
    stroke(255)
    line(x, y, x, y + 50)
    line(x + 50, y, x + 50, y + 50)
    
def drawShapeThree(x, y):
    stroke(255)
    line(x,y,x+50,y)
    line(x+50,y+50,x+50,y)
    
def drawShapeFour(x, y):
    stroke(255)
    line(x,y,x+50,y)
    line(x,y,x,y + 50)
    
def drawShapeFive(x, y):
    stroke(255)
    line(x,y + 50,x + 50, y + 50)
    line(x + 50, y+ 50, x+ 50, y)

def drawShapeSix(x, y):
    stroke(255)
    line(x,y,x,y + 50)
    line(x,y + 50, x+ 50,y+ 50)
        
    
