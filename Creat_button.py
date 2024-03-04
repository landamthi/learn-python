import pygame
from random import randint
pygame.init()
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption('Kmean visualization')
running = True
clock = pygame.time.Clock()

BACKGROUD = (214, 214, 214)
BACK = (0, 64, 61)
BACKGROUD_PANEL = (155, 170, 169)
WHITE = (255, 255, 255)

Red = (255, 0, 0)
Green = (0, 128, 0)
Blue = (0, 0, 255)
Yellow = (255, 255, 0)
Orange = (255, 165, 0)
Purple = (128, 0, 128)
Pink = (255, 192, 203)
Gray = (128, 128, 128)
Brown = (165, 42, 42)
Cyan = (0, 255, 255)

Colors = [Red, Green, Blue, Yellow, Orange, Purple, Pink, Gray]

font = pygame.font.SysFont('sans', 40)
font_mall = pygame.font.SysFont('sans', 20)
text_plus = font.render('+', True, WHITE)
text_minus = font.render('-', True, WHITE)
# text_k = font.render('k', True, WHITE)
text_run = font.render('Run', True, WHITE)
text_random = font.render('Random', True, WHITE)
text_algorithm = font.render('Algorithm', True, WHITE)
text_reset = font.render('Reset', True, WHITE)



k=0
error = 0
points = []
clusters = []
while running:

	clock.tick(60)
	screen.fill(BACKGROUD)
	
	#Draw interface

	#Draw panel
	pygame.draw.rect(screen, BACK, (50, 50, 700, 500))
	pygame.draw.rect(screen, BACKGROUD_PANEL, (55, 55, 690, 490))
	# K button
	pygame.draw.rect(screen, BACK, (850, 50, 50, 50))
	screen.blit(text_plus, (866, 50))
	# K - button
	pygame.draw.rect(screen, BACK, (950, 50, 50, 50))
	screen.blit(text_minus, (968, 50))
	# K-TEXT
	text_k = font.render("text k=" + str(k), True, BACK)
	screen.blit(text_k, (1050, 50))
	# Run button
	pygame.draw.rect(screen, BACK, (850, 150, 150, 50))
	screen.blit(text_run, (900, 150))
	# Random button
	pygame.draw.rect(screen, BACK, (850, 250, 150, 50) )
	screen.blit(text_random, (860, 250))
	# algorithm button
	pygame.draw.rect(screen, BACK, (850, 450,  150, 50))
	screen.blit(text_algorithm, (855,450))
	# Reset button
	pygame.draw.rect(screen, BACK, (850, 550, 150, 50))
	screen.blit(text_reset, (880, 550))
	# Error 
	text_error = font.render("Error = " + str(error), True, BACK )
	screen.blit(text_error, (850, 350))



	#End draw interface
	mouse_x, mouse_y = pygame.mouse.get_pos()

	if  50 < mouse_x < 750 and  50 < mouse_y < 550:
		text_mouse = font_mall.render("(" + str(mouse_x - 50) + "," + str (mouse_y - 50) + ")", True, BACK)
		screen.blit(text_mouse, (mouse_x + 15, mouse_y))
	
	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			# Add in list
			if  50 < mouse_x < 750 and  50 < mouse_y < 550:
				pont = [mouse_x, mouse_y]
				points.append(pont)
				print(points)
			# k+ button change 
			if 850 < mouse_x < 900 and 50 < mouse_y < 100:
				k+=1
				print("Press K +")
			# K- button change
			if 950 < mouse_x < 1000 and 50 < mouse_y < 100:
				if k > 0:
					k-=1
				print("Press K -")
			#  Run button
			if 850 < mouse_x < 1000 and 150 < mouse_y < 200:
				print("Press run")
			#  Random button
			if 850 < mouse_x < 1000 and 250 < mouse_y < 300:
				clusters = []
				for i in range(k):
					random_point = [randint(0, 700), randint(0, 500)]
					clusters.append(random_point)

				print("Press random")
			#  Algorithm button
			if 850 < mouse_x < 1000 and 450 < mouse_y < 500:
				print("Press algorithm")
			#  Reset button 
			if 850 < mouse_x < 1000 and 550 < mouse_y < 600:
				print("Press Reset")

	#  Draw clusters
	for i in range(len(clusters)):
		pygame.draw.circle(screen, Colors[i], (clusters[i][0] + 60, clusters[i][1] + 60), 10)
	# Draw point
	for i  in range(len(points)):
		pygame.draw.circle(screen, BACK, (points[i][0] + 50, points[i][1] + 50), 6)
		pygame.draw.circle(screen, WHITE, (points[i][0] + 50, points[i][1] + 50), 5)
		
	pygame.display.flip()

pygame.quit()
