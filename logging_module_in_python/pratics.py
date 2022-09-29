import logging

# logging.basicConfig(level=logging.DEBUG,filemode="w",format="%(asctime)s-%(levelname)s-%(message)s",
#                     datefmt="%D-%m-%Y-%H-%M-%S",)

# logging.critical("Hello There how you are")


logger=logging.getLogger(name="sample")

logger.setLevel(logging.DEBUG)


# stream_handler = logging.FileHandler(filename="xyz.log",mode="w")

stream_handler = logging.StreamHandler()

stream_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(levelname)s-%(name)s-%(message)s")

stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)

logger.info("Hello There")