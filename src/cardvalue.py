from enum import Enum
from enum import auto
class CardValue(Enum):
    UNTER = 2
    OBER = 3
    KÖNIG = 4
    ZEHNER = 10
    SAU = 11

class CardColour(Enum):
    HERZ = auto()
    SCHELLEN = auto()
    EICHEL = auto()
    GRÜN = auto()
