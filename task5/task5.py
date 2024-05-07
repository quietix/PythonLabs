import pathlib


def task5():
    # creating dir
    dir_path = pathlib.Path("test_dir")
    dir_path.mkdir(exist_ok=True)
    print(f"Directory {dir_path} is created")

    # creating file inside the dir
    file_path = dir_path.joinpath("test_file.txt")
    file_path.touch(exist_ok=True)
    print(f"File {file_path} is created\n")

    with open(file_path.__fspath__(), "w+") as f:
        # writing into file
        f.write("Python")

        # reading from the file
        f.seek(0)
        file_text = f.read()
        print(file_text)

    file_path.unlink()
    print("\nFile path is removed")

    dir_path.rmdir()
    print("Directory is removed")


if __name__ == "__main__":
    task5()