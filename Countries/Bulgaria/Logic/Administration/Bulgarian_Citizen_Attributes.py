import re


class BulgarianUniformCivilNumber:
    def __init__(self, birth_date: str, birth_place: str) -> None:
        self.__birth_date_day = birth_date[0:2]
        self.__birth_date_month = birth_date[3:5]
        self.__birth_date_year = birth_date[6:10]

        self.__birth_place_lower_limit = self.build_city_codes()[birth_place][0]
        self.__birth_place_upper_limit = self.build_city_codes()[birth_place][1]

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

    @staticmethod
    def build_city_codes() -> dict[str, list[str]]:
        with open('../../Others/City Codes.txt', 'r') as file:
            city_codes = dict()

            for file_line in file.readlines():
                file_line = file_line.strip('\n')
                file_line = re.split('\t+', file_line)
                city_codes[file_line[0]] = file_line[1:]

            return city_codes
