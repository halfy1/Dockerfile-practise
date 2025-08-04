import os
import sys

DATA_PATH = os.getenv("DATA_PATH", "/opt/data")

def main():
    # Пример: просто напечатать список файлов в DATA_PATH
    print(f"Files in {DATA_PATH}:")
    for root, dirs, files in os.walk(DATA_PATH):
        for f in files:
            print(os.path.join(root, f))

if __name__ == "__main__":
    main()