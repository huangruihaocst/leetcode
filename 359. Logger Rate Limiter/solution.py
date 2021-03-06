class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.printed = dict()

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message in self.printed:
            if timestamp - self.printed[message] >= 10:
                self.printed[message] = timestamp
                return True
            else:
                return False
        else:
            self.printed[message] = timestamp
            return True


if __name__ == '__main__':
    logger = Logger()
    print(logger.shouldPrintMessage(1, 'foo'))
    print(logger.shouldPrintMessage(2, 'bar'))
    print(logger.shouldPrintMessage(3, 'foo'))
    print(logger.shouldPrintMessage(8, 'bar'))
    print(logger.shouldPrintMessage(10, 'foo'))
    print(logger.shouldPrintMessage(11, 'foo'))
