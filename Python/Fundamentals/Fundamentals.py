"""This script contains fundamental Python functions"""
import random

def generate_random_number(start:int, end:int) -> int:
    """Generates a random number between start and end (inclusive).
        args:
        start (int): The lower bound of the random number range.
        end (int): The upper bound of the random number range.
        returns:
        int: A random integer between start and end."""
    return random.randint(start, end)

def list_of_random_numbers(size:int, start:int, end:int) -> list:
    """Generates a list of random numbers.
        args:
        size (int): The number of random numbers to generate.
        start (int): The lower bound of the random number range.
        end (int): The upper bound of the random number range.
        returns:
        list: A list containing 'size' random integers between start and end."""
    try:
        if size <= 0:
            raise ValueError("Size must be a positive integer.")
        if start > end:
            raise ValueError("Start must be less than or equal to end.")
        return [generate_random_number(start, end) for _ in range(size)]
    except ValueError as e:
        print(f"Error: {e}")
        return []

def delete_duplicates(input_list:list) -> list:
    """Removes duplicates from a list.
        args:
        input_list (list): The list from which to remove duplicates.
        returns:
        list: A new list with duplicates removed."""
    return list(set(input_list))

def save_to_file(filename:str, data:list) -> None:
    """Saves a list to a file.
        args:
        filename (str): The name of the file to save the data to.
        data (list): The list of data to save."""
    with open(filename, 'w') as file:
        for item in data:
            file.write(f"{item}\n")

def main():
    """Main function to demonstrate the functionality."""
    random_numbers = list_of_random_numbers(20, 10, 1)
    print("Random Numbers:", random_numbers)

    unique_numbers = delete_duplicates(random_numbers)
    print("Unique Numbers:", unique_numbers)

    save_to_file('random_numbers.txt', unique_numbers)
    print("Unique numbers saved to 'random_numbers.txt'.")

if __name__ == "__main__":
    main()