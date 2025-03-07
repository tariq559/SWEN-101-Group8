def has_double_letters(word):
    word = word.lower()  # Convert to lowercase for case insensitivity
    index = 0
    length = len(word) - 1
    
    while index < length:
        if word[index] == word[index + 1]:  # Check consecutive letters
            return True
        index += 1
    
    return False


def double_letter_word_count(sentence):
    words = sentence.split()  # Split sentence into words
    count = 0
    index = 0
    length = len(words)
    
    while index < length:
        if has_double_letters(words[index]):
            count += 1
        index += 1
    
    return count


# Example usage:
print(double_letter_word_count("Balloon"))  # Expected: 1
print(double_letter_word_count("Llamas eat grass"))  # Expected: 2
print(double_letter_word_count("No doubles"))  # Expected: 0


import arrays

def arrays_equal(array1, array2, index=0):
    if len(array1) != len(array2):  
        return False  # If lengths differ, arrays are not equal

    if index >= len(array1):  
        return True  # Base case: reached end of arrays, they are equal

    if array1[index] != array2[index]:  
        return False  # Mismatch found, return False

    return arrays_equal(array1, array2, index + 1)  # Recursive call




def digit_sum(digit_string):
    if digit_string == "":
        raise ValueError("Input string cannot be empty")
    
    if len(digit_string) == 1:
        return digit_string  # Base case: single-digit string
    
    total = 0
    index = 0
    length = len(digit_string)

    while index < length:
        total += int(digit_string[index])
        index += 1

    return digit_sum(str(total))  # Recursive call with summed digits


print(digit_sum("879"))  # Expected: "6"
print(digit_sum("24"))   # Expected: "6"
print(digit_sum("6"))    # Expected: "6"
print(digit_sum("9536187496829"))  # Expected: "5"


import csv

def count_sales(filename, year, platform, sales_threshold):
    try:
        file = open(filename, "r")  
    except:
        return -1  # Return -1 if file cannot be opened

    reader = csv.reader(file)
    next(reader)  # Skip the header row

    count = 0
    for row in reader:
        record_year = int(row[1])  # Assuming Year is at index 1
        record_platform = row[2]   # Assuming Platform is at index 2
        record_sales = float(row[4])  # Assuming Sales are at index 4

        if record_year == year and record_platform == platform and record_sales >= sales_threshold:
            count += 1

    file.close()
    return count


count_sales("data/video_game_sales_1990s.csv", 1993, "SNES", 0.8)  # Expected: 14
count_sales("data/video_game_sales_1980s.csv", 1980, "2600", 1.0)  # Expected: 4
count_sales("data/video_game_sales_1980s.csv", 1989, "GB", 99.9)   # Expected: 0