from Logging import Logging

class Main:

    def __init__(self):
        self.logger = Logging.get(module=self.__class__.__name__)

    def test_logging(self):
        self.logger.info('This is Test about info')
        self.logger.debug('This is Test about debug')
        self.logger.error('This is Test about error')


if __name__ == '__main__':
    m = Main()
    m.test_logging()
