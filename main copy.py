import pygame
import os
import time


def ReturnPos(loc : str):
	return os.getcwd() + loc

# def AddFontText(Text, Alias, Color):
# 	global FontTexts, FontRects
# 	FontTexts.append(MyFont.render("불러오기", True, FontColor))
# 	FontRects.append(FontTexts[len(FontTexts) - 1].get_rect())
# 	# print(FontRects[len(FontRects) - 1])
	


pygame.init()

ScreenWidth = 800
ScreenHeight = 800
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight), pygame.RESIZABLE)


# MyFont = pygame.font.Font(ReturnPos("\\font\\NEXONLv1GothicRegular.ttf"), 20)

# FontColor = (255, 255, 255)
# FontTexts = []
# FontRects = []
# AddFontText("불러오기", True, FontColor)
# AddFontText("저장하기", True, FontColor)



BoxOnColor = (255, 255, 255)
BoxOffColor = (0, 0, 0)
BoxNum = 32
BoxFillSize1 = 0 # y 50 ~ 950
BoxFillSize2 = 1000 #

ImgSelected = None
ImgUnSelected = None



def DrawBoxs():
	BoxSize = (BoxFillSize2 - BoxFillSize1) / BoxNum * ScreenHeight / 1000
	

	for loopx in range(BoxNum):
		for loopy in range(BoxNum):
			if loopx == 15 and loopy == 15:
				pygame.draw.rect(screen, (0, 255, 0), [BoxFillSize1  * ScreenHeight / 1000 + loopx * BoxSize * ZoomValue + X, 
												BoxFillSize1  * ScreenHeight / 1000 + loopy * BoxSize * ZoomValue + Y, 
												BoxSize * ZoomValue, BoxSize * ZoomValue], 2)
			else:
				pygame.draw.rect(screen, BoxOffColor, [BoxFillSize1  * ScreenHeight / 1000 + loopx * BoxSize * ZoomValue + X, 
													BoxFillSize1  * ScreenHeight / 1000 + loopy * BoxSize * ZoomValue + Y, 
													BoxSize * ZoomValue, BoxSize * ZoomValue], 2)
			if BoxData[loopx][loopy]:
				pygame.draw.rect(screen, BoxOnColor, [BoxFillSize1  * ScreenHeight / 1000 + loopx * BoxSize * ZoomValue + X + 2, 
													BoxFillSize1  * ScreenHeight / 1000 + loopy * BoxSize * ZoomValue + Y + 2, 
													BoxSize * ZoomValue - 4, BoxSize * ZoomValue - 4], 0)


def ReturnBoxNum(MousePos):
	Exit = False
	for loopx in range(BoxNum):
		for loopy in range(BoxNum):
			BoxSize = (BoxFillSize2 - BoxFillSize1) / BoxNum * ScreenHeight / 1000
			x = BoxFillSize1  * ScreenHeight / 1000 + loopx * BoxSize * ZoomValue + X
			y = BoxFillSize1  * ScreenHeight / 1000 + loopy * BoxSize * ZoomValue + Y
			if MousePos[0] >= x and MousePos[0] <= x + BoxSize * ZoomValue:
				if MousePos[1] >= y and MousePos[1] <= y + BoxSize * ZoomValue:
					Exit = True
					# BoxData[loopx][loopy] = not BoxData[loopx][loopy]
					return loopx, loopy
					break
		if Exit:
			break

	return -1, -1

BoxData = [[False] * BoxNum for _ in range(BoxNum)]
# for i in range(BoxNum):
# 	for x in range(int(BoxNum / 2)):
# 		BoxData[i][x + int(BoxNum / 2)] = True

X, Y = 0, 0
ZoomValue = 1
Draging = False
MouseLastPos = None
SceneFrame = 0

clock = pygame.time.Clock()
LineStart = None

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
			exit()

		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				X, Y = 0, 0
				ZoomValue = 1

		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				Draging = True

				# BoxX, BoxY = ReturnBoxNum(pygame.mouse.get_pos())
				# if BoxX == -1:
				# 	break
				# BoxData[BoxX][BoxY] = not BoxData[BoxX][BoxY]
			elif event.button == 2:
				BoxX, BoxY = ReturnBoxNum(pygame.mouse.get_pos())
				if BoxX == -1:
					break
				# BoxData[BoxX][BoxY] = not BoxData[BoxX][BoxY]
				for x in range(2):
					for y in range(2):
						BoxData[BoxX + x][BoxY + y] = True
			elif event.button == 3:
				BoxX, BoxY = ReturnBoxNum(pygame.mouse.get_pos())
				if BoxX == -1:
					break
				LineStart = (BoxX, BoxY)
			

		elif event.type == pygame.MOUSEBUTTONUP:
			if event.button == 1:
				Draging = False
			elif event.button == 3:
				BoxX, BoxY = ReturnBoxNum(pygame.mouse.get_pos())
				if BoxX == -1:
					break
				LineEnd = (BoxX, BoxY)
				# print(LineStart, LineEnd)

				Xval = LineStart[0]
				Yval = LineStart[1]
				length = abs(LineStart[0] - LineEnd[0])
				for x in range(length):
					BoxData[int(Xval)][int(Yval)] = not BoxData[int(Xval)][int(Yval)]
					Xval -= (LineStart[0] - LineEnd[0]) / length
					Yval -= (LineStart[1] - LineEnd[1]) / length
					# print(int(Xval), int(Yval))

				Xval = LineStart[0]
				Yval = LineStart[1]
				length = abs(LineStart[1] - LineEnd[1])
				for y in range(length):
					BoxData[int(Xval)][int(Yval)] = not BoxData[int(Xval + 1)][int(Yval + 1)]
					Xval -= (LineStart[0] - LineEnd[0]) / length
					Yval -= (LineStart[1] - LineEnd[1]) / length

		
	if Draging:
		BoxX, BoxY = ReturnBoxNum(pygame.mouse.get_pos())
		if BoxX == -1:
			break
		BoxData[BoxX][BoxY] = not BoxData[BoxX][BoxY]

	clock.tick(60)