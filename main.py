import pygame
from pygame.math import Vector2

pygame.init()

ScreenWidth = 1000
ScreenHeight = 800
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight), pygame.RESIZABLE)

BoxOnColor = (255, 255, 255)
BoxOffColor = (0, 0, 0)
BoxNum = 41
BoxFillSize1 = 50 # y 50 ~ 950
BoxFillSize2 = 950 #

def DrawBoxs():
	BoxSize = (BoxFillSize2 - BoxFillSize1) / BoxNum * ScreenHeight / 1000
	

	for loopx in range(BoxNum):
		for loopy in range(BoxNum):
			if BoxData[loopx][loopy]:
				ColorValue = BoxOnColor
			else:
				ColorValue = BoxOffColor
			pygame.draw.rect(screen, ColorValue, [BoxFillSize1  * ScreenHeight / 1000 + loopx * BoxSize * ZoomValue + X, 
												BoxFillSize1  * ScreenHeight / 1000 + loopy * BoxSize * ZoomValue + Y, 
												BoxSize * ZoomValue, BoxSize * ZoomValue], 2)


BoxData = [[False] * BoxNum for _ in range(BoxNum)]

X, Y = 0, 0
ZoomValue = 1
Draging = False
MouseLastPos = None

Run = True
while Run:
	ScreenWidth, ScreenHeight = pygame.display.get_surface().get_size()

	screen.fill((50,50,50))
	DrawBoxs()

	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
			pygame.quit()

		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 4: #줌 인
				ZoomValue += 0.05
				MousePos = pygame.mouse.get_pos()
				# print(MousePos[0] / ScreenWidth, MousePos[1] / ScreenHeight)
				X -= (MousePos[0] / ScreenWidth - 0.5) * 65 * ScreenWidth / 1000
				Y -= (MousePos[1] / ScreenHeight - 0.5) * 65 * ScreenHeight / 1000
 
			elif event.button == 5: # 줌 아웃
				ZoomValue -= 0.05
				MousePos = pygame.mouse.get_pos()
				X += (MousePos[0] / ScreenWidth - 0.5) * 65 * ScreenWidth / 1000
				Y += (MousePos[1] / ScreenHeight - 0.5) * 65 * ScreenHeight / 1000

			elif event.button == 1: #드래그 중
				MouseLastPos = pygame.mouse.get_pos()
				Draging = True

			elif event.button == 3: #드래그 중
				MousePos = pygame.mouse.get_pos()
				Exit = False
				for loopx in range(BoxNum):
					for loopy in range(BoxNum):
						BoxSize = (BoxFillSize2 - BoxFillSize1) / BoxNum * ScreenHeight / 1000
						x = BoxFillSize1  * ScreenHeight / 1000 + loopx * BoxSize * ZoomValue + X
						y = BoxFillSize1  * ScreenHeight / 1000 + loopy * BoxSize * ZoomValue + Y
						if MousePos[0] >= x and MousePos[0] <= x + BoxSize * ZoomValue:
							if MousePos[1] >= y and MousePos[1] <= y + BoxSize * ZoomValue:
								Exit = True
								BoxData[loopx][loopy] = not BoxData[loopx][loopy]
								break
					if Exit:
						break
			
			elif event.button == 2:
				for loopx in range(BoxNum):
					ExportValue = ""
					for loopy in range(BoxNum):
						ExportValue += str(1 if BoxData[loopy][loopx] else 0)
					print(hex(int(ExportValue, 2)))

		elif event.type == pygame.MOUSEBUTTONUP:
			if event.button == 1:
				Draging = False
		
	if Draging:
		ChangeValue = MouseLastPos[0] - pygame.mouse.get_pos()[0], MouseLastPos[1] - pygame.mouse.get_pos()[1]
		MouseLastPos = pygame.mouse.get_pos()
		X -= ChangeValue[0]
		Y -= ChangeValue[1]