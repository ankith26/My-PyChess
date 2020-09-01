'''
This file is a part of My-PyChess application.
In this file, we define a few general utilities for My-PyChess.
'''

import time

import pygame
import pygame.gfxdraw

# This function needs to be called when user wants to draw a rounded rect
def rounded_rect(surf, color, rect, radius=10, border=2, incolor=(0, 0, 0)):    
    if min(rect[2], rect[3]) > 2 * (radius + border):
        _filled_rounded_rect(surf, color, rect, radius)
        rect = (rect[0] + border, rect[1] + border,
                rect[2] - 2*border, rect[3] - 2*border)
        _filled_rounded_rect(surf, incolor, rect, radius)

# This is the function that draws a solid rounded rect
def _filled_rounded_rect(surf, color, rect, r):
    for x, y in [(rect[0] + r, rect[1] + r),
                 (rect[0] + rect[2] - r - 1, rect[1] + r),
                 (rect[0] + r, rect[1] + rect[3] - r - 1),
                 (rect[0] + rect[2] - r - 1, rect[1] + rect[3] - r - 1)]:
        pygame.gfxdraw.aacircle(surf, x, y, r, color)
        pygame.gfxdraw.filled_circle(surf, x, y, r, color)
    
    pygame.draw.rect(surf, color, (rect[0] + r, rect[1], rect[2] - 2*r, rect[3]))
    pygame.draw.rect(surf, color, (rect[0], rect[1] + r, rect[2], rect[3] - 2*r))

# A function to be used as a decorator to check execution time of a function
# Used only while testing.
def timeit(func):
    def inner(*args, **kwargs):
        start = time.perf_counter()
        ret = func(*args, **kwargs)
        end = time.perf_counter()
        print("Time:", round((end-start)*1000, 4), "ms")
        return ret
    return inner