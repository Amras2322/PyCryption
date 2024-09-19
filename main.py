import subprocess

def run_script(script_name):
    """Run a script with the given name"""
    try:
        subprocess.run(['python', script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    print("Text Encrypter/Decrypter")
    print("------------------------")

    while True:
        print("\nOptions:")
        print("1. Encrypt text")
        print("2. Decrypt text")
        print("3. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            run_script('encrypt.py')
        elif choice == "2":
            run_script('decrypt.py')
        elif choice == "3":
            break
        else:
            print("Invalid option. Please choose again.")
