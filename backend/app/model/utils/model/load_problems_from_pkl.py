import pickle

def load_problems_from_pkl(path: str):
    with open(path, 'rb') as file:
        data = pickle.load(file)
    return data