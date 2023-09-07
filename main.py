import dotenv as env
import os
from libs.client import *
from libs.events import *
from libs.commands import *

env.load_dotenv()

botClient.run(os.environ["TOKEN"])
