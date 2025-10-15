import json

class DataProcessor:
    def __init__(self, file_path):
        self.data = None
        self.file = file_path

    def read_data(self):
        # Reads data from the file
        f = open(self.file, 'r')
        self.data = json.load(f)
        f.close()

    def process_and_filter(self):
        # Processes the data based on a fixed condition
        if self.data:
            temp_list = []
            for item in self.data['records']:
                if item['value'] > 50 and item['status'] == 'active':
                    new_val = item['value'] * 1.1 # increase value by 10%
                    temp_list.append(new_val)
            return temp_list

# Example usage
dp = DataProcessor("my_data.json")
dp.read_data()
processed = dp.process_and_filter()
print(processed)