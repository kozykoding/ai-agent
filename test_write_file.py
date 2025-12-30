from functions.write_file import write_file

if __name__ == "__main__":
    result_lorem = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print("lorem.txt result:")
    print(f"  {result_lorem}")
    result_main = write_file(
        "calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"
    )
    print("pkg/morelorem.txt result:")
    print(f"  {result_main}")
    result_pkg = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print("/tmp/temp.txt result:")
    print(f"  {result_pkg}")
