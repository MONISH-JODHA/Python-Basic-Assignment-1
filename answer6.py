def visualize_csv(file_path):
    with open(file_path, 'r') as f:
        lines = [line.strip().split(',') for line in f.readlines()]
    
    max_cols = max(len(row) for row in lines)
    for row in lines:
        while len(row) < max_cols:
            row.append('')  
    
    col_widths = [max(len(row[i]) for row in lines) for i in range(max_cols)]
    border = '+' + '+'.join('-' * (w + 2) for w in col_widths) + '+'
    
    print(border)
    for row in lines:
        print('| ' + ' | '.join(f"{row[i]:<{col_widths[i]}}" for i in range(max_cols)) + ' |')
        print(border)


if __name__ == "__main__":
    data = visualize_csv("/home/monish/assignments/scripts/python_basic/dataq6.csv")
print(data)