from chopstick_state_class import ChopstickState

class Chopstick():

    def __init__(self):
        self._state = ChopstickState.free
        self._owner = None

    @property
    def owner(self):
        return self.owner

    @owner.setter
    def owner(self, owner):
        self._owner = owner

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

