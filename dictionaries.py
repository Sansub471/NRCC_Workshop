# syntax : dictionary.clear()
# removes all the elements from a dictionary

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car)
car.clear()
print(car)

# syntax  : dictionary.copy()
# returns a copy of the specified dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.copy()

print(x)
