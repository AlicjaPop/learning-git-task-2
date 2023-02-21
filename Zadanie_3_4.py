shops_dict = {
    "piekarnia" : ["chleb", "bułki", "pączek"],
    "warzywniak" : ["marchew", "seler", "rukola"]
}

print("Lista Zakupów")

product_list=[]
for shop, product in shops_dict.items():
    Shop=shop.capitalize()
    Cap_product_list=[]
    for Product in product:
        Cap_product_list.append(Product.capitalize())
    print(f"Idę do {Shop}, kupuję tu następujące rzeczy:", Cap_product_list)
    product_list=product_list + product
print(f"W sumie kupuję", len(product_list), "produktów.")