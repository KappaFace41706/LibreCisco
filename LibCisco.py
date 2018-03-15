import sys, time, traceback

from queue import Queue
from Config import Config
from switch.Manager import SwitchManager
from server.Server import LibServer
from schedule.Manager import ScheduleManager
from utils.Enums import LogLevel
from utils.Manager import ThreadManager

class OutputStream(ThreadManager):

    def __init__(self, inputStream, outputQueue):
        ThreadManager.__init__(self, 'OutputStream', outputQueue)
        self.inputStream = inputStream
        self.print('Inited.', LogLevel.SUCCESS)

    def run(self):
        while not self.stopped.wait(0.1) or not self.outputQueue.empty():
            if not self.outputQueue.empty():
                print('[%17f]%s %s\x1b[0m' % (self.outputQueue.get()))
            elif self.inputStream.isExit():
                self.exit()

    def exit(self):
        super(OutputStream, self).exit()
        self.outputQueue.put((time.time(), LogLevel.SUCCESS.value, 'LibCisco all Process/Thread exited, bye.'))

class InputStream(ThreadManager):
    
    def __init__(self, instance, outputQueue):
        ThreadManager.__init__(self, 'InputStream', outputQueue)
        self.instance = instance
        self.outputQueue = outputQueue
        self.print('Inited.', LogLevel.SUCCESS)

    def run(self):
        while True:
            if self.outputQueue.empty():
                choice = input('> ')
                self.print('operator execute command: %s' % choice)
                if '--schedule' in choice:
                    self.instance['scheduleManager'].command(choice.replace('--schedule', ''))
                elif choice == 'exit':
                    for (key, values) in self.instance.items():
                        values.exit()
                    return

if __name__ == '__main__':

    try:
        instance = {}
        outputQueue = Queue()

        switchManager = SwitchManager(outputQueue)
        switchManager.start()
        instance['switchManager'] = switchManager

        scheduleManager = ScheduleManager(switchManager.tempDB, outputQueue)
        scheduleManager.start()
        instance['scheduleManager'] = scheduleManager

        LIB_HOST = Config.LIB_SERVER['HOST']
        LIB_PORT = Config.LIB_SERVER['PORT']

        for each in sys.argv:
            if '--LIB_HOST=' in each:
                LIB_HOST = str(each[7:])
            elif '--LIB_PORT=' in each:
                LIB_PORT = int(each[7:])
    
        #libServer = LibServer(outputQueue, LIB_HOST, LIB_PORT)
        #libServer.start()
        #instance['libServer'] = libServer

        inputStream = InputStream(instance, outputQueue)
        inputStream.start()
        instance['inputStream'] = inputStream

        outputStream = OutputStream(inputStream, outputQueue)
        outputStream.start()
        outputStream.join()
    except:
        traceback.print_exc()
    
