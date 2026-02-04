import json


class DataManager:
    DATA_FILE_PATH = "data.json"

    @staticmethod
    def save_data_to_file(data):
        with open(DataManager.DATA_FILE_PATH, "w") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def retieve_file_data():
        with open(DataManager.DATA_FILE_PATH, "r") as file:
            return json.load(file)
