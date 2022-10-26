import pygame

pygame.init()

display = pygame.display.set_mode([840, 480])

pygame.display.set_caption("Melhor Jogo de Todos")

player = pygame.Rect(25, 25, 25, 25)

gameLoop = True
if __name__ == '__main__':
	while gameLoop:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameLoop = False
		
		keys = pygame.key.get_pressed()
		if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
			player.x += 1
		if keys[pygame.K_a] or keys[pygame.K_LEFT]:
			player.x -= 1
		if keys[pygame.K_w] or keys[pygame.K_UP]:
			player.y -=1
		if keys[pygame.K_s] or keys[pygame.K_DOWN]:
			player.y +=1


		# Draw
		display.fill([0, 0, 0])
		pygame.draw.rect(display, [255, 255, 255, 255],player)


		pygame.display.update()


