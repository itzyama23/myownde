from enum import Enum
from source.colors import ColorList as color

class LogPrefix(Enum):
   INFO = f"{color.CYAN.value}[INFO]{color.RESET.value}"
   WARNING = f"{color.YELLOW.value}[WARNING]{color.RESET.value}"
   ERROR = f"{color.RED.value}[ERROR]{color.RESET.value}"
   SUCCESS = f"{color.GREEN.value}[SUCCESS]{color.RESET.value}"

