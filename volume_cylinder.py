#!/usr/bin/env python3

# Created by: Teddy Sannan
# Created on: November 2019
# This program shows the volume of a cylinder

import math


def volume(radius, height):
    # calculates volume
    volume = math.pi * radius ** 2 * height

    return volume


def main():
    # calls other functions
    while True:

        radius_from_user = input("Enter the radius of the cylinder (cm): ")
        height_from_user = input("Enter the height of the cylinder (cm): ")

        try:
            radius_from_user_number = int(radius_from_user)
            height_from_user_number = int(height_from_user)

            if radius_from_user_number < 0 and height_from_user_number < 0:
                print("Not a valid Number")
                print("")

            else:
                volume_of_cylinder = volume(height=height_from_user_number,
                                            radius=radius_from_user_number)

                print("the volume is {0}".format(volume_of_cylinder))
                break

        except(ValueError):
            print("Not a valid number inputted")


if __name__ == "__main__":
    main()
