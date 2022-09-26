import re


class BulgarianCitizenAttributesBuilder:
    @staticmethod
    def build_city_codes() -> dict[str, list[str]]:
        with open('../../Others/City Codes.txt', 'r') as file:
            city_codes = dict()

            for file_line in file.readlines():
                file_line = file_line.strip('\n')
                file_line = re.split('\t+', file_line)
                city_codes[file_line[0]] = file_line[1:]

            return city_codes
