"""Functions to help Azara and Rui locate pirate treasure."""
import sys


def print_python_version():
    """Function printing python version."""
    print(sys.version)

def get_coordinate(record):
    return record[1]


def convert_coordinate(coordinate):
    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    azara_coordinate = convert_coordinate(get_coordinate(azara_record))
    rui_coordinate = rui_record[1]

    return azara_coordinate == rui_coordinate


def create_record(azara_record, rui_record):
    if compare_records(azara_record, rui_record):
        return (
            azara_record[0],
            azara_record[1],
            rui_record[0],
            rui_record[1],
            rui_record[2]
        )

    return "not a match"


def clean_up(combined_data):
    """Clean up the combined data."""
    result = ""

    for item in combined_data:
        name, _, location, coordinates, color = item
        result += f"{(name, location, coordinates, color)}\n"

    return result