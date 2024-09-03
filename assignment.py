import time
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.preprocessing import TransactionEncoder

# Step 1: Read the Dataset and Preprocess It
def read_dataset(file_path):
    with open(file_path, 'r') as file:
        transactions = [line.strip().split() for line in file]
    return transactions

# Step 2: Implement the Apriori Algorithm to Find Frequent Itemsets
def find_frequent_itemsets(transactions, min_support=0.5):
    te = TransactionEncoder()
    te_ary = te.fit(transactions).transform(transactions)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    
    frequent_itemsets = apriori(df, min_support=min_support, use_colnames=True)
    return frequent_itemsets

# Step 3: Create a Mapping of Itemsets to Identifiers
def create_mapping(frequent_itemsets):
    mapping = {}
    id_counter = 1
    
    sorted_itemsets = frequent_itemsets.sort_values(by=['support', 'itemsets'], ascending=[False, False])
    
    for _, row in sorted_itemsets.iterrows():
        itemset = tuple(sorted(row['itemsets']))
        if itemset not in mapping:
            mapping[itemset] = f'X{id_counter}'
            id_counter += 1
    
    return mapping

# Step 4: Compress the Dataset Using the Mapping
def compress_dataset(transactions, mapping):
    compressed_transactions = []
    
    for transaction in transactions:
        compressed_transaction = []
        for itemset, identifier in mapping.items():
            if all(item in transaction for item in itemset):
                compressed_transaction.append(identifier)
                transaction = [item for item in transaction if item not in itemset]
        compressed_transaction.extend(transaction)
        compressed_transactions.append(compressed_transaction)
    
    return compressed_transactions

# Step 5: Implement Decompression Logic
def decompress_dataset(compressed_transactions, mapping):
    reverse_mapping = {v: k for k, v in mapping.items()}
    decompressed_transactions = []
    
    for compressed_transaction in compressed_transactions:
        decompressed_transaction = []
        for identifier in compressed_transaction:
            if identifier in reverse_mapping:
                decompressed_transaction.extend(reverse_mapping[identifier])
            else:
                decompressed_transaction.append(identifier)
        decompressed_transactions.append(decompressed_transaction)
    
    return decompressed_transactions

# Step 6: Evaluate the Compression Ratio
def calculate_compression_ratio(original_transactions, compressed_transactions, mapping):
    original_size = sum(len(transaction) for transaction in original_transactions)
    compressed_size = sum(len(transaction) for transaction in compressed_transactions) + len(mapping)
    compression_ratio = (original_size - compressed_size) / original_size
    return compression_ratio

# Main Function to Run the Full Program
def main(file_path, min_support=0.5):
    st = time.time()
    # Step 1: Read the Dataset
    transactions = read_dataset(file_path)
    # print(transactions)
    
    # Step 2: Find Frequent Itemsets
    frequent_itemsets = find_frequent_itemsets(transactions, min_support=min_support)
    filtered_frequent_itemsets = frequent_itemsets[frequent_itemsets['itemsets'].apply(lambda x: len(x) > 2)]
    mapping =create_mapping(filtered_frequent_itemsets)
    
    # Step 3: Create the Mapping
    # mapping = create_mapping(frequent_itemsets)
    print(mapping)
    
    # Step 4: Compress the Dataset
    compressed_transactions = compress_dataset(transactions, mapping)
    print(compressed_transactions)
    
    # Step 5: Decompress the Dataset (for verification)
    decompressed_transactions = decompress_dataset(compressed_transactions, mapping)
    
    # Step 6: Calculate and Print the Compression Ratio
    compression_ratio = calculate_compression_ratio(transactions, compressed_transactions, mapping)
    print(f"Compression Ratio: {compression_ratio * 100:.2f}%")
    
    # Verify if decompression is lossless
   
    sorted_transaction = [sorted(list) for list in transactions]
    sorted_decompressed_transaction = [sorted(list) for list in decompressed_transactions]
    if sorted_transaction == sorted_decompressed_transaction:
        print("Decompression is lossless!")
    else:
        print("Decompression is not lossless!")
    end = time.time()
    print("time = ", end - st)

# Example usage (replace 'transactions.txt' with your dataset file path)
if __name__== "__main__":
    file_path = 'small.dat'
    main(file_path, min_support=0.5)
