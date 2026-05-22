def cleaner(file : str):
    cleaned_file_name = file.strip().lower().replace(" ","_")
    isValid = cleaned_file_name.endswith(".py")

    if not isValid : return print("The file is not valid")

    print(f"File name: {cleaned_file_name}")
    type_file = cleaned_file_name.split(".")[1]
    print(f"Type file: {type_file}")


if __name__ == "__main__":
    cleaner("  cLeAnER.pY")