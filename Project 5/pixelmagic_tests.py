"""
Project 5

CPE101
Spring 2021
Author: Jack Forrester
"""


import unittest
import pixelmagic


class MyTest(unittest.TestCase):
    def test_make_pixel_list(self):
        pixel_data1 = ['1 2 3','4 5 6']
        expected1 = [[1,2,3],[4,5,6]]
        self.assertEqual(pixelmagic.make_pixel_list(pixel_data1), expected1)
        pixel_data2 = ['1 1 1','2 2 2','3 3 3']
        expected2 = [[1,1,1],[2,2,2],[3,3,3]]
        self.assertEqual(pixelmagic.make_pixel_list(pixel_data2), expected2)
        pixel_data3 = ['1 2 3 4 5 6 7 8 9 10']
        expected3 = [[1,2,3,4,5,6,7,8,9,10]]
        self.assertEqual(pixelmagic.make_pixel_list(pixel_data3), expected3)
    

    def test_find_image(self):
        pixel_list1 = [[245, 246, 241], [244, 245, 240], [253, 253, 251],
                [245, 246, 241], [244, 245, 240], [253, 253, 251], 
                [245, 246, 241], [244, 245, 240], [253, 253, 251]]
        expected1 = [[255, 255, 255], [255, 255, 255], [255, 255, 255], 
                [255, 255, 255], [255, 255, 255], [255, 255, 255], 
                [255, 255, 255], [255, 255, 255], [255, 255, 255]]
        pixelmagic.find_image(pixel_list1, 255)
        self.assertEqual(pixel_list1, expected1)
        pixel_list2 = [[21, 11, 2], [24, 14, 4], [24, 14, 5], [25, 14, 5], 
                [25, 15, 5], [26, 16, 6], [26, 16, 6], [27, 16, 7], [27, 17, 7]]
        expected2 = [[210, 210, 210], [240, 240, 240], [240, 240, 240], 
                [250, 250, 250], [250, 250, 250], [255, 255, 255], 
                [255, 255, 255], [255, 255, 255], [255, 255, 255]]
        pixelmagic.find_image(pixel_list2, 255)
        self.assertEqual(pixel_list2, expected2)
        pixel_list3 = [[51, 50, 49], [50, 50, 48], [50, 49, 47], [51, 50, 49], 
                [50, 50, 48], [50, 49, 47], [51, 50, 49], [50, 50, 48], 
                [50, 49, 47]]
        expected3 = [[255, 255, 255], [255, 255, 255], [255, 255, 255],
                [255, 255, 255], [255, 255, 255], [255, 255, 255], 
                [255, 255, 255], [255, 255, 255], [255, 255, 255]]
        pixelmagic.find_image(pixel_list3, 255)
        self.assertEqual(pixel_list3, expected3)


    def test_fade_image(self):
        pixel_list1 = [[245, 246, 241], [244, 245, 240], [253, 253, 251],
                [245, 246, 241], [244, 245, 240], [253, 253, 251], 
                [245, 246, 241], [244, 245, 240], [253, 253, 251]]
        expected1 = [[49, 49, 48], [48, 49, 48], [50, 50, 50], [49, 49, 48],
                [244, 245, 240], [50, 50, 50], [49, 49, 48], [48, 49, 48],
                [50, 50, 50]]
        pixelmagic.fade_image(pixel_list1,3,1,1,1,255)
        self.assertEqual(pixel_list1, expected1)
        pixel_list2 = [[21, 11, 2], [24, 14, 4], [24, 14, 5], [25, 14, 5],
                [25, 15, 5], [26, 16, 6], [26, 16, 6], [27, 16, 7], [27, 17, 7]]
        expected2 = [[4, 2, 0], [4, 2, 0], [4, 2, 1], [5, 2, 1], [25, 15, 5],
                [5, 3, 1], [5, 3, 1], [5, 3, 1], [5, 3, 1]]
        pixelmagic.fade_image(pixel_list2,3,1,1,1,255)
        self.assertEqual(pixel_list2, expected2)
        pixel_list3 = [[51, 50, 49], [50, 50, 48], [50, 49, 47], [51, 50, 49],
                [50, 50, 48], [50, 49, 47], [51, 50, 49], [50, 50, 48],
                [50, 49, 47]]
        expected3 = [[10, 10, 9], [10, 10, 9], [10, 9, 9], [10, 10, 9],
                [50, 50, 48], [10, 9, 9], [10, 10, 9], [10, 10, 9], [10, 9, 9]]
        pixelmagic.fade_image(pixel_list3,3,1,1,1,255)
        self.assertEqual(pixel_list3, expected3)


    def test_make_3d_list(self):
        list1 = [1,2,3,4,5,6,7,8,9]
        expected1 = [[1,2,3],[4,5,6],[7,8,9]]
        self.assertEqual(pixelmagic.make_3d_list(list1, 3), expected1)
        list2 = [0,1,2,3,4,5,6,7,8,9]
        expected2 = [[0,1,2,3,4],[5,6,7,8,9]]
        self.assertEqual(pixelmagic.make_3d_list(list2, 5), expected2)
        list3 = [[1,2,3],[3,1,2],[2,3,1],[1,1,1],[2,2,2],[3,3,3]]
        expected3 = [[[1,2,3],[3,1,2],[2,3,1]],[[1,1,1],[2,2,2],[3,3,3]]]
        self.assertEqual(pixelmagic.make_3d_list(list3, 3), expected3)


    def test_find_neighbors(self):
        grid = [[[0],[1],[2],[3],[4],[5],[6]],
                [[7],[8],[9],[10],[11],[12],[13]],
                [[14],[15],[16],[17],[18],[19],[20]],
                [[21],[22],[23],[24],[25],[26],[27]],
                [[28],[29],[30],[31],[32],[33],[34]],
                [[35],[36],[37],[38],[39],[40],[41]],
                [[42],[43],[44],[45],[46],[47],[48]]]
        expected1 = [0,7,1,8]
        self.assertEqual(pixelmagic.find_neighbors(grid, 0, 0, 1), expected1)
        expected2 = [0,7,14,21,1,8,15,22,2,9,16,23,3,10,17,24]
        self.assertEqual(pixelmagic.find_neighbors(grid, 1, 1, 2), expected2)
        expected3 = [8,15,22,29,36,9,16,23,30,37,10,17,24,31,38,11,18,25,32,39,
                12,19,26,33,40]
        self.assertEqual(pixelmagic.find_neighbors(grid, 3, 3, 2), expected3)


    def test_sort_list(self):
        list1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
        list2 = [14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]
        list3 = [3,5,2,7,14,9,13,8,10,12,11,0,6,4,1]
        expected = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
        pixelmagic.sort_list(list1)
        pixelmagic.sort_list(list2)
        pixelmagic.sort_list(list3)
        self.assertEqual(list1, expected)
        self.assertEqual(list2, expected)
        self.assertEqual(list3, expected)


    def test_find_median(self):
        list1 = [0,1,2,3,4,5,6,7,8]
        self.assertEqual(pixelmagic.find_median(list1), 4)
        list2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
        self.assertEqual(pixelmagic.find_median(list2), 7)
        list3 = [4,7,10,22,33,44,56,78,99]
        self.assertEqual(pixelmagic.find_median(list3), 33)


    def test_denoise_image(self):
        list1 = [[245, 245, 245], [245, 245, 245], [253, 253, 253],
                [245, 245, 245], [10, 10, 10], [253, 253, 253],
                [100, 100, 100], [240, 240, 240], [70, 70, 70]]
        expected1 = [[245, 245, 245], [245, 245, 245], [253, 253, 253],
                [245, 245, 245], [245, 245, 245], [253, 253, 253],
                [245, 245, 245], [240, 240, 240], [245, 245, 245]]
        self.assertEqual(pixelmagic.denoise_image(list1,3,3), expected1)
        list2 = [[11, 11, 11], [24, 24, 24], [25, 25, 25], [25, 25, 25],
                [25, 25, 25], [26, 26, 26], [6, 6, 6], [27, 27, 27],
                [17, 17, 17]]
        expected2 = [[25, 25, 25], [24, 24, 24], [25, 25, 25], [25, 25, 25],
                [25, 25, 25], [26, 26, 26], [25, 25, 25], [27, 27, 27],
                [25, 25, 25]]
        self.assertEqual(pixelmagic.denoise_image(list2,3,3,2,0.1), expected2)
        list3 = [[50, 50, 50], [50, 50, 50], [49, 49, 49], [51, 51, 51],
                [50, 50, 50], [19, 19, 19], [45, 45, 45], [40, 40, 40],
                [30, 30, 30]]
        expected3 = [[50, 50, 50], [50, 50, 50], [49, 49, 49], [51, 51, 51],
                [50, 50, 50], [49, 49, 49], [50, 50, 50], [45, 45, 45],
                [40, 40, 40]]
        self.assertEqual(pixelmagic.denoise_image(list3,3,3,1,0.1), expected3)


if __name__ == '__main__':
    unittest.main()
