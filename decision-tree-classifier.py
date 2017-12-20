
# About: Use supervised learning decision tree classifier to predict intrusion/suspecious activities in http logs
# Author: walid.daboubi@gmail.com
# Version: 1.0 - 2017/03/07

from utilities import *
import datetime
import time
while 1:
    today = datetime.date.today()
    print(today)
    conn = pymysql.connect(host='localhost', port=3306, user='snort', password='1234', database='snort')
    #트레이닝
    training_query = "select e.signature, sig_rev, signature.sig_priority from event as e inner join iphdr on e.cid = iphdr.cid AND e.sid = iphdr.sid inner join signature on e.signature = signature.sig_id inner join sig_class on signature.sig_class_id = sig_class.sig_class_id where  e.timestamp <  '" + str(today) + "'order by e.cid;"
    cursor = conn.cursor(pymysql.cursors.SSCursor)
    cursor.execute(training_query)
    rows = cursor.fetchall()
    cursor.close()
    #테스트
    testing_query = "select e.signature, sig_rev, signature.sig_priority from event as e inner join iphdr on e.cid = iphdr.cid AND e.sid = iphdr.sid inner join signature on e.signature = signature.sig_id inner join sig_class on signature.sig_class_id = sig_class.sig_class_id where  e.timestamp > '" + str(today) + "' order by e.cid ;"
    cursor2 = conn.cursor(pymysql.cursors.SSCursor)
    cursor2.execute(testing_query)
    rows2 = cursor2.fetchall()
    cursor2.close()
    """
    # for function test
    for row in rows:
        f, l = get_data_details(row)
       # print("features : {0}".format(f))
        #print("labels: {0}".format(l))
        #print("==================================")
    for row2 in rows2:
        f, l = get_data_details(row2)
    """

    conn.close()

    """

    # Get training features and labeles
    training_features, traning_labels = get_data_details(row) # training
    #print(training_features)
    #print(traning_labels)
    # Get testing features and labels
    testing_features, testing_labels = get_data_details(row2) #test
    """
    ### DECISON TREE CLASSIFIER
    #print("\n\n=-=-=-=-=-=-=- Decision Tree Classifier -=-=-=-=-=-=-=-\n")

    # Instanciate the classifier
    attack_classifier = tree.DecisionTreeClassifier()

    training_features = []
    training_labels = []
    count = 0 # row count test
    count2 = 0
    for row in rows:
        count+=1
        # Train the classifier
        # training_features, training_labels = get_data_details(row)
        # train_label_list.append(training_labels)
        f, l = get_data_details(row)
        training_features.append(f)
        training_labels.append(l)
    print("트레이닝데이타 : "+str(count))
    training_features = np.array(training_features).squeeze()
    training_labels = np.array(training_labels).squeeze()
    #print(training_features)
    # print(training_labels)
    attack_classifier = attack_classifier.fit(training_features, training_labels)

    # get predections for the testing data
    testLabel = []
    testResult = []

    testing_features = []
    testing_labels = []
    for row2 in rows2:
        count2 +=1
        f, l = get_data_details(row2)
        testing_features.append(f)
        testing_labels.append(l)
    print("학습 데이타 : "+str(count2))
    testing_features = np.array(testing_features).squeeze()
    predictions = attack_classifier.predict(testing_features)
    # testResult.append(predictions.item())

    testing_labels = np.array(testing_labels).squeeze()
    # print(predictions[predictions==1])
    # print(testing_labels)
    # print("의사 결정 트리 분류기의 정밀도 is: " + str(get_occuracy(testing_labels, predictions, 1)) + "%")
    #print("의사 결정 트리 분류기의 정밀도 is: " + str(get_occuracy(testing_labels, predictions, 1)) + "%")
    precision = str(get_occuracy(testing_labels, predictions, 1))
    time.sleep(1800)
