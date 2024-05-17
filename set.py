import json

SETTINGS = {
    "path_to_matrix_one": "./data/matrix1.txt",
    "path_to_matrix_two": "./data/matrix2.txt",
    "path_to_matrix_result": "./data/resultMatrix.txt",
    "path_to_data": "./data/data.json",
    "path_to_save": "./data/"
}


if __name__ == "__main__":
    with open("settings.json", "w") as fp:
        json.dump(SETTINGS, fp)