import json
import csv

def process_orders(json_file, csv_file):
    with open(json_file, 'r') as f:
        content = f.read().replace("'", '"')  
        data = json.loads(content)
    
    orders_list = []
    for order in data['orders']:
        total_value = sum(item['price'] * item['quantity'] for item in order['items'])
        discount = total_value * 0.1 if total_value > 100 else 0
        shipping_cost = sum(item['quantity'] for item in order['items']) * 5
        final_total = total_value - discount + shipping_cost
        
        for item in order['items']:
            orders_list.append([
                order['order_id'], 
                order['customer']['name'], 
                item['name'], 
                item['price'], 
                item['quantity'], 
                total_value, 
                discount, 
                shipping_cost, 
                final_total, 
                order['shipping_address'], 
                "US"
            ])
    
    orders_list.sort(key=lambda x: x[8], reverse=True)
    
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Order ID", "Customer Name", "Product Name", "Product Price", "Quantity", "Total Value", "Discount", "Shipping Cost", "Final Total", "Shipping Address", "Country Code"])
        writer.writerows(orders_list)
    
    print(f"Data has been processed and saved to {csv_file}")

process_orders('salesq8.json', 'sales_report.csv')
