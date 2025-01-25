def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
    word_amount = word_count(file_contents)
    character_count = character_counter(file_contents)
    char_list = making_list(character_count)
    char_list.sort(reverse = True, key = sort_size)

    report(path, word_amount, char_list)

#counting the words
def word_count(text):
        return len(text.split())

#counting the different characters
def character_counter(text):
    character_count = {}
    for x in text.lower():
        if x not in character_count:
            character_count[x] = 1
        else:
            character_count[x] += 1
    return(character_count)

def making_list(dict):
    list_dict = []
    for key in dict:
        if key.isalpha() == True:
            list_dict.append({"letter": key, "amount" : dict[key]})
    return list_dict

#sorting the list of dictionaries
def sort_size(dict):
    return dict["amount"]

#defining the report structure
def report(path, words, char_list):
    print(f"--- Begin report of {path} ---")
    print(f"{words} found in the document")
    print("")
    for item in char_list:
        print(f"The '{item["letter"]}' character was found {item["amount"]} times")
    print("--- End report ---")

# only calling the function if file is run directly
if __name__ == "__main__":
    main()
