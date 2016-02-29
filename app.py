import curses
import thread
import time

class Sound:
    def __init__(self):
        self.useless = True
    def beep():
        curses.beep()

class Screen:
    def __init__(self):
        self.screen = None

    def create(self):
        self.screen = curses.initscr()
        tup = self.screen.getmaxyx()
        self.x = tup[0]
        self.y = tup[1]

    def destroy(self):
        curses.endwin()

    def refresh(self):
        self.screen.refresh()

    def repch(self, x, y, c):
        self.screen.delch(x, y)
        self.screen.addch(x, y, c)

class World:
    def __init__(self):

        self.objects = []

    def addObject(self, obj):
        self.objects.append(obj)

    def tick():
        for obj in self.objects:
            obj.tick()
        
class Object:
    def __init__(self, pattern):
        self.pattern = pattern
        self.x = 0
        self.y = 0

    def moveTo(self, x, y):
        self.x = x
        self.y = y
        
    def draw(self, screen):
        if self.pattern is isinstance(self.pattern, str):
            self.drawString(screen)
        else:
            self.drawMatrix(screen)

    def drawString(self, screen):
        index = 0
        for c in self.pattern:
            screen.repch(self.x + index, self.y, c)
            index += 1
            
    def drawMatrix(self, screen):
        for w in range(0, len(self.pattern)):
            for h in range(0, len(self.pattern[w])):
                if pattern[w][h] is not '':
                    screen.repch(self.x + w, self.y + h, self.pattern[w][h])
    def tick(self):
        self.x += 1
        self.y += 1
        
class Engine:
    def __init__(self, screen, world):
        self.screen = screen
        self.world = world
        self.stop = False
        
    def stop(self):
        self.stop = True
        
    def renderLoop(self):
        while True:
            if self.stop:
                break
            self.render()
            
    def render(self):
        for obj in self.world.objects:
            obj.draw(screen)
        screen.refresh()

    def tickLoop():
        while True:
            if self.stop:
                break
            self.world.tick()
        
screen = Screen()
screen.create()
world = World()
engine = Engine(screen, world)

pattern = '@'
obj = Object(pattern)

world.addObject(obj)

thread.start_new_thread(engine.renderLoop())

time.sleep(2)
obj.moveTo(5,5)
