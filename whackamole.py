import pygame
#Test


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()

        running = True
        mole = (0,0) #cooridinates
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")

            for i in range(10):
                pygame.draw.line(screen, "blue", (i*64,0), (i * 64, 512))
            for i in range(8):
                pygame.draw.line(screen, "red", (0, i * 64), (640, i * 64))
            screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
            pygame.display.flip()
            clock.tick(60)


    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
