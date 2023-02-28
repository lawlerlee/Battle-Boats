import random
import pygame
from pygame import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

#setup pygame
mainClock = pygame.time.Clock()

#define screen size
screen_width = 900
screen_height = 900

#setup screen
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Battle Boats')

#load images
menuBG = pygame.image.load('assets/menuBG.png')
gameOverIMG = pygame.image.load('assets/gameOverIMG.png')
youWinIMG = pygame.image.load('assets/youWinIMG.png')
newGameBTN = pygame.image.load('assets/new_btn.png')
newGameBTN = pygame.transform.scale(newGameBTN, (320, 320))
continueBTN = pygame.image.load('assets/continue_btn.png')
continueBTN = pygame.transform.scale(continueBTN, (320, 320))
howToBTN = pygame.image.load('assets/howto_btn.png')
howToBTN = pygame.transform.scale(howToBTN, (320, 320))
quitBTN = pygame.image.load('assets/quit_btn.png')
quitBTN = pygame.transform.scale(quitBTN, (320, 320))
Title = pygame.image.load('assets/Title.png')
instructions = pygame.image.load('assets/instructions.png')
backBTN = pygame.image.load('assets/back_btn.png')
backBTN = pygame.transform.scale(backBTN, (240, 240))
gamegrid = pygame.image.load('assets/gamegrid.png')
SAQbtn = pygame.image.load('assets/SAQ_btn.png')
SAQbtn = pygame.transform.scale(SAQbtn, (120, 120))
chooseboat = pygame.image.load('assets/chooseboat.png')
chooseboat = pygame.transform.scale(chooseboat, (170, 50))
newGameBTNr = pygame.image.load('assets/new_btnR.png')
newGameBTNr = pygame.transform.scale(newGameBTNr, (320, 320))
continueBTNr = pygame.image.load('assets/continue_btnR.png')
continueBTNr = pygame.transform.scale(continueBTNr, (320, 320))
howToBTNr = pygame.image.load('assets/howto_btnR.png')
howToBTNr = pygame.transform.scale(howToBTNr, (320, 320))
quitBTNr = pygame.image.load('assets/quit_btnR.png')
quitBTNr = pygame.transform.scale(quitBTNr, (320, 320))
backBTNr = pygame.image.load('assets/back_btnR.png')
backBTNr = pygame.transform.scale(backBTNr, (240, 240))
SAQbtnR = pygame.image.load('assets/SAQ_btnR.png')
SAQbtnR = pygame.transform.scale(SAQbtnR, (120, 120))
chosenBoat = pygame.image.load('assets/chosenBoat.png')
chosenBoat = pygame.transform.scale(chosenBoat, (170, 50))
beginBTN = pygame.image.load('assets/begin_btn.png')
beginBTN = pygame.transform.scale(beginBTN, (320, 320))
fog = pygame.image.load('assets/fog.png')
fog = pygame.transform.scale(fog, (200, 80))
sunkship = pygame.image.load('assets/boatsunk.png')
sunkship = pygame.transform.scale(sunkship, (170, 50))
GOQuit = pygame.image.load('assets/quit_btn.png')
GOQuit = pygame.transform.scale(quitBTN, (360, 360))

#initialise mixer (Music and Sounds)
mixer.init()
splash = pygame.mixer.Sound('assets/splash.wav')
explosion = pygame.mixer.Sound('assets/explosion.mp3')

#set selected to false, will become True when tile selected so can't be picked twice
selected11 = False
selected12 = False
selected13 = False
selected14 = False
selected15 = False
selected16 = False
selected17 = False
selected18 = False
selected19 = False
selected20 = False
selected21 = False
selected22 = False
selected23 = False
selected24 = False
selected25 = False
selected26 = False
selected27 = False
selected28 = False
selected29 = False
selected30 = False
selected31 = False
selected32 = False
selected33 = False
selected34 = False
selected35 = False

click = False

class Button():                                        #Create Button Class 
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):
        action = False

        #get mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked condition
        if self.rect.collidepoint(pos):
            if click == True:
                action = True
            elif click == False:
                action = False

        #draw button
        screen.blit(self.image, self.rect)

        return action

#create buttons
newGameButton = Button(50, 300, newGameBTN)
continueButton = Button(520, 300, continueBTN)
howToButton = Button(50, 600, howToBTN)
quitButton = Button(520, 600, quitBTN)
backButton = Button(320, 700, backBTN)
SAQbutton = Button(30, 780, SAQbtn)
begin = Button(250, 250, beginBTN)
FinalQuit = Button(250, 500, GOQuit)

#choose ship positions
chooseBoat11 = Button(0, 430, chooseboat)
chooseBoat12 = Button(185, 430, chooseboat)
chooseBoat13 = Button(365, 430, chooseboat)
chooseBoat14 = Button(545, 430, chooseboat)
chooseBoat15 = Button(750, 430, chooseboat)
chooseBoat16 = Button(0, 500, chooseboat)
chooseBoat17 = Button(185, 500, chooseboat)
chooseBoat18 = Button(365, 500, chooseboat)
chooseBoat19 = Button(545, 500, chooseboat)
chooseBoat20 = Button(750, 500, chooseboat)
chooseBoat21 = Button(0, 580, chooseboat)
chooseBoat22 = Button(185, 580, chooseboat)
chooseBoat23 = Button(365, 580, chooseboat)
chooseBoat24 = Button(545, 580, chooseboat)
chooseBoat25 = Button(750, 580, chooseboat)
chooseBoat26 = Button(0, 650, chooseboat)
chooseBoat27 = Button(185, 650, chooseboat)
chooseBoat28 = Button(365, 650, chooseboat)
chooseBoat29 = Button(545, 650, chooseboat)
chooseBoat30 = Button(750, 650, chooseboat)
chooseBoat31 = Button(0, 725, chooseboat)
chooseBoat32 = Button(185, 725, chooseboat)
chooseBoat33 = Button(365, 725, chooseboat)
chooseBoat34 = Button(545, 725, chooseboat)
chooseBoat35 = Button(750, 725, chooseboat)

#add picked boats
pickedBoat11 = Button(0, 430, chosenBoat)
pickedBoat12 = Button(185, 430, chosenBoat)
pickedBoat13 = Button(365, 430, chosenBoat)
pickedBoat14 = Button(545, 430, chosenBoat)
pickedBoat15 = Button(750, 430, chosenBoat)
pickedBoat16 = Button(0, 500, chosenBoat)
pickedBoat17 = Button(185, 500, chosenBoat)
pickedBoat18 = Button(365, 500, chosenBoat)
pickedBoat19 = Button(545, 500, chosenBoat)
pickedBoat20 = Button(750, 500, chosenBoat)
pickedBoat21 = Button(0, 580, chosenBoat)
pickedBoat22 = Button(185, 580, chosenBoat)
pickedBoat23 = Button(365, 580, chosenBoat)
pickedBoat24 = Button(545, 580, chosenBoat)
pickedBoat25 = Button(750, 580, chosenBoat)
pickedBoat26 = Button(0, 650, chosenBoat)
pickedBoat27 = Button(185, 650, chosenBoat)
pickedBoat28 = Button(365, 650, chosenBoat)
pickedBoat29 = Button(545, 650, chosenBoat)
pickedBoat30 = Button(750, 650, chosenBoat)
pickedBoat31 = Button(0, 725, chosenBoat)
pickedBoat32 = Button(185, 725, chosenBoat)
pickedBoat33 = Button(365, 725, chosenBoat)
pickedBoat34 = Button(545, 725, chosenBoat)
pickedBoat35 = Button(750, 725, chosenBoat)

#add fog
fog11 = Button(0, -10, fog)
fog12 = Button(180, -10, fog)
fog13 = Button(350, -10, fog)
fog14 = Button(530, -10, fog)
fog15 = Button(720, -10, fog)
fog16 = Button(0, 70, fog)
fog17 = Button(180, 70, fog)
fog18 = Button(350, 70, fog)
fog19 = Button(530, 70, fog)
fog20 = Button(720, 70, fog)
fog21 = Button(0, 150, fog)
fog22 = Button(180, 150, fog)
fog23 = Button(350, 150, fog)
fog24 = Button(530, 150, fog)
fog25 = Button(720, 150, fog)
fog26 = Button(0, 230, fog)
fog27 = Button(180, 230, fog)
fog28 = Button(350, 230, fog)
fog29 = Button(530, 230, fog)
fog30 = Button(720, 230, fog)
fog31 = Button(0, 310, fog)
fog32 = Button(180, 310, fog)
fog33 = Button(350, 310, fog)
fog34 = Button(530, 310, fog)
fog35 = Button(720, 310, fog)

Fog11 = Button(-60, -10, fog)
Fog12 = Button(130, -10, fog)
Fog13 = Button(310, -10, fog)
Fog14 = Button(480, -10, fog)
Fog15 = Button(650, -10, fog)
Fog16 = Button(-60, 70, fog)
Fog17 = Button(130, 70, fog)
Fog18 = Button(310, 70, fog)
Fog19 = Button(480, 70, fog)
Fog20 = Button(650, 70, fog)
Fog21 = Button(-60, 150, fog)
Fog22 = Button(130, 150, fog)
Fog23 = Button(310, 150, fog)
Fog24 = Button(480, 150, fog)
Fog25 = Button(650, 150, fog)
Fog26 = Button(-60, 230, fog)
Fog27 = Button(130, 230, fog)
Fog28 = Button(310, 230, fog)
Fog29 = Button(480, 230, fog)
Fog30 = Button(650, 230, fog)
Fog31 = Button(-60, 310, fog)
Fog32 = Button(130, 310, fog)
Fog33 = Button(310, 310, fog)
Fog34 = Button(480, 310, fog)
Fog35 = Button(650, 310, fog)

#add sunkboats
Pboatsunk11 = Button(0, 430, sunkship)
Pboatsunk12 = Button(185, 430, sunkship)
Pboatsunk13 = Button(365, 430, sunkship)
Pboatsunk14 = Button(545, 430, sunkship)
Pboatsunk15 = Button(750, 430, sunkship)
Pboatsunk16 = Button(0, 500, sunkship)
Pboatsunk17 = Button(185, 500, sunkship)
Pboatsunk18 = Button(365, 500, sunkship)
Pboatsunk19 = Button(545, 500, sunkship)
Pboatsunk20 = Button(750, 500, sunkship)
Pboatsunk21 = Button(0, 580, sunkship)
Pboatsunk22 = Button(185, 580, sunkship)
Pboatsunk23 = Button(365, 580, sunkship)
Pboatsunk24 = Button(545, 580, sunkship)
Pboatsunk25 = Button(750, 580, sunkship)
Pboatsunk26 = Button(0, 650, sunkship)
Pboatsunk27 = Button(185, 650, sunkship)
Pboatsunk28 = Button(365, 650, sunkship)
Pboatsunk29 = Button(545, 650, sunkship)
Pboatsunk30 = Button(750, 650, sunkship)
Pboatsunk31 = Button(0, 725, sunkship)
Pboatsunk32 = Button(185, 725, sunkship)
Pboatsunk33 = Button(365, 725, sunkship)
Pboatsunk34 = Button(545, 725, sunkship)
Pboatsunk35 = Button(750, 725, sunkship)

boatsunk11 = Button(0, 10, sunkship)
boatsunk12 = Button(185, 10, sunkship)
boatsunk13 = Button(365, 10, sunkship)
boatsunk14 = Button(545, 10, sunkship)
boatsunk15 = Button(750, 10, sunkship)
boatsunk16 = Button(0, 100, sunkship)
boatsunk17 = Button(185, 100, sunkship)
boatsunk18 = Button(365, 100, sunkship)
boatsunk19 = Button(545, 100, sunkship)
boatsunk20 = Button(750, 100, sunkship)
boatsunk21 = Button(0, 180, sunkship)
boatsunk22 = Button(185, 180, sunkship)
boatsunk23 = Button(365, 180, sunkship)
boatsunk24 = Button(545, 180, sunkship)
boatsunk25 = Button(750, 180, sunkship)
boatsunk26 = Button(0, 260, sunkship)
boatsunk27 = Button(185, 260, sunkship)
boatsunk28 = Button(365, 260, sunkship)
boatsunk29 = Button(545, 260, sunkship)
boatsunk30 = Button(750, 260, sunkship)
boatsunk31 = Button(0, 330, sunkship)
boatsunk32 = Button(185, 330, sunkship)
boatsunk33 = Button(365, 330, sunkship)
boatsunk34 = Button(545, 330, sunkship)
boatsunk35 = Button(750, 330, sunkship)

#add empty tiles
empty11 = Button(0, 10, chooseboat)
empty12 = Button(185, 10, chooseboat)
empty13 = Button(365, 10, chooseboat)
empty14 = Button(545, 10, chooseboat)
empty15 = Button(750, 10, chooseboat)
empty16 = Button(0, 100, chooseboat)
empty17 = Button(185, 100, chooseboat)
empty18 = Button(365, 100, chooseboat)
empty19 = Button(545, 100, chooseboat)
empty20 = Button(750, 100, chooseboat)
empty21 = Button(0, 180, chooseboat)
empty22 = Button(185, 180, chooseboat)
empty23 = Button(365, 180, chooseboat)
empty24 = Button(545, 180, chooseboat)
empty25 = Button(750, 180, chooseboat)
empty26 = Button(0, 260, chooseboat)
empty27 = Button(185, 260, chooseboat)
empty28 = Button(365, 260, chooseboat)
empty29 = Button(545, 260, chooseboat)
empty30 = Button(750, 260, chooseboat)
empty31 = Button(0, 330, chooseboat)
empty32 = Button(185, 330, chooseboat)
empty33 = Button(365, 330, chooseboat)
empty34 = Button(545, 330, chooseboat)
empty35 = Button(750, 330, chooseboat)

#setup AI picking spots
availableSlots = ['11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35']
pickableSlots = ['11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35']
aiPicked = 0
aiLocations = []
botselected = []

#Set up player spots
spotsPicked = 0
playerLocations = []
boatsShown = 0

#other game data
aiSunk = 0
playerSunk = 0

#setup run
run = True
mainMenu = True
howto = False
newgame = False
turns = False
musicload = False
gameEnd = False

#play menu music when main menu is active
mixer.music.load('assets/battle.wav')
mixer.music.play(-1)


while run:

    clock.tick(fps)

    #creates main menu
    if mainMenu == True:
        screen.blit(menuBG, (0, 0))
        screen.blit(Title, (0, 30))
        if newGameButton.draw(): 
            #starts game music when new game button clicked
            mixer.music.load('assets/game.wav')
            mixer.music.play(-1)                   #starts game when new game button clicked
            newgame = True
            mainMenu = False
        continueButton.draw()                   #continues game if save data exists
        if howToButton.draw():                  #shows instructions when how to button clicked
            howto = True
            mainMenu = False
        if quitButton.draw():                   #quits game when quit button clicked
            run = False

    #creates instructions
    if howto == True:
        screen.blit(menuBG, (0, 0))
        screen.blit(instructions, (150, 50))
        if backButton.draw():
            howto = False
            mainMenu = True

    #begins game
    if newgame == True:
        if aiPicked < 5:                                 #if ai hasn't picked all spots yet it chooses 5 random spots
            aiSpots = random.choice(pickableSlots)
            while aiSpots in aiLocations:
                aiSpots = random.choice(pickableSlots)
            aiLocations.append(aiSpots)
            aiPicked += 1
            print (aiLocations)
        screen.blit(gamegrid, (0, 0))
        #creates save and quit button
        if SAQbutton.draw():
            run = False
        #places boats in 5 picked locations
        if chooseBoat11.draw() and selected11 == False:           #Adds boat if tile picked and hasn't been picked already and 5 spots haven't already been picked
            if spotsPicked == 5:
                selected11 = True
            elif spotsPicked <= 5:
                chooseBoat11 = pickedBoat11
                spotsPicked += 1
                playerLocations.append('11')
                print(spotsPicked)
                print(playerLocations)
                selected11 = True
                boatsShown += 1
        if chooseBoat12.draw() and selected12 == False:           #Repeats for all below V V V
            if spotsPicked == 5:
                selected12 = True
            elif spotsPicked <= 5:
                chooseBoat12 = pickedBoat12
                spotsPicked += 1
                playerLocations.append('12')
                print(spotsPicked)
                print(playerLocations)
                selected12 = True
                boatsShown += 1
        if chooseBoat13.draw() and selected13 == False:
            if spotsPicked == 5:
                selected13 = True
            elif spotsPicked <= 5:
                chooseBoat13 = pickedBoat13
                spotsPicked += 1
                playerLocations.append('13')
                print(spotsPicked)
                print(playerLocations)
                selected13 = True
                boatsShown += 1
        if chooseBoat14.draw() and selected14 == False: 
            if spotsPicked == 5:
                selected14 = True
            elif spotsPicked <= 5:
                chooseBoat14 = pickedBoat14
                spotsPicked += 1
                playerLocations.append('14')
                print(spotsPicked)
                print(playerLocations)
                selected14 = True
                boatsShown += 1
        if chooseBoat15.draw() and selected15 == False: 
            if spotsPicked == 5:
                selected15 = True
            elif spotsPicked <= 5:
                chooseBoat15 = pickedBoat15
                spotsPicked += 1
                playerLocations.append('15')
                print(spotsPicked)
                print(playerLocations)
                selected15 = True
                boatsShown += 1
        if chooseBoat16.draw() and selected16 == False: 
            if spotsPicked == 5:
                selected16 = True
            elif spotsPicked <= 5:
                chooseBoat16 = pickedBoat16
                spotsPicked += 1
                playerLocations.append('16')
                print(spotsPicked)
                print(playerLocations)
                selected16 = True
                boatsShown += 1
        if chooseBoat17.draw() and selected17 == False: 
            if spotsPicked == 5:
                selected17 = True
            elif spotsPicked <= 5:
                chooseBoat17 = pickedBoat17
                spotsPicked += 1
                playerLocations.append('17')
                print(spotsPicked)
                print(playerLocations)
                selected17 = True
                boatsShown += 1
        if chooseBoat18.draw() and selected18 == False: 
            if spotsPicked == 5:
                selected18 = True
            elif spotsPicked <= 5:
                chooseBoat18 = pickedBoat18
                spotsPicked += 1
                playerLocations.append('18')
                print(spotsPicked)
                print(playerLocations)
                selected18 = True
                boatsShown += 1
        if chooseBoat19.draw() and selected19 == False: 
            if spotsPicked == 5:
                selected19 = True
            elif spotsPicked <= 5:
                chooseBoat19 = pickedBoat19
                spotsPicked += 1
                playerLocations.append('19')
                print(spotsPicked)
                print(playerLocations)
                selected19 = True
                boatsShown += 1
        if chooseBoat20.draw() and selected20 == False: 
            if spotsPicked == 5:
                selected20 = True
            elif spotsPicked <= 5:
                chooseBoat20 = pickedBoat20
                spotsPicked += 1
                playerLocations.append('20')
                print(spotsPicked)
                print(playerLocations)
                selected20 = True
                boatsShown += 1
        if chooseBoat21.draw() and selected21 == False: 
            if spotsPicked == 5:
                selected21 = True
            elif spotsPicked <= 5:
                chooseBoat21 = pickedBoat21
                spotsPicked += 1
                playerLocations.append('21')
                print(spotsPicked)
                print(playerLocations)
                selected21 = True
                boatsShown += 1
        if chooseBoat22.draw() and selected22 == False: 
            if spotsPicked == 5:
                selected22 = True
            elif spotsPicked <= 5:
                chooseBoat22 = pickedBoat22
                spotsPicked += 1
                playerLocations.append('22')
                print(spotsPicked)
                print(playerLocations)
                selected22 = True
                boatsShown += 1
        if chooseBoat23.draw() and selected23 == False: 
            if spotsPicked == 5:
                selected23 = True
            elif spotsPicked <= 5:
                chooseBoat23 = pickedBoat23
                spotsPicked += 1
                playerLocations.append('23')
                print(spotsPicked)
                print(playerLocations)
                selected23 = True
                boatsShown += 1
        if chooseBoat24.draw() and selected24 == False: 
            if spotsPicked == 5:
                selected24 = True
            elif spotsPicked <= 5:
                chooseBoat24 = pickedBoat24
                spotsPicked += 1
                playerLocations.append('24')
                print(spotsPicked)
                print(playerLocations)
                selected24 = True
                boatsShown += 1
        if chooseBoat25.draw() and selected25 == False: 
            if spotsPicked == 5:
                selected25 = True
            elif spotsPicked <= 5:
                chooseBoat25 = pickedBoat25
                spotsPicked += 1
                playerLocations.append('25')
                print(spotsPicked)
                print(playerLocations)
                selected25 = True
                boatsShown += 1
        if chooseBoat26.draw() and selected26 == False: 
            if spotsPicked == 5:
                selected26 = True
            elif spotsPicked <= 5:
                chooseBoat26 = pickedBoat26
                spotsPicked += 1
                playerLocations.append('26')
                print(spotsPicked)
                print(playerLocations)
                selected26 = True
                boatsShown += 1
        if chooseBoat27.draw() and selected27 == False: 
            if spotsPicked == 5:
                selected27 = True
            elif spotsPicked <= 5:
                chooseBoat27 = pickedBoat27
                spotsPicked += 1
                playerLocations.append('27')
                print(spotsPicked)
                print(playerLocations)
                selected27 = True
                boatsShown += 1
        if chooseBoat28.draw() and selected28 == False: 
            if spotsPicked == 5:
                selected28 = True
            elif spotsPicked <= 5:
                chooseBoat28 = pickedBoat28
                spotsPicked += 1
                playerLocations.append('28')
                print(spotsPicked)
                print(playerLocations)
                selected28 = True
                boatsShown += 1
        if chooseBoat29.draw() and selected29 == False: 
            if spotsPicked == 5:
                selected29 = True
            elif spotsPicked <= 5:
                chooseBoat29 = pickedBoat29
                spotsPicked += 1
                playerLocations.append('29')
                print(spotsPicked)
                print(playerLocations)
                selected29 = True
                boatsShown += 1
        if chooseBoat30.draw() and selected30 == False: 
            if spotsPicked == 5:
                selected30 = True
            elif spotsPicked <= 5:
                chooseBoat30 = pickedBoat30
                spotsPicked += 1
                playerLocations.append('30')
                print(spotsPicked)
                print(playerLocations)
                selected30 = True
                boatsShown += 1
        if chooseBoat31.draw() and selected31 == False:
            if spotsPicked == 5:
                selected31 = True
            elif spotsPicked <= 5:
                chooseBoat31 = pickedBoat31
                spotsPicked += 1
                playerLocations.append('31')
                print(spotsPicked)
                print(playerLocations)
                selected31 = True
                boatsShown += 1
        if chooseBoat32.draw() and selected32 == False:
            if spotsPicked == 5:
                selected32 = True
            elif spotsPicked <= 5:
                chooseBoat32 = pickedBoat32
                spotsPicked += 1
                playerLocations.append('32')
                print(spotsPicked)
                print(playerLocations)
                selected32 = True
                boatsShown += 1
        if chooseBoat33.draw() and selected33 == False: 
            if spotsPicked == 5:
                selected33 = True
            elif spotsPicked <= 5:
                chooseBoat33 = pickedBoat33
                spotsPicked += 1
                playerLocations.append('33')
                print(spotsPicked)
                print(playerLocations)
                selected33 = True
                boatsShown += 1
        if chooseBoat34.draw() and selected34 == False: 
            if spotsPicked == 5:
                selected34 = True
            elif spotsPicked <= 5:
                chooseBoat34 = pickedBoat34
                spotsPicked += 1
                playerLocations.append('34')
                print(spotsPicked)
                print(playerLocations)
                selected34 = True
                boatsShown += 1
        if chooseBoat35.draw() and selected35 == False:
            if spotsPicked == 5:
                selected35 = True
            elif spotsPicked < 5:
                chooseBoat35 = pickedBoat35
                spotsPicked += 1
                playerLocations.append('35')
                print(spotsPicked)
                print(playerLocations)
                selected35 = True
                boatsShown += 1
        
        #when all spots picked shows begin game button which when clicked starts the game
        if spotsPicked == 5 and boatsShown == 5:
            if begin.draw():
                newgame = False
                turns = True

    if turns == True:
        screen.blit(gamegrid, (0, 0))
        playerTurn = True
        #creates save and quit button
        if SAQbutton.draw():
            run = False
        if '11' in playerLocations:        #checks if coordinate is in player picked locations and if so puts the boat there repeats for all 35 VVV
            chooseBoat11.draw()
        if '12' in playerLocations:
            chooseBoat12.draw()
        if '13' in playerLocations:
            chooseBoat13.draw()
        if '14' in playerLocations:
            chooseBoat14.draw()
        if '15' in playerLocations:
            chooseBoat15.draw()
        if '16' in playerLocations:
            chooseBoat16.draw()
        if '17' in playerLocations:
            chooseBoat17.draw()
        if '18' in playerLocations:
            chooseBoat18.draw()
        if '19' in playerLocations:
            chooseBoat19.draw()
        if '20' in playerLocations:
            chooseBoat20.draw()
        if '21' in playerLocations:
            chooseBoat21.draw()
        if '22' in playerLocations:
            chooseBoat22.draw()
        if '23' in playerLocations:
            chooseBoat23.draw()
        if '24' in playerLocations:
            chooseBoat24.draw()
        if '25' in playerLocations:
            chooseBoat25.draw()
        if '26' in playerLocations:
            chooseBoat26.draw()
        if '27' in playerLocations:
            chooseBoat27.draw()
        if '28' in playerLocations:
            chooseBoat28.draw()
        if '29' in playerLocations:
            chooseBoat29.draw()
        if '30' in playerLocations:
            chooseBoat30.draw()
        if '31' in playerLocations:
            chooseBoat31.draw()
        if '32' in playerLocations:
            chooseBoat32.draw()
        if '33' in playerLocations:
            chooseBoat33.draw()
        if '34' in playerLocations:
            chooseBoat34.draw()
        if '35' in playerLocations:
            chooseBoat35.draw()
        if playerTurn == True:             #Adds fog as buttons if clicked checks if AI ship exists there and either shows a sunken ship or an empty tile
            if fog11.draw():               #Repeats for all 35 VVV
                if '11' in aiLocations:
                    aiSunk += 1
                    fog11 = boatsunk11
                    playerTurn = False
                    explosion.play()
                else:
                    fog11 = empty11
                    playerTurn = False
                    splash.play()
            if fog12.draw():
                if '12' in aiLocations:
                    aiSunk += 1
                    fog12 = boatsunk12
                    playerTurn = False
                    explosion.play()
                else:
                    fog12 = empty12
                    playerTurn = False
                    splash.play()
            if fog13.draw():
                if '13' in aiLocations:
                    aiSunk += 1
                    fog13 = boatsunk13
                    playerTurn = False
                    explosion.play()
                else:
                    fog13 = empty13
                    playerTurn = False
                    splash.play()
            if fog14.draw():
                if '14' in aiLocations:
                    aiSunk += 1
                    fog14 = boatsunk14
                    playerTurn = False
                    explosion.play()
                else:
                    fog14 = empty14
                    playerTurn = False
                    splash.play()
            if fog15.draw():
                if '15' in aiLocations:
                    aiSunk += 1
                    fog15 = boatsunk15
                    playerTurn = False
                    explosion.play()
                else:
                    fog15 = empty15
                    playerTurn = False
                    splash.play()
            if fog16.draw():
                if '16' in aiLocations:
                    aiSunk += 1
                    fog16 = boatsunk16
                    playerTurn = False
                    explosion.play()
                else:
                    fog16 = empty16
                    playerTurn = False
                    splash.play()
            if fog17.draw():
                if '17' in aiLocations:
                    aiSunk += 1
                    fog17 = boatsunk17
                    playerTurn = False
                    explosion.play()
                else:
                    fog17 = empty17
                    playerTurn = False
                    splash.play()
            if fog18.draw():
                if '18' in aiLocations:
                    aiSunk += 1
                    fog18 = boatsunk18
                    playerTurn = False
                    explosion.play()
                else:
                    fog18 = empty18
                    playerTurn = False
                    splash.play()
            if fog19.draw():
                if '19' in aiLocations:
                    aiSunk += 1
                    fog19 = boatsunk19
                    playerTurn = False
                    explosion.play()
                else:
                    fog19 = empty19
                    playerTurn = False
                    splash.play()
            if fog20.draw():
                if '20' in aiLocations:
                    aiSunk += 1
                    fog20 = boatsunk20
                    playerTurn = False
                    explosion.play()
                else:
                    fog20 = empty20
                    playerTurn = False
                    splash.play()
            if fog21.draw():
                if '21' in aiLocations:
                    aiSunk += 1
                    fog21 = boatsunk21
                    playerTurn = False
                    explosion.play()
                else:
                    fog21 = empty21
                    playerTurn = False
                    splash.play()
            if fog22.draw():
                if '22' in aiLocations:
                    aiSunk += 1
                    fog22 = boatsunk22
                    playerTurn = False
                    explosion.play()
                else:
                    fog22 = empty22
                    playerTurn = False
                    splash.play()
            if fog23.draw():
                if '23' in aiLocations:
                    aiSunk += 1
                    fog23 = boatsunk23
                    playerTurn = False
                    explosion.play()
                else:
                    fog23 = empty23
                    playerTurn = False
                    splash.play()
            if fog24.draw():
                if '24' in aiLocations:
                    aiSunk += 1
                    fog24 = boatsunk24
                    playerTurn = False
                    explosion.play()
                else:
                    fog24 = empty24
                    playerTurn = False
                    splash.play()
            if fog25.draw():
                if '25' in aiLocations:
                    aiSunk += 1
                    fog25 = boatsunk25
                    playerTurn = False
                    explosion.play()
                else:
                    fog25 = empty25
                    playerTurn = False
                    splash.play()
            if fog26.draw():
                if '26' in aiLocations:
                    aiSunk += 1
                    fog26 = boatsunk26
                    playerTurn = False
                    explosion.play()
                else:
                    fog26 = empty26
                    playerTurn = False
                    splash.play()
            if fog27.draw():
                if '27' in aiLocations:
                    aiSunk += 1
                    fog27 = boatsunk27
                    playerTurn = False
                    explosion.play()
                else:
                    fog27 = empty27
                    playerTurn = False
                    splash.play()
            if fog28.draw():
                if '28' in aiLocations:
                    aiSunk += 1
                    fog28 = boatsunk28
                    playerTurn = False
                    explosion.play()
                else:
                    fog28 = empty28
                    playerTurn = False
                    splash.play()
            if fog29.draw():
                if '29' in aiLocations:
                    aiSunk += 1
                    fog29 = boatsunk29
                    playerTurn = False
                    explosion.play()
                else:
                    fog29 = empty29
                    playerTurn = False
                    splash.play()
            if fog30.draw():
                if '30' in aiLocations:
                    aiSunk += 1
                    fog30 = boatsunk30
                    playerTurn = False
                    explosion.play()
                else:
                    fog30 = empty30
                    playerTurn = False
                    splash.play()
            if fog31.draw():
                if '31' in aiLocations:
                    aiSunk += 1
                    fog31 = boatsunk31
                    playerTurn = False
                    explosion.play()
                else:
                    fog31 = empty31
                    playerTurn = False
                    splash.play()
            if fog32.draw():
                if '32' in aiLocations:
                    aiSunk += 1
                    fog32 = boatsunk32
                    playerTurn = False
                    explosion.play()
                else:
                    fog32 = empty32
                    playerTurn = False
                    splash.play()
            if fog33.draw():
                if '33' in aiLocations:
                    aiSunk += 1
                    fog33 = boatsunk33
                    playerTurn = False
                    explosion.play()
                else:
                    fog33 = empty33
                    playerTurn = False
                    splash.play()
            if fog34.draw():
                if '34' in aiLocations:
                    aiSunk += 1
                    fog34 = boatsunk34
                    playerTurn = False
                    explosion.play()
                else:
                    fog34 = empty34
                    playerTurn = False
                    splash.play()
            if fog35.draw():
                if '35' in aiLocations:
                    aiSunk += 1
                    fog35 = boatsunk35
                    playerTurn = False
                    explosion.play()
                else:
                    fog35 = empty35
                    playerTurn = False
                    splash.play()

            if playerTurn == False:                               #Has AI pick a location if player's boat exists there it destroys it 
                botchoice = random.choice(availableSlots)
                while botchoice in botselected:
                    botchoice = random.choice(availableSlots)
                botselected.append(botchoice)
                if botchoice in playerLocations:
                    if '11' in botselected:
                        chooseBoat11 = Pboatsunk11               # checks each spot to see if a player's boat is there if it is it sinks it and plays a sound repeats for all below V V V 
                    if '12' in botselected:
                        chooseBoat12 = Pboatsunk12
                    if '13' in botselected:
                        chooseBoat13 = Pboatsunk13
                    if '14' in botselected:
                        chooseBoat14 = Pboatsunk14
                    if '15' in botselected:
                        chooseBoat15 = Pboatsunk15
                    if '16' in botselected:
                        chooseBoat16 = Pboatsunk16
                    if '17' in botselected:
                        chooseBoat17 = Pboatsunk17
                    if '18' in botselected:
                        chooseBoat18 = Pboatsunk18
                    if '19' in botselected:
                        chooseBoat19 = Pboatsunk19
                    if '20' in botselected:
                        chooseBoat20 = Pboatsunk20
                    if '21' in botselected:
                        chooseBoat21 = Pboatsunk21
                    if '22' in botselected:
                        chooseBoat22 = Pboatsunk22
                    if '23' in botselected:
                        chooseBoat23 = Pboatsunk23
                    if '24' in botselected:
                        chooseBoat24 = Pboatsunk24
                    if '25' in botselected:
                        chooseBoat25 = Pboatsunk25
                    if '26' in botselected:
                        chooseBoat26 = Pboatsunk26
                    if '27' in botselected:
                        chooseBoat27 = Pboatsunk27
                    if '28' in botselected:
                        chooseBoat28 = Pboatsunk28
                    if '29' in botselected:
                        chooseBoat29 = Pboatsunk29
                    if '30' in botselected:
                        chooseBoat30 = Pboatsunk30
                    if '31' in botselected:
                        chooseBoat31 = Pboatsunk31
                    if '32' in botselected:
                        chooseBoat32 = Pboatsunk32
                    if '33' in botselected:
                        chooseBoat33 = Pboatsunk33
                    if '34' in botselected:
                        chooseBoat34 = Pboatsunk34
                    if '35' in botselected:
                        chooseBoat35 = Pboatsunk35
                    print(botchoice)
                    playerSunk += 1
                    explosion.play()
                else:
                    splash.play()
                if aiSunk == 5:              #If all AI ships sunk player wins
                    mixer.music.load('assets/victory.wav')
                    mixer.music.play()
                    gameEnd = True
                    turns = False
                if playerSunk == 5:          #If all player ships sunk player loses
                    mixer.music.load('assets/gameover.wav')
                    mixer.music.play()
                    gameEnd = True
                    turns = False

    if gameEnd == True:                     
        if aiSunk == 5:
            screen.blit(youWinIMG, (0, 0))
        if playerSunk == 5:
            screen.blit(gameOverIMG, (0, 0))
        if FinalQuit.draw():
            run = False


    click = False
    #event section       
    for event in pygame.event.get():      
        if event.type == pygame.MOUSEBUTTONDOWN and not click:        #if mouse button released sets click to true
            click = True
        elif event.type == pygame.MOUSEBUTTONUP:                     #if mouse button clicked and hasn't been clicked already it registers a click (stops it registering tons of clicks)
            click = False
        if event.type == pygame.QUIT:                                #exits game if run is set to false
            run = False

    pygame.display.update()