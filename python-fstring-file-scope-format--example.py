Products={
"laptop":1.500000,
"mouse":2.254000,
"keybord":3.546000,
"monitor":5.554949
}

def list_products():
    name=input("enter customer name :")
    productse=input("Enter productse name (laptop/mouse/keyboard").lower()
    quantiy=int(input("enter quantiy"))
    return name,productse,quantiy

def calculate_total(productse,quantiy):
    unit_price=Products.get(productse,0)
    total=unit_price * quantiy
    return total

def save_order(name,productse,quantity,total):
    with open("order.txt","a") as file:
        file.write("{} ordered {} x {} = {}\n".format(name, quantity, productse, total))
        def print_order_summary(name, productse, quantity, total):
            print(f"Order Summary for {name}")
    print(f"{quantity} x {productse} = {total} Toman")

    def main():
        name, product, quantity = get_order()
        total = calculate_total(productse, quantity)
        print_order_summary(name, productse, quantity, total)
        save_order(name, productse, quantity, total)

    main()