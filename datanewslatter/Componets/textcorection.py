from autocorrect import Speller
import pyautogui
import time

def corrigirtxt(text):
    spell = Speller(lang='pt')
    misspell = text.split()
    rt =''
    for palavra in misspell:
        rt += spell(palavra)+ ' '
    return rt


