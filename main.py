from tkinter import YView
from PIL import Image
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

ScreenWidth = 1000
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
BoxNum = 41
BoxFillSize1 = 50 # y 50 ~ 950
BoxFillSize2 = 950 #

ImgSelected = None

def GetImageSize():
	return int(ScreenHeight / 1000 * 100)

def ImageResize():
	global ImgSelected
	a = Image.open(ReturnPos("\\img\\original\\Selected.png"))
	SizeValue = GetImageSize()
	b = a.resize((SizeValue, SizeValue))
	b.save(ReturnPos("\\img\\edited\\Selected.png"))
	ImgSelected = pygame.image.load(ReturnPos("\\img\\edited\\Selected.png"))

ImageResize()


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

def DrawIcons():
	ImageList = [ImgSelected]
	for i in range(len(ImageList)):
		Xval = ScreenWidth - GetImageSize()
		Yval = (50 + i * GetImageSize() + 50) * ScreenHeight / 1000
		screen.blit(ImageList[i], (Xval, Yval))

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

BoxData = [[False] * BoxNum for _ in range(BoxNum)]

X, Y = 0, 0
ZoomValue = 1
Draging = False
MouseLastPos = None

clock = pygame.time.Clock()

Run = True
while Run:
	ScreenWidth, ScreenHeight = pygame.display.get_surface().get_size()


	screen.fill((50,50,50))
	DrawBoxs()
	DrawIcons()

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
				BoxX, BoxY = ReturnBoxNum(pygame.mouse.get_pos())
				BoxData[BoxX][BoxY] = not BoxData[BoxX][BoxY]
			
			elif event.button == 2:
				for loopx in range(BoxNum):
					ExportValue = ""
					for loopy in range(BoxNum):
						ExportValue += str(1 if BoxData[loopy][loopx] else 0)
					print(hex(int(ExportValue, 2)))

		elif event.type == pygame.MOUSEBUTTONUP:
			if event.button == 1:
				Draging = False

		elif event.type == pygame.VIDEORESIZE:
			ScreenWidth, ScreenHeight = pygame.display.get_surface().get_size()
			ImageResize()
			# print("Resize")
		
	if Draging:
		ChangeValue = MouseLastPos[0] - pygame.mouse.get_pos()[0], MouseLastPos[1] - pygame.mouse.get_pos()[1]
		MouseLastPos = pygame.mouse.get_pos()
		X -= ChangeValue[0]
		Y -= ChangeValue[1]

	clock.tick(60)