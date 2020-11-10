from rasa.core.channels.facebook import FacebookInput
from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter
import os
from rasa.core.utils import EndpointConfig
# load your trained agent
#interpreter = RasaNLUInterpreter("models/nlu/default/horoscopebot/")
MODEL_PATH = "./models/20200820-074654.tar.gz"
action_end_point = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load(MODEL_PATH, action_endpoint=action_end_point)
input_channel = FacebookInput(
fb_verify="asdf;lkj",
# you need tell facebook this token, to confirm your URL
fb_secret="99deccebeaed0c908a974c12f901176d", # your app secret
fb_access_token="EAARixYEP3lQBAEe6DUj8snZBEcN2EHS1xeN5SEtP6Y0ZBDdKMdFcaXNg8tbffmEx5ZALgWEVzCFhILiIrlKISFiEZAGCJu3SMEnN8YExcyO0tNRwQuDru9BoikZAdDq1qvncnfYl5LWhIYAoEP4dXD7cOJ1tfE9ahY2cqE5JM6IizDCFttoVq"
)

s = agent.handle_channels([input_channel], int(os.environ.get('PORT',5004)))
