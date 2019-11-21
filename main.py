from flask import Flask,request
import os
import re
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
app.config['sensor_log'] = "sensor_log"
app.config['learning_log'] = "learning_log"

# app.logger.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s ')

# if not os.path.exists("log"):
#     os.makedirs("log")

# file_handler = RotatingFileHandler('log/appLog.log',maxBytes=10*1024*1024,backupCount=10)

# file_handler.setFormatter(formatter)
# file_handler.setLevel(logging.INFO)

# app.logger.addHandler(file_handler)
    


@app.route('/')
def index():
    return 'hello!'

@app.route('/user_log_post/<learning_log>',methods=['GET','POST'])
def receive_user_learning_log(learning_log):
    temp = learning_log.encode('utf-8')
    temp_pro = temp.decode('utf-8')
    split_temp_pro = re.split(r"&",temp_pro)
    file_name_1 = re.sub(r's=',"",split_temp_pro[1])
    file_name_2 = re.sub(r't=',"",split_temp_pro[3])[:10]
    download_path = "learning_log" + "/" + file_name_1
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    file_name = download_path + "/" + file_name_1 + '_' + file_name_2 + '.txt'
    with open(file_name,'a',encoding='utf-8') as f:
        f.write(temp_pro+'\n')
    # print (learning_log.encode('utf-8'))
    return 'learning_log_posted done',200

@app.route('/sensor_log_post/',methods=['GET','POST'])
def receive_sensor_log():
    file = request.files['uploadedfile']
    temp = file.filename
    # temp_pro = temp.decode('utf-8')
    split_temp_pro = re.split(r"-",temp)
    path_0 = "sensor_log"
    path_1 = split_temp_pro[0]
    path_2 = "_".join(split_temp_pro[3:6])
    download_path = path_0 + "/" + path_1 + "/" + path_2
    isExists = os.path.exists(download_path)
    if not isExists:
        os.makedirs(path_0 +"/"+path_1+"/"+path_2)
        file.save(os.path.join(download_path,file.filename))
    else:
        file.save(os.path.join(download_path,file.filename))
    # print (request.files['uploadedfile'])
    return 'sensor_log_posted done',200