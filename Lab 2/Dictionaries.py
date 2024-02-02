#exercise 1
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964}
print(car.get("model"))
#exercise 2
car["year"] = 2020
print(car.get("year"))
#exercise 3
car["color"] = "red"
print(car.get("color"))
#exercise 4
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
#exercise 5
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()