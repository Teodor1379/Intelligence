from Bulgarian_Citizen_Builders import BulgarianCitizenAttributesBuilder


class BulgarianUniformCivilNumber:
    CITY_CODES = BulgarianCitizenAttributesBuilder.build_city_codes()

    def __init__(self, birth_date: str, birth_place: str) -> None:
        self.__birth_date_day = birth_date[0:2]
        self.__birth_date_month = birth_date[3:5]
        self.__birth_date_year = birth_date[6:10]

        self.__birth_place_lower_limit = BulgarianUniformCivilNumber.CITY_CODES[birth_place][0]
        self.__birth_place_upper_limit = BulgarianUniformCivilNumber.CITY_CODES[birth_place][1]

    @property
    def birth_date_day(self) -> str:
        return self.__birth_date_day

    @property
    def birth_date_month(self) -> str:
        return self.__birth_date_month

    @property
    def birth_date_year(self) -> str:
        return self.__birth_date_year

    @property
    def birth_place_lower_limit(self) -> str:
        return self.__birth_place_lower_limit

    @property
    def birth_place_upper_limit(self) -> str:
        return self.__birth_place_upper_limit

    def __del__(self) -> None:
        del self.__birth_date_day
        del self.__birth_date_month
        del self.__birth_date_year

        del self.__birth_place_lower_limit
        del self.__birth_place_upper_limit    
