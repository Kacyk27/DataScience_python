import pandas as pd


products_dict = {
    'product_id': ['001', '004', '007', '010'],
    'name': ['mobile phone', 'laptop', 'mouse', 'tablet'],
    'price': [1490.0, 3400.0, 59.99, 999.00]
}

orders_day_1_dict = {
    'order_id': ['1001', '1002', '1003', '1004'],
    'product_id': ['004', '001', '001', '007'],
    'quantity': [2, 1, 1, 3]
}       

orders_day_2_dict = {
    'order_id': ['1005', '1006', '1007'],
    'product_id': ['010', '001', '007'],
    'quantity': [2, 1, 1]
}                

products = pd.DataFrame(products_dict)
orders_day_1 = pd.DataFrame(orders_day_1_dict)
orders_day_2 = pd.DataFrame(orders_day_2_dict)

orders = pd.concat([orders_day_1, orders_day_2], axis=0).reset_index()
del orders['index']
print(orders)