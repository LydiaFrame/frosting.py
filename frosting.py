#!/usr/bin/env python3

"""Module to calculate how many tubs of frosting are needed for a cake."""

__author__ = 'Lydia Frame'
__date__ = '3/30/2025'

import math
import locale


def calculate_area(diameter, height, layers):
    """Calculate the total area of frosting needed for the cake.
    
    Args:
    diameter (float): diameter of the cake
    height (float): height of the cake
    layers (int): number of layers of the cake

    Returns:
    float: total area that needs to be covered by frosting
    """
    radius = diameter / 2
    area_per_layer = math.pi * (radius ** 2)  # Area of the top/bottom of the layer
    side_area = math.pi * diameter * height  # Side area (side wrapped around the cake)
    
    total_area = (area_per_layer * layers) + side_area
    return total_area


def main():
    """Main function to calculate and display the number of tubs and price for frosting."""
    # Prompt user for cake dimensions
    diameter = float(input('Diameter? '))
    print()  # Print a newline after input
    height = float(input('Height? '))
    print()  # Print a newline after input
    layers = int(input('Layers? '))
    print()  # Print a newline after input

    # Calculate total area
    total_area = calculate_area(diameter, height, layers)

    # Each tub covers 60 square inches
    coverage_per_tub = 60
    tubs_needed = math.ceil(total_area / coverage_per_tub)  # Round up to nearest tub

    # Each tub costs $1.25
    cost_per_tub = 1.25
    total_cost = tubs_needed * cost_per_tub

    # Set the locale to 'en_US.UTF-8' if the default locale is unsupported
    try:
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    except locale.Error:
        locale.setlocale(locale.LC_ALL, 'en_US')  # Fallback to en_US

    # Output the results
    print(f'Num tubs: {tubs_needed:5d}')
    print(f'Price: {locale.currency(total_cost, grouping=True):>8}')

if __name__ == '__main__':
    main()