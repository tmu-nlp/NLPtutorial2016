from collections import defaultdict

def create_features(x):
    phi = defaultdict(int)
    words = x.split()
    for word in words:
        phi["UNI:" + word] += 1
    return phi

def predict_one(w, phi):
    score = 0
    for name, value in phi.items():
        if name in w:
            score =+ value*w[name]
    if score >= 0:
        return 1
    else:
        return -1

def update_weights(w, phi, y):
    for name, value in phi.items():
        w[name] += value * int(y)

if __name__ == "__main__":
    w = defaultdict(int)
    count = 0
    while count < 15:
        count += 1
        for line in open("titles-en-train.labeled"):
            y,x = line.strip().split("\t")
            phi = create_features(x)
            yy = predict_one(w,phi)
            if yy != y:
                update_weights(w, phi, y)
    with open("perceptron_model.txt","w") as line:
        for key,value in w.items():
            line.write("{} {}\n".format(key, value))
