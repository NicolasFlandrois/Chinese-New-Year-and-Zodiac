# Chinese-New-Year-and-Zodiac

**Date**: Fri 10 February 2023 20:21:38 CET

**Author**: Nicolas Flandrois

**Licence**: MIT License - Copyright (c) 2023 - Nicolas Flandrois

![](https://img.shields.io/badge/Python-%3E%3D3.7-blue.svg) ![](https://img.shields.io/badge/dependencies-astral%20%3E%3D%203.2-informational.svg) ![GitHub](https://img.shields.io/github/license/NicolasFlandrois/Chinese-New-Year-and-Zodiac) ![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/NicolasFlandrois/Chinese-New-Year-and-Zodiac?style=flat)

----
## DESCRIPTION:
Chinese-New-Year-and-Zodiac package aim to automate finding Chinese New Year's date, and/or find the Chinese Zodiac sign, for a given Year or Date.

This package is set to be multi languages:
- 'en' - English (default)
- 'fr' - French
- 'cn' - Chinese (simplified chinese, mainland china, mandarin) *work in progress*

## Install

`pip install ChineseNewYear-Zodiac`

## How to use it?
*exemples:*

```python
from CnyZodiac import ChineseNewYearZodiac as cnyz

# Default settings (lang='en')
my_cnyz = cnyz()

# Change Language
en_cnyz = cnyz(lang='en')  # English
fr_cnyz = cnyz(lang='fr')  # French
cn_cnyz = cnyz(lang='cn')  # Simplified Chinese Mandarin  (Work In Progress)


# Chinese Zodiac for a given Year
zodiac_2023 = my_cnyz.zodiac(2023)
# output: Rabbit

# Find the Chinese New Year's date for a given year (Integer)
cny_2023 = my_cnyz.chinese_new_year(2023)
# output: datetime.date(2023, 1, 22)

# Given a datetime object find out it's Chinese Zodiac sign
zodiac_date = zodiac_date(datetime.datetime(1998, 7, 15))
# output: Tiger

# Find out what Chinese Zodiac sign is it right now
now_zodiac = my_cnyz.zodiac_now()  # e.g. if command launched on 2023-02-10
# outupt: Rabbit

# For a given datetime object, find out in more detailed informations: New Year this year, and current Chinese Zodiac
cnyz_1968 = my_cnyz.chinese_new_year_zodiac_full_details_date(datetime.datetime(1968, 6, 6, 1, 59, 5))
# output:
# {
#     'Chinese New Year': date(1968, 1, 30),
#     'Zodiac': 'Monkey',
#     'date': datetime(1968, 6, 6, 1, 59, 5),
#     'year': 1968
# }

# Get detailed information for current datetime.now() automatically
cnyz_now = my_cnyz.chinese_new_year_zodiac_full_details_now()
# output (if current datetime is 2023-02-10):
# {
#     'Chinese New Year': date(2023, 1, 22),
#     'Zodiac': 'Rabbit',
#     'date': datetime(2023, 2, 10, 1, 59, 5),
#     'year': 2023
# }

# Get detailed information for next (comming) year, based on datetime.now() automatically
cnyz_now = my_cnyz.chinese_new_year_zodiac_full_details_now()
# output (if current datetime is 2023-07-04):
# {
#     'Chinese New Year': date(2024, 2, 10),
#     'Zodiac': 'Dragon',
#     'year': 2024
# }
```

---
### TODO (Work In Progress, still in development)
- [ ] Add Simplified Chinese in multi lang.
- [ ] Optimize code AND find a mathematical full proof way to conteract leap months, so this package can work for ANY given year/date (past of future).
