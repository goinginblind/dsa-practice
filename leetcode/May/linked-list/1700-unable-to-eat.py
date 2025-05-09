from collections import deque 

def countStudents(students: list[int], sandwiches: list[int]) -> int:
    student_queue = deque(students)
    sandwiches_stack = deque(sandwiches)  # top is on the left
    counter = 0  # Tells us how many students were checked and no sandwich was taken

    while sandwiches_stack and counter < len(student_queue):
        if sandwiches_stack[0] == student_queue[0]:
            sandwiches_stack.popleft()
            student_queue.popleft()
            counter = 0

        else:
            student_queue.append(student_queue.popleft())
            counter += 1

    return len(student_queue)


def main():
    students = [1,1,0,0]
    sandwiches = [0,1,0,1]

    print(countStudents(students=students, sandwiches=sandwiches))


main()
