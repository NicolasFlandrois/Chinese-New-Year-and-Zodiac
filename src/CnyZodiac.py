#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date: Thu 09 February 2023 20:38:36 CET
# Last Modified time: Fri 10 February 2023 02:29:03 CET

# Description:

from datetime import datetime, timedelta, date

from astral import moon


class ChineseNewYearZodiac:

    def __init__(self, lang: str = 'en'):
        self.ZODIAC = {
            'en': [
                'Monkey', 'Rooster', 'Dog', 'Pig', 'Rat', 'Ox', 'Tiger',
                'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat'
            ],  # English (default)
            'fr': [
                'Singe', 'Coq', 'Chien', 'Cochon', 'Rat', 'Boeuf', 'Tigre',
                'Lapin', 'Dragon', 'Serpent', 'Cheval', 'Chèvre'
            ],  # French
            'cn': [],  # Chinese Simplified (mainland mandarin)
        }
        self.lang = lang

    def zodiac(self, year: int) -> str:
        """
        For any given year (Integer), the zodiac() method will return its
        Zodiac sign (String).
        """
        return self.ZODIAC.get(self.lang, 'en')[year % 12]

    def chinese_new_year(self, year: int) -> date:
        """
        The chinese_new_year() method, givena year (Integer), will return the
        Chinese New Year's date, faor that same year.

        ---
        source: https://en.wikipedia.org/wiki/Chinese_calendar
        > Years start on the second (or third) new moon
        > after the winter solstice.
        > [...]
        > Chinese New Year
        > The date of the Chinese New Year accords with the patterns of the
        > lunisolar calendar and hence is variable from year to year.
        > However, two general rules govern the date. Firstly, Chinese New Year
        > transpires on the second new moon following the December solstice.
        > If there is a **leap month** after the eleventh or twelfth month,
        > then Chinese New Year falls on the third new moon after the December
        > solstice. Alternately, Chinese New Year will fall on the new moon
        > that is closest to lì chūn, or the solar term that begins spring
        > (typically falls on 4 February). However, this rule is not as
        > reliable since it can be difficult to determine which new moon is the
        > closest in the case of an early or late Chinese New Year.
        > It has been found that Chinese New Year moves back by either 10, 11,
        > or 12 days in some years. If it falls before 21 January, then it
        > moves forward in the next year by either 18, 19, or 20 days.

        Which, according to records between 1930 and 2030, statistically
        settles between January 22nd and February 19th.

        ---
        source: https://en.wikipedia.org/wiki/Winter_solstice
        > The winter solstice occurs during the hemisphere's winter.
        > In the Northern Hemisphere, this is the December solstice (usually
        > 21st or 22nd December) and in the Southern Hemisphere, this is the
        > June solstice (usually 20th or 21st of June).
        As China is located in Northern Hemisphere, December's winter solstice
        is the one we'll use, statistically mostly on the 21st.

        ---
        **NB**:
        There is the theory (above), and lots of exceptions (cf code).
        So far I don't understand the logic, nor see a pattern.
        How to compute the special cases and leap months?
        How to make it a full proof mathematical algorythm,
        so it works whatever the year?
        """
        cny_range = [
            datetime(year=year, month=1, day=22) + timedelta(days=delta)
            for delta in range(30)
            ]
        date = min((moon.phase(date), date) for date in cny_range)[1]
        previous_day = date - timedelta(days=1)
        cny_day_range = [previous_day + timedelta(hours=delta)
                         for delta in range(72)]

        cny = min((moon.phase(date), date) for date in cny_day_range)[1]

        if cny.year in [1902, 1916, 1918, 1925, 1931, 1932, 1938, 1941, 1942,
                        1943, 1944, 1946, 1954, 1958, 1963, 1964, 1978, 1987,
                        1988, 1994, 1997, 2000, 2001, 2006, 2016, 2025, 2026,
                        2027, 2028,]:
            # Treating "some" exceptions...
            # I don't see the logic, or pattern, but those dates are facts.
            return cny.date()

        elif cny.year in [1966]:
            # Treating a special exceptions...
            # I don't see the logic, or pattern, but those dates are facts.
            return datetime(cny.year, 1, 21).date()

        elif cny.year in [2004, 2023]:
            # Treating some VERY special exceptions...
            # I don't see the logic, or pattern, but those dates are facts.
            return datetime(cny.year, 1, 22).date()

        else:
            cny += timedelta(days=1)
            return cny.date()

    def zodiac_date(self, date: datetime) -> str:
        """
        Returns the zodiac sign for a given date (datetime).
        Takes into account if the date is before or after
        Chinese New Year's day.
        """
        if date.date() < self.chinese_new_year(date.year):
            return self.zodiac(date.year - 1)
        return self.zodiac(date.year)

    def zodiac_now(self) -> str:
        """
        Returns today's zodiac sign.
        Takes into account if the date is before or after
        Chinese New Year's day.
        """
        return self.zodiac_date(datetime.now())

    def chinese_new_year_zodiac_full_details_date(self,
                                                  date: datetime) -> dict:
        """
        Given a date, this method will return detailed informations about that
        year's Chinese New Year and Zodiac sign.
        """
        return {
            'date': date,
            'year': date.year,
            'Chinese New Year': self.chinese_new_year(date.year),
            'Zodiac': self.zodiac(date.year),
        }

    def chinese_new_year_zodiac_full_details_now(self) -> dict:
        """
        This method will return detailed informations about
        Chinese New Year and Zodiac sign, for the current date & year.
        """
        return self.chinese_new_year_zodiac_full_details_date(datetime.now())

    def chinese_new_year_zodiac_when_next_year(self) -> dict:
        """
        This method will return detailed informations about
        Chinese New Year and Zodiac sign, for the current date's next year.
        """
        now = datetime.now()
        nxt_year = datetime(year=now.year + 1, month=now.month, day=now.day,
                            hour=now.hour, minute=now.minute,
                            second=now.second, microsecond=now.microsecond)
        next_yr_data = self.chinese_new_year_zodiac_full_details_date(nxt_year)
        del next_yr_data['date']
        return next_yr_data
