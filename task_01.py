#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Temp Conversion."""


import decimal


ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


def fahrenheit_to_celsius(degrees):
    """
    This will change degrees in fahrenheit to celsius.

    Args:
        degrees (int): The degress to be changed to celsius.

    Returns:
        int: in celcius.

    Examples:

        >>> fahrenheit_to_celsius(212)
        Decimal('100')

        >>> fahrenheit_to_celsius(200)
        Decimal('100')

        """
    celsius = (((decimal.Decimal(degrees) - 32) * 5) / 9)
    return celsius


def celsius_to_kelvin(degrees):
    """
    This will convert # of degrees in celsius to kelvin.

    Args:
        degrees (int): the # of degrees.

    Returns:
        int: Conversion.

    Examples:
        >>> celsius_to_kelvin(100)
        Decimal('373.15')

        >>> celsius_to_kelvin(200)
        Decimal('473.15')

        """
    kelvin = (decimal.Decimal(degrees + ABSOLUTE_DIFFERENCE))
    return kelvin


def fahrenheit_to_kelvin(degrees):
    """
    This will convert degrees in fahrenheit to kelvin.

    Args:
        degrees (int): # of degrees to be converted.

    Returns:
        int: degrees in kelvin.

    Examples:

        >>> farenheit_to_kelvin(212)
        Decimal('373.15')

        >>> farenheit_to_kelvin(41)
        Decimal('230.09')

    """
    kelvin = (fahrenheit_to_celsius(degrees) + celsius_to_kelvin(degrees)
              - degrees)
    return kelvin
