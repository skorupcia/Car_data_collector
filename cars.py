import pandas as pd
import tkinter as tk
from tkinter import messagebox

#---------------Main---------------
window = tk.Tk()
window.title("CarStore data collector")
window.geometry("400x470")

fprint = pd.read_excel("cars.xlsx", sheet_name="Sheet1")
print(fprint)

car_data = []
currency = 0.0

#---------------Functions---------------
def read():
    data = []
    currency = float(input("Enter EUR/PLN: "))

    headers = ["Car", "Year", "Fuel", "Transmission", "Mileage", "Price in EURO(inc transport)", "Price in PLN", "Potential Earn"]
    data.append(headers)

    while True:
        car = input("Car: ")
        if not car:
            break
        
        year = int(input("Year: "))
        fuel = input("Fuel: ")
        transmission = input("Transmission: ")
        mileage = int(input("Enter Mileage: "))
        price = float(input("Enter the price of the car: "))
        price+=300
        
        data.append([car, year, fuel, transmission, mileage, price, price * currency, price*0.03,])

    df = pd.DataFrame(data[1:], columns=data[0])
    df.to_excel("cars.xlsx", index=False)

def add_car():
    car = car_entry.get()
    if car:
        year = int(year_entry.get())
        fuel = fuel_entry.get()
        transmission = transmission_entry.get()
        mileage = int(mileage_entry.get())
        price = float(price_entry.get())
        currency = float(currency_entry.get())
        price_pln = price * currency
        car_data.append([car, year, fuel, transmission, mileage, price, price_pln])

        # Clear the entry fields for the next car
        car_entry.delete(0, tk.END)
        year_entry.delete(0, tk.END)
        fuel_entry.delete(0, tk.END)
        transmission_entry.delete(0, tk.END)
        mileage_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)

def save_data():
    if len(car_data) == 0:
        messagebox.showwarning("No Data", "No cars have been added.")
        return

    headers = ["Car", "Year", "Fuel type", "Transmission", "Mileage", "Price in EURO", "Price in PLN"]
    df = pd.DataFrame(car_data, columns=headers)
    df.to_excel("cars.xlsx", index=False)

    # Show a message box when the data is saved
    messagebox.showinfo("Car Data Saved", "Car data saved to cars.xlsx")
    window.destroy()

def display_cars():
    if len(car_data) == 0:
        tk.messagebox.showwarning("No Cars", "No cars have been added yet.")
        return

    # display window
    display_window = tk.Toplevel(window)
    display_window.title("Car Data")
    display_window.geometry("400x300")

    # widget
    car_text = tk.Text(display_window)
    car_text.pack()

    for car in car_data:
        car_text.insert(tk.END, f"Car: {car[0]}\n")
        car_text.insert(tk.END, f"Year: {car[1]}\n")
        car_text.insert(tk.END, f"Fuel type: {car[2]}\n")
        car_text.insert(tk.END, f"Transmission: {car[3]}\n")
        car_text.insert(tk.END, f"Mileage: {car[4]}\n")
        car_text.insert(tk.END, f"Price in EURO: {car[5]}\n")
        car_text.insert(tk.END, f"Price in PLN: {car[6]}\n")
        car_text.insert(tk.END, "-" * 20 + "\n")

    car_text.config(state=tk.DISABLED)


#---------------Options---------------
car_label = tk.Label(window, text="Car:")
car_label.pack()
car_entry = tk.Entry(window)
car_entry.pack()

year_label = tk.Label(window, text="Year:")
year_label.pack()
year_entry = tk.Entry(window)
year_entry.pack()

fuel_label = tk.Label(window, text="Fuel type:")
fuel_label.pack()
fuel_entry = tk.Entry(window)
fuel_entry.pack()

transmission_label = tk.Label(window, text="Transmission:")
transmission_label.pack()
transmission_entry = tk.Entry(window)
transmission_entry.pack()

mileage_label = tk.Label(window, text="Mileage:")
mileage_label.pack()
mileage_entry = tk.Entry(window)
mileage_entry.pack()

price_label = tk.Label(window, text="Price:")
price_label.pack()
price_entry = tk.Entry(window)
price_entry.pack()

currency_label = tk.Label(window, text="Currency (EUR/PLN):")
currency_label.pack()
currency_entry = tk.Entry(window)
currency_entry.pack()



#---------------Buttons---------------
# Display button
display_button = tk.Button(window, text="Display Cars", command=display_cars)
display_button.pack()

# add button
add_button = tk.Button(window, text="Add Car", command=add_car)
add_button.pack()

# save button
save_button = tk.Button(window, text="Save", command=lambda: [save_data(), window.destroy()])
save_button.pack()

#---------------loop---------------
window.mainloop()