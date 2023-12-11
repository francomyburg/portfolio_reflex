import reflex as rx
from .fonts import Font
from .colors import TextColor,Color
from enum import Enum

class Size(Enum):
    SMALL = "0.5em"
    DEFAULT = "1em"
    BIG = "2em"

STYLESHEETS = ["https://unpkg.com/nes.css@latest/css/nes.min.css",
               "https://fonts.googleapis.com/css?family=Press+Start+2P&display=swap"]

BASE_STYLE = {"font_family":Font.DEFAULT.value,
              "color":TextColor.PRIMARY.value}
    