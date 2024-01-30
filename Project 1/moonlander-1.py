"""
CPE101
Spring 2021
Author: Jack Forrester
"""


class Moonlander:
    """Moonlander
    Attributes:
        altitude (float): the distance from the surface of the moon
        fuel (int): the fuel
        velocity (float): It is positive when the Moonlander is moving away
                          from the moon
        acceleration (float): It is positive when the Moonlander is moving away
                              from the moon
    """

    def __init__(self, alt, fuel):
        """The initiaizer for a moonlander object
        Args:
            alt (float) = altitude
            fuel (int) = fuel
        """

        self.altitude = alt
        self.fuel = fuel
        self.velocity = 0
        self.acceleration = 0


def show_welcome():
    """Displays a welcome message
    """

    return print("Welcome to the Moon Lander Simulation!")


def get_fuel():
    """Prompts the user to enter an integer and checks if it is positive
    Args:
        fuel (int) = the initial ammount of fuel in the lunar lander
    Returns:
        An error message if the entered fuel ammount in not positive,
        otherwise the initial fuel amount
    """

    while True:
        fuel = int(input("Please enter initial fuel amount [a positive number]: "))
        if fuel > 0:
            break
        print(fuel, "is not a positive number!")
    return fuel


def get_altitude():
    """Prompts the user for an integer and check if it is within the interval
    [1, 9999]
    Args:
        altitude (int): the initial altitude
    Returns:
        an error message if not within the interval [1, 9999],
        otherwise the initial altitude
    """

    while True:
        altitude = int(input("Please enter initial altitude [1, 9999]: "))
        if 1 <= altitude <= 9999:
            break
        print(altitude, "is not a value between 1 and 9999!")
    return altitude


def display_state(time:int, altitude:float, velocity:float, fuel:int, fuel_rate:int):
    """Displays the state of the lunar module as indicated by the parameters
    Args:
        time (int): the time
        altitude (float): the current altitude
        velocity (float): the current velocity
        fuel (int): the current amount of fuel in the lunar lander
        fuel_rate (int): the current fuel rate
    Returns:
        a display of the given values in a certain format
    """

    return print(("time={t}, altitude={alt}, velocity={v}, fuel={f}," +
        " fuel rate={fr}").format(t=time, alt=altitude, v=velocity, f=fuel, fr=fuel_rate))


def get_fuel_rate(fuel):
    """Prompts the user to enter an integer and checks if it is within the
    interval [0, 9] and is less than or more than the amount of fuel
    remaining on the lunar lander
    Args:
        fuel (int): the ammount of fuel remaining
        fuel_rate (int): the fuel rate
    Returns:
        An error message if fuel rate is not within interval [0, 9],
        otherwise the lesser of the fuel rate and fuel remaining
    """

    while True:
        fuel_rate = int(input("Please enter fuel rate [0, 9]: "))
        if 0 <= fuel_rate <= 9:
            break
        print(fuel_rate, "is not a value between 0 and 9!")
    return min(fuel_rate, fuel)


def display_landing_status(velocity:float):
    """Displays the status of the lunar module upon landing
    Args:
        velocity (float): the final velocity of the lunar lander
    Returns:
        the result - safe, damaged, or death
    """

    if -1 <= velocity <= 0:
        print("Status at landing - The eagle has landed!")
    elif -10 < velocity < -1:
        print("Status at landing - Enjoy your oxygen while it lasts!")
    else:
        print("Status at landing - Ouch - that hurt!")


def update_acceleration(gravity, fuel_rate):
    """Finds the new acceleration based on provided inputs
    Args:
        gravity: the moon's gravitational force
        fuel_rate: the current fuel rate
    Raturns:
        the new acceleration
    Examples:
        >>> update_acceleration(1.62, 0)
        -1.62
        >>> update_acceleration(1.62, 5)
        0.0
        >>> update_acceleration(1.62, 9)
        1.2960000000000003
    """

    return gravity * ((fuel_rate / 5) - 1)


def update_altitude(altitude, velocity, acceleration):
    """Finds the new altitude based on provided inputs
    Args:
        altitude: the previous altitude
        velocity: the previous velocity
        acceleration: the current acceleration
    Returns:
        anew: the new altitude
    Examples:
        >>> update_altitude(10, -1, -1.62)
        8.19
        >>> update_altitude(8.19, -2.62, 0)
        5.57
        >>> update_altitude(5.57, -2.62, 1.296)
        3.6
    """

    anew = altitude + velocity + (acceleration / 2)
    return round(anew, 2)


def update_velocity(velocity, acceleration):
    """Finds the new velocity based on provided inputs
    Args:
        velocity: the previous velocity
        acceleration: the current acceleration
    Returns:
        vnew: the new velocity
    Examples:
        >>> update_velocity(-1, -1.62)
        -2.62
        >>> update_velocity(-2.62, 0)
        -2.62
        >>> update_velocity(-2.62, 1.296)
        -1.32
    """

    vnew = velocity + acceleration
    return round(vnew, 2)


def update_fuel(fuel, fuel_rate):
    """Finds the new remaining amount of fuel based on provided inputs
    Args:
        fuel: the previous amount of fuel remaining in the lunar lander
        fuel_rate: the current fuel rate
    Returns:
        fnew: the current amount of fuel remaining in the lunar lander
    Examples:
        >>> update_fuel(20, 0)
        20
        >>> update_fuel(20, 5)
        15
        >>> update_fuel(15, 9)
        6
    """

    fnew = fuel - fuel_rate
    return round(fnew, 2)


def main():
    """Simulates the advancement of the LM from time period 0 to landing
    """

    show_welcome()
    alt = get_altitude()
    fuel = get_fuel()
    mlndr = Moonlander(alt, fuel)
    display_state(0, alt, 0, fuel, 0)
    time = 0
    while mlndr.altitude >= 0:
        if mlndr.fuel > 0:
            fuel_rate = get_fuel_rate(mlndr.fuel)
        else:
            fuel_rate = 0
        mlndr.acceleration = update_acceleration(1.62, fuel_rate)
        mlndr.fuel = update_fuel(mlndr.fuel, fuel_rate)
        mlndr.altitude = update_altitude(mlndr.altitude, mlndr.velocity, mlndr.acceleration)
        mlndr.velocity = update_velocity(mlndr.velocity, mlndr.acceleration)
        time += 1
        if mlndr.altitude < 0:
            break
        display_state(time, mlndr.altitude, mlndr.velocity, mlndr.fuel, fuel_rate)
    display_state(time, 0, mlndr.velocity, mlndr.fuel, fuel_rate)
    display_landing_status(mlndr.velocity)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
