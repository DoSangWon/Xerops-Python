#Author: Walid Daboubi
#walid.daboubi@gmail.com

import numpy as np
import pymysql

import json
from collections import OrderedDict
from sklearn import tree,linear_model


def get_data_details(args):
    data = np.array(args)
    features=data[:len(args)-1]
    features = features.reshape(1,-1)
    labels=data[len(args)-1:] # 성능이 중요시 된다면 하드코딩해주세요
    return features, labels

def get_occuracy(labels,predic,fltr):
    real_label_count=0.0
    predicted_label_count=0.0
    correct_count = 0.0
    for real_label in labels: #실제 라벨의 수
        if real_label==fltr:
            real_label_count+=1

    for i, val in enumerate(predic):
        if val == fltr and val == labels[i]:
            correct_count+=1

        if val == fltr:
            predicted_label_count += 1


    tmp = 0.0
    target = 0.0
    for i, val in enumerate(predic):
        if(labels[i] == fltr):
            target+=1
            if(labels[i] == val):
                tmp+=1


    """
    for predicted_label in predicted_labels:
    if predicted_label==fltr:
            predicted_label_count+=1
    """

    #print ("실제 공격 횟수:"+str(real_label_count))
    #print ("예측된 공격 횟수:"+str(predicted_label_count))

    #정밀도 = precision
    #precision=predicted_label_count*100/real_label_count
    #precision = predicted_label_count* 100 / real_label_count
    precision = tmp * 100 / target
    # group_data
    file_data = OrderedDict()
    file_data['real_attack'] = str(target)
    file_data['predict_attack'] = str(tmp)
    file_data['precision'] = str(precision)
    print(json.dumps(file_data, ensure_ascii=False, indent="\t"))
    print(json.dumps(file_data))
    with open('/opt/was/tomcat9/webapps/Xerops/data/xerops_learning.json', 'w', encoding='utf-8') as make_file:
        json.dump(file_data, make_file, ensure_ascii=False, indent="\t")
    return precision
