import json

from network.commands.Command import Command
from network.commands.Message import Message
from network.commands.LoadConfig import LoadConfig
from network.commands.Shutdown import Shutdown

from status.Command import StatusCommand
from core.Command import LibreCiscoCommand
from switch.Command import SwitchCommand
from schedule.Command import ScheduleCommand
from server.Command import LibServerCommand

class Commander:

    @staticmethod
    def processRes(redis, command):
        if 'message' in command._command:
            Message.res(redis, command)
        elif 'load-config' in command._command:
            LoadConfig.res(redis, command)
        elif 'shutdown' in command._command:
            Shutdown.res(redis, command)

        elif StatusCommand.processCheck(command._command):
            StatusCommand.processRes(redis, command)

        elif '--librecisco' in command._command:
            LibreCiscoCommand.processRes(redis, command)
        elif '--switch' in command._command:
            SwitchCommand.processRes(redis, command)
        elif '--schedule' in command._command:
            ScheduleCommand.processRes(redis, command)
        elif '--libserver' in command._command:
            LibServerCommand.processRes(redis, command)

    @staticmethod
    def processReq(redis, _to=None, _command=None, _data=None):
        if 'message' in _command:
            Message.req(redis, _to, _command.replace('message ', ''))
        elif 'load-config' in _command:
            LoadConfig.req(redis, _to, _data)
        elif 'shutdown' in _command or 'exit' in _command:
            Shutdown.req(redis, _to, _data)

        elif StatusCommand.processCheck(_command):
            StatusCommand.processReq(redis, _to, _command, _data)

        elif '--librecisco' in _command:
            LibreCiscoCommand.processReq(redis, _to, _command, _data)
        elif '--switch' in _command:
            SwitchCommand.processReq(redis, _to, _command, _data)
        elif '--schedule' in _command:
            ScheduleCommand.processReq(redis, _to, _command, _data)
        elif '--libserver' in _command:
            LibServerCommand.processReq(redis, _to, _command, _data)
