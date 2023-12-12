def filter_names(input_file, names_file, output_file):
    import csv

    with open(names_file, 'r', encoding='utf-8') as file:
        filter_names = set(name.lower() for name in file.read().strip().split(';'))

    filtered_sorted_data = []
    with open(input_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        for name, count in reader:
            if name.lower() in filter_names:
                filtered_sorted_data.append((name, int(count)))

    filtered_sorted_data.sort(key=lambda x: x[1])

    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        for name, count in filtered_sorted_data:
            writer.writerow([name, count])

# input_file = 'sorted.csv'
# names_file = 'germanic.txt'
# output_file = 'filtered.csv'
input_file = 'filtered.csv'
names_file = 'christians.txt'
output_file = 'filtered2.csv'
filter_names(input_file, names_file, output_file)
