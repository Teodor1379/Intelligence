class BulgarianCitizen:
    def __init__(self, names):
        self.__first_name = names[0]
        self.__second_name = names[1]
        self.__third_name = names[2]
        self.__other_names = names[3:]

    def __del__(self):
        del self.__first_name
        del self.__second_name
        del self.__third_name
        del self.__other_names
