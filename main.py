from my_row import *
import my_csv_extract as csv



def build_vector(Row1, Row2, fields, dist_str):
    result = list()
    for elem in fields:
        if elem != "rec_id" and elem != "csv_row":
            result.append(dist_str(getattr(Row1, elem), getattr(Row2, elem)))
    return result
            
   
            
def build_pairs(data, dist_str, amount_marked):
    fields = [a for a in dir(data[0]) if not a.startswith('__')]
    X =  list()
    Y =  list()
    for i in range(amount_marked):
        for j in range(i, amount_marked):
            X.append(build_vector(data[i], data[j], fields, dist_str))
            if (data[i].rec_id // 10 == data[j].rec_id // 10):
                Y.append(1)
            else:
                Y.append(0)     
    return X, Y



def cross_validated(clf, amount_marked, n_folds, X, Y):
    accuracies = list()
    precisions = list()
    recalls = list()
    f1_scores = list()
    for i in range(n_folds):
        tp = 0
        tn = 0
        fp = 0
        fn = 0
        bias = i * amount_marked
        clf.fit(X[bias:(bias + amount_marked)], Y[bias:(bias + amount_marked)])
        
        for j in range(0, bias):
            predict = (clf.predict([X[j]])[0] == Y[j])
            if Y[j] == 1 and predict:
                tp += 1
            elif Y[j] == 1 and (not predict):
                fn += 1
            elif Y[j] == 0 and (not predict):
                fp += 1
            else:
                tn += 1
            
        for j in range(bias + amount_marked, len(X)):
            predict = (clf.predict([X[j]])[0] == Y[j])
            if Y[j] == 1 and predict:
                tp += 1
            elif Y[j] == 1 and (not predict):
                fn += 1
            elif Y[j] == 0 and (not predict):
                fp += 1
            else:
                tn += 1
        accuracy = (tp + tn) / (tp + tn + fp + fn)
        accuracies.append(accuracy)
        
        precision = tp / (tp + fp)
        precisions.append(precision)
        
        recall = tp / (tp + fn)
        recalls.append(recall)
        
        f1_scores.append(2 * (precision * recall) / (precision + recall))
    
    print("accuracies")
    print(accuracies)
    print("average_accuracy =", sum(accuracies) / n_folds)
    
    print("precisions")
    print(precisions)
    print("average_precision =", sum(precisions) / n_folds)
    
    print("recalls")
    print(recalls)
    print("average_recall =", sum(recalls) / n_folds)
    
    print("f1_scores")
    print(f1_scores)
    print("average_f1_score =", sum(f1_scores) / n_folds)
    


def classify(data, amount_marked, n_folds, dist_str):
    X, Y = build_pairs(data, dist_str, amount_marked)
    
    from sklearn import tree
    clf = tree.DecisionTreeClassifier()
    
    cross_validated(clf, amount_marked, n_folds, X, Y)  
    

"""
main
"""

print("Write marked filename:")
filename = input()

data, fieldnames = csv.extract_data(filename)
data.sort()

print("Write amount of marked:")
amount_marked = int(input())


print("n_folds:")
n_folds = int(input())


print("Levenstein")
from nltk.metrics import edit_distance

classify(data, amount_marked, n_folds, edit_distance)



print("Jaccard")
from nltk.metrics import jaccard_distance

def my_jaccard(s1, s2):
    return jaccard_distance(set(s1), set(s2))

classify(data, amount_marked, n_folds, my_jaccard)


#csv.write_data(data, fieldnames, filename)