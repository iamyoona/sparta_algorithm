all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


def get_absent_student(all_array, present_array):
    absent_student = []
    for name in all_array:
        if name not in present_array:
            absent_student.append(name)
    return absent_student


print(get_absent_student(all_students, present_students))