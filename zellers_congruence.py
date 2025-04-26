class DateCalculator:
    def __init__(self, year: int, month: int, day: int):
        """
        Initialize the DateCalculator with year, month, and day.
        Adjust the month and year for January and February.
        """
        if month < 3:  # January and February are treated as months 13 and 14 of the previous year
            self.year = year - 1
            self.month = month + 12
        else:
            self.year = year
            self.month = month
        self.day = day

    def calculate_day_of_week(self) -> str:
        """
        Calculate the day of the week using Zeller's Congruence formula.
        Returns the name of the day.
        """
        q = self.day
        m = self.month
        Y = self.year
        K = Y % 100  # Year of the century
        J = Y // 100  # Zero-based century

        # Zeller's Congruence formula
        h = (q + (13 * (m + 1)) // 5 + K + (K // 4) + (J // 4) + (5 * J)) % 7

        # Map the result to the corresponding day of the week
        days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        return days[h]

# Example usage
if __name__ == "__main__":
    # Example: What day of the week was September 15, 1589?
    calculator = DateCalculator(1589, 9, 15)
    day_of_week = calculator.calculate_day_of_week()
    print(f"The day of the week for September 15, 1589, was {day_of_week}.")