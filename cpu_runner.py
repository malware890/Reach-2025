from sys import argv
import cpu_bound.cpu_bound

if __name__ == "__main__":
    cpu_bound.cpu_bound.get_cpu(argv[1])
