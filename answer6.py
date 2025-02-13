import csv

def read_csv(file):
    """Read a CSV file and return the data as a list of lists."""
    with open(file, 'r'):
        return [row for row in csv.reader(file)]

# def get_column_widths(data):
#     """Calculate the maximum width of each column."""
#     return [max(len(str(item)) for item in col) for col in zip(*data)]

# def print_table(data):
#     """Print a formatted table."""
#     col_widths = get_column_widths(data)
    
#     def print_row(row):
#         print(" | ".join(str(item).ljust(col_widths[i]) for i, item in enumerate(row)))
    
#     print("-" * (sum(col_widths) + len(col_widths) * 3))
#     print_row(data[0])
#     print("-" * (sum(col_widths) + len(col_widths) * 3))
#     for row in data[1:]:
#         print_row(row)
#     print("-" * (sum(col_widths) + len(col_widths) * 3))

if __name__ == "__main__":
    data = read_csv("dataq6.csv")
    # print_table(data)
print(data)