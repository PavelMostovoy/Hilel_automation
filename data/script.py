import json
import yaml
# data = {"tests": {"suite_1": [],
#                   "suite_2": [],
#                   "suite_3": []}}
#
#
# for i in range(10):
#     data["tests"]["suite_1"].append(("value", i))
#
#
# with open("data.json", "w") as f:
#     json.dump(data, f)
#     # f.write(str(data))

with open("data.yaml", "r") as f:
    data = yaml.safe_load(f)


# with open("data.yaml", "w") as f:
#     yaml.dump(data, f)

print(data["tests"]["suite_2"][0])