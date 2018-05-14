import multiprocessing as mp
from typing import Callable, List

class BaseHandler:
    """ Handling tasks efficiently
    """
    def __init__(self, n: int = mp.cpu_count()):
        self.pool = mp.Pool(n)

    def task(args):
        """ Override
        """
        pass

    def callback(result):
        """ Override
        """
        pass

    def run(args: List):
        self.result = self.pool.map_async(self.task, args, callback=self.callback)
        self.result.wait()


class Handler(BaseHandler):
    """ Handling tasks efficiently
    """
    def __init__(self, task: Callable, callback: Callable = lambda g: None, n: int = mp.cpu_count()):
        super().__init__(n)
        self.task = task
        self.callback = callback
