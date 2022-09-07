class BulgarianCitizen:
    def __init__(self, names, birth_date, birth_place):
        self.__first_name = names[0]
        self.__second_name = names[1]
        self.__third_name = names[2]
        self.__other_names = names[3:]

        self.__birth_date = birth_date
        self.__birth_place = birth_place

    @property
    def first_name(self):
        return self.__first_name

    @property
    def second_name(self):
        return self.__second_name

    @property
    def third_name(self):
        return self.__third_name

    @property
    def other_names(self):
        return self.__other_names

    @property
    def birth_date(self):
        return self.__birth_date

    @property
    def birth_place(self):
        return self.__birth_place

    def __del__(self):
        del self.__first_name
        del self.__second_name
        del self.__third_name
        del self.__other_names

        del self.__birth_date
        del self.__birth_place
