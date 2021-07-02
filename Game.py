import pygame
from pygame.constants import RESIZABLE
import time
import sys

class Morpion:

    def __init__(self,mode) -> None:
        pygame.init()
        self.mode = mode # Mode = SOLO / MULTI
        self.resolution = (500,500)
        self.gameOver = False
        self.game = self.game = pygame.display.set_mode(self.resolution,RESIZABLE)
        self.turn = "cross" # First player plays the cross / Second player plays the circle
        self.game.fill((255,255,255))

        self.board=[["x","x","x"],["x","x","x"],["x","x","x"]]

    def verif(self):
        exit = (False,"")
        cpt = 0
        for y in range(0,len(self.board)):
            for x in range(0,len(self.board[y])):
                if self.board[y][x] != "x":
                    cpt += 1
                if cpt == 9:
                    exit = (True,2)
                    break
                if x == 0: # Verif horizontale pour chaque ligne
                    if self.board[y][x] == 0:
                        if self.board[y][x+1] == 0:
                            if self.board[y][x+2] == 0:
                                exit = (True,0)
                    if self.board[y][x] == 1:
                        if self.board[y][x+1] == 1:
                            if self.board[y][x+2] == 1:
                                exit = (True,1)
                if y == 0: # Verif vertical pour chaque colonne
                    if self.board[y][x] == self.board[y+1][x] and self.board[y][x] == self.board[y+2][x]:
                        if self.board[y][x] == 0:
                            if self.board[y+1][x] == 0:
                                if self.board[y+2][x] == 0:
                                    exit = (True,0)
                        if self.board[y][x] == 1:
                            if self.board[y+1][x] == 1:
                                if self.board[y+2][x] == 1:
                                    exit = (True,1)
                if x == 0 and y == 0: # Verif diagonale bas vers haut
                    if self.board[y][x] == 0:
                        if self.board[y+1][x+1] == 0:
                            if self.board[y+2][x+2] == 0:
                                exit = (True,0)
                    if self.board[y][x] == 1:
                        if self.board[y+1][x+1] == 1:
                            if self.board[y+2][x+2] == 1:
                                exit = (True,1)
                if x == 0 and y == 2: # Verif diagonale bas vers haut
                    if self.board[y][x] == 0:
                        if self.board[y-1][x+1] == 0:
                            if self.board[y-2][x+2] == 0:
                                exit = (True,0)
                    if self.board[y][x] == 1:
                        if self.board[y-1][x+1] == 1:
                            if self.board[y-2][x+2] == 1:
                                exit = (True,1)
        return exit
                
    def set_text(self,string, coordx, coordy, fontSize): #Function to set text
        font = pygame.font.Font('freesansbold.ttf', fontSize) 
        text = font.render(string, True, (0, 0, 0)) 
        textRect = text.get_rect()
        textRect.center = (coordx, coordy) 
        return (text, textRect)

    def afficheGagnant(self):
        text = self.set_text("Player "+str(self.winner)+" won the game !",250,50,30)
        self.game.blit(text[0],text[1])
        pygame.display.update()

    def afficheEgalite(self):
        text = self.set_text("PAT - No winner this time !",250,50,30)
        self.game.blit(text[0],text[1])
        pygame.display.update()

    def run(self):
        if self.gameOver== False:
            hasPlayed = False
            
            pygame.draw.lines(self.game,(0,0,0),False,((100,200),(400,200)),3) # Ligne horizontale haute
            pygame.draw.lines(self.game,(0,0,0),False,((100,300),(400,300)),3) # Ligne horizontale basse

            pygame.draw.lines(self.game,(0,0,0),False,((200,100),(200,400)),3) # Ligne verticale gauche
            pygame.draw.lines(self.game,(0,0,0),False,((300,100),(300,400)),3) # Ligne verticale droite
            pygame.display.update()
            ### Game Loop
            
            while hasPlayed == False:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            self.gameOver = True
                            break
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.gameOver = True
                            return

                    if event.type == pygame.MOUSEBUTTONDOWN :
                        mpos = pygame.mouse.get_pos()
                        if mpos[0] > 100 and mpos[0] < 200:
                            if mpos[1] > 100 and mpos[1] < 200: 
                                # ROW 1 | COL 1
                                if self.board[0][0] != 0 and self.board[0][0] != 1:
                                    if self.turn == "cross":
                                        if self.board[0][0] != 0 and self.board[0][0] != 1:
                                            self.board[0][0] = 0
                                            pygame.draw.lines(self.game,(0,0,250),False,((110,110),(190,190)),3)
                                            pygame.draw.lines(self.game,(0,0,250),False,((110,190),(190,110)),3)
                                            hasPlayed = True
                                    else:
                                        self.board[0][0] = 1
                                        pygame.draw.circle(self.game,(255,0,0),(150,150),40,3)
                                        hasPlayed = True
                                
                            if mpos[1] > 200 and mpos[1] < 300:
                                # ROW 2 | COL 1
                                if self.board[1][0] != 0 and self.board[1][0] != 1:
                                    if self.turn == "cross":
                                            self.board[1][0] = 0
                                            pygame.draw.lines(self.game,(0,0,250),False,((110,210),(190,290)),3)
                                            pygame.draw.lines(self.game,(0,0,250),False,((110,290),(190,210)),3)
                                            hasPlayed = True
                                    else:
                                        self.board[1][0] = 1
                                        pygame.draw.circle(self.game,(255,0,0),(150,250),40,3)
                                        hasPlayed = True
                                
                            if mpos[1] > 300 and mpos[1] < 400:
                                # ROW 3 | COL 1
                                if self.board[2][0] != 0 and self.board[2][0] != 1:
                                    if self.turn == "cross":
                                        self.board[2][0] = 0
                                        pygame.draw.lines(self.game,(0,0,250),False,((110,310),(190,390)),3)
                                        pygame.draw.lines(self.game,(0,0,250),False,((110,390),(190,310)),3)
                                        hasPlayed = True
                                    else:
                                        self.board[2][0] = 1
                                        pygame.draw.circle(self.game,(255,0,0),(150,350),40,3)
                                        hasPlayed = True
                                
                        if mpos[0] > 200 and mpos[0] < 300:
                            if mpos[1] > 100 and mpos[1] < 200:
                                # ROW 1 | COL 2
                                if self.board[0][1] != 0 and self.board[0][1] != 1:
                                    if self.turn == "cross":
                                        self.board[0][1] = 0
                                        pygame.draw.lines(self.game,(0,0,250),False,((210,110),(290,190)),3)
                                        pygame.draw.lines(self.game,(0,0,250),False,((210,190),(290,110)),3)
                                        hasPlayed = True
                                    else:
                                        self.board[0][1] = 1
                                        pygame.draw.circle(self.game,(255,0,0),(250,150),40,3)
                                        hasPlayed = True
                                    
                            if mpos[1] > 200 and mpos[1] < 300:
                                # ROW 2 | COL 2
                                if self.board[1][1] != 0 and self.board[1][1] != 1:
                                    if self.turn == "cross":
                                        self.board[1][1] = 0
                                        pygame.draw.lines(self.game,(0,0,250),False,((210,210),(290,290)),3)
                                        pygame.draw.lines(self.game,(0,0,250),False,((210,290),(290,210)),3)
                                        hasPlayed = True
                                    else:
                                        self.board[1][1] = 1
                                        pygame.draw.circle(self.game,(255,0,0),(250,250),40,3)
                                        hasPlayed = True
                                
                            if mpos[1] > 300 and mpos[1] < 400:
                                # ROW 3 | COL 2
                                if self.board[2][1] != 0 and self.board[2][1] != 1:
                                    if self.turn == "cross":
                                        self.board[2][1] = 0
                                        pygame.draw.lines(self.game,(0,0,250),False,((210,310),(290,390)),3)
                                        pygame.draw.lines(self.game,(0,0,250),False,((210,390),(290,310)),3)
                                        hasPlayed = True
                                    else:
                                        self.board[2][1] = 1
                                        pygame.draw.circle(self.game,(255,0,0),(250,350),40,3)
                                        hasPlayed = True
                                
                        if mpos[0] > 300 and mpos[0] < 400:
                            if mpos[1] > 100 and mpos[1] < 200:
                                # ROW 1 | COL 3
                                if self.board[0][2] != 0 and self.board[0][2] != 1:
                                    if self.turn == "cross":
                                        self.board[0][2] = 0
                                        pygame.draw.lines(self.game,(0,0,250),False,((310,110),(390,190)),3)
                                        pygame.draw.lines(self.game,(0,0,250),False,((310,190),(390,110)),3)
                                        hasPlayed = True
                                    else:
                                        self.board[0][2] = 1
                                        pygame.draw.circle(self.game,(255,0,0),(350,150),40,3)
                                        hasPlayed = True
                                
                            if mpos[1] > 200 and mpos[1] < 300:
                                # ROW 2 | COL 3
                                if self.board[1][2] != 0 and self.board[1][2] != 1:
                                    if self.turn == "cross":
                                        self.board[1][2] = 0
                                        pygame.draw.lines(self.game,(0,0,250),False,((310,210),(390,290)),3)
                                        pygame.draw.lines(self.game,(0,0,250),False,((310,290),(390,210)),3)
                                        hasPlayed = True
                                    else:
                                        self.board[1][2] = 1
                                        pygame.draw.circle(self.game,(255,0,0),(350,250),40,3)
                                        hasPlayed = True
                                
                            if mpos[1] > 300 and mpos[1] < 400:
                                # ROW 3 | COL 3
                                if self.board[2][2] != 0 and self.board[2][2] != 1:
                                    if self.turn == "cross":
                                        self.board[2][2] = 0
                                        pygame.draw.lines(self.game,(0,0,250),False,((310,310),(390,390)),3)
                                        pygame.draw.lines(self.game,(0,0,250),False,((310,390),(390,310)),3)
                                        hasPlayed = True
                                    else:
                                        self.board[2][2] = 1
                                        pygame.draw.circle(self.game,(255,0,0),(350,350),40,3)
                                        hasPlayed = True

                        verif = self.verif()
                        if verif[0] == True:
                            self.gameOver = True
                            if verif[1] == 0 or verif[1] == 1:
                                self.winner = verif[1]
                                self.afficheGagnant()
                            else:
                                self.afficheEgalite()
                            
                            time.sleep(4)
                            pygame.quit()
                            sys.exit()
                        else:
                            if self.turn == "cross":
                                self.turn = "circle"
                            elif self.turn == "circle":
                                self.turn = "cross"
                            pygame.display.update()
            
if __name__ == "__main__":
    game = Morpion("SOLO")
    isOver = game.gameOver
    while isOver == False:
        game.run()


