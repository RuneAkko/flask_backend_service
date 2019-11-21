# import logging
# from logging.handlers import RotatingFileHandler
# import os
# from flask import Flask
# def create_app(config_name=None):
#     if config_name is None:
#         config_name = os.getenv('FLASK_CONFIG','development')
#     app = Flask('web')
#     app.config.from_object(config[config_name])
#     register_logging(app)


# def register_logging(app):
#     app.logger.setLevel(logging.INFO)
#     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s ')

#     file_handler = RotatingFileHandler('appLog.log',maxBytes=10*1024*1024,backupCount=10)

#     file_handler.setFormatter(formatter)
#     file_handler.setLevel(logging.INFO)
    
#     if not app.debug:
#         app.logger.addHandler(file_handler)