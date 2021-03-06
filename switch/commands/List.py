
from network.commands.Command import Command

class List:

    @staticmethod
    def req(redis, _to, _data=None):
        Command(redis.name, _to, '--switch ls', _data).send(redis)
        return None

    @staticmethod
    def res(redis, cmd):
        argv = cmd._command.replace('--switch ls', '').split(' ')
        if not cmd._data:
            manager = redis.instance['switchManager']
            redis.print('List command from %s, responsed' % cmd._from)
            cmd._data = { 'response': 1 }
            if argv == ['']:
                cmd._data['value'] = [ value.info() for (key, value) in manager.devices.items()]
            else:
                cmd._data['value'] = [ value.info() for (key, value) in manager.devices.items() if key in argv ]
            cmd.swap()
            cmd.send(redis)
        else:
            redis.print('List feed back from %s, %s' % (cmd._from, cmd._data))
        return None

