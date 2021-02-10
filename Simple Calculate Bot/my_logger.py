import logging


def my_logger():
  logger = logging.Logger(__name__)
  logger.setLevel(logging.DEBUG)
  formatter = logging.Formatter('%(levelname)s - %(filename)s - %(process)d - %(asctime)s - %(message)s')
  streamFormatter = logging.Formatter('%(levelname)s:  %(asctime)s  %(message)s')


  streamHandler = logging.StreamHandler()
  streamHandler.setLevel(logging.DEBUG)
  streamHandler.setFormatter(streamFormatter)

  logger.addHandler(streamHandler)
  return logger

