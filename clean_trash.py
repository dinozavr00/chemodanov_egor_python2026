import os
import time
import argparse
from datetime import datetime

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--trash_folder_path', required=True)
    parser.add_argument('--age_thr', required=True, type=int)
    args = parser.parse_args()

    trash = args.trash_folder_path
    age_thr = args.age_thr

    while True:
        with open('clean_trash.log', 'a') as log:
            for root, dirs, files in os.walk(trash, topdown=False):
                for file in files:
                    full_path = os.path.join(root, file)
                    mtime = os.path.getmtime(full_path)
                    if time.time() - mtime > age_thr:
                        age = time.time() - mtime
                        os.remove(full_path)
                        log.write(f"{datetime.now()} |/| Возраст: {age:.0f} сек |/| Удалён файл: {full_path}\n")
                        log.flush()
                        print(f"{datetime.now()} |/| Возраст: {age:.0f} сек |/| Удалён файл: {full_path}\n")
                if root != trash:
                    os.rmdir(root)
                    log.write(f"{datetime.now()} |/| Удалена пустая папка: {root}\n")
                    log.flush()
                    print(f"{datetime.now()} |/| Удалена пустая папка: {root}")
        time.sleep(1)

if __name__ == '__main__':
    main()
