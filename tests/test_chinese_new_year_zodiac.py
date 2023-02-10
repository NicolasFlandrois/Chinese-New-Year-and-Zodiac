from datetime import datetime, date

from freezegun import freeze_time

from CnyZodiac import ChineseNewYearZodiac as CnyZodiac


class TestChineseNewYearZodiac:
    """
    Testing default settings and all computing processes.
    """
    cny_zodiac_obj = CnyZodiac()

    def test_lang(self):
        assert self.cny_zodiac_obj.lang == 'en'

    def test_zodiac(self):
        assert self.cny_zodiac_obj.zodiac(2023) == 'Rabbit'
        assert self.cny_zodiac_obj.zodiac(2022) == 'Tiger'
        assert self.cny_zodiac_obj.zodiac(2021) == 'Ox'
        assert self.cny_zodiac_obj.zodiac(2020) == 'Rat'
        assert self.cny_zodiac_obj.zodiac(2019) == 'Pig'
        assert self.cny_zodiac_obj.zodiac(2018) == 'Dog'
        assert self.cny_zodiac_obj.zodiac(2017) == 'Rooster'
        assert self.cny_zodiac_obj.zodiac(2016) == 'Monkey'
        assert self.cny_zodiac_obj.zodiac(2015) == 'Goat'
        assert self.cny_zodiac_obj.zodiac(2014) == 'Horse'
        assert self.cny_zodiac_obj.zodiac(2013) == 'Snake'
        assert self.cny_zodiac_obj.zodiac(2012) == 'Dragon'
        assert self.cny_zodiac_obj.zodiac(2011) == 'Rabbit'
        assert self.cny_zodiac_obj.zodiac(2010) == 'Tiger'
        assert self.cny_zodiac_obj.zodiac(2009) == 'Ox'
        assert self.cny_zodiac_obj.zodiac(2008) == 'Rat'
        assert self.cny_zodiac_obj.zodiac(2007) == 'Pig'
        assert self.cny_zodiac_obj.zodiac(2006) == 'Dog'
        assert self.cny_zodiac_obj.zodiac(2005) == 'Rooster'
        assert self.cny_zodiac_obj.zodiac(2004) == 'Monkey'
        assert self.cny_zodiac_obj.zodiac(2003) == 'Goat'
        assert self.cny_zodiac_obj.zodiac(2002) == 'Horse'
        assert self.cny_zodiac_obj.zodiac(2001) == 'Snake'
        assert self.cny_zodiac_obj.zodiac(2000) == 'Dragon'
        assert self.cny_zodiac_obj.zodiac(1999) == 'Rabbit'
        assert self.cny_zodiac_obj.zodiac(1998) == 'Tiger'
        assert self.cny_zodiac_obj.zodiac(1997) == 'Ox'
        assert self.cny_zodiac_obj.zodiac(1996) == 'Rat'
        assert self.cny_zodiac_obj.zodiac(1995) == 'Pig'
        assert self.cny_zodiac_obj.zodiac(1994) == 'Dog'
        assert self.cny_zodiac_obj.zodiac(1993) == 'Rooster'
        assert self.cny_zodiac_obj.zodiac(1992) == 'Monkey'
        assert self.cny_zodiac_obj.zodiac(1991) == 'Goat'
        assert self.cny_zodiac_obj.zodiac(1990) == 'Horse'
        assert self.cny_zodiac_obj.zodiac(1989) == 'Snake'
        assert self.cny_zodiac_obj.zodiac(1988) == 'Dragon'
        assert self.cny_zodiac_obj.zodiac(1987) == 'Rabbit'
        assert self.cny_zodiac_obj.zodiac(1986) == 'Tiger'
        assert self.cny_zodiac_obj.zodiac(1985) == 'Ox'
        assert self.cny_zodiac_obj.zodiac(1984) == 'Rat'
        assert self.cny_zodiac_obj.zodiac(1983) == 'Pig'
        assert self.cny_zodiac_obj.zodiac(1982) == 'Dog'
        assert self.cny_zodiac_obj.zodiac(1981) == 'Rooster'
        assert self.cny_zodiac_obj.zodiac(1980) == 'Monkey'
        assert self.cny_zodiac_obj.zodiac(1979) == 'Goat'
        assert self.cny_zodiac_obj.zodiac(1978) == 'Horse'
        assert self.cny_zodiac_obj.zodiac(1977) == 'Snake'
        assert self.cny_zodiac_obj.zodiac(1976) == 'Dragon'
        assert self.cny_zodiac_obj.zodiac(1975) == 'Rabbit'

    def test_chinese_new_year(self):
        assert self.cny_zodiac_obj.chinese_new_year(1900) == \
            datetime.strptime('Jan. 31, 1900', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1901) == \
            datetime.strptime('Feb. 19, 1901', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1902) == \
            datetime.strptime('Feb. 08, 1902', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1903) == \
            datetime.strptime('Jan. 29, 1903', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1904) == \
            datetime.strptime('Feb. 16, 1904', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1905) == \
            datetime.strptime('Feb. 04, 1905', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1906) == \
            datetime.strptime('Jan. 25, 1906', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1907) == \
            datetime.strptime('Feb. 13, 1907', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1908) == \
            datetime.strptime('Feb. 02, 1908', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1909) == \
            datetime.strptime('Jan. 22, 1909', '%b. %d, %Y').date()

        assert self.cny_zodiac_obj.chinese_new_year(1910) == \
            datetime.strptime('Feb. 10, 1910', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1911) == \
            datetime.strptime('Jan. 30, 1911', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1912) == \
            datetime.strptime('Feb. 18, 1912', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1913) == \
            datetime.strptime('Feb. 06, 1913', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1914) == \
            datetime.strptime('Jan. 26, 1914', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1915) == \
            datetime.strptime('Feb. 14, 1915', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1916) == \
            datetime.strptime('Feb. 03, 1916', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1917) == \
            datetime.strptime('Jan. 23, 1917', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1918) == \
            datetime.strptime('Feb. 11, 1918', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1919) == \
            datetime.strptime('Feb. 01, 1919', '%b. %d, %Y').date()

        assert self.cny_zodiac_obj.chinese_new_year(1920) == \
            datetime.strptime('Feb. 20, 1920', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1921) == \
            datetime.strptime('Feb. 08, 1921', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1922) == \
            datetime.strptime('Jan. 28, 1922', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1923) == \
            datetime.strptime('Feb. 16, 1923', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1924) == \
            datetime.strptime('Feb. 05, 1924', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1925) == \
            datetime.strptime('Jan. 24, 1925', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1926) == \
            datetime.strptime('Feb. 13, 1926', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1927) == \
            datetime.strptime('Feb. 02, 1927', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1928) == \
            datetime.strptime('Jan. 23, 1928', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1929) == \
            datetime.strptime('Feb. 10, 1929', '%b. %d, %Y').date()

        assert self.cny_zodiac_obj.chinese_new_year(1930) == \
            datetime.strptime('Jan. 30, 1930', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1931) == \
            datetime.strptime('Feb. 17, 1931', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1932) == \
            datetime.strptime('Feb. 06, 1932', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1933) == \
            datetime.strptime('Jan. 26, 1933', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1934) == \
            datetime.strptime('Feb. 14, 1934', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1935) == \
            datetime.strptime('Feb. 04, 1935', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1936) == \
            datetime.strptime('Jan. 24, 1936', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1937) == \
            datetime.strptime('Feb. 11, 1937', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1938) == \
            datetime.strptime('Jan. 31, 1938', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1939) == \
            datetime.strptime('Feb. 19, 1939', '%b. %d, %Y').date()

        assert self.cny_zodiac_obj.chinese_new_year(1940) == \
            datetime.strptime('Feb. 08, 1940', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1941) == \
            datetime.strptime('Jan. 27, 1941', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1942) == \
            datetime.strptime('Feb. 15, 1942', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1943) == \
            datetime.strptime('Feb. 04, 1943', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1944) == \
            datetime.strptime('Jan. 25, 1944', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1945) == \
            datetime.strptime('Feb. 13, 1945', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1946) == \
            datetime.strptime('Feb. 01, 1946', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1947) == \
            datetime.strptime('Jan. 22, 1947', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1948) == \
            datetime.strptime('Feb. 10, 1948', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1949) == \
            datetime.strptime('Jan. 29, 1949', '%b. %d, %Y').date()

        assert self.cny_zodiac_obj.chinese_new_year(1950) == \
            datetime.strptime('Feb. 17, 1950', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1951) == \
            datetime.strptime('Feb. 06, 1951', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1952) == \
            datetime.strptime('Jan. 27, 1952', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1953) == \
            datetime.strptime('Feb. 14, 1953', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1954) == \
            datetime.strptime('Feb. 03, 1954', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1955) == \
            datetime.strptime('Jan. 24, 1955', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1956) == \
            datetime.strptime('Feb. 12, 1956', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1957) == \
            datetime.strptime('Jan. 31, 1957', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1958) == \
            datetime.strptime('Feb. 18, 1958', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1959) == \
            datetime.strptime('Feb. 08, 1959', '%b. %d, %Y').date()

        assert self.cny_zodiac_obj.chinese_new_year(1960) == \
            datetime.strptime('Jan. 28, 1960', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1961) == \
            datetime.strptime('Feb. 15, 1961', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1962) == \
            datetime.strptime('Feb. 05, 1962', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1963) == \
            datetime.strptime('Jan. 25, 1963', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1964) == \
            datetime.strptime('Feb. 13, 1964', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1965) == \
            datetime.strptime('Feb. 02, 1965', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1966) == \
            datetime.strptime('Jan. 21, 1966', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1967) == \
            datetime.strptime('Feb. 09, 1967', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1968) == \
            datetime.strptime('Jan. 30, 1968', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1969) == \
            datetime.strptime('Feb. 17, 1969', '%b. %d, %Y').date()

        assert self.cny_zodiac_obj.chinese_new_year(1970) == \
            datetime.strptime('Feb. 06, 1970', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1971) == \
            datetime.strptime('Jan. 27, 1971', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1972) == \
            datetime.strptime('Feb. 15, 1972', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1973) == \
            datetime.strptime('Feb. 03, 1973', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1974) == \
            datetime.strptime('Jan. 23, 1974', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1975) == \
            datetime.strptime('Feb. 11, 1975', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1976) == \
            datetime.strptime('Jan. 31, 1976', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1977) == \
            datetime.strptime('Feb. 18, 1977', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1978) == \
            datetime.strptime('Feb. 07, 1978', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1979) == \
            datetime.strptime('Jan. 28, 1979', '%b. %d, %Y').date()

        assert self.cny_zodiac_obj.chinese_new_year(1980) == \
            datetime.strptime('Feb. 16, 1980', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1981) == \
            datetime.strptime('Feb. 05, 1981', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1982) == \
            datetime.strptime('Jan. 25, 1982', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1983) == \
            datetime.strptime('Feb. 13, 1983', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1984) == \
            datetime.strptime('Feb. 02, 1984', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1985) == \
            datetime.strptime('Feb. 20, 1985', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1986) == \
            datetime.strptime('Feb. 09, 1986', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1987) == \
            datetime.strptime('Jan. 29, 1987', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1988) == \
            datetime.strptime('Feb. 17, 1988', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1989) == \
            datetime.strptime('Feb. 06, 1989', '%b. %d, %Y').date()

        assert self.cny_zodiac_obj.chinese_new_year(1990) == \
            datetime.strptime('Jan. 27, 1990', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1991) == \
            datetime.strptime('Feb. 15, 1991', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1992) == \
            datetime.strptime('Feb. 04, 1992', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1993) == \
            datetime.strptime('Jan. 23, 1993', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1994) == \
            datetime.strptime('Feb. 10, 1994', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1995) == \
            datetime.strptime('Jan. 31, 1995', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1996) == \
            datetime.strptime('Feb. 19, 1996', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1997) == \
            datetime.strptime('Feb. 07, 1997', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1998) == \
            datetime.strptime('Jan. 28, 1998', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(1999) == \
            datetime.strptime('Feb. 16, 1999', '%b. %d, %Y').date()

        assert self.cny_zodiac_obj.chinese_new_year(2000) == \
            datetime.strptime('Feb. 05, 2000', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(2001) == \
            datetime.strptime('Jan. 24, 2001', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(2002) == \
            datetime.strptime('Feb. 12, 2002', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(2003) == \
            datetime.strptime('Feb. 01, 2003', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(2004) == \
            datetime.strptime('Jan. 22, 2004', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(2005) == \
            datetime.strptime('Feb. 09, 2005', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(2006) == \
            datetime.strptime('Jan. 29, 2006', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(2007) == \
            datetime.strptime('Feb. 18, 2007', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(2008) == \
            datetime.strptime('Feb. 07, 2008', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(2009) == \
            datetime.strptime('Jan. 26, 2009', '%b. %d, %Y').date()

        assert self.cny_zodiac_obj.chinese_new_year(2010) == \
            datetime.strptime('Feb. 14, 2010', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(2011) == \
            datetime.strptime('Feb. 03, 2011', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(2012) == \
            datetime.strptime('Jan. 23, 2012', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(2013) == \
            datetime.strptime('Feb. 10, 2013', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(2014) == \
            datetime.strptime('Jan. 31, 2014', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(2015) == \
            datetime.strptime('Feb. 19, 2015', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(2016) == \
            datetime.strptime('Feb. 08, 2016', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(2017) == \
            datetime.strptime('Jan. 28, 2017', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(2018) == \
            datetime.strptime('Feb. 16, 2018', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(2019) == \
            datetime.strptime('Feb. 05, 2019', '%b. %d, %Y').date()

        assert self.cny_zodiac_obj.chinese_new_year(2020) == \
            datetime.strptime('Jan. 25, 2020', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(2021) == \
            datetime.strptime('Feb. 12, 2021', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(2022) == \
            datetime.strptime('Feb. 01, 2022', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(2023) == \
            datetime.strptime('Jan. 22, 2023', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(2024) == \
            datetime.strptime('Feb. 10, 2024', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(2025) == \
            datetime.strptime('Jan. 29, 2025', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(2026) == \
            datetime.strptime('Feb. 17, 2026', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(2027) == \
            datetime.strptime('Feb. 06, 2027', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(2028) == \
            datetime.strptime('Jan. 26, 2028', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(2029) == \
            datetime.strptime('Feb. 13, 2029', '%b. %d, %Y').date()

        assert self.cny_zodiac_obj.chinese_new_year(2030) == \
            datetime.strptime('Feb. 03, 2030', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(2031) == \
            datetime.strptime('Jan. 23, 2031', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(2032) == \
            datetime.strptime('Feb. 11, 2032', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(2033) == \
            datetime.strptime('Jan. 31, 2033', '%b. %d, %Y').date()
        assert self.cny_zodiac_obj.chinese_new_year(2034) == \
            datetime.strptime('Feb. 19, 2034', '%b. %d, %Y').date()

    def test_zodiac_now_2022_01(self):
        assert self.cny_zodiac_obj.zodiac_date(datetime(2022, 1, 1)) == 'Ox'

    def test_zodiac_now_2022_02(self):
        assert self.cny_zodiac_obj.zodiac_date(datetime(2022, 2, 1)) == 'Tiger'

    def test_zodiac_now_1998_01(self):
        assert self.cny_zodiac_obj.zodiac_date(datetime(1998, 1, 1)) == 'Ox'

    def test_zodiac_now_1998_07(self):
        assert self.cny_zodiac_obj.zodiac_date(datetime(1998, 7, 1)) == 'Tiger'

    def test_zodiac_now_1988_01(self):
        assert self.cny_zodiac_obj.zodiac_date(datetime(1988, 1, 1)) == \
            'Rabbit'

    def test_zodiac_now_1988_12(self):
        assert self.cny_zodiac_obj.zodiac_date(datetime(1988, 12, 1)) == \
            'Dragon'

    @freeze_time('2023-01-01 12:00:00')
    def test_zodiac_now_2023_01(self):
        assert self.cny_zodiac_obj.zodiac_now() == 'Tiger'

    @freeze_time('2023-02-10 01:59:05')
    def test_zodiac_now_2023_02(self):
        assert self.cny_zodiac_obj.zodiac_now() == 'Rabbit'

    @freeze_time('2015-01-01 12:00:00')
    def test_zodiac_now_2015_01(self):
        assert self.cny_zodiac_obj.zodiac_now() == 'Horse'

    @freeze_time('2015-10-01 12:00:00')
    def test_zodiac_now_2015_10(self):
        assert self.cny_zodiac_obj.zodiac_now() == 'Goat'

    @freeze_time('2018-01-06 01:59:05')
    def test_zodiac_now_2018_01(self):
        assert self.cny_zodiac_obj.zodiac_now() == 'Rooster'

    @freeze_time('2018-03-06 01:59:05')
    def test_zodiac_now_2018_03(self):
        assert self.cny_zodiac_obj.zodiac_now() == 'Dog'

    def test_chinese_new_year_zodiac_full_details_date(self):
        # Given
        expected = {
                        'Chinese New Year': date(2023, 1, 22),
                        'Zodiac': 'Rabbit',
                        'date': datetime(2023, 2, 10, 0, 0),
                        'year': 2023
                    }
        date_test = datetime(2023, 2, 10)
        # When / Then
        assert self.cny_zodiac_obj.chinese_new_year_zodiac_full_details_date(date_test) == expected  # noqa

    @freeze_time('1968-06-06 01:59:05')
    def test_chinese_new_year_zodiac_full_details_now(self):
        # Given
        expected = {
                        'Chinese New Year': date(1968, 1, 30),
                        'Zodiac': 'Monkey',
                        'date': datetime(1968, 6, 6, 1, 59, 5),
                        'year': 1968
                    }
        # When / Then
        assert self.cny_zodiac_obj.chinese_new_year_zodiac_full_details_now() == expected  # noqa

    @freeze_time('1957-03-07 01:59:05')
    def test_chinese_new_year_zodiac_full_details_when_next_year(self):
        # Given
        expected = {
                        'Chinese New Year': date(1958, 2, 18),
                        'Zodiac': 'Dog',
                        'year': 1958
                    }
        # When / Then
        assert self.cny_zodiac_obj.chinese_new_year_zodiac_when_next_year() == expected  # noqa

    def test_chinese_new_year_zodiac_full_details_date_jan(self):
        # Given
        expected = {
                        'Chinese New Year': date(2023, 1, 22),
                        'Zodiac': 'Rabbit',
                        'date': datetime(2023, 1, 10, 0, 0),
                        'year': 2023
                    }
        date_test = datetime(2023, 1, 10)
        # When / Then
        assert self.cny_zodiac_obj.chinese_new_year_zodiac_full_details_date(date_test) == expected  # noqa

    @freeze_time('1968-01-06 01:59:05')
    def test_chinese_new_year_zodiac_full_details_now_jan(self):
        # Given
        expected = {
                        'Chinese New Year': date(1968, 1, 30),
                        'Zodiac': 'Monkey',
                        'date': datetime(1968, 1, 6, 1, 59, 5),
                        'year': 1968
                    }
        # When / Then
        assert self.cny_zodiac_obj.chinese_new_year_zodiac_full_details_now() == expected  # noqa

    @freeze_time('1957-01-07 01:59:05')
    def test_chinese_new_year_zodiac_full_details_when_next_year_jan(self):
        # Given
        expected = {
                        'Chinese New Year': date(1958, 2, 18),
                        'Zodiac': 'Dog',
                        'year': 1958
                    }
        # When / Then
        assert self.cny_zodiac_obj.chinese_new_year_zodiac_when_next_year() == expected  # noqa


class TestChineseNewYearZodiacEnglish:
    cny_zodiac_obj = CnyZodiac(lang='en')

    def test_lang(self):
        assert self.cny_zodiac_obj.lang == 'en'

    def test_zodiac(self):
        assert self.cny_zodiac_obj.zodiac(2023) == 'Rabbit'
        assert self.cny_zodiac_obj.zodiac(2022) == 'Tiger'
        assert self.cny_zodiac_obj.zodiac(2021) == 'Ox'
        assert self.cny_zodiac_obj.zodiac(2020) == 'Rat'
        assert self.cny_zodiac_obj.zodiac(2019) == 'Pig'
        assert self.cny_zodiac_obj.zodiac(2018) == 'Dog'
        assert self.cny_zodiac_obj.zodiac(2017) == 'Rooster'
        assert self.cny_zodiac_obj.zodiac(2016) == 'Monkey'
        assert self.cny_zodiac_obj.zodiac(2015) == 'Goat'
        assert self.cny_zodiac_obj.zodiac(2014) == 'Horse'
        assert self.cny_zodiac_obj.zodiac(2013) == 'Snake'
        assert self.cny_zodiac_obj.zodiac(2012) == 'Dragon'
        assert self.cny_zodiac_obj.zodiac(2011) == 'Rabbit'
        assert self.cny_zodiac_obj.zodiac(2010) == 'Tiger'
        assert self.cny_zodiac_obj.zodiac(2009) == 'Ox'
        assert self.cny_zodiac_obj.zodiac(2008) == 'Rat'
        assert self.cny_zodiac_obj.zodiac(2007) == 'Pig'
        assert self.cny_zodiac_obj.zodiac(2006) == 'Dog'
        assert self.cny_zodiac_obj.zodiac(2005) == 'Rooster'
        assert self.cny_zodiac_obj.zodiac(2004) == 'Monkey'
        assert self.cny_zodiac_obj.zodiac(2003) == 'Goat'
        assert self.cny_zodiac_obj.zodiac(2002) == 'Horse'
        assert self.cny_zodiac_obj.zodiac(2001) == 'Snake'
        assert self.cny_zodiac_obj.zodiac(2000) == 'Dragon'
        assert self.cny_zodiac_obj.zodiac(1999) == 'Rabbit'
        assert self.cny_zodiac_obj.zodiac(1998) == 'Tiger'
        assert self.cny_zodiac_obj.zodiac(1997) == 'Ox'
        assert self.cny_zodiac_obj.zodiac(1996) == 'Rat'
        assert self.cny_zodiac_obj.zodiac(1995) == 'Pig'
        assert self.cny_zodiac_obj.zodiac(1994) == 'Dog'
        assert self.cny_zodiac_obj.zodiac(1993) == 'Rooster'
        assert self.cny_zodiac_obj.zodiac(1992) == 'Monkey'
        assert self.cny_zodiac_obj.zodiac(1991) == 'Goat'
        assert self.cny_zodiac_obj.zodiac(1990) == 'Horse'
        assert self.cny_zodiac_obj.zodiac(1989) == 'Snake'
        assert self.cny_zodiac_obj.zodiac(1988) == 'Dragon'
        assert self.cny_zodiac_obj.zodiac(1987) == 'Rabbit'
        assert self.cny_zodiac_obj.zodiac(1986) == 'Tiger'
        assert self.cny_zodiac_obj.zodiac(1985) == 'Ox'
        assert self.cny_zodiac_obj.zodiac(1984) == 'Rat'
        assert self.cny_zodiac_obj.zodiac(1983) == 'Pig'
        assert self.cny_zodiac_obj.zodiac(1982) == 'Dog'
        assert self.cny_zodiac_obj.zodiac(1981) == 'Rooster'
        assert self.cny_zodiac_obj.zodiac(1980) == 'Monkey'
        assert self.cny_zodiac_obj.zodiac(1979) == 'Goat'
        assert self.cny_zodiac_obj.zodiac(1978) == 'Horse'
        assert self.cny_zodiac_obj.zodiac(1977) == 'Snake'
        assert self.cny_zodiac_obj.zodiac(1976) == 'Dragon'
        assert self.cny_zodiac_obj.zodiac(1975) == 'Rabbit'

    def test_zodiac_now_2022_01(self):
        assert self.cny_zodiac_obj.zodiac_date(datetime(2022, 1, 1)) == 'Ox'

    def test_zodiac_now_2022_02(self):
        assert self.cny_zodiac_obj.zodiac_date(datetime(2022, 2, 1)) == 'Tiger'

    def test_zodiac_now_1998_01(self):
        assert self.cny_zodiac_obj.zodiac_date(datetime(1998, 1, 1)) == 'Ox'

    def test_zodiac_now_1998_07(self):
        assert self.cny_zodiac_obj.zodiac_date(datetime(1998, 7, 1)) == 'Tiger'

    def test_zodiac_now_1988_01(self):
        assert self.cny_zodiac_obj.zodiac_date(datetime(1988, 1, 1)) == \
            'Rabbit'

    def test_zodiac_now_1988_12(self):
        assert self.cny_zodiac_obj.zodiac_date(datetime(1988, 12, 1)) == \
            'Dragon'

    @freeze_time('2023-01-01 12:00:00')
    def test_zodiac_now_2023_01(self):
        assert self.cny_zodiac_obj.zodiac_now() == 'Tiger'

    @freeze_time('2023-02-10 01:59:05')
    def test_zodiac_now_2023_02(self):
        assert self.cny_zodiac_obj.zodiac_now() == 'Rabbit'

    @freeze_time('2015-01-01 12:00:00')
    def test_zodiac_now_2015_01(self):
        assert self.cny_zodiac_obj.zodiac_now() == 'Horse'

    @freeze_time('2015-10-01 12:00:00')
    def test_zodiac_now_2015_10(self):
        assert self.cny_zodiac_obj.zodiac_now() == 'Goat'

    @freeze_time('2018-01-06 01:59:05')
    def test_zodiac_now_2018_01(self):
        assert self.cny_zodiac_obj.zodiac_now() == 'Rooster'

    @freeze_time('2018-03-06 01:59:05')
    def test_zodiac_now_2018_03(self):
        assert self.cny_zodiac_obj.zodiac_now() == 'Dog'

    def test_chinese_new_year_zodiac_full_details_date(self):
        # Given
        expected = {
                        'Chinese New Year': date(2023, 1, 22),
                        'Zodiac': 'Rabbit',
                        'date': datetime(2023, 2, 10, 0, 0),
                        'year': 2023
                    }
        date_test = datetime(2023, 2, 10)
        # When / Then
        assert self.cny_zodiac_obj.chinese_new_year_zodiac_full_details_date(date_test) == expected  # noqa

    @freeze_time('1968-06-06 01:59:05')
    def test_chinese_new_year_zodiac_full_details_now(self):
        # Given
        expected = {
                        'Chinese New Year': date(1968, 1, 30),
                        'Zodiac': 'Monkey',
                        'date': datetime(1968, 6, 6, 1, 59, 5),
                        'year': 1968
                    }
        # When / Then
        assert self.cny_zodiac_obj.chinese_new_year_zodiac_full_details_now() == expected  # noqa

    @freeze_time('1957-03-07 01:59:05')
    def test_chinese_new_year_zodiac_full_details_when_next_year(self):
        # Given
        expected = {
                        'Chinese New Year': date(1958, 2, 18),
                        'Zodiac': 'Dog',
                        'year': 1958
                    }
        # When / Then
        assert self.cny_zodiac_obj.chinese_new_year_zodiac_when_next_year() == expected  # noqa

    def test_chinese_new_year_zodiac_full_details_date_jan(self):
        # Given
        expected = {
                        'Chinese New Year': date(2023, 1, 22),
                        'Zodiac': 'Rabbit',
                        'date': datetime(2023, 1, 10, 0, 0),
                        'year': 2023
                    }
        date_test = datetime(2023, 1, 10)
        # When / Then
        assert self.cny_zodiac_obj.chinese_new_year_zodiac_full_details_date(date_test) == expected  # noqa

    @freeze_time('1968-01-06 01:59:05')
    def test_chinese_new_year_zodiac_full_details_now_jan(self):
        # Given
        expected = {
                        'Chinese New Year': date(1968, 1, 30),
                        'Zodiac': 'Monkey',
                        'date': datetime(1968, 1, 6, 1, 59, 5),
                        'year': 1968
                    }
        # When / Then
        assert self.cny_zodiac_obj.chinese_new_year_zodiac_full_details_now() == expected  # noqa

    @freeze_time('1957-01-07 01:59:05')
    def test_chinese_new_year_zodiac_full_details_when_next_year_jan(self):
        # Given
        expected = {
                        'Chinese New Year': date(1958, 2, 18),
                        'Zodiac': 'Dog',
                        'year': 1958
                    }
        # When / Then
        assert self.cny_zodiac_obj.chinese_new_year_zodiac_when_next_year() == expected  # noqa


class TestChineseNewYearZodiacFrench:
    cny_zodiac_obj = CnyZodiac(lang='fr')

    def test_lang(self):
        assert self.cny_zodiac_obj.lang == 'fr'

    def test_zodiac(self):
        assert self.cny_zodiac_obj.zodiac(2023) == 'Lapin'
        assert self.cny_zodiac_obj.zodiac(2022) == 'Tigre'
        assert self.cny_zodiac_obj.zodiac(2021) == 'Boeuf'
        assert self.cny_zodiac_obj.zodiac(2020) == 'Rat'
        assert self.cny_zodiac_obj.zodiac(2019) == 'Cochon'
        assert self.cny_zodiac_obj.zodiac(2018) == 'Chien'
        assert self.cny_zodiac_obj.zodiac(2017) == 'Coq'
        assert self.cny_zodiac_obj.zodiac(2016) == 'Singe'
        assert self.cny_zodiac_obj.zodiac(2015) == 'Chèvre'
        assert self.cny_zodiac_obj.zodiac(2014) == 'Cheval'
        assert self.cny_zodiac_obj.zodiac(2013) == 'Serpent'
        assert self.cny_zodiac_obj.zodiac(2012) == 'Dragon'
        assert self.cny_zodiac_obj.zodiac(2011) == 'Lapin'
        assert self.cny_zodiac_obj.zodiac(2010) == 'Tigre'
        assert self.cny_zodiac_obj.zodiac(2009) == 'Boeuf'
        assert self.cny_zodiac_obj.zodiac(2008) == 'Rat'
        assert self.cny_zodiac_obj.zodiac(2007) == 'Cochon'
        assert self.cny_zodiac_obj.zodiac(2006) == 'Chien'
        assert self.cny_zodiac_obj.zodiac(2005) == 'Coq'
        assert self.cny_zodiac_obj.zodiac(2004) == 'Singe'
        assert self.cny_zodiac_obj.zodiac(2003) == 'Chèvre'
        assert self.cny_zodiac_obj.zodiac(2002) == 'Cheval'
        assert self.cny_zodiac_obj.zodiac(2001) == 'Serpent'
        assert self.cny_zodiac_obj.zodiac(2000) == 'Dragon'
        assert self.cny_zodiac_obj.zodiac(1999) == 'Lapin'
        assert self.cny_zodiac_obj.zodiac(1998) == 'Tigre'
        assert self.cny_zodiac_obj.zodiac(1997) == 'Boeuf'
        assert self.cny_zodiac_obj.zodiac(1996) == 'Rat'
        assert self.cny_zodiac_obj.zodiac(1995) == 'Cochon'
        assert self.cny_zodiac_obj.zodiac(1994) == 'Chien'
        assert self.cny_zodiac_obj.zodiac(1993) == 'Coq'
        assert self.cny_zodiac_obj.zodiac(1992) == 'Singe'
        assert self.cny_zodiac_obj.zodiac(1991) == 'Chèvre'
        assert self.cny_zodiac_obj.zodiac(1990) == 'Cheval'
        assert self.cny_zodiac_obj.zodiac(1989) == 'Serpent'
        assert self.cny_zodiac_obj.zodiac(1988) == 'Dragon'
        assert self.cny_zodiac_obj.zodiac(1987) == 'Lapin'
        assert self.cny_zodiac_obj.zodiac(1986) == 'Tigre'
        assert self.cny_zodiac_obj.zodiac(1985) == 'Boeuf'
        assert self.cny_zodiac_obj.zodiac(1984) == 'Rat'
        assert self.cny_zodiac_obj.zodiac(1983) == 'Cochon'
        assert self.cny_zodiac_obj.zodiac(1982) == 'Chien'
        assert self.cny_zodiac_obj.zodiac(1981) == 'Coq'
        assert self.cny_zodiac_obj.zodiac(1980) == 'Singe'
        assert self.cny_zodiac_obj.zodiac(1979) == 'Chèvre'
        assert self.cny_zodiac_obj.zodiac(1978) == 'Cheval'
        assert self.cny_zodiac_obj.zodiac(1977) == 'Serpent'
        assert self.cny_zodiac_obj.zodiac(1976) == 'Dragon'
        assert self.cny_zodiac_obj.zodiac(1975) == 'Lapin'

    def test_zodiac_now_2022_01(self):
        assert self.cny_zodiac_obj.zodiac_date(datetime(2022, 1, 1)) == 'Boeuf'

    def test_zodiac_now_2022_02(self):
        assert self.cny_zodiac_obj.zodiac_date(datetime(2022, 2, 1)) == 'Tigre'

    def test_zodiac_now_1998_01(self):
        assert self.cny_zodiac_obj.zodiac_date(datetime(1998, 1, 1)) == 'Boeuf'

    def test_zodiac_now_1998_07(self):
        assert self.cny_zodiac_obj.zodiac_date(datetime(1998, 7, 1)) == 'Tigre'

    def test_zodiac_now_1988_01(self):
        assert self.cny_zodiac_obj.zodiac_date(datetime(1988, 1, 1)) == 'Lapin'

    def test_zodiac_now_1988_12(self):
        assert self.cny_zodiac_obj.zodiac_date(datetime(1988, 12, 1)) == \
            'Dragon'

    @freeze_time('2023-01-01 12:00:00')
    def test_zodiac_now_2023_01(self):
        assert self.cny_zodiac_obj.zodiac_now() == 'Tigre'

    @freeze_time('2023-02-10 01:59:05')
    def test_zodiac_now_2023_02(self):
        assert self.cny_zodiac_obj.zodiac_now() == 'Lapin'

    @freeze_time('2015-01-01 12:00:00')
    def test_zodiac_now_2015_01(self):
        assert self.cny_zodiac_obj.zodiac_now() == 'Cheval'

    @freeze_time('2015-10-01 12:00:00')
    def test_zodiac_now_2015_10(self):
        assert self.cny_zodiac_obj.zodiac_now() == 'Chèvre'

    @freeze_time('2018-01-06 01:59:05')
    def test_zodiac_now_2018_01(self):
        assert self.cny_zodiac_obj.zodiac_now() == 'Coq'

    @freeze_time('2018-03-06 01:59:05')
    def test_zodiac_now_2018_03(self):
        assert self.cny_zodiac_obj.zodiac_now() == 'Chien'

    def test_chinese_new_year_zodiac_full_details_date(self):
        # Given
        expected = {
                        'Chinese New Year': date(2023, 1, 22),
                        'Zodiac': 'Lapin',
                        'date': datetime(2023, 2, 10, 0, 0),
                        'year': 2023
                    }
        date_test = datetime(2023, 2, 10)
        # When / Then
        assert self.cny_zodiac_obj.chinese_new_year_zodiac_full_details_date(date_test) == expected  # noqa

    @freeze_time('1968-06-06 01:59:05')
    def test_chinese_new_year_zodiac_full_details_now(self):
        # Given
        expected = {
                        'Chinese New Year': date(1968, 1, 30),
                        'Zodiac': 'Singe',
                        'date': datetime(1968, 6, 6, 1, 59, 5),
                        'year': 1968
                    }
        # When / Then
        assert self.cny_zodiac_obj.chinese_new_year_zodiac_full_details_now() == expected  # noqa

    @freeze_time('1957-03-07 01:59:05')
    def test_chinese_new_year_zodiac_full_details_when_next_year(self):
        # Given
        expected = {
                        'Chinese New Year': date(1958, 2, 18),
                        'Zodiac': 'Chien',
                        'year': 1958
                    }
        # When / Then
        assert self.cny_zodiac_obj.chinese_new_year_zodiac_when_next_year() == expected  # noqa

    def test_chinese_new_year_zodiac_full_details_date_jan(self):
        # Given
        expected = {
                        'Chinese New Year': date(2023, 1, 22),
                        'Zodiac': 'Lapin',
                        'date': datetime(2023, 1, 10, 0, 0),
                        'year': 2023
                    }
        date_test = datetime(2023, 1, 10)
        # When / Then
        assert self.cny_zodiac_obj.chinese_new_year_zodiac_full_details_date(date_test) == expected  # noqa

    @freeze_time('1968-01-06 01:59:05')
    def test_chinese_new_year_zodiac_full_details_now_jan(self):
        # Given
        expected = {
                        'Chinese New Year': date(1968, 1, 30),
                        'Zodiac': 'Singe',
                        'date': datetime(1968, 1, 6, 1, 59, 5),
                        'year': 1968
                    }
        # When / Then
        assert self.cny_zodiac_obj.chinese_new_year_zodiac_full_details_now() == expected  # noqa

    @freeze_time('1957-01-07 01:59:05')
    def test_chinese_new_year_zodiac_full_details_when_next_year_jan(self):
        # Given
        expected = {
                        'Chinese New Year': date(1958, 2, 18),
                        'Zodiac': 'Chien',
                        'year': 1958
                    }
        # When / Then
        assert self.cny_zodiac_obj.chinese_new_year_zodiac_when_next_year() == expected  # noqa


class TestChineseNewYearZodiacChinese:
    cny_zodiac_obj = CnyZodiac(lang='cn')

    def test_lang(self):
        assert self.cny_zodiac_obj.lang == 'cn'

    def test_zodiac(self):
        pass
        # TODO - IN CHINESE
