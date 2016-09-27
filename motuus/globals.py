import os
from importlib import import_module

from config import PLAYER_SCRIPT

ROOT_FOLDER = os.path.dirname(os.path.abspath(__file__))
ROOT_FOLDER = os.path.dirname(ROOT_FOLDER)
print "The current root folder is:", ROOT_FOLDER
print "Motuus will try to execute '" + PLAYER_SCRIPT + ".py'"
Player = getattr(import_module('players.' + PLAYER_SCRIPT), 'Player')
