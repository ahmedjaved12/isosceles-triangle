class IsoscelesTriangle:
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_height(self):
        """
        Calculate the height of the isosceles triangle.
        """
        height = (self.side_length ** 2 - (self.side_length / 2) ** 2) ** 0.5
        return height

    def calculate_area(self):
        """
        Calculate the area of the isosceles triangle.
        """
        height = self.calculate_height()
        area = 0.5 * self.side_length * height
        return area

    def calculate_perimeter(self):
        """
        Calculate the perimeter of the isosceles triangle.
        """
        perimeter = 2 * self.side_length + self.side_length
        return perimeter

    def calculate_angle(self):
        """
        Calculate the measure of each angle in the isosceles triangle.
        """
        angle = 180 - 2 * self.calculate_angle_base()
        return angle

    def calculate_angle_base(self):
        """
        Calculate the measure of the base angle in the isosceles triangle.
        """
        angle_base = 180 / 2
        return angle_base

# Example usage:
if __name__ == "__main__":
    side_length = 5
    triangle = IsoscelesTriangle(side_length)
    print("Height:", triangle.calculate_height())
    print("Area:", triangle.calculate_area())
    print("Perimeter:", triangle.calculate_perimeter())
    print("Angle:", triangle.calculate_angle())
    print("Angle of the base:", triangle.calculate_angle_base())
