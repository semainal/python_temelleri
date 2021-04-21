class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
    print("Movie Objesi oluşturuldu.")

    def __str__(self):
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration

    def __del__(self):
        print("Film objesi silindi")

m = Movie("Film adı", "Yönetmeni", 120)

print(str(m))
print(len(m))

# del m 

# print(m)
