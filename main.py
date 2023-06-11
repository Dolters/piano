import play
import pygame
pygame.init()
pygame.mixer.init()
play.set_backdrop("Light green")
text1 = play.new_text(words='Це класне піаніно для гри.', x = 0, y =200, font_size = 40)
text2 = play.new_text(words='Створи свою мелодію, натискаючи на клавіші.', x = 0, y =150, font_size = 40)
piano_on = play.new_circle(color="black", x = -180, y = -100, radius = 10, border_color = "black", border_width=3)
piano_txt = play.new_text(words="piano",  x = -145, y = -100, font_size = 25)
flute_on = play.new_circle(color="black", x = -100, y = -100, radius = 10, border_color = "black", border_width=3)
flute_txt = play.new_text(words = "flute", x = -65, y = -100, font_size = 25)
guitar_on = play.new_circle(color="black", x = -20, y = -100, radius = 10, border_color = "black", border_width=3)
guitar_txt = play.new_text(words = "guitar", x = 20, y = -100, font_size = 25)
violin_on = play.new_circle(color="black", x = 60, y = -100, radius = 10, border_color = "black", border_width=3)
violin_txt = play.new_text(words = "violin", x = 100, y = -100, font_size = 25)
keys = []
sounds = []
for s in range(4):
    sounds.append([])
# формуємо списки з клавішами та звуками 
for i in range(8):
    key_x = -180 + i * 50
    key = play.new_box(color = "white", width = 40, height = 120, x = key_x, y = 0, border_width = 3, border_color = "black")
    keys.append(key)
    sound = pygame.mixer.Sound(str(i + 1) + '.ogg')
    sounds[0].append(sound)
    sound = pygame.mixer.Sound('f' + str(i + 1) + ".ogg")
    sounds[1].append(sound)
    sound = pygame.mixer.Sound('g' + str(i + 1) + ".ogg")
    sounds[2].append(sound)
    sound = pygame.mixer.Sound('v' + str(i + 1) + ".ogg")
    sounds[3].append(sound)
get_instrument = 0
@piano_on.when_clicked
def piano_on():
    global get_instrument
    get_instrument = 0
    piano_on.color = "black"
    flute_on.color = "white"
    guitar_on.color = "white"
    violin_on.color = "white"
@flute_on.when_clicked
def flute_on():
    global get_instrument
    get_instrument = 1
    piano_on.color = "white"
    flute_on.color = "black"
    guitar_on.color = "white"
    violin_on.color = "white"
@guitar_on.when_clicked
def guitar_on():
    global get_instrument
    get_instrument = 2
    piano_on.color = "white"
    flute_on.color = "white"
    guitar_on.color = "black"
    violin_on.color = "white"
@violin_on.when_clicked
def violin_on():
    global get_instrument
    get_instrument = 3
    piano_on.color = "white"
    flute_on.color = "white"
    guitar_on.color = "white"
    violin_on.color = "black"
@play.when_program_starts
def start():
    pass
    
@play.repeat_forever
async def play_piano():
    for j in range(8):
        if keys[j].is_clicked:
            sounds[j].play()
            keys[j].color = "light green"
            await play.timer(0.3)
            keys[j].color = "white"


play.start_program()