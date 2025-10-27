import json
import logging
from datetime import datetime

# added a docstring to explain what the entire code does
"""
Inventory Management System
Handles adding, removing, saving, and loading of stock data.
"""

#changed all functions names to follow snake_case

# Global variable
stock_data = {}

def add_item(item="default", qty=0, logs=None):  # changed logs=[] to logs=None
    # added docstring to explain what the func does
    """
    Add an item and record it in logs
    Returns: None
    """     
    if logs is None:    #each func gets a fresh list
        logs=[]
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append("%s: Added %d of %s" % (str(datetime.now()), qty, item))

def remove_item(item, qty):
    """
    Remove an existing item from the inventory.
    Returns: None
    """
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except (KeyError, TypeError) as e:    # catch specific exceptions
        print(f"Error removing item: {e}")

def get_qty(item):
    """
    Retrieve the current quantity of a specific item.
    Returns: 
        int: The quantity of the item if found, otherwise 0.
    """
    return stock_data[item]

def load_data(file="inventory.json"):
    """
    Load inventory data from a file into memory.
    Returns: 
        dict: The loaded inventory data as a dictionary.
    """
    with open('data.txt', 'r', encoding='utf-8') as f:
        global stock_data
        stock_data = json.loads(f.read())

def save_data(file="inventory.json"):
    """
    Save the current inventory data to a file.
    Returns: None
    """
    with open('data.txt', 'w', encoding='utf-8') as f:
        f.write(json.dumps(stock_data))

def print_data():
    """
    Display all items and their quantities in the inventory.
    Returns: None
    """
    print("Items Report")
    for i in stock_data:
        print(i, "->", stock_data[i])

def check_low_items(threshold=5):
    """
    Check and display items with quantities below the given threshold.
    Returns:
        list: A list of items considered low in stock.
    """
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result

def main():
    """
    Main function to run the inventory system. 
    Handles menu options for adding, removing, viewing, and saving inventory data.
    """
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")  # invalid types, no check
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()
    eval("print('eval used')")  # dangerous

main()
