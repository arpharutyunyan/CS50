"""
    In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY), otherwise known as middle-endian order, 
    which is arguably bad design. Dates in that format can’t be easily sorted because the date’s year comes last instead of first. Try sorting, 
    for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet). Dates in that format are also ambiguous. 
    Harvard was founded on September 8, 1636, but 9/8/1636 could also be interpreted as August 9, 1636!

    Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates should be formatted in year-month-day (YYYY-MM-DD) 
    order, no matter the country, formatting years with four digits, months with two digits, and days with two digits, “padding” each with leading zeroes 
    as needed.

    In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 
    or September 8, 1636, wherein the month in the latter might be any of the values in the list below:

    [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again. Assume that 
    every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.
    
"""

from copy import copy

month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:

    date = input("Date: ")
    date_copy = copy(date).replace("/", " ").replace(",", "").split(" ")


    if len(date_copy) == 3:

        for i in range(3):

            if date_copy[i].isdigit():
                date_copy[i] = int(date_copy[i])

        if date_copy[0] in month:
            if date_copy[1] < 31 and "/" not in date and "," in date:
                print(f"{date_copy[2]}-{(month.index(date_copy[0])+1):02}-{date_copy[1]:02}")
                break
            else:
                continue
        elif date_copy[0] <= 12:
            if date_copy[1] in month:
                continue

            elif date_copy[1] <= 31:
                print(f"{date_copy[2]}-{date_copy[0]:02}-{date_copy[1]:02}")
                break
            else:
                continue