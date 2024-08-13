from customer import Customer
from item import Item
from seller import Seller

seller = Seller("Tienda DIC")
for i in range(10):
    Item("CPU", 40830, seller)
    Item("Memoria", 13880, seller)
    Item("Placa Madre", 28980, seller)
    Item("Fuente de Alimentación", 8980, seller)
    Item("Caja de la PC", 8727, seller)
    Item("HDD de 3.5 pulgadas", 10980, seller)
    Item("SSD de 2.5 pulgadas", 13370, seller)
    Item("M.2 SSD", 12980, seller)
    Item("Enfriador de CPU", 13400, seller)
    Item("Tarjeta Gráfica", 23800, seller)

print("🤖 Favor dime tu nombre")
customer = Customer(input())

print("🏧 Ingresa el monto a cargar a tu billetera")
customer.wallet.deposit(int(input()))

print("🛍️ Empezar a Comprar")
end_shopping = False
while not end_shopping:
    print("📜 Lista de Productos")
    seller.show_items()

    print("️️⛏ Ingrese el número de producto")
    number = int(input())

    print("⛏ Ingrese la cantidad del producto")
    quantity = int(input())

    items = seller.pick_items(number, quantity)
    for item in items:
        customer.cart.add(item)
    print("🛒 Contenido del Carrito")
    customer.cart.show_items()
    print(f"🤑 Cantidad total: {customer.cart.total_amount()}")

    print("😭 ¿Quieres finalizar la compra？(yes/no)")
    end_shopping = input() == "yes"

print("💸 QUieres confirmar tu compra？(yes/no)")
if input() == "yes":
    customer.cart.check_out()

print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈Resultado┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
print(f"️🛍️ ️Propiedad de {customer.name}")
customer.show_items()
print(f"😱👛 Saldo en la billetera de {customer.name}: {customer.wallet.balance}")

print(f"📦 {seller.name} Estado del stock")
seller.show_items()
print(f"😻👛 Saldo en la billetera de {seller.name}: {seller.wallet.balance}")

print("🛒 Contenido del carrito")
customer.cart.show_items()
print(f"🌚 Cantidad total: {customer.cart.total_amount()}")

print("🎉 Fin")
