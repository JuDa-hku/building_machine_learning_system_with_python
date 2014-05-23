import numpy as np

def learn_model(features, labels):
    best_acc=-1.0
    for f in range(features.shape[1]):
        thresh = features[:, f].copy()
        thresh.sort()
        for value in thresh:
            pred=(features[:, f] > value)
            acc= (pred == labels).mean()
            if acc > best_acc:
                best_acc = acc
                best_f = f
                best_value = value
    return best_value, best_f
    
def apply_model(features, model):
    value, f = model
    return features[:, f] > value
    
def accuracy(features, labels, model):
    preds = apply_model(features, model)
    return np.mean(preds==labels)



    