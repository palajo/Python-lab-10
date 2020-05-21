class Film:
    # static field
    lpnu = "let me live"

    def __init__(self, title=None, durationInMinutes=None, quantityOfReviewsIMDB=None, genre=None,
                 yearOfCreation=None, budget=None):
        self.title = title
        self.durationInMinutes = durationInMinutes
        self.quantityOfReviewsIMDB = quantityOfReviewsIMDB
        self.genre = genre
        self.yearOfCreation = yearOfCreation
        self.budget = budget

    def __del__(self):
        return

    def __str__(self):
        return \
            "Title: " + str(self.title) + "\n" + \
            "Duration (min.): " + str(self.durationInMinutes) + "\n" + \
            "Quantity of reviews on IMDB: " + str(self.quantityOfReviewsIMDB) + "\n" + \
            "Genre: " + str(self.genre) + "\n" + \
            "Year: " + str(self.yearOfCreation) + "\n" + \
            "Budget: " + str(self.budget) + "\n"

    @staticmethod
    def printStaticVariable():
        return Film.lpnu

    @staticmethod
    def main():
        film_1 = Film("Bad boys for life", "124", "1029", "Comedy/Thriller", "2020", "90 000 0000")
        film_2 = Film("Fast&Furious 8", "149", "2901", "Thriller")
        film_3 = Film()

        print(film_1.__str__())
        print(film_2.__str__())
        print(film_3.__str__())

        print(Film.printStaticVariable())


if __name__ == '__main__':
    Film.main()
