"""(3) Define a dictionary containing 10 fruits and their colours. Make sure that the colours
are repeated as values. Write a loop to iterate over the key-value pairs, and check which
all fruits are green in colour (this means that your dictionary should contain at least two
fruits with green as its value (for this example to work well)."""
D={"Mango": "orange", "Banana":"yellow","Apple":"red","Avocado":"green","Pomegranate":"red","Pineapple":"yellow","Kiwi":"green","Grapes":"green","Honeydew Melon":"green","Raspberry":"red"}

for key,value in D.items():
    if value=="green":
     print(f"The fruit green in colour is:{key}")
