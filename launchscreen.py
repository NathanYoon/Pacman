from characters import *

def displayLaunchScreen():
    # Draw Pacman Title
    pacmanTitle = ["tile016.png", "tile000.png", "tile456.png", "tile012.png", "tile000.png", "tile013.png"]
    for i in range(len(pacmanTitle)):
        letter = pygame.image.load(TextPath + pacmanTitle[i])
        letter = pygame.transform.scale(letter, (int(square * 4), int(square * 4)))
        screen.blit(letter, ((2 + 4 * i) * square, 2 * square, square, square))

    # Draw Character / Nickname
    characterTitle = [
        #Character
        "tile002.png", "tile007.png", "tile000.png", "tile018.png", "tile000.png", "tile002.png", "tile020.png", "tile004.png", "tile018.png",
        # /
        "tile015.png", "tile042.png", "tile015.png",
        # Nickname
        "tile013.png", "tile008.png", "tile002.png", "tile010.png", "tile013.png", "tile000.png", "tile012.png", "tile004.png"
    ]
    for i in range(len(characterTitle)):
        letter = pygame.image.load(TextPath + characterTitle[i])
        letter = pygame.transform.scale(letter, (int(square), int(square)))
        screen.blit(letter, ((4 + i) * square, 10 * square, square, square))

    #Draw Characters and their Nickname
    characters = [
        # Blinky
        [
            "tile457.png", "tile015.png", "tile107.png", "tile015.png", "tile083.png", "tile071.png", "tile064.png", "tile067.png", "tile078.png", "tile087.png",
            "tile015.png", "tile015.png", "tile015.png", "tile015.png",
            "tile108.png", "tile065.png", "tile075.png", "tile072.png", "tile077.png", "tile074.png", "tile089.png", "tile108.png"
        ],
        # Pinky
        [
            "tile458.png", "tile015.png", "tile363.png", "tile015.png", "tile339.png", "tile336.png", "tile324.png", "tile324.png", "tile323.png", "tile345.png",
            "tile015.png", "tile015.png", "tile015.png", "tile015.png",
            "tile364.png", "tile336.png", "tile328.png", "tile333.png", "tile330.png", "tile345.png", "tile364.png"
        ],
        # Inky
        [
            "tile460.png", "tile015.png", "tile363.png", "tile015.png", "tile193.png", "tile192.png", "tile211.png", "tile199.png", "tile197.png", "tile213.png", "tile203.png",
            "tile015.png", "tile015.png", "tile015.png",
            "tile236.png", "tile200.png", "tile205.png", "tile202.png", "tile217.png", "tile236.png"
        ],
        # Clyde
        [
            "tile459.png", "tile015.png", "tile363.png", "tile015.png", "tile272.png", "tile270.png", "tile266.png", "tile260.png", "tile281.png",
            "tile015.png", "tile015.png", "tile015.png", "tile015.png", "tile015.png",
            "tile300.png", "tile258.png", "tile267.png", "tile281.png", "tile259.png", "tile260.png", "tile300.png"
        ]
    ]
    for i in range(len(characters)):
        for j in range(len(characters[i])):
            if j == 0:
                    letter = pygame.image.load(TextPath + characters[i][j])
                    letter = pygame.transform.scale(letter, (int(square * spriteRatio), int(square * spriteRatio)))
                    screen.blit(letter, ((2 + j) * square - square//2, (12 + 2 * i) * square - square//3, square, square))
            else:
                letter = pygame.image.load(TextPath + characters[i][j])
                letter = pygame.transform.scale(letter, (int(square), int(square)))
                screen.blit(letter, ((2 + j) * square, (12 + 2 * i) * square, square, square))
    # Draw Ghosts chasing Pacman
    event1 = ["tile457.png", "tile015.png", "tile458.png", "tile015.png",  "tile459.png", "tile015.png", "tile460.png", "tile015.png", "tile456.png", "tile015.png",  "tile455.png"]
    for i in range(len(event1)):
        character = pygame.image.load(TextPath + event1[i])
        character = pygame.transform.scale(character, (int(square * 2), int(square * 2)))
        screen.blit(character, ((4 + i * 2) * square, 21 * square, square, square))
    # Draw Pacman chasing Ghosts
    event2 = ["tile015.png", "tile456.png", "tile015.png", "tile462.png", "tile015.png", "tile462.png", "tile015.png", "tile462.png", "tile015.png", "tile462.png", "tile015.png"]
    for i in range(len(event2)):
        platform = pygame.image.load(TextPath + event2[i])
        platform = pygame.transform.scale(platform, (int(square * 2), int(square * 2)))
        screen.blit(platform, ((4 + i * 2) * square, 25 * square, square, square))
    # highscores
    highscores = ["tile007.png", "tile008.png", "tile006.png", "tile007.png", "tile019.png", "tile002.png", "tile032.png", "tile018.png", "tile004.png", "tile019.png"]
    for i in range(len(highscores)):
        letter = pygame.image.load(TextPath + highscores[i])
        letter = pygame.transform.scale(letter, (int(square), int(square)))
        screen.blit(letter, ((9 + i) * square, 33 * square, square, square))
    # Press Space to Play
    instructions = ["tile016.png", "tile018.png", "tile004.png", "tile019.png", "tile019.png", "tile015.png", "tile019.png", "tile016.png", "tile000.png", "tile002.png", "tile004.png", "tile015.png", "tile020.png", "tile014.png", "tile015.png", "tile016.png", "tile011.png", "tile000.png", "tile025.png"]
    for i in range(len(instructions)):
        letter = pygame.image.load(TextPath + instructions[i])
        letter = pygame.transform.scale(letter, (int(square), int(square)))
        screen.blit(letter, ((4.5 + i) * square, 30 * square - 10, square, square))

    pygame.display.update()