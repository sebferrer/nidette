def sort_by_count(input_file, output_file):
    import csv

    with open(input_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        data = list(reader)

    sorted_data = sorted(data, key=lambda x: int(x[1]))

    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        for row in sorted_data:
            writer.writerow(row)

input_file = 'cleaned.csv'
output_file = 'sorted.csv'
sort_by_count(input_file, output_file)
