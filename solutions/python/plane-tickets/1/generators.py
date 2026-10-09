"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats."""
    letters = "ABCD"

    for index in range(number):
        yield letters[index % 4]


def generate_seats(number):
    """Generate a series of identifiers for airline seats."""
    for index, letter in enumerate(generate_seat_letters(number)):
        row = index // 4 + 1

        # There is no row 13.
        if row >= 13:
            row += 1

        yield f"{row}{letter}"


def assign_seats(passengers):
    """Assign seats to passengers."""
    seats = generate_seats(len(passengers))

    return dict(zip(passengers, seats))


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket."""
    for seat_number in seat_numbers:
        ticket_code = seat_number + flight_id
        ticket_code += "0" * (12 - len(ticket_code))
        yield ticket_code