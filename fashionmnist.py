import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import  confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from collections import defaultdict
from datetime import datetime

def neural_network():
    startTime = datetime.now()
    
    train_data = pd.read_csv('DataSets/sign_mnist_13bal_train.csv')
    
    X_train = train_data.drop('class', axis=1)
    X_train = X_train / 255.0
    y_train = train_data['class']
    
    X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=2, stratify=y_train)
    
    test_data = pd.read_csv('DataSets/sign_mnist_13bal_test.csv')
    
    X_test = test_data.drop('class', axis=1)
    X_test = X_test / 255.0
    y_test = test_data['class']
    
    neural_net_model = MLPClassifier(hidden_layer_sizes=(128, 64, 32), activation='relu', random_state=42, tol=0.005)
    
    neural_net_model.fit(X_train, y_train)
    
    layer_sizes = [neural_net_model.coefs_[0].shape[0]]
    layer_sizes += [coef.shape[1] for coef in neural_net_model.coefs_]
    layer_size_str = " x ".join(map(str, layer_sizes))
    print(f"Training set size: {len(y_train)}")
    print(f"Layer sizes: {layer_size_str}")
    
    y_pred_train = neural_net_model.predict(X_train)
    y_pred = neural_net_model.predict(X_test)
    y_pred2 = neural_net_model.predict(X_val)
    
    correct_counts = defaultdict(int)
    total_counts = defaultdict(int)
    overall_correct = 0
    
    correct_counts2 = defaultdict(int)
    total_counts2 = defaultdict(int)
    overall_correct2 = 0
    
    for true, pred in zip(y_test, y_pred):
        total_counts[true] += 1
        if true == pred:
            correct_counts[true] += 1
            overall_correct += 1
    
    for true, pred in zip(y_val, y_pred2):
        total_counts2[true] += 1
        if true == pred:
            correct_counts2[true] += 1
            overall_correct2 += 1
    
    total_counts_training = 0
    correct_counts_training = 0
    for true, pred in zip(y_train, y_pred_train):
        total_counts_training += 1
        if true == pred:
            correct_counts_training += 1
    
    for class_id in sorted(total_counts.keys()):
        accuracy = correct_counts[class_id] / total_counts[class_id] *100
        print(f"Accuracy for class {class_id}: {accuracy:3.0f}%")
    print(f"----------")
    overall_accuracy = overall_correct / len(y_test)*100
    overall_accuracy2 = overall_correct2 / len(y_val)*100
    print(f"Overall Test Accuracy: {overall_accuracy:3.1f}%")
    print(f"Overall Validation Accuracy: {overall_accuracy2:3.1f}%")
    overall_training_accuracy = correct_counts_training / total_counts_training*100
    print(f"Overall Training Accuracy: {overall_training_accuracy:3.1f}%")
    
    print(datetime.now() - startTime)
