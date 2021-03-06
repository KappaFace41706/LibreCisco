import re

from network.commands.Command import Command

class LoadFolder:

    @staticmethod
    def req(redis, _to, _data=None):
        Command(redis.name, _to, '--schedule load-folder', _data).send(redis)
        return None

    @staticmethod
    def res(redis, cmd): 
        argv = cmd._command.replace('--schedule load-fodler', '').split(' ')
        if not cmd._data:
            manager = redis.instance['scheduleManager']
            path = re.compile('-path=.*?.json', re.DOTALL).search(cmd._command)

            redis.print('Load-Folder command from %s, responsed' % cmd._from)
            manager.loadFolder(path=path.group(0)[6:] if path else None, overwrite='-force' in argv, immediate='-immediate' in argv)
            cmd.swap()
            cmd._data = { 'response': 1 }
            cmd.send(redis)
        else:
            redis.print('Load-Folder command feed back from %s.' % cmd._from)
        return None

