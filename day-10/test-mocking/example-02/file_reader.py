def read_first_line(filename):
    with open(filename, 'r') as file:
        return file.readline().strip()