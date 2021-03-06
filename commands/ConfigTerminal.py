from commands.Command import Command
from utils.Enums import SwitchMode

class ConfigTerminal(Command):
    
    reg = '^conf{1}(igure)? t{1}(erminal)?'
    mode = SwitchMode.ENABLE

    def __init__(self):
        super().__init__()
        self.name = 'configure terminal'

    def __pre_execute__(self, exe):
        if exe.mode == SwitchMode.ENABLE:
            exe.mode = SwitchMode.CONTER
        else:
            pass
