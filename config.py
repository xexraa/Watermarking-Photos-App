import configparser


config = configparser.ConfigParser()
config.read('config.ini')

FONT = config.get('DEFAULT', 'FONT')
IMAGE_FONT = config.get('DEFAULT', 'IMAGE_FONT')
IMAGE_BLUR_FONT = config.getint('DEFAULT', 'IMAGE_BLUR_FONT')
IMAGE_FONT_COLOR = tuple(int(c) for c in config.get('DEFAULT', 'IMAGE_FONT_COLOR').split(','))
IMAGE_FONT_SIZE = config.getint('DEFAULT', 'IMAGE_FONT_SIZE')


# Signature position, default is bottom right corner
POSITION_X = config.getint('DEFAULT', 'POSITION_X')
POSITION_Y = config.getint('DEFAULT', 'POSITION_Y')


DEFAULT_FILE_NAME = config.get('DEFAULT', 'DEFAULT_FILE_NAME')
BG_COLOR = config.get('DEFAULT', 'BG_COLOR')
