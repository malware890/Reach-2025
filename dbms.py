import json
import os


class SimpleJSONDatabase:
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
        if not isinstance(record, dict):
            raise ValueError("Record must be a dictionary.")
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


# db = SimpleJSONDatabase('database.json')

# db.insert({"id": 1, "name": "Alice", "age": 25})
# db.insert({"id": 2, "name": "Bob", "age": 30})

# print("All Records:", db.select())

# def update_age(record):
#     record["age"] = 26

# db.update(lambda r: r["id"] == 1, update_age)
# print("After Update:", db.select())

# db.delete(lambda r: r["id"] == 2)
# print("After Deletion:", db.select())
