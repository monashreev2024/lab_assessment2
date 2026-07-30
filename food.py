from collections import Counter

orders = [
    {"customer_name": "Alice", "food_item": "Burger", "quantity": 2, "unit_price": 8.50},
    {"customer_name": "Bob", "food_item": "Pizza", "quantity": 1, "unit_price": 12.00},
    {"customer_name": "Charlie", "food_item": "Burger", "quantity": 1, "unit_price": 8.50},
    {"customer_name": "David", "food_item": "Pasta", "quantity": 3, "unit_price": 10.00},
    {"customer_name": "Eva", "food_item": "Salad", "quantity": 2, "unit_price": 7.00}
]

for order in orders:
    order["total_bill"] = order["quantity"] * order["unit_price"]

highest_value_order = max(orders, key=lambda x: x["total_bill"])
item_counts = Counter()
for order in orders:
    item_counts[order["food_item"]] += order["quantity"]
most_frequent_item, max_qty = item_counts.most_common(1)[0]

total_daily_revenue = sum(order["total_bill"] for order in orders)

sorted_orders = sorted(orders, key=lambda x: x["total_bill"], reverse=True)

print("--- Customer Bills & Order Details ---")
for order in sorted_orders:
    print(f"Customer: {order['customer_name']:<8} | Item: {order['food_item']:<7} | "
          f"Qty: {order['quantity']} | Total Bill: ${order['total_bill']:.2f}")

print("\n--- Analytics Summary ---")
print(f"Highest-Value Order        : {highest_value_order['customer_name']} "
      f"(${highest_value_order['total_bill']:.2f} for {highest_value_order['food_item']})")
print(f"Most Frequent Food Item   : {most_frequent_item} (Total Quantity: {max_qty})")
print(f"Total Daily Revenue       : ${total_daily_revenue:.2f}")
