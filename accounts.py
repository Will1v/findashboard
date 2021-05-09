import logger as log_util

logger = log_util.get_logger("Accounts", "FinanceTracker")

class BankAccount:

    def __init__(self, account_name, balance=0, currency='GBP', url=None):
        logger.info("Creating new {}. Name: {} / initial balance = {} {}".format(self.__class__.__name__, account_name, balance, currency))
        self.name = account_name
        self.balance = balance
        self.currency = currency
        self.url = url

    def __repr__(self):
        return "[{}] {}: {} {}".format(self.__class__.__name__, self.name, self.balance, self.currency)

    def deposit(self, amount):
        self.balance += amount
        logger.info("{} deposited on {} ({})".format(amount, self.name, self.__class__.__name__))

    def withdraw(self, amount):
        self.balance -= amount
        logger.info("{} withdrawn from {} ({})".format(amount, self.name, self.__class__.__name__))




class FixedRateAccount(BankAccount):

    def __init__(self, account_name, rate, term_duration, balance=0, ):
        pass