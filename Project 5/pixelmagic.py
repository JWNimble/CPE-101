"""
Project 5

CPE101
Spring 2021
Author: Jack Forrester
"""


import sys
import copy


def make_pixel_list(pixel_data):
    """Converts a list of strings into a list of integers
    Args:
        pixel_data (list): a list of strings
    Returns:
        pixel_list (list): a list of integers
    """

    pixel_list = []
    for line in pixel_data:
        line_list = line.strip().split()
        pixel = []
        for color_val in line_list:
            pixel.append(int(color_val))
        pixel_list.append(pixel)
    return pixel_list


def write_file(new_file, pixel_list, header):
    """Helper function for writing .ppm files of the filtered image
    Args:
        new_file (str): the name of the output file
        pixel_list (list): a list of filtered pixel values
        header (list): info containing the image width height and max RGB value
    """

    with open(new_file, 'w') as name:
        width = int(header[0][0])
        height = int(header[0][1])
        max_color_val = int(header[1][0])
        name.write('P3\n')
        name.write(f"{width} {height}\n")
        name.write(f"{max_color_val}\n")
        for pixel in pixel_list:
            red = pixel[0]
            green = pixel [1]
            blue = pixel[2]
            name.write(f"{red} {green} {blue}\n")


def find_image(pixels, max_color_val):
    """Returns decoded pixels. Corresponds to the filter mode 'decode'.
    Args:
        pixels (list): A list of lists, each with containing 3 values for
        RGB designation.
        max_color_val (int): max RGB value of pixels
    Returns:
        list: An updated pixel list with the decode filter applied.
    """

    for pixel in pixels:
        pixel[0] = pixel[0] * 10
        if pixel[0] > max_color_val:
            pixel[0] = max_color_val
        pixel[1] = pixel[0]
        pixel[2] = pixel[0]


def fade_image(pixels, width, row, col, radius, max_color_val):
    """Returns faded pixels. Corresponds to the filter mode 'fade'.
    Args:
        pixels (list): A list of lists, each with containing 3 values for
        RGB designation.
        width (int): An integer value for the width of the image in pixels.
        row (int): The y-value for the center of the fade.
        col (int): The x-value for the center of the fade.
        radius (int): The radius of the region to be faded.
        max_color_val (int): max RGB value of pixels
    Returns:
        list: An updated pixel list with the fade filter applied.
    """

    for num, pixel in enumerate(pixels):
        pxlcol = num % int(width)
        pxlrow = num // int(width)
        dist = (((int(col) - pxlcol) ** 2) + ((int(row) - pxlrow) ** 2)) ** 0.5
        scale = (int(radius) - dist) / int(radius)
        if scale < 0.2:
            scale = 0.2
        for pxlnum, color_val in enumerate(pixel):
            pixel[pxlnum] = int(color_val * scale)
            if pixel[pxlnum] > max_color_val:
                pixel[pxlnum] = max_color_val
            if pixel[pxlnum] < 0:
                pixel[pxlnum] = 0


def make_3d_list(pixels, width):
    """Separates a list of pixels into a list of lists containing the pixels in
    reach row of the image
    Args:
        pixels (list): A list of lists, each with containing 3 values for
        RGB designation.
        width (int): the width of the image
    Returns:
        pxl_3d_list (list): A list of lists of lists containg the pixels in each
        row of the image
    """

    real_index = 0
    index = 0
    pxl_3d_list = []
    row = []
    for pixel in pixels:
        index += 1
        real_index += 1
        if index <= width:
            if real_index == len(pixels):
                row.append(pixel)
                pxl_3d_list.append(row)
            else:
                row.append(pixel)
        else:
            pxl_3d_list.append(row)
            row = [pixel]
            index = 1
    return pxl_3d_list


def find_neighbors(pixels, row, col, reach):
    """Finds the neighbors of a given pixel for a given radius and creates a
    list of the pixel and its neighbors color values
    Args:
        pixels (list): A list of lists, each with containing 3 values for
        RGB designation.
        row (int): the row the primary pixel occupies
        col (int): the column the primary pixel occupies
        reach (int): the radius of neighbors to be accounted for
    Returns:
        neighbors_list (list): a list of color values for the primary pixel and
        its neighboring pixels
    """

    neighbors_list = []
    for pxlcol in range((col - reach), (col + reach + 1)):
        for pxlrow in range((row - reach), (row + reach + 1)):
            if pxlrow >= 0 and pxlrow < len(pixels) and\
                    pxlcol >= 0 and pxlcol < len(pixels[0]):
                        neighbors_list.append(pixels[pxlrow][pxlcol][0])
    return neighbors_list


def sort_list(pixels):
    """Sorts a list of integers using an insertion sort method
    Args:
        pixels (list): a list of integers representing the color values of the
        primary pixel and its neighboring pixels
    Returns:
        list: a list of sorted integers
    """

    size = len(pixels)
    for row in range(1, size):
        col = row
        while col > 0 and pixels[col-1] > pixels[col]:
            pixels[col-1], pixels[col] = pixels[col], pixels[col-1]
            col -= 1


def find_median(sorted_list):
    """Find the median of a sorted list of integers
    Args:
        sorted_list (list): a sorted list of integers
    Returns:
       median (int): the median value
    """

    list_len = len(sorted_list)
    median = sorted_list[list_len//2]
    return median


def denoise_image(pixels, width, height, reach = 2, beta = 0.2):
    """Returns denoised pixels. Corresponds to the filter mode 'denoise'.
    Args:i
        pixels (list): A list of lists, each with containing 3 values for RGB
        designation.
        width (int): An integer value for the width of the image in pixels.
        height (int): An integer value for the height of the image in pixels.
        reach (int): An integer value for the size of the denoise window.
        beta (float): A value to reference in determining if a pixel needs to
        be replaced.
    Returns:
        denoised (list): A list with the denoised filter applied
    """

    new_pixels = copy.deepcopy(pixels)
    pxl_3d_list = make_3d_list(pixels, width)
    denoised = []
    for index, pixel in enumerate(new_pixels):
        pxlcol = index % int(width)
        pxlrow = index // int(width)
        neighbors_list = find_neighbors(pxl_3d_list, pxlrow, pxlcol, reach)
        sort_list(neighbors_list)
        med = find_median(neighbors_list)
        if (abs(int(pixel[0]) - med)/(int(pixel[0]) + 0.1)) > beta:
            pixel = [med, med, med]
            denoised.append(pixel)
        else:
            denoised.append(pixel)
    return denoised


def main():
    """Interpreting commandline arguments and executes a filters accordingly
    to produce a new ppm file in which the requested filter has been applied
    to a given file
    """

    args = sys.argv
    if len(args) < 3 or len(args) > 6:
        print('Usage: python3 pixelmagic.py <mode> <image>')
    if 'decode' in args or 'fade' in args or 'denoise' in args:
        try:
            with open(args[2], 'r') as image:
                pixel_data = image.readlines()
        except FileNotFoundError:
            print('Error: Unable to Open', args[2])
        else:
            try:
                pixel_data.remove(pixel_data[0])
                pixel_list = make_pixel_list(pixel_data)
                header = pixel_list[:2]
                pixel_list.remove(pixel_list[0])
                pixel_list.remove(pixel_list[0])
                width = int(header[0][0])
                height = int(header[0][1])
                max_color_val = int(header[1][0])
                if 'decode' in args:
                    if len(args) != 3:
                        print('Usage: python3 pixelmagic.py decode <image>')
                    find_image(pixel_list, max_color_val)
                    write_file('decoded.ppm', pixel_list, header)
                if 'fade' in args:
                    if len(args) != 6:
                        print('Usage: python3 pixelmagic.py fade <image>' +
                                ' <row> <col> <radius>')
                    fade_image(pixel_list, width, int(args[3]), int(args[4]),
                            int(args[5]), max_color_val)
                    write_file('faded.ppm', pixel_list, header)
                if 'denoise' in args:
                    if len(args) == 3:
                        denoised_list = denoise_image(pixel_list, width, height)
                    elif len(args) == 5:
                        denoised_list = denoise_image(pixel_list, width, height,
                            int(args[3]), float(args[4]))
                    else:
                        print('Usage: python3 pixelmagic.py denoise <image>' +
                            ' <reach> <beta>')
                    write_file('denoised.ppm', denoised_list, header)
            except:
                print('An Error has Occurred')
    else:
        print('Error: Invalid Mode')


if __name__ == '__main__':
    main()
