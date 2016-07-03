from motuus.config import ROOT_FOLDER
# It seems to need the full path, otherwise it gets lost (plays a "pop" noise).
SOUND_FOLDER = ROOT_FOLDER + '/data/sound'

# pygame.mixer initialization values
FREQUENCY = 44100
SIZE = -16
CHANNELS = 2
BUFFER = 4096
