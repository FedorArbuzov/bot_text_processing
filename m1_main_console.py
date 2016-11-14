from m1_main import *
from constants import START_MSG

print(START_MSG)
s = input()
if s != '':  # if there's no text after /search, start questioning user w/ buttons
    # parse message after the /search command and pass it further
    s1 = main_func(s.lower())
    asked_question = s.lower()
    s_mod2 = forming_string_from_neural(s1)
    querying_and_visualizing(s, s_mod2)
