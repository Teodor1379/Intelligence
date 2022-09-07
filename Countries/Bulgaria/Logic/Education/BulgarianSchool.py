class BulgarianSchool:
    def __init__(self, school_name, school_logo):
        self.__school_name = school_name
        self.__school_logo = school_logo

    @property
    def school_name(self):
        return self.__school_name

    @property
    def school_logo(self):
        return self.__school_logo

    def __del__(self):
        del self.__school_name
        del self.__school_logo
