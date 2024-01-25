def main():
    student_A_name = "Lan"# local variable
    student_A_math_score = 9
    student_A_literrature_score = 8
    
    student_B_name = "Thinh"
    student_B_math_score = 8
    student_B_litterrature_score = 6

    print_student(student_A_name, student_A_math_score, student_A_literrature_score)
    print_student(student_B_name, student_B_math_score, student_B_litterrature_score)

def print_student(name, math_score, literrature_score):
    print("Name: " + name)
    print("math: " + str(math_score))
    print("Liter: " + str(literrature_score))

#student_B_name = "Thinh" global variable 
main()