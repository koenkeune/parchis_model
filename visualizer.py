import pygame

def drawBoard(screen, W, H):
    pygame.display.set_caption('Parchis')
    
    global BLACK, WHITE, RED, GREEN, BLUE, YELLOW, GRAY
    
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0,0, 255)
    YELLOW = (255, 255, 0)
    GRAY = (192, 192, 192)
    screen.fill(WHITE)

    # colored places:
    pygame.draw.rect(screen, RED, ((4*W)/9, H/21, W/9, (43*H)/126 + 1)) ### base
    pygame.draw.rect(screen, YELLOW, ((4*W)/9, (11*H)/18, W/9, (43*H)/126 + 1))
    pygame.draw.rect(screen, GREEN, (W/21, (4*H)/9, (43*H)/126 + 1, H/9))
    pygame.draw.rect(screen, BLUE, ((11*W)/18, (4*H)/9, (43*H)/126 + 1, H/9))
    pygame.draw.rect(screen, RED, (W/3, (4*H)/21, W/9, H/21 + 1)) ### startingPoint
    pygame.draw.rect(screen, YELLOW, ((5*W)/9, (16*H)/21, W/9, H/21 + 1))
    pygame.draw.rect(screen, GREEN, ((4*W)/21, (5*H)/9, W/21 + 1, H/9))
    pygame.draw.rect(screen, BLUE, ((16*W)/21, H/3, W/21 + 1, H/9))
    pygame.draw.polygon(screen, RED, (((7*W)/18, (7*H)/18), (W/2, H/2), ((11*W)/18, (7*H)/18))) ### home square filled
    pygame.draw.polygon(screen, GREEN, (((7*W)/18, (7*H)/18), (W/2, H/2), ((7*W)/18, (11*H)/18)))
    pygame.draw.polygon(screen, YELLOW, (((11*W)/18, (11*H)/18), (W/2, H/2), ((7*W)/18, (11*H)/18)))
    pygame.draw.polygon(screen, BLUE, (((11*W)/18, (11*H)/18), (W/2, H/2), ((11*W)/18, (7*H)/18)))

    # contours of the board:
    lines = [[((3*W)/9, 0), ((3*W)/9, H/3)], [((4*W)/9, 0), ((4*W)/9, H/3)],
             [((5*W)/9, 0), ((5*W)/9, H/3)], [((6*W)/9, 0), ((6*W)/9, H/3)],
             [(W/3, 0), ((2*W)/3, 0)], [(W/3, H/21), ((2*W)/3, H/21)], 
             [(W/3, (2*H)/21), ((2*W)/3, (2*H)/21)], [(W/3, (3*H)/21), ((2*W)/3, (3*H)/21)],
             [(W/3, (4*H)/21), ((2*W)/3, (4*H)/21)], [(W/3, (5*H)/21), ((2*W)/3, (5*H)/21)],
             [(W/3, (6*H)/21), ((2*W)/3, (6*H)/21)], [(W/3, (7*H)/21), ((2*W)/3, (7*H)/21)],
             [((4*W)/9, (2*H)/3), ((4*W)/9, H)], [((5*W)/9, (2*H)/3), ((5*W)/9, H)],
             [((3*W)/9, (2*H)/3), ((3*W)/9, H)], [((4*W)/9, (2*H)/3), ((4*W)/9, H)], ### second square
             [((5*W)/9, (2*H)/3), ((5*W)/9, H)], [((6*W)/9, (2*H)/3), ((6*W)/9, H)],
             [(W/3, (14*H)/21), ((2*W)/3, (14*H)/21)], [(W/3, (15*H)/21), ((2*W)/3, (15*H)/21)], 
             [(W/3, (16*H)/21), ((2*W)/3, (16*H)/21)], [(W/3, (17*H)/21), ((2*W)/3, (17*H)/21)],
             [(W/3, (18*H)/21), ((2*W)/3, (18*H)/21)], [(W/3, (19*H)/21), ((2*W)/3, (19*H)/21)],
             [(W/3, (20*H)/21), ((2*W)/3, (20*H)/21)], [(W/3, H-1), ((2*W)/3, H-1)],
             [(0, (3*H)/9), (W/3, (3*H)/9)], [(0, (4*H)/9),(W/3, (4*H)/9)], ### third square
             [(0, (5*H)/9), (W/3, (5*H)/9)], [(0, (6*H)/9),(W/3, (6*H)/9)],
             [(0, H/3), (0, (2*H)/3)], [(W/21, H/3), (W/21, (2*H)/3)],
             [((2*W)/21, H/3), ((2*W)/21, (2*H)/3)], [((3*W)/21, H/3), ((3*W)/21, (2*H)/3)],
             [((4*W)/21, H/3), ((4*W)/21, (2*H)/3)], [((5*W)/21, H/3), ((5*W)/21, (2*H)/3)],
             [((6*W)/21, H/3), ((6*W)/21, (2*H)/3)], [((7*W)/21, H/3), ((7*W)/21, (2*H)/3)],
             [((2*W)/3, H/3), (W, H/3)], [((2*W)/3, (4*H)/9),(W, (4*H)/9)], ### fourth square
             [((2*W)/3, (5*H)/9), (W, (5*H)/9)], [((2*W)/3, (6*H)/9),(W, (6*H)/9)],
             [((14*W)/21, H/3), ((14*W)/21, (2*H)/3)], [((15*W)/21, H/3), ((15*W)/21, (2*H)/3)],
             [((16*W)/21, H/3), ((16*W)/21, (2*H)/3)], [((17*W)/21, H/3), ((17*W)/21, (2*H)/3)],
             [((18*W)/21, H/3), ((18*W)/21, (2*H)/3)], [((19*W)/21, H/3), ((19*W)/21, (2*H)/3)],
             [((20*W)/21, H/3), ((20*W)/21, (2*H)/3)], [(W-1, H/3), (W-1, (2*H)/3)],
             [(W/3,H/3),((2*W)/3,(2*H)/3)],[((2*W)/3,H/3),(W/3,(2*H)/3)], ### cross lines
             [((7*W)/18,(7*H)/18),((7*W)/18,(11*H)/18)],[((7*W)/18,(7*H)/18),((11*W)/18,(7*H)/18)], ### inner square
             [((7*W)/18,(11*H)/18),((11*W)/18,(11*H)/18)],[((11*W)/18,(11*H)/18),((11*W)/18,(7*H)/18)],
             [((4*W)/9,(6*H)/18),((4*W)/9,(7*H)/18)],[((5*W)/9,(6*H)/18),((5*W)/9,(7*H)/18)], ### home square
             [((6*W)/18,(4*H)/9),((7*W)/18,(4*H)/9)],[((6*W)/18,(5*H)/9),((7*W)/18,(5*H)/9)],
             [((11*W)/18,(4*H)/9),((12*W)/18,(4*H)/9)],[((11*W)/18,(5*H)/9),((12*W)/18,(5*H)/9)],
             [((4*W)/9,(11*H)/18),((4*W)/9,(12*H)/18)],[((5*W)/9,(11*H)/18),((5*W)/9,(12*H)/18)]]
    for line in lines:
        pygame.draw.line(screen, BLACK, line[0], line[1], 2)

    # safespots:
    circles = [[(W/2, H/42), True], [(W/2, (41*H)/42), True], [(W/42, H/2), True], [((41*W)/42, H/2), True],
               [((7*W)/18, (9*H)/42), False], [((11*W)/18, (9*H)/42), True], [((7*W)/18, (33*H)/42), True], [((11*W)/18, (33*H)/42), False],
               [((9*W)/42, (7*H)/18), True], [((9*W)/42, (11*H)/18), False], [((33*W)/42, (7*H)/18), False], [((33*W)/42, (11*H)/18), True]]
    for circle in circles:
        pygame.draw.circle(screen, BLACK, circle[0], H/42 -4, 2)
        if circle[1]:
            pygame.draw.circle(screen, GRAY, circle[0], H/42 -6, 0)
     
    # homes:
    circleHomes = [[(W/6, H/6), RED, GREEN], [(W/6, (5*H)/6), GREEN, YELLOW], [((5*W)/6, (5*H)/6), YELLOW, BLUE], [((5*W)/6, H/6), BLUE, RED]] 
    for circleHome in circleHomes:
        pygame.draw.circle(screen, circleHome[1], circleHome[0], W/6 - 10, 0)
        pygame.draw.circle(screen, BLACK, circleHome[0], W/6 - 10, 2)
        pygame.draw.circle(screen, BLACK, circleHome[0], ((W/6 - 10)*2)/3, 2)
        pygame.draw.circle(screen, circleHome[2], circleHome[0], (W/6 - 10)/3, 0)
        pygame.draw.circle(screen, BLACK, circleHome[0], (W/6 - 10)/3, 2)

    # numbers:
    myfont = pygame.font.SysFont("calibri", 18)
    for i in range(1,9):
        screen.blit(myfont.render(str(i), 1, BLACK), ((5*W)/9 + 5, ((21-i)*H)/21 + 12))
        screen.blit(myfont.render(str(34-i), 1, BLACK), ((5*W)/9 + 5, ((i-1)*H)/21 + 12))
        screen.blit(myfont.render(str(34+i), 1, BLACK), ((11*W)/27 + 12, ((i-1)*H)/21 + 12))
        screen.blit(myfont.render(str(68-i), 1, BLACK), ((11*W)/27 + 12, ((21-i)*H)/21 + 12))
        screen.blit(myfont.render(str(51-i), 1, BLACK), (((i-1)*W)/21 + 18, (11*H)/27 + 12))
        screen.blit(myfont.render(str(51+i), 1, BLACK), (((i-1)*W)/21 + 18, (5*H)/9 + 5))
        screen.blit(myfont.render(str(17+i), 1, BLACK), (((21-i)*H)/21 + 12, (11*H)/27 + 12))
        screen.blit(myfont.render(str(17-i), 1, BLACK), (((21-i)*H)/21 + 12, (5*H)/9 + 5))
    screen.blit(myfont.render(str(34), 1, BLACK), (W/2 - 9, 12))
    screen.blit(myfont.render(str(68), 1, BLACK), (W/2 - 9, (20*H)/21 + 12))
    screen.blit(myfont.render(str(51), 1, BLACK), (12, H/2 - 9))
    screen.blit(myfont.render(str(17), 1, BLACK), ((20*W)/21 + 12, H/2 - 9))

def getDrawingPos(posOfPawn, playerNum, twoPawns, pawnsInBase, W, H):
    if posOfPawn == -1 and playerNum == 2:
        homePos = [(W/6 + 25, H/6 + 25), (W/6 - 25, H/6 + 25), (W/6 + 25, H/6 - 25), (W/6 - 25, H/6 - 25)]
        pos = homePos[pawnsInBase - 1]
    elif posOfPawn == -1 and playerNum == 3:
        homePos = [(W/6 + 25, (5*H)/6 + 25), (W/6 - 25, (5*H)/6 + 25), (W/6 + 25, (5*H)/6 - 25), (W/6 - 25, (5*H)/6 - 25)]
        pos = homePos[pawnsInBase - 1]
    elif posOfPawn == -1 and playerNum == 1:
        homePos = [((5*W)/6 + 25, H/6 + 25), ((5*W)/6 - 25, H/6 + 25), ((5*W)/6 + 25, H/6 - 25), ((5*W)/6 - 25, H/6 - 25)]
        pos = homePos[pawnsInBase - 1]
    elif posOfPawn == -1 and playerNum == 0:
        homePos = [((5*W)/6 + 25, (5*H)/6 + 25), ((5*W)/6 - 25, (5*H)/6 + 25), ((5*W)/6 + 25, (5*H)/6 - 25), ((5*W)/6 - 25, (5*H)/6 - 25)]
        pos = homePos[pawnsInBase - 1]
    if posOfPawn in range(8):
        pos = ((5*W)/9 + W/19 + 4, ((41-(posOfPawn*2))*H)/42)
    elif posOfPawn in range(25,33):
        pos = ((5*W)/9 + W/19 + 4, ((15-((posOfPawn-25)*2))*H)/42)
    elif posOfPawn in range(59, 67):
        pos = ((3*W)/9 + W/19 + 4, ((27+((posOfPawn-59)*2))*H)/42)
    elif posOfPawn in range(34, 42):
        pos = ((3*W)/9 + W/19 + 4, ((1+((posOfPawn-34)*2))*H)/42)
    elif posOfPawn in range(42, 50):
        pos = (((15-((posOfPawn-42)*2))*W)/42, (3*H)/9 + H/19 + 4)
    elif posOfPawn in range(17, 25):
        pos = (((41-((posOfPawn-17)*2))*W)/42, (3*H)/9 + H/19 + 4)
    elif posOfPawn in range(8, 16):
        pos = (((27+((posOfPawn-8)*2))*W)/42, (5*H)/9 + H/19 + 4)
    elif posOfPawn in range(51, 59):
        pos = (((1+((posOfPawn-51)*2))*W)/42, (5*H)/9 + H/19 + 4)
    elif posOfPawn == 67:
        pos = (W/2, ((41)*H)/42)
    elif posOfPawn == 50:
        pos = (W/42, H/2)
    elif posOfPawn == 33:
        pos = (W/2, H/42)
    elif posOfPawn == 16:
        pos = ((41*W)/42, H/2)
        
    if twoPawns > 0:
        if posOfPawn in list(range(8)) + list(range(25,42)) + list(range(59, 67)):
            if twoPawns == 1:
                posX = pos[0] - W/42
            elif twoPawns == 2:
                posX = pos[0] + W/42
            pos = (posX, pos[1])
        elif posOfPawn in list(range(8,25)) + list(range(42,59)):
            if twoPawns == 1:
                posY = pos[1] - H/42
            elif twoPawns == 2:
                posY = pos[1] + H/42
            pos = (pos[0], posY)
    
    return(pos)
        
def getPlayerColor(playerNum):
    if playerNum == 0:
        return(YELLOW)
    elif playerNum == 1:
        return(BLUE)
    elif playerNum == 2:
        return(RED)
    elif playerNum == 3:
        return(GREEN)

def drawPawn(posOfPawn, playerNum, screen, W, H, twoPawns, pawnsInBase):
    pos = getDrawingPos(posOfPawn, playerNum, twoPawns, pawnsInBase, W, H)
    color = getPlayerColor(playerNum)
    if color == RED:
        darkColor = (200, 0, 0)
    elif color == BLUE:
        darkColor = (0,0, 200)
    elif color == YELLOW:
        darkColor = (200, 200, 0)
    elif color == GREEN:
        darkColor = (0, 200, 0)
    posX = pos[0]
    posY = pos[1]
    pygame.draw.circle(screen, color, pos, H/42 - 2, 0)
    pygame.draw.circle(screen, darkColor, pos, H/42 - 2, 4)
    pygame.draw.line(screen, darkColor, (posX - 8, posY - 8), (posX + 8, posY + 8), 4)
    pygame.draw.line(screen, darkColor, (posX + 8, posY - 8), (posX - 8, posY + 8), 4)
    

    

