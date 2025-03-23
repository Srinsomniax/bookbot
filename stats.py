def word_count(booktext):
    string = booktext
    num_words = len(string.split())
    return f"{num_words} words found in the document"

def char_count(booktext):
    char={}
    for i in booktext:
        if i.lower() in char:
            char[i.lower()]=char[i.lower()]+1
        else:
            char[i.lower()]= 1
        
    return char

def sort_chars_by_count(dict):
    new_list=[]
    for char, count in dict.items():
        char_dict={"char":char, "count":count}
        new_list.append(char_dict)
    
    def sort_on(dict):
        return dict["count"]

    new_list.sort(reverse=True, key=sort_on)

    return new_list

