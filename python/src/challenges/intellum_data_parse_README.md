# Coding Challenge: Parse Data Files

**Difficulty:** Medium  
**Estimated Time:** 45–60 minutes  

## Problem Description

You are given a set of data files containing information about products in a store. Each file may contain data in different formats: CSV, JSON, or a custom plain text format. Your task is to write a program that reads these files, extracts the product information, and outputs a consolidated JSON list of all products.

## File Formats

1. CSV (.csv)  
   Each row represents a product with the following fields:  
   id,name,price,quantity  
   101,Apple,0.5,50  
   102,Banana,0.3,100  

2. JSON (.json)  
   Each file contains an array of products:  
   [  
       {"id": 201, "name": "Orange", "price": 0.6, "quantity": 30},  
       {"id": 202, "name": "Grapes", "price": 2.5, "quantity": 20}  
   ]  

3. Custom Text Format (.txt)  
   Each line contains a product separated by semicolons:  
   301;Mango;1.2;15  
   302;Pineapple;3.0;10  

## Requirements

1. Create a function parse_file(file_path) that:  
   - Detects the file format based on the file extension.  
   - Reads the file and extracts product information.  
   - Returns a list of product objects in this format:  
     {"id": 101, "name": "Apple", "price": 0.5, "quantity": 50}  

2. Create a function parse_all_files(file_paths) that:  
   - Accepts a list of file paths.  
   - Calls parse_file for each file.  
   - Returns a single consolidated list of all products from all files.  

3. Optional Bonus:  
   - Handle invalid/malformed lines gracefully by skipping them.  
   - Sort the final list of products by id.  

## Example Usage

files = ["products1.csv", "products2.json", "products3.txt"]  
all_products = parse_all_files(files)  
print(all_products)  

Expected Output (JSON-like):  

[  
    {"id": 101, "name": "Apple", "price": 0.5, "quantity": 50},  
    {"id": 102, "name": "Banana", "price": 0.3, "quantity": 100},  
    {"id": 201, "name": "Orange", "price": 0.6, "quantity": 30},  
    {"id": 202, "name": "Grapes", "price": 2.5, "quantity": 20},  
    {"id": 301, "name": "Mango", "price": 1.2, "quantity": 15},  
    {"id": 302, "name": "Pineapple", "price": 3.0, "quantity": 10}  
]  

## Evaluation Criteria

- Correct parsing of all three file types.  
- Correctly returns a consolidated list of products.  
- Handles edge cases and malformed data.  
- Code readability and modularity.
