"""
Your task is to complete the implementation of a simple "Student Manager" application
for a university.
This programme allows to keep track of a student academic progress, i.e., doing exams, calculate GPA etc.

The Student Manager is implemented as a "class", that is, using the "object-oriented" paradigm.
You should be already familiar with the concept of class and objects in object-oriented programming.
If not, please refer to Chapter 2 of the GTG book.
"""

class Student:

    POINTS = {'A+': 4.3, 'A0': 4.0, 'A-': 3.7, 'B+': 3.3, 'B0': 3.0, 'B-': 2.7, 'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
              'D0': 1.0}

    def __init__(self, student_name, student_id):
        """
        This is the "costructor" of the class, it is invoked avery time a new object of this class is created
        :param student_name: the name of student (a string)
        :param student_id:  the id of the student (a string)
        """
        # use the following dictionary to store the letter grades of courses that the student has passed,
        # e.g., self._grades = {"APME" : "A0, "Math": "B+"}; self_grades["APME"]="A0"
        self._grades = {}
        self._student_id = student_id
        self._student_name = student_name

    def get_student_name(self):
        """ Returns the name of the student """
        return self._student_name

    def get_student_id(self):
        """ Returns the id of the student """
        return self._student_id


    def get_gpa(self):
        """ returns the GPA of the student """
        # this function should calculate the GPA and print it.
        # HINT: for each course in self._grades, you need to retrieve the corresponding points from Student.POINTS
        # (and then calculate the GPA)
        # COMPLETE THE IMPLEMENTATION
        sum = 0

        """
        This dictionary is the same for all students, it maps letter grades onto the corresponding numerical grades
        """


        for i in self._grades:
                sum += self.POINTS[ self._grades[i]]
        return sum/len(self._grades)


    def add_grade(self,course_name,letter):
        """
        This functions adds a new grade, that is, it registers the fact that the student has
        passed the exam 'course_name' with the grade 'letter'
        """
        # You should improve this function by checking that the letter grade entered is correct.
        # Note that, for instance, 'Good', 'AB', 'AB+' or 'D-' are not allowed as letter grades
        # (only letter grades in the dictionary POINTS are allowed)
        # COMPLETE THE IMPLEMENTATION
        if letter in self.POINTS.keys():
            self._grades[course_name] = letter
        else:
            print("Unexpected grade input{0}".format(letter))
            return

    def print_grades(self):
        """
        This function should print the list of courses with the respective letter grades achieved by a student
        """
        # COMPLETE THE IMPLEMETATION BELOW
        for i in self._grades:
            print("{0} : {1}".format(i,self._grades[i]))



# =======================  END OF class definition

""" main to test the implementation"""
if __name__ == '__main__':
    # Run this test to check the correctness of your implementation

    mc = Student("Marco Comuzzi","112233")

    mc.add_grade("APME","A+")
    mc.add_grade("Math101", "A-")
    mc.add_grade("Italian101","B0")
    mc.add_grade("Italian101","AS")

    print("{0} GPA is: {1}".format(mc.get_student_name(), mc.get_gpa()))

    mc.print_grades()

    # BONUS: Can you extend this test to test for unexpected letter grades?