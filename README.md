# Frequent-Itemset-Mining

# Overview
This project provides an algorithm to compress a transactional dataset using frequent itemset mining. By creating mappings for frequent itemsets, we aim to reduce the size of the dataset while retaining the ability to reconstruct the original dataset exactly (lossless compression).

# Approach
Frequent Itemset Mining: <br> Utilizes algorithms like Apriori to identify itemsets that frequently occur together in transactions. <br>
<br>
Mapping Creation: <br> Maps frequent itemsets to unique identifiers to minimize storage. <br>
<br>
Compression: <br> Replaces frequent itemsets in the dataset with their mapped identifiers to create a compressed version. <br>
<br>
Decompression: <br> Uses the mapping to reconstruct the original dataset from the compressed version. <br>

# Case Scenario 1
# Dataset: small.dat <br>
![WhatsApp Image 2024-09-03 at 22 54 55_fbf2449b](https://github.com/user-attachments/assets/a47e5a0e-78f2-437a-b360-5e283818f636)

# Frequent Itemset <br>
![WhatsApp Image 2024-09-03 at 22 56 03_72a27dd7](https://github.com/user-attachments/assets/ed56170a-fb24-4367-8454-45da32823786)

# Mapping <br>
![WhatsApp Image 2024-09-03 at 22 56 54_5cd0e9a5](https://github.com/user-attachments/assets/76c395f4-f17d-461c-8d37-41e04ef3fc1a)

# Compressed Dataset <br>
![WhatsApp Image 2024-09-03 at 22 57 17_5c31fc93](https://github.com/user-attachments/assets/bb2e3e6b-dfdc-4d36-91f0-cff29cc85bbb)

# Compression ratio & Time taken <br>
![WhatsApp Image 2024-09-03 at 22 57 47_9da7f371](https://github.com/user-attachments/assets/84688712-9d38-4358-9a86-26f67df50541)

<br>

# Case Scenario 2
# Dataset: D_small.dat <br>
![WhatsApp Image 2024-09-03 at 23 25 34_3f115b5a](https://github.com/user-attachments/assets/db4cc931-8b20-461d-ba25-e935a8300c5c)

# Frequent Itemset <br>
![WhatsApp Image 2024-09-03 at 23 25 53_8bda3925](https://github.com/user-attachments/assets/3922e388-4d4c-4b22-897f-83c2b4ed9280)

# Mapping <br>
![WhatsApp Image 2024-09-03 at 23 26 31_fbd1a919](https://github.com/user-attachments/assets/0829b3ee-d44c-4376-b330-5f0cbb230188)

# Compressed Dataset <br>
![WhatsApp Image 2024-09-03 at 23 26 54_81dd23c7](https://github.com/user-attachments/assets/a46f404a-7627-443e-92e3-677109fb4bb3)

# Compression ratio & Time taken <br>
![WhatsApp Image 2024-09-03 at 23 27 16_191b8ffd](https://github.com/user-attachments/assets/ae21febc-e5d4-4d91-a091-021bb72afacb)
