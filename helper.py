import csv
import os

input_csv = os.path.join(os.path.dirname(__file__), 'snowboard.csv')
output_csv = os.path.join(os.path.dirname(__file__), 'snowboard_size_chart.csv')

with open(input_csv, "r", newline="", encoding="utf-8") as fin, \
     open(output_csv, "w", newline="", encoding="utf-8") as fout:
    
    reader = csv.reader(fin)
    writer = csv.writer(fout)
    
    header = next(reader)
    lbs_labels = header[1:]
    
    writer.writerow(["height_in_cm", "weight_in_lbs", "length"])
    
    for row in reader:
        height_cm = row[0]
        for col_index, lbs_value in enumerate(lbs_labels, start=1):
            table_value = row[col_index]
            writer.writerow([height_cm, lbs_value, table_value])
