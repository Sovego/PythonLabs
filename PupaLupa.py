def read_matrix(file_name):
    """Matrix read from file"""
    strs_1 = []
    with open(file_name, "r") as file:
        s = ''
        while s != '\n':
            s = file.readline()
            if s == '\n':
                break
            strs_1.append(s)
    first_matrix = [list(map(int, row.split())) for row in strs_1]
    return first_matrix


class Pupa:
    def __init__(self):
        self._work_count = 0
        self._second_matrix = None
        self._first_matrix = None
        self._salary = 0

    def do_work(self, filename1, filename2):
        self._first_matrix = read_matrix(filename1)
        self._second_matrix = read_matrix(filename2)
        result = [[self._first_matrix[i][j] + self._second_matrix[i][j] for j in range(len(self._first_matrix[0]))] for
                  i in range(len(self._first_matrix))]
        for r in result:
            print(r)
        self._work_count += 1

    def take_salary(self, count):
        self._salary += count

    @property
    def get_work_count(self):
        return self._work_count


class Lupa:
    def __init__(self):
        self._work_count = 0
        self._salary = 0
        self._second_matrix = None
        self._first_matrix = None

    def do_work(self, filename1, filename2):
        self._first_matrix = read_matrix(filename1)
        self._second_matrix = read_matrix(filename2)
        result = [[self._first_matrix[i][j] - self._second_matrix[i][j] for j in range(len(self._first_matrix[0]))] for
                  i in range(len(self._first_matrix))]
        for r in result:
            print(r)
        self._work_count += 1

    def take_salary(self, count):
        self._salary += count

    @property
    def get_work_count(self):
        return self._work_count


class Accountant:
    def __init__(self):
        self._rate = 100

    def give_salary(self, worker):
        worker.take_salary(self._rate*worker.get_work_count())
