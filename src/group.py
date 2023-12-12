def aggregate_names(input_file, output_file):
    import csv
    
    from collections import defaultdict

    counts_by_name = defaultdict(int)

    with open(input_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        for _, name, _, count in reader:
            counts_by_name[name] += int(count)

    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        for name, count in counts_by_name.items():
            writer.writerow([name, count])


input_file = 'nat2022.csv'
output_file = 'cleaned.csv'
aggregate_names(input_file, output_file)
