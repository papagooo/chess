""" This is our main driver file, will handle User input and
    display current GameState object
"""
import time
import pygame as p
# from ChessEngine import GameState  # does not work
# from ChessGam import ChessEngine  # does not work
import ChessEngine

IMAGE_PATH = (
    "images/"
    #    "d:/doc-share/@MyOwnDoc/Computer/@MyDevlop/python/myPack/images/"
)
WIDTH = HEIGHT = 512
DIMENSION = 8                                       # Rows/Cols
SQ_SIZE = HEIGHT // DIMENSION                       # Chessfield square size
# EDGE = 64                                         # Border width
# WIDTH = HEIGHT = 512 + 2 * EDGE                   # Screensize + Border
BACKGROUND_COL = (41, 41, 41)
WHITE = (255, 255, 255)
FONTSIZE = 32

IMAGES = {}
MAX_FPS = 10
MOVENUMBER = 1


"""
Load images just 1 time and create a global dictionary of images
"""


def loadImages():
    # method is    IMAGES['wP'] = p.image.load("images/wP.png")

    pieces = ["wR", "wN", "wB", "wQ", "wK",
              "wP", "bR", "bN", "bB", "bQ", "bK", "bP"]
    #    image_path = 'myChessE/images/'

    for piece in pieces:
        IMAGES[piece] = p.transform.scale(
            p.image.load(IMAGE_PATH + piece + ".png"), (SQ_SIZE, SQ_SIZE)
        )

        # use Dictionary by refering IMAGES["wR"]


"""
Main driver for input and updating
"""


def main():
    p.init()
    p.display.set_caption("My Chess Engine in Python")
    logo = p.image.load(IMAGE_PATH + "myIcon.png")
    p.display.set_icon(logo)

    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("black"))
    # create instance gs of GameState
    gs = ChessEngine.GameState()
    # print(gs.board)                               # debug show instance gs.board in console
    loadImages()                                    # do this only once before while loop
    running = True

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


""" 
Draw graphics for current game state

"""


def drawGameState(screen, gs):
    drawBoard(screen)                               # draw squares on the board
    drawPieces(screen, gs.board)                    # draw pieces on top


""" Draw squares on board, top left is always light color """


def drawBoard(screen):
    # Index 0 light, Index 1 black, mod2 of r+c
    colors = [p.Color("light gray"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            field_color = colors[((r + c) % 2)]
            p.draw.rect(screen, field_color, p.Rect(
                c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


""" Draw pieces on the board using current GameState.board """


def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(
                    c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":      # main only runs if this file is explicitely called
    main()
