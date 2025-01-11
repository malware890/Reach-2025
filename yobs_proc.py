from csv import reader, writer


def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        j = i
        while j and arr[j] > arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


def selection_sort(arr: list):
    for i in range(len(arr) - 1):
        maxi = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[maxi]:
                maxi = j
        arr[i], arr[maxi] = arr[maxi], arr[i]


def merge_sort(arr: list):
    if len(arr) > 1:
        mid = len(arr) // 2

        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] > right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def quick_sort(arr: list):
    def partition(a, low, high):
        pivot = a[high]
        i = low - 1

        for j in range(low, high):
            if a[j] > pivot:
                i += 1
                a[i], a[j] = a[j], a[i]

        a[i + 1], a[high] = a[high], a[i + 1]
        return i + 1

    def sort(a, low, high):
        if low < high:
            partition_index = partition(a, low, high)
            sort(a, low, partition_index - 1)
            sort(a, partition_index + 1, high)

    sort(arr, 0, len(arr) - 1)


def heap_sort(arr: list):
    def heapify(a, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and a[left] < a[largest]:
            largest = left

        if right < n and a[right] < a[largest]:
            largest = right

        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            heapify(a, n, largest)

    def sort(a):
        n = len(a)

        for i in range(n // 2 - 1, -1, -1):
            heapify(a, n, i)

        for i in range(n - 1, 0, -1):
            a[i], a[0] = a[0], a[i]
            heapify(a, i, 0)

    sort(arr)


class AlphaToNumeric:
    atoi = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26
}

    def __init__(self, alpha, sex, count):
        self.alpha = alpha.lower()
        self.sex = sex
        self.count = count
        self.numeric = []
        for letter in self.alpha:
            self.numeric.append(AlphaToNumeric.atoi[letter])

    def __gt__(self, other):
        short = len(self) if len(self) < len(other) else len(other)

        for i in range(short):
            if self.numeric[i] < other.numeric[i]:
                return True
            elif self.numeric[i] > other.numeric[i]:
                return False

        return True if len(self) == short else False

    def __lt__(self, other):
        short = len(self) if len(self) < len(other) else len(other)

        for i in range(short):
            if self.numeric[i] > other.numeric[i]:
                return True
            elif self.numeric[i] < other.numeric[i]:
                return False

        return False if len(self) == short else True

    def __len__(self):
        return len(self.alpha)

    def __repr__(self):
        return self.alpha


def yob_process(write_yob, read_yob, sort):
    r = reader(read_yob)
    lines = []
    for row in r:
        lines.append(AlphaToNumeric(row[0].lower(), row[1], row[2]))

    sort(lines)

    w = writer(write_yob, lineterminator='\n')
    for line in lines:
        w.writerow([line.alpha.capitalize(), line.sex, str(line.count)])

