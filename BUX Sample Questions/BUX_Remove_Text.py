def remove_text(s: str, to_remove: str):
    return s.replace(to_remove, '')


text = '''NumPy Video Tutorial Edit
CONFIGURE 
DUPLICATE 
DELETE 
Drag to reorder
Panda's Video Tutorial Edit
CONFIGURE 
DUPLICATE 
DELETE 
Drag to reorder
Handling/Imputing Missing Values Edit
CONFIGURE 
DUPLICATE 
DELETE 
Drag to reorder
Feature Scaling/Normalization Edit
CONFIGURE 
DUPLICATE 
DELETE 
Drag to reorder
Encoding Categorical Features Edit
CONFIGURE 
DUPLICATE 
DELETE 
Drag to reorder
Basic Feature Engineering Edit
CONFIGURE 
DUPLICATE 
DELETE 
Drag to reorder
Feature Selection and ML Pipeline Edit
CONFIGURE 
DUPLICATE 
DELETE 
Drag to reorder
Colab Notebook for Intro to Data Processing Edit
CONFIGURE 
DUPLICATE 
DELETE 
Drag to reorder
Datasets used Edit
CONFIGURE 
DUPLICATE 
DELETE 
Drag to reorder
Lab 5 task Edit'''

remove_str = '''Edit
CONFIGURE 
DUPLICATE 
DELETE 
Drag to reorder'''

print(remove_text(text, remove_str))
