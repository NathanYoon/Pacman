from characters import *


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            game.recordHighScore()
        elif event.type == pygame.KEYDOWN:
            game.paused = False
            game.started = True
            if event.key == pygame.K_w:
                if not onLaunchScreen:
                    game.pacman.newDir = 0
            elif event.key == pygame.K_d:
                if not onLaunchScreen:
                    game.pacman.newDir = 1
            elif event.key == pygame.K_s:
                if not onLaunchScreen:
                    game.pacman.newDir = 2
            elif event.key == pygame.K_a:
                if not onLaunchScreen:
                    game.pacman.newDir = 3
            elif event.key == pygame.K_SPACE:
                if onLaunchScreen:
                    onLaunchScreen = False
                    game.paused = True
                    game.started = False
                    game.render()
                    pygame.mixer.music.load(MusicPath + "pacman_beginning.wav")
                    pygame.mixer.music.play()
                    musicPlaying = 1
            elif event.key == pygame.K_q:
                running = False
                game.recordHighScore()

    if not onLaunchScreen:
        game.update()
