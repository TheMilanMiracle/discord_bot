import dotenv as env
import os
from libs import client as bc
from libs import events

env.load_dotenv()

bc.botClient.run(os.environ["TOKEN"])
