"""
Your task is to extend the implementation of the Student Manager class of Week 03
First, you should cut and paste where indicated your implementation of Week 03,
then you should complete the implementatin of the additional functions
"""

#=================== CUT & PASTE your implementation of week 02 ================================================================
#===============================================================================================================================

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

# =============================================== END CUT AND PASTE ======================================================================
#=======================================================================================================================================================

# New methods to implement
    def update_grade(self, course_name, letter):
        """
        This method should check if a letter grade is already registered for a course
        if the a grade is already registered, then the letter grade is updated
        otherwise an error message is returned to the user, something like: "Grade not registered for course_name"
        :param course_name: the name of the course to be updated
        :param letter: the new letter grade
        """
        if course_name in self._grades :
            self._grades[course_name] = letter
        else:
            print("Grade not registered for {0}".format(course_name));
            return False

    def get_strange_gpa(self):
        """
        this method calculates a "strange" GPA by multiplying the points value of all the grades currently registered for a student
        For example, if the following grades are registered: "ADSA":A0, "Math": B0
        then the GPA returned will be 4.0 * 3.0 = 12.0
        You should try to implement this function RECURSIVELY
        """
        strange_gpa = 1.0

        for i in self._grades:
            strange_gpa = strange_gpa * self.POINTS[self._grades[i]]

        return strange_gpa




    def get_count_of_above_bplus(self):
        """
        This function should return the number of courses passed by a student with a grade equal to or greater than B+
        """
        above_number = 0
        for i in self._grades:
            if self.POINTS[self._grades[i]] >= self.POINTS["B+"]:
                above_number = above_number + 1
        return above_number


if __name__ == '__main__':
    # Run this test to check the correctness of your implementation
    """
    def strange_gpa(l):
        if len(l) == 1:
            return l[0]
        else:
            print("calling...")
            print(l[1:])
            return l[0] * strange_gpa(l[1:])

    l = [3, 8, 9, 2]
    print(strange_gpa(l))
    """



    mc = Student("Marco Comuzzi","112233")
    mc.add_grade("ADSA","A+")
    mc.add_grade("Math101", "B-")
    mc.add_grade("Italian101","B0")
    mc.add_grade("Italian101","B+")

    print("{0} GPA is: {1}".format(mc.get_student_name(), mc.get_gpa()))

    mc.print_grades()

    print("========================")
    print("WEEK 03 TESTS ==========")
    print("========================")

    mc.update_grade("Korean101","C0")
    mc.update_grade("Italian101","A+")
    print()
    print("{0}'s strange GPA is: {1}".format(mc.get_student_name(), mc.get_strange_gpa()))
    print("{0}'s number of courses with B+ or above is: {1}".format(mc.get_student_name(), mc.get_count_of_above_bplus()))
