import sys

def find_pairs(numbers):
    pairs = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == 10:
                pairs.append((numbers[i], numbers[j]))
    return pairs

if __name__ == '__main__':
    if len(sys.argv) > 1:
        numbers = [int(num) for num in sys.argv[1:]]
        pairs = find_pairs(numbers)
        for pair in pairs:
            print(f"{pair[0]} + {pair[1]}")
    else:
        print("Usage: python pairs.py <numbers>")
