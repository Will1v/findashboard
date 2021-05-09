import logger as log_util
from accounts import BankAccount

logger = log_util.get_logger("FinanceTracker", "FinanceTracker")
logger.setLevel("INFO")

if __name__ == "__main__":
    logger.info("Starting Finance Tracker...")
    account = BankAccount("New account", 10)
    logger.info(account)