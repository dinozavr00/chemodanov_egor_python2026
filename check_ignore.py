import os
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--project_dir', required=True)
    args = parser.parse_args()
    
    ex_suf = []
    ex_paths = []

    gitignore_path = os.path.join(args.project_dir, ".gitignore")

    if not os.path.exists(gitignore_path):
        print(".gitignore not found :(")
        return 0

    with open(gitignore_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip()
            if line.startswith('*') and line[1:] != '':
                ex_suf.append(line[1:])
            else:
                ex_paths.append(line)

    root_name = os.path.basename(os.path.abspath(args.project_dir))
    ignored = []


    for root, dirs, files in os.walk(args.project_dir):
        for file in files:
            if (file == ".gitignore"): 
                    continue                
            full_path = os.path.join(root, file)                        ###получим полный путь
            rel_path = os.path.relpath(full_path, args.project_dir)     ###обережм до искомой директории
            rel_path = rel_path.replace(os.sep, '/')                    ###для разных осей

            if rel_path in ex_paths:
                ignored.append(f"{root_name}/{rel_path} ignored by expression {rel_path}")
            else:
                for suf in ex_suf:
                    if file.endswith(suf):
                        ignored.append(f"{root_name}/{rel_path} ignored by expression *{suf}")
                        break

    if ignored:
        print("Ignored files:")
        for el in ignored:
            print(el)
    else:
        print("No ignored files")

if __name__ == '__main__':
    main()
