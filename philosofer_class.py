import random
from time import sleep

from philosopher_state import PhilosopherState
import threading

from chopstick_class import Chopstick, ChopstickState


class Philosopher(threading.Thread):


    def __init__(self, name, resource):
        self._philosopher_name = name
        self._eating_time = 5
        self._state = PhilosopherState.thinking
        self._resource_pointer = [Chopstick()]
        threading.Thread.__init__(self) #, name=self.philosopher_name, target=self.run(), args=())

    @property
    def philosopher_name(self):
        return self._philosopher_name

    @philosopher_name.setter
    def philosopher_name(self, name):
        self._philosopher_name = name

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state


    def eat(self, chopsticks):
        self.state(PhilosopherState.eating)
        print ("Philosopher {} is eating.".format(self.philosopher_name))
        sleep(self._eating_time)
        for chop in chopsticks:
            chop.state = ChopstickState.free
            chop.owner = None

    def think(self):
        self.state = PhilosopherState.thinking
        print ("Philosopher {} is thinking.".format(self.philosopher_name))
        sleep(random.randint(1,10))

    def run(self):
        print("Philosopher {} has joined the table.".format(self.philosopher_name))
        while True:
            acquired_chopsticks = []
            for chopstick in self._resource_pointer:
                if chopstick.state == ChopstickState.free:
                    chopstick.state = ChopstickState.busy
                    chopstick.owner = self.name
                    acquired_chopsticks.append(chopstick)
                    if len(acquired_chopsticks) == 2:
                        self.eat()
                else:
                        self.think()









