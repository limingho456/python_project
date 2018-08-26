import sys

from ibapi.wrapper import EWrapper
from ibapi.client import EClient
import ibapi.wrapper
import ibapi.decoder

class AppMain(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)
        self.nextValidOrderId = None
        self.permId2ord = {}


def main():
    appMain = AppMain()

if __name__ == "__main__":
    main()
