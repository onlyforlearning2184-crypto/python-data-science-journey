products = {"phones": {"Samsung", "Apple", "Vivo"}, "laptops": {"Dell", "HP", "Apple"}}
print(products["phones"].union(products["laptops"]))
print(products["phones"].intersection(products["laptops"]))
