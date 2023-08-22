import json
# content of the text file
system_output = """
0 0.634286 0.175238 0.0914286 0.190476
0 0.632857 0.393333 0.0942857 0.180952
0 0.632857 0.282857 0.0942857 0.401905
0 0.142857 0.439048 0.0942857 0.127619
0 0.106429 0.797143 0.192857 0.379048
0 0.0435714 0.440952 0.0871429 0.127619
0 0.0364286 0.165714 0.0728571 0.140952
0 0.0371429 0.305714 0.0742857 0.131429
0 0.777143 0.301905 0.185714 0.36381
0 0.904286 0.78 0.191429 0.371429
0 0.131429 0.301905 0.0971429 0.135238
0 0.937857 0.295238 0.124286 0.361905
0 0.306429 0.791429 0.201429 0.379048
0 0.23 0.195238 0.1 0.211429
0 0.242143 0.400952 0.09 0.19619
0 0.705 0.779048 0.201429 0.407619
0 0.437143 0.395238 0.0914286 0.188571
0 0.339286 0.399048 0.0928571 0.192381
0 0.505 0.795238 0.192857 0.371429
0 0.535 0.393333 0.0928571 0.188571
0 0.534286 0.186667 0.0971429 0.209524
0 0.331429 0.193333 0.0971429 0.211429
0 0.432857 0.190476 0.0971429 0.213333
"""

#Parse the system output text and process it
objects_data = []
lines = system_output.strip().split('\n')  # Split by newlines
for line in lines:
    fields = line.split()  # Split each line by spaces
    image_rotation = int(fields[0])
    x, y, width, height = map(float, fields[1:5])
    rectanglelabels= "object"

    object_data = {
        "image_rotation": image_rotation,
        "value": {
            "x": x,
            "y": y,
            "width": width,
            "height": height,
            "rotation": image_rotation,
            "rectanglelabels":rectanglelabels
        }
    }
    objects_data.append(object_data)


# Convert the processed data to a JSON file
json_file_path = "output.json"
with open(json_file_path, 'w') as json_file:
    json.dump(objects_data, json_file, indent=4)

print("JSON file generated successfully.")
