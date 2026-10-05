dist_KM = float(input())
fuel_100KM = float(input())
fuel_price = float(input())

fuel = (dist_KM / 100) * fuel_100KM
cost = fuel * fuel_price

print(f"Топливо: {fuel:.2f} л")
print(f"Стоимость: {cost:.2f}  руб")