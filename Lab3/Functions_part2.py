mov_dict = [ { "name": "Usual Suspects", "imdb": 7.0, "category": "Thriller" },
             { "name": "Hitman", "imdb": 6.3, "category": "Action" },
             { "name": "Dark Knight", "imdb": 9.0, "category": "Adventure" },
             { "name": "The Help", "imdb": 8.0, "category": "Drama" },
             { "name": "The Choice", "imdb": 6.2, "category": "Romance" },
             { "name": "Colonia", "imdb": 7.4, "category": "Romance" },
             { "name": "Love", "imdb": 6.0, "category": "Romance" },
             { "name": "Bride Wars", "imdb": 5.4, "category": "Romance" },
             { "name": "AlphaJet", "imdb": 3.2, "category": "War" },
             { "name": "Ringing Crime", "imdb": 4.0, "category": "Crime" },
             { "name": "Joking muck", "imdb": 7.2, "category": "Comedy" },
             { "name": "What is the name", "imdb": 9.2, "category": "Suspense" },
             { "name": "Detective", "imdb": 7.0, "category": "Suspense" },
             { "name": "Exam", "imdb": 4.2, "category": "Thriller" },
             { "name": "We Two", "imdb": 7.2, "category": "Romance" } ]
#exercise 1
def check_imdb_rating(movie):
        return movie["imdb"] > 5.5


result = check_imdb_rating(mov_dict[0])
print(result)

#exercise 2
def check_imdb_rating(movie_list):
        for i in movie_list:
            if i["imdb"] > 5.5:
                 print(i["name"])
        return "Operation Complete"


result = check_imdb_rating(mov_dict)
print(result)



#exercise 3
def find_category(movie_list, category_name):
    for i in movie_list:
        if i["category"] == category_name:
            print(i["name"])
    return "Operation Complete"


cat_name = input("Add your category:")
result = find_category(mov_dict, cat_name)
print(result)


#exercise 4
def find_average_rating(movie_list):
    sum_rating = 0.0
    counter = 0
    for i in movie_list:
        sum_rating += i["imdb"]
        counter += 1
    res = sum_rating / counter
    return res

result = find_average_rating(mov_dict)
print(result)


#exercise 5
def avg_rating(movie_list, category_name):
    sum_rating = 0.0
    counter = 0
    for i in movie_list:
        if i["category"] == category_name:
            sum_rating += i["imdb"]
            counter += 1
    res = sum_rating / counter
    return res

cat_name = input("Add your category:")
result = avg_rating(mov_dict, cat_name)
print(result)





