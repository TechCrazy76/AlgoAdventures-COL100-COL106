import time

import library
import hash_table
from prime_generator import set_primes

def check_lib(lib, unique_words, word_to_books, sort_output=True):
    dw1 = lib.distinct_words("book1")
    dw2 = lib.distinct_words("book2")
    
    if sort_output:
        dw1.sort()
        dw2.sort()
    if dw1 == sorted(unique_words[0]) and dw2 == sorted(unique_words[1]):
        print("DISTINCT WORDS CORRECT!")
    else:
        print("DISTINCT WORDS FAILED!")
    
    if lib.count_distinct_words("book1") == len(unique_words[0]) and lib.count_distinct_words("book2") == len(unique_words[1]):
        print("COUNT DISTINCT WORDS CORRECT!")
    else:
        print("COUNT DINSTINCT WORDS FAILED!")
        
    word = "book"
    
    sk = lib.search_keyword(word)
    if sort_output:
        sk.sort()
        
    if sk == sorted(word_to_books[word]):
        print("SEARCH KEYWORD CORRECT!")
    else:
        print("SEARCH KEYWORD FAILED!")
    print("\n\n")
    

def get_primes(start = 10**3, end = 10**5):
    is_prime = [True] * (end+1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, end+1):
        if not is_prime[i]: continue
        
        for j in range(2*i, end+1, i):
            is_prime[j] = False
    
    prime_sizes = []
    sz = start
    while sz <= end:
        if not is_prime[sz]:
            sz += 1
            continue
        
        prime_sizes.append(sz)
        sz *= 2
        
    prime_sizes.reverse()
    return prime_sizes

def main():
    book_titles = ["book1", "book2"]
    texts = [["The", "name", "of", "this", "book", "contains", "a", "number"],
             ["You", "can", "name", "this", "book", "anything"]]
            
    unique_words = []
    
    for text in texts:
        unique = []
        
        for word in text:
            if word not in unique:
                unique.append(word)
        
        unique_words.append(sorted(unique))
        
    word_to_books = {}
    
    for book, text in zip(book_titles, texts):
        for word in text:  # Corrected line: iterate over individual words in each text
           if word not in word_to_books:
              word_to_books[word] = [book]
           else:
              word_to_books[word].append(book)
        
    set_primes(get_primes())
        
    # Check Musk         
    musk_time = time.time()
    musk_lib = library.MuskLibrary(book_titles, texts)
    musk_time = time.time() - musk_time
    
    print(f"Musk Library sorting took {musk_time:.4f}s")
    print(f"Checking Library functions for Musk:")
    check_lib(musk_lib, unique_words, word_to_books)
    
    jobs_lib = library.JGBLibrary("Jobs", (10, 29))
    gates_lib = library.JGBLibrary("Gates", (10, 37))
    bezos_lib = library.JGBLibrary("Bezos", 
                              (10, 37,
                               7, 13)
                              )
    
    for lib, name in zip([jobs_lib, gates_lib, bezos_lib], ["Jobs", "Gates", "Bezos"]):
        time_taken = time.time()
        
        for book, text in zip(book_titles, texts):
            lib.add_book(book, text)
        
        time_taken = time.time() - time_taken
        
        print(f"{name} Library took {time_taken:.4f}s")
        print(f"Checking Library Functions for {name}: ")
        check_lib(lib, unique_words, word_to_books)
    

if __name__ == "__main__":
    main()