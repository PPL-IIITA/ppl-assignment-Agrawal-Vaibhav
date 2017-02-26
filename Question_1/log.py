import logging

def log(write):
	logging.basicConfig(filename='1.log', filemode='w+', level=logging.DEBUG, format='%(asctime)s %(name)-%(levelname)s - %(message)s')
	logging.info(write)
