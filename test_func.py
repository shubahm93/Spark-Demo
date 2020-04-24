import logging
from datetime import datetime

tm = str(datetime.now().timestamp())


logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s', filename=r'C:\Users\HP\Desktop\sample_'+tm+'.log')
logging.info("This is info msg!!!")
logging.error("This is error msg!!!")
logging.warning("This is warning msg!!!")
