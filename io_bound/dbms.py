import json
import os


class DBMS:
    def __init__(self, file_path):
        self.file_path = file_path
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                json.dump([], f)

    def _load_data(self):
        with open(self.file_path, 'r') as f:
            return json.load(f)

    def _save_data(self, data):
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)

    def select(self, filter_fn=None):
        data = self._load_data()
        return list(filter(filter_fn, data)) if filter_fn else data

    def insert(self, record):
        data = self._load_data()
        data.append(record)
        self._save_data(data)

    def update(self, filter_fn, update_fn):
        data = self._load_data()
        for record in data:
            if filter_fn(record):
                update_fn(record)
        self._save_data(data)

    def delete(self, filter_fn):
        data = self._load_data()
        data = [record for record in data if not filter_fn(record)]
        self._save_data(data)
