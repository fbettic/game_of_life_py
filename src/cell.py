class Cell:
    def __init__(self):
        self._status = 'Dead'

    # matar celula
    def set_dead(self):
        self._status = 'Dead'

    # revivir celula
    def set_alive(self):
        self._status = 'Alive'

    def is_alive(self):
        if self._status == 'Alive':
            return True
        return False
