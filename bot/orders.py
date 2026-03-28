from bot.logging_config import setup_logger

logger = setup_logger()

def log_order_request(params):
    logger.info(f"Order Request: {params}")

def log_order_response(response):
    logger.info(f"Order Response: {response}")

def log_error(error):
    logger.error(f"Error: {str(error)}")