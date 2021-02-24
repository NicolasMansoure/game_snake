import sys
import random
import pygame
import sys
from pygame.constants import WINDOWHITTEST


# la classe va contenir toutes les variables et fonctions pour le bon déroulement du jeu
class Jeu:

    def __init__(self):
        # defini la taille de la fenetre
        self.ecran = pygame.display.set_mode((800, 600))
        # Rajoute un titre a la fenetre
        pygame.display.set_caption("Jeu Snake")
        self.jeu_encours = True

        # Creer les variables de position et de direction du serpent
        self.serpent_position_x = 300
        self.serpent_position_y = 300
        self.serpent_direction_x = 0
        self.serpent_direction_y = 0
        self.serpent_corps = 10

        # Creer la variable pour la taille du serpent
        self.taille_serpent = 1

        # Creet l'écran d'acceuil
        self.ecran_acceuil = True

        # Charger l'image de l'écran d'acceuil
        self.image = pygame.image.load("snake.png")
        # Taille de l'image 
        self.image_titre = pygame.transform.scale(self.image,(300,200))

        # Creee la variable score
        self.score = 0        

        # Cree une liste qui enregistre toutes les positions du serpent
        self.positions_serpent = []

        # Charge l'image de la tete du serpent
        self.image_tete_serpent = pygame.image.load("tete_serpent.png")

        # Creer les variables de position de la pomme
        self.pomme_position_x = random.randrange(110, 690, 10)
        self.pomme_position_y = random.randrange(110, 590, 10)
        self.pomme = 10

        # Fixer les fps
        self.clock = pygame.time.Clock()


    def fonction_principale(self):
        # Ecran d'acceuil avec les regles du jeu
        while self.ecran_acceuil:
            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    sys.exit()

                if evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_RETURN:
                        self.ecran_acceuil = False

                self.ecran.fill((0, 0, 0))

                self.ecran.blit(self.image_titre,(250,50,100,50))

                self.creer_message("moyenne","Le but du jeu est de faire grandir le serpent",(240,200,200,5),(240,240,240)) 
                self.creer_message("moyenne","Pour y arriver, il a besoin de manger des pommes. Mangez en autant que possible !",(70,220,200,5),(240,240,240)) 
                self.creer_message("moyenne","Appuyer sur 'Entrer' pour commencer",(250,450,200,5),(255,255,255))  
                 
                pygame.display.flip()


        # fonction qui permet de gerer les evenement, d'afficher certain composants du jeu grace a une boucle while
        while self.jeu_encours:
            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    sys.exit()

                # creer les evenement pour faire bouger le serpent
                if evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_RIGHT:
                        self.serpent_direction_x = 10
                        self.serpent_direction_y = 0

                    if evenement.key == pygame.K_LEFT:
                        self.serpent_direction_x = -10
                        self.serpent_direction_y = 0

                    if evenement.key == pygame.K_DOWN:
                        self.serpent_direction_y = 10
                        self.serpent_direction_x = 0

                    if evenement.key == pygame.K_UP:
                        self.serpent_direction_y = -10
                        self.serpent_direction_x = 0


            # Animer le serpent si il se trouve dans les limites
            if self.serpent_position_x <= 100 or self.serpent_position_x >= 700 or self.serpent_position_y <= 100 or self.serpent_position_y >= 600:
                sys.exit()
            self.serpent_mouvement()

            # Creation de la condition si le serpent mange la pomme
            if self.pomme_position_y == self.serpent_position_y and self.pomme_position_x == self.serpent_position_x:
                self.pomme_position_x = random.randrange(110, 690, 10)
                self.pomme_position_y = random.randrange(110, 590, 10)

                # Augmenter la taille du serpent
                self.taille_serpent += 1

                # Augmenter le score
                self.score += 1

            # Crer une liste qui enregistre la position de la tete du serpent
            tete_serpent = []
            tete_serpent.append(self.serpent_position_x)
            tete_serpent.append(self.serpent_position_y)

            # Append dans la liste des positons du serpent
            self.positions_serpent.append(tete_serpent)

            # Condition pour gerer la taille et la positions du serpent
            if len(self.positions_serpent) > self.taille_serpent:
                self.positions_serpent.pop(0)

            self.afficher_les_elements()

            # Si le serpent se "mord" lui meme alors le jeu s'arete
            for corps_du_serpent in self.positions_serpent[:-1]:
                if tete_serpent == corps_du_serpent:
                    sys.exit()

            self.creer_message("grande","Snake game",(320,10,100,50),(255,255,255))
            self.creer_message("grande","{}".format(str(self.score)), (374,50,50,50), (255,255,255))
 
            # Afficher les limites
            self.creer_limites()
            self.clock.tick(10)

            # Mise a jour de l'ecran
            pygame.display.flip()


    # Creation d'une limite pour le jeu de taille ((100,100,600,500),3)
    def creer_limites(self):
        pygame.draw.rect(self.ecran, (255, 255, 255), (100, 100, 600, 500), 3)


    def serpent_mouvement(self):
        # animation du serpent
        self.serpent_position_x += self.serpent_direction_x
        self.serpent_position_y += self.serpent_direction_y


    def afficher_les_elements(self):
        # Defini la couleur de l'ecran en noir
        self.ecran.fill((0, 0, 0))

        # Afficher le serpent

        #pygame.draw.rect(self.ecran, (0, 255, 0), (self.serpent_position_x,
        #                                           self.serpent_position_y, self.serpent_corps, self.serpent_corps))
        self.ecran.blit(self.image_tete_serpent, (self.serpent_position_x, self.serpent_position_y, self.serpent_corps, self.serpent_corps))

        # Afficher le corps du serpent
        for corps_du_serpent in self.positions_serpent[:-1]:
            pygame.draw.rect(self.ecran, (0, 255, 0), (
                corps_du_serpent[0], corps_du_serpent[1], self.serpent_corps, self.serpent_corps))

        # Afficher la pomme
        pygame.draw.rect(self.ecran, (255, 0, 0), (self.pomme_position_x,
                                                   self.pomme_position_y, self.pomme, self.pomme))


    def creer_message(self, font, message, message_rectangle, couleur,):
        if font == 'petite':
            font = pygame.font.SysFont('Lato', 20, False)
        elif font == 'moyenne':
            font = pygame.font.SysFont('Lato', 25, False)

        elif font == 'grande':
            font = pygame.font.SysFont('Lato', 40, False)

        message = font.render(message, True, couleur)

        self.ecran.blit(message, message_rectangle)


if __name__ == '__main__':
    # Initialise le jeu
    pygame.init()
    Jeu().fonction_principale()
    # Quitte le jeu
    pygame.quit()
