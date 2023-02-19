from logging import getLogger, StreamHandler, FileHandler, DEBUG, INFO, WARNING, ERROR, CRITICAL, Formatter

### LOGGER SETTINGS
DEFAULT_LOG_ADDRESS = 'log.txt'
DEFAULT_FORMAT = Formatter('%(asctime)s - %(levelname)s - logger:%(name)s - %(filename)s - L%(lineno)d - %(funcName)s - %(message)s')

# board
SIZE = 8

# index
FILE = 0
RANK = 1
WHITE, BLACK = 1, -1
A, B, C, D, E, F, G, H = 1, 2, 3, 4, 5, 6, 7, 8

# pieces
EMPTY = 0
P = PAWN = 1
R = ROOK = 2
N = NIGHT = 3
B = BISHOP = 4
Q = QUEEN = 5
K = KING = 6

def setLogger(name='default', *, level=INFO, fhandler=None, shandler=None, fhandler_level=DEBUG, shandler_level=CRITICAL, filemode='w', filename=DEFAULT_LOG_ADDRESS, fhandler_format=DEFAULT_FORMAT, shandler_format=DEFAULT_FORMAT):
    logger = getLogger()    
    logger.setLevel(level)
    
    # file handler
    fhandler = fhandler or FileHandler(filename, mode=filemode)
    fhandler.setLevel(fhandler_level)
    fhandler.setFormatter(fhandler_format)
    logger.addHandler(fhandler)
    
    # stream handler
    shandler = shandler or StreamHandler()
    shandler.setLevel(shandler_level)
    shandler.setFormatter(shandler_format)
    logger.addHandler(shandler)
    
    return logger
