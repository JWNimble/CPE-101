"""
Project 4

CPE101
Spring 2021
Author: Jack Forrester
"""


import unittest
import crimetime
from crimetime import Crime


class MyTest(unittest.TestCase):
    def test_create_crimes(self):
        lines = ['150096082\tROBBERY\tROBBERY, BODILY FORCE\n',
                '150096082\tROBBERY\tROBBERY, BODILY FORCE\n',
                '150096082\tASSAULT\tAGGRAVATED ASSAULT WITH BODILY FORCE\n',
                '150096082\tOTHER OFFENSES\tPROBATION VIOLATION\n',
                '150096195\tOTHER OFFENSES\tTRAFFIC VIOLATION ARREST\n',
                '150096082\tROBBERY\tROBBERY, BODILY FORCE\n',
                '150096082\tASSAULT\tAGGRAVATED ASSAULT WITH BODILY FORCE\n',
                '150096208\tROBBERY\tCARJACKING WITH BODILY FORCE\n',
                '150096208\tVEHICLE THEFT\tSTOLEN AUTOMOBILE\n']
        expected = [Crime(150096082, 'ROBBERY'), Crime(150096208, 'ROBBERY')]
        self.assertEqual(crimetime.create_crimes(lines), expected)
        lines2 = ['1\tROBBERY\tROBBERY\n', '2\tVANDALISM\tVANDALISM\n',
                '3\tROBBERY\tROBBERY\n', '3\tASSAULT\tASSAULT\n',
                '4\tDRUGS\tPOSSESSION\n', '4\tOTHER OFFENSE\tTRAFFIC VIOLATION']
        expected2 = [Crime(1, 'ROBBERY'), Crime(3, 'ROBBERY')]
        self.assertEqual(crimetime.create_crimes(lines2), expected2)
        lines3 = ['1\tVANDALISM\tGRAFFITI\n', '1\tVANDALISM\tVANDALISM\n',
                '2\tROBBERY\tROBBERY\n', '2\tROBBERY\tROBBERY\n',
                '3\tDOG\tWAS A BAD BOI\n', '4\tROBBERY\tROBBERY']
        expected3 = [Crime(2, 'ROBBERY'), Crime(4, 'ROBBERY')]
        self.assertEqual(crimetime.create_crimes(lines3), expected3)


    def test_sort_crimes(self):
        crimes = [Crime(150011660, 'ROBBERY'), Crime(150023994, 'ROBBERY'),
                Crime(150027300, 'ROBBERY'), Crime(150096082, 'ROBBERY'),
                Crime(150096208, 'ROBBERY')]
        expected = [Crime(150011660, 'ROBBERY'), Crime(150023994, 'ROBBERY'),
                Crime(150027300, 'ROBBERY'), Crime(150096082, 'ROBBERY'),
                Crime(150096208, 'ROBBERY')]
        self.assertEqual(crimetime.sort_crimes(crimes), expected)
        crimes2 = [Crime(150027300, 'ROBBERY'), Crime(150096208, 'ROBBERY'),
                Crime(150011660, 'ROBBERY'), Crime(150096082, 'ROBBERY'),
                Crime(150023994, 'ROBBERY')]
        expected2 = [Crime(150011660, 'ROBBERY'), Crime(150023994, 'ROBBERY'),
                Crime(150027300, 'ROBBERY'), Crime(150096082, 'ROBBERY'),
                Crime(150096208, 'ROBBERY')]
        self.assertEqual(crimetime.sort_crimes(crimes2), expected2)
        crimes3 = [Crime(5, 'ROBBERY'), Crime(4, 'ROBBERY'),
                Crime(3, 'ROBBERY'), Crime(2, 'ROBBERY'),
                Crime(1, 'ROBBERY'), Crime(0, 'ROBBERY')]
        expected3 = [Crime(0, 'ROBBERY'), Crime(1, 'ROBBERY'),
                Crime(2, 'ROBBERY'), Crime(3, 'ROBBERY'),
                Crime(4, 'ROBBERY'), Crime(5, 'ROBBERY')]
        self.assertEqual(crimetime.sort_crimes(crimes3), expected3)


    def test_set_crimetime(self):
        c1 = Crime(150011660, 'ROBBERY')
        crimetime.set_crimetime(c1, 'Wednesday', 7, 17)
        c2 = Crime(150027300, 'ROBBERY')
        crimetime.set_crimetime(c2, 'Friday', 11, 12)
        c3 = Crime(150096082, 'ROBBERY')
        crimetime.set_crimetime(c3, 'Sunday', 12, 0)
        c4 = Crime(150011660, 'ROBBERY')
        c4.day_of_week = 'Wednesday'
        c4.month = 'July'
        c4.hour = '5PM'
        c5 = Crime(150027300, 'ROBBERY')
        c5.day_of_week = 'Friday'
        c5.month = 'November'
        c5.hour = '12PM'
        c6 = Crime(150096082, 'ROBBERY')
        c6.day_of_week = 'Sunday'
        c6.month = 'December'
        c6.hour = '12AM'
        self.assertEqual(c1, c4)
        self.assertEqual(c2, c5)
        self.assertEqual(c3, c6)


    def test_update_crimes(self):
        crimes = [Crime(150011660, 'ROBBERY'), Crime(150027300, 'ROBBERY'),
                Crime(150096082, 'ROBBERY')]
        lines = ['150011660\tWednesday\t07/23/2015\t17:35\n',
                '150027300\tFriday\t11/01/2014\t12:12\n',
                '150096082\tSunday\t12/12/2012\t00:00\n']
        crimetime.update_crimes(crimes, lines)
        c1 = Crime(150011660, 'ROBBERY')
        c1.day_of_week = 'Wednesday'
        c1.month = 'July'
        c1.hour = '5PM'
        c2 = Crime(150027300, 'ROBBERY')
        c2.day_of_week = 'Friday'
        c2.month = 'November'
        c2.hour = '12PM'
        c3 = Crime(150096082, 'ROBBERY')
        c3.day_of_week = 'Sunday'
        c3.month = 'December'
        c3.hour = '12AM'
        self.assertEqual(crimes[0], c1)
        self.assertEqual(crimes[1], c2)
        self.assertEqual(crimes[2], c3)


    def test_find_crime(self):
        crimes = [Crime(150011660, 'ROBBERY'), Crime(150027300, 'ROBBERY'),
                Crime(150096082, 'ROBBERY')]
        self.assertEqual(crimetime.find_crime(crimes, 150011660), 0)
        crimes2 = [Crime(150011660, 'ROBBERY'), Crime(150023994, 'ROBBERY'),
                Crime(150027300, 'ROBBERY'), Crime(150096082, 'ROBBERY'),
                Crime(150096208, 'ROBBERY')]
        self.assertEqual(crimetime.find_crime(crimes2, 150000000), -1)
        crimes3 = [Crime(1, 'ROBBERY'), Crime(2, 'ROBBERY'),
                Crime(3, 'ROBBERY')]
        self.assertEqual(crimetime.find_crime(crimes3, 3), 2)


    def test_how_many(self):
        lst = [1, 2, 3, 4, 4, 4, 3, 2, 2]
        self.assertEqual(crimetime.how_many(lst, 4), 3)
        lst2 = ['d', 's', 's', 'a', 'a']
        self.assertEqual(crimetime.how_many(lst2, 'b'), 0)
        lst3 = ['Friday', 'Friday', 'Saturday', 'Wednesday']
        self.assertEqual(crimetime.how_many(lst3, 'Friday'), 2)


    def test_max_rob_by_attr(self):
        crimes = [Crime(150011660, 'ROBBERY'), Crime(150027300, 'ROBBERY'),
                Crime(150096082, 'ROBBERY')]
        lines = ['150011660\tWednesday\t07/23/2015\t17:35\n',
                '150027300\tWednesday\t12/01/2014\t00:12\n',
                '150096082\tSunday\t12/12/2012\t00:00\n']
        crime_sort = crimetime.sort_crimes(crimes)
        crimetime.update_crimes(crime_sort, lines)
        day_most = crimetime.max_rob_by_attr(crime_sort, 'day_of_week')
        month_most = crimetime.max_rob_by_attr(crime_sort, 'month')
        hour_most = crimetime.max_rob_by_attr(crime_sort, 'hour')
        self.assertEqual(day_most, 'Wednesday')
        self.assertEqual(month_most, 'December')
        self.assertEqual(hour_most, '12AM')
        crimes2 = [Crime(1, 'ROBBERY'), Crime(2, 'ROBBERY'),
                Crime(3, 'ROBBERY'), Crime(4, 'ROBBERY'),  Crime(5, 'ROBBERY'),
                Crime(6, 'ROBBERY'), Crime(7, 'ROBBERY'),  Crime(8, 'ROBBERY')]
        lines2 = ['1\tMonday\t07/23/2015\t17:35\n', 
                '2\tWednesday\t04/01/2014\t22:12\n',
                '3\tSaturday\t05/07/2016\t00:23\n',
                '4\tSaturday\t10/17/2018\t22:00\n',
                '5\tSunday\t12/13/2020\t01:45\n',
                '6\tSaturday\t10/24/2018\t22:15\n',
                '7\tMonday\t10/05/2017\t17:30\n',
                '8\tTuesday\t11/28/2012\t01:06\n']
        crime_sort2 = crimetime.sort_crimes(crimes2)
        crimetime.update_crimes(crime_sort2, lines2)
        day_most2 = crimetime.max_rob_by_attr(crime_sort2, 'day_of_week')
        month_most2 = crimetime.max_rob_by_attr(crime_sort2, 'month')
        hour_most2 = crimetime.max_rob_by_attr(crime_sort2, 'hour')
        self.assertEqual(day_most2, 'Saturday')
        self.assertEqual(month_most2, 'October')
        self.assertEqual(hour_most2, '10PM')
        crimes3 = [Crime(1, 'ROBBERY'), Crime(2, 'ROBBERY'),
                Crime(3, 'ROBBERY')]
        lines3 = ['1\tFriday\t01/23/2015\t01:35\n',
                '2\tFriday\t01/01/2014\t01:12\n',
                '3\tFriday\t01/12/2012\t01:00\n']
        crime_sort3 = crimetime.sort_crimes(crimes3)
        crimetime.update_crimes(crime_sort3, lines3)
        day_most3 = crimetime.max_rob_by_attr(crime_sort3, 'day_of_week')
        month_most3 = crimetime.max_rob_by_attr(crime_sort3, 'month')
        hour_most3 = crimetime.max_rob_by_attr(crime_sort3, 'hour')
        self.assertEqual(day_most3, 'Friday')
        self.assertEqual(month_most3, 'January')
        self.assertEqual(hour_most3, '1AM')


if __name__ == '__main__':
    unittest.main()
