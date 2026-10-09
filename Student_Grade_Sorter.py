def student_grade_sorter(student, grade):
    """ Sort students based on their grades in ascending order.
     
        Args:
            student (list ) : A list of student names
            grade (list) : A list of corresponding grades for the students

        Returns: A list of tuples containing the student names and their grades in sorted order.

    """

    # Check if student and grade lists are of the same length.
    if len(student) != len(grade):
        raise ValueError("The length of student and grade list must be the same.")

    for i in range(len(student)):
        