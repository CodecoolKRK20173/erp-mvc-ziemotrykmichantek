from asciimatics.particles import Rain
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
from asciimatics.effects import BannerText, Print, Scroll
from asciimatics.renderers import ColourImageFile, FigletText, ImageFile, SpeechBubble
import sys


def demo(screen):
    scenes = []
    effects = [
        Rain(screen,99**99,),
        Print(screen,
              FigletText("Pr0j3ct InFInIt3",
                         font='banner3' if screen.width > 80 else 'banner'),
              screen.height//2-3,
              colour=2, bg=2),
        Print(screen,
                  SpeechBubble("Pr3ss Q to St@rt"),
                  screen.height-5,
                  speed=1, transparent=False)
    ]
    scenes.append(Scene(effects))
    screen.play(scenes, stop_on_resize=True)

def start():
    Screen.wrapper(demo)
