import requests
import pickle

def list_maker():
    with open("Iris_data.txt", "r") as f:
        text = f.read()
        list_data = text.split("\n")
        return list_data

if __name__ == '__main__':
    with open("Iris_data.txt") as f:
        c = f.read()
    if c != "":
        a = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
        data = (a.text)
        with open("Iris_data.txt", "w") as f:
            f.write(data)
    file = "Iris_Pickle.pkl"
    with open(file, "wb") as f:
        pickle.dump(list_maker(), f)
    
    file = "Iris_Pickle.pkl"
    with open(file, "rb") as f:
        a = pickle.load(f)
        for i in a:
            print(i)
