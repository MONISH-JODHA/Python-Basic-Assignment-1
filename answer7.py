import csv

def ec2_recommendation(instance_type, cpu_util):
    sizes = ['nano', 'micro', 'small', 'medium', 'large', 'xlarge', '2xlarge', '4xlarge', '8xlarge', '16xlarge', '32xlarge']
    parts = instance_type.split('.')
    instance_family, instance_size = parts[0], parts[1]
    
    if instance_size in sizes:
        idx = sizes.index(instance_size)
        
        if cpu_util < 20 and idx > 0:
            recommended = f"{instance_family}.{sizes[idx - 1]}"
            status = "Underutilized"
        elif cpu_util > 80 and idx < len(sizes) - 1:
            recommended = f"{instance_family}.{sizes[idx + 1]}"
            status = "Overutilized"
        else:
            recommended = instance_type  
            status = "Optimized"
        
        return [["1", instance_type, f"{cpu_util}%", status, recommended]]

def save_to_csv(data, filename='ec2_recommendation.csv'):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Serial No.", "Current EC2", "Current CPU", "Status", "Recommended EC2"])
        writer.writerows(data)

def visualize_csv_table(csv_file):
    with open(csv_file, 'r') as f:
        rows = [line.strip().split(',') for line in f.readlines()]
    col_widths = [max(len(row[i]) for row in rows) for i in range(len(rows[0]))]
    border = '+' + '+'.join('-' * (w + 2) for w in col_widths) + '+'
    print(border)
    for row in rows:
        print('| ' + ' | '.join(f"{row[i]:<{col_widths[i]}}" for i in range(len(row))) + ' |')
        print(border)
        
        
#ye variable input leke try karenge
instance = "t2.large"
cpu_utilization = 20
recommendation = ec2_recommendation(instance, cpu_utilization)
save_to_csv(recommendation)
visualize_csv_table('ec2_recommendation.csv')