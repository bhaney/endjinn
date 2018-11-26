import json


class Report(object):
    def __init__(self):
        self.report = {
            "title": "",
            "header": "",
            "run_time": "",
            "data": [{
                "name": "",
                "y_axis_label": "",
                "x_axis_label": "",
                "caption": "",
                "data_type": "",
                "values": []
            }]
        }

    def add_data_entry(self, data):
        assert "name" in data
        self.report["data"].append(data)

    def add_values_to_entry(self, name, values):
        assert isinstance(values, list)
        idx = [i for i, thing in enumerate(self.report["data"]) if thing["name"] == name][0]
        self.report["data"][idx]["values"].append(values)

    def to_json_file(self, filename="endjinn_report.json"):
        with open(filename, 'w') as f:
            json.dump(self.report, f)
