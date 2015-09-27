#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ionyshchenko
#
# Created:     17.03.2015
# Copyright:   (c) ionyshchenko 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

#import user interface
import SimpleGUICS2Pyscripter.simpleguics2pyscripter as simplegui

# import random module
import random

# global variables
x=random.randint(0,100)
guess_left=7
value=0
guess_result="Unknown"
hint="Try to guess my number"

# input handler
def input_handler(text):
    
    global value, guess_left, guess_result, hint
    value=int(text)
    
    if guess_left>0:
        guess_left=guess_left-1

        if value>x:
            hint="My number is smaller"
        if value<x:
            hint="My number is greater"
        if value==x:
            guess_left=0
            
    if guess_left<=0:
        if value==x:
            hint='You win! My number is ' + str(x)
        if value!=x:
            hint='You loose! My number was ' + str(x)
    return guess_result


def draw(canvas):
    canvas.draw_text("Guesses left:"+str(guess_left),[10,10],10,"White")
    canvas.draw_text(hint,[10,30],10,"Red")

frame=simplegui.create_frame("Example",200,200)
frame.set_draw_handler(draw)
frame.add_input("Number:",input_handler, 100)

frame.start()
