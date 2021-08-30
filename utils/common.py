import uuid
def generateToken():
    return uuid.uuid4().hex
def get_logger():
    import logging
    import logging.handlers
    import datetime
    dt = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.DEBUG)
    logger.setLevel(logging.DEBUG)
    rf_handler = logging.handlers.TimedRotatingFileHandler(filename='../log/all@'+dt+'.log',when='midnight',interval=1,backupCount=7,atTime=datetime.time(0,0,0,0))
    rf_handler.setFormatter((logging.Formatter("%(asctime)s-%(levelname)s-%(message)s")))
    f_handler = logging.FileHandler(filename='../log/error@'+dt+'.log')
    f_handler.setLevel(logging.ERROR)
    f_handler.setFormatter(logging.Formatter("%(asctime)s-%(levelname)s-%(filename)s[:%(lineo)d]-%(message)s"))
    logger.addHandler(rf_handler)
    logger.addHandler(f_handler)
    return logger