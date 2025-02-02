# 4/4 -- >1,2,3,4
#function
def open_file(file):
    with open(file, 'r') as file:
            content = file.read()
    return content

#1. Write a Python program to read a text file and count the occurrences of each word.
def count_word_occurrences(file):
    try:
        text = open_file(file)
        words = text.lower().split()
        word_count = {}
        for word in words:
            word = word.strip('.,!?()[]{}":;')  
            if word:
                word_count[word] = word_count.get(word, 0) + 1
        return word_count
    except FileNotFoundError:
        return "The file was not found."
file = 'C:/Users/kalem/Videos/QA Automation/pytext1.txt'
word_counts = count_word_occurrences(file)
print(word_counts)

#2. Create a program to merge the contents of two text files into one.
def merge_files(file1, file2, output_file):
    try:
        content1 = open_file(file1)
        content2 = open_file(file2)
        with open(output_file, 'w') as output_file:
            output_file.write(content1)
            output_file.write("\n")  
            output_file.write(content2)
        print("********************************************************")
        print(f"Contents of file1 and file2 have been merged into output_file.")
        # print(f"file1 {count_word_occurrences(file1)}")
        # print(f"file2 {count_word_occurrences(file2)}")
        # print(f"the output in the new file {count_word_occurrences(output_file)}")
    
    except FileNotFoundError:
        print("One or both of the files were not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
file1 = 'C:/Users/kalem/Videos/QA Automation/pytext1.txt'  
file2 = 'C:/Users/kalem/Videos/QA Automation/pytext2.txt'  
output_file = 'C:/Users/kalem/Videos/QA Automation/pytext3.txt'
merge_files(file1, file2, output_file)

#3. Write a function to search for a specific word in a file and print its line number.
def search_word_in_file(file, word_to_search):
    try:
        with open(file, 'r') as file:
            line_number = 1
            for line in file:
                if word_to_search.lower() in line.lower():  
                    print(f"'{word_to_search}' found on line {line_number}: {line.strip()}")
                line_number += 1 
    except FileNotFoundError:
        print(f"The file '{file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
file = 'C:/Users/kalem/Videos/QA Automation/pytext1.txt'  
word_to_search = 'Hello'
search_word_in_file(file, word_to_search)

#4. Implement a Python script to count the number of lines, words, and characters in a file.
def count_file_details(file):
    try:
        lines_count = 0
        words_count = 0
        chars_count = 0
        with open(file, 'r') as file:
            for line in file:
                lines_count += 1  
                words_count += len(line.split())  
                chars_count += len(line)
        print(f"Lines: {lines_count}")
        print(f"Words: {words_count}")
        print(f"Characters: {chars_count}")
    except FileNotFoundError:
        print(f"The file '{file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
file = 'C:/Users/kalem/Videos/QA Automation/pytext1.txt'  
count_file_details(file)
