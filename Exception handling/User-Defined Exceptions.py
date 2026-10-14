class InvalidRollNumberError(Exception):
    def __init__(self, roll_number, message="Roll number must be between 1 and 100"):
        self.roll_number = roll_number
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}. Provided roll number: {self.roll_number}"


def set_roll_number(roll_number):
    if roll_number < 1 or roll_number > 100:
        raise InvalidRollNumberError(roll_number)
    print(f"Roll number is set to {roll_number}")


try:
    set_roll_number(150)
except InvalidRollNumberError as e:
    print(f"Invalid roll number: {e.roll_number}. {e.message}")