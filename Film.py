class Film:

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
            "Duration: " + str(self.durationInMinutes) + "\n" + \
            "Quantity of reviews on IMDB: " + str(self.quantityOfReviewsIMDB) + "\n" + \
            "Genre: " + str(self.genre) + "\n" + \
            "Year: " + str(self.yearOfCreation) + "\n" + \
            "Budget: " + str(self.budget) + "\n"

    @staticmethod
    def main():

        film_1 = Film("Bad boys forver", "30", "1029", "Blockbuster", "2020", "21 000 0000")
        film_2 = Film("Bad boys forver 2", "12", "987", "Blockbuster")
        film_3 = Film()

        print(film_1.__str__())
        print(film_2.__str__())
        print(film_3.__str__())


if __name__ == '__main__':
    Film.main()
