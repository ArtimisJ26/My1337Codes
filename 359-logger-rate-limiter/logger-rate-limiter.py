class Logger:

    def __init__(self):
        self.messageLog = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.messageLog:
            if timestamp < self.messageLog[message] + 10:
                return False

        self.messageLog[message] = timestamp
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)