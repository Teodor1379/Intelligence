class BulgarianCitizen:
    def __init__(self, citizen_names, birth_date, birth_place):
        self.__citizen_first_name = citizen_names[0]
        self.__citizen_second_name = citizen_names[1]
        self.__citizen_third_name = citizen_names[2]
        self.__citizen_other_names = citizen_names[3:]

        self.__citizen_birth_date = birth_date
        self.__citizen_birth_place = birth_place

        self.__citizen_father = None
        self.__citizen_mother = None
        self.__citizen_brothers = list()
        self.__citizen_sisters = list()

    @property
    def citizen_first_name(self):
        return self.__citizen_first_name

    @property
    def citizen_second_name(self):
        return self.__citizen_second_name

    @property
    def citizen_third_name(self):
        return self.__citizen_third_name

    @property
    def citizen_other_names(self):
        return self.__citizen_other_names

    @property
    def citizen_birth_date(self):
        return self.__citizen_birth_date

    @property
    def citizen_birth_place(self):
        return self.__citizen_birth_place

    @property
    def citizen_father(self):
        return self.__citizen_father

    @property
    def citizen_mother(self):
        return self.__citizen_mother

    @property
    def citizen_brothers(self):
        return self.__citizen_brothers

    @property
    def citizen_sisters(self):
        return self.__citizen_sisters

    def __del__(self):
        del self.__citizen_first_name
        del self.__citizen_second_name
        del self.__citizen_third_name
        del self.__citizen_other_names

        del self.__citizen_birth_date
        del self.__citizen_birth_place

        del self.__citizen_father
        del self.__citizen_mother
        del self.__citizen_brothers
        del self.__citizen_sisters
