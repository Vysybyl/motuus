import os
from importlib import import_module

from config import PLAYER_SCRIPT

ROOT_FOLDER = os.path.dirname(os.path.abspath(__file__))
ROOT_FOLDER = os.path.dirname(ROOT_FOLDER)

Player = getattr(import_module('players.' + PLAYER_SCRIPT), 'Player')
