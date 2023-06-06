def count_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return len(lines)

def count_empty_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        empty_lines = [line for line in lines if line.strip() == '']
        return len(empty_lines)

def count_lines_with_z(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        lines_with_z = [line for line in lines if 'z' in line]
        return len(lines_with_z)

def count_z_occurrences(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        return content.count('z')

def count_lines_with_and(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        lines_with_and = [line for line in lines if 'and' in line]
        return len(lines_with_and)

def analyze_file(file_path):
    print(f"Statistics for file: {file_path}")
    print("1. Number of lines:", count_lines(file_path))
    print("2. Number of empty lines:", count_empty_lines(file_path))
    print("3. Number of lines with 'z':", count_lines_with_z(file_path))
    print("4. Number of occurrences of 'z':", count_z_occurrences(file_path))
    print("5. Number of lines with 'and':", count_lines_with_and(file_path))

def main():
    while True:
        file_path = input("Enter the path to the file (or 'q' to quit): ")
        if file_path == 'q':
            break
        analyze_file(file_path)

if __name__ == '__main__':
    main()
