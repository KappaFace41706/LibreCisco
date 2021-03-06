
from network.commands.Command import Command
from schedule.commands.List import List
from schedule.commands.Sync import Sync
from schedule.commands.LoadFolder import LoadFolder
from schedule.commands.Start import Start
from schedule.commands.Stop import Stop

class ScheduleCommand:

    @staticmethod
    def processRes(redis, command):
        if 'ls' in command._command:
            List.res(redis, command)
        elif 'sync' in command._command:
            Sync.res(redis, command)
        elif 'load-folder' in command._command:
            LoadFolder.res(redis, command)
        elif 'start' in command._command:
            Start.res(redis, command)
        elif 'stop' in command._command:
            Stop.res(redis, command)

    @staticmethod
    def processReq(redis, _to, _command, _data):
        if 'ls' in _command:
            List.req(redis, _to, _data)
        elif 'sync' in _command:
            Sync.req(redis, _to, _data)
        elif 'load-folder' in _command:
            LoadFolder.req(redis, _to, _data)
        elif 'start' in _command:
            Start.req(redis, _to, _data)
        elif 'stop' in _command:
            Stop.req(redis, _to, _data)
        
