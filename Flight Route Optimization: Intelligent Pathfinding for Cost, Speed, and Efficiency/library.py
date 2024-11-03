import hash_table as ht

class DigitalLibrary:
    # DO NOT CHANGE FUNCTIONS IN THIS BASE CLASS
    def __init__(self):
        pass
    
    def distinct_words(self, book_title):
        pass
    
    def count_distinct_words(self, book_title):
        pass
    
    def search_keyword(self, keyword):
        pass
    
    def print_books(self):
        pass

class MuskLibrary(DigitalLibrary):
    def __init__(self, book_titles, texts):
        # Sort books and texts by title, remove duplicates without set or dict
        self.book_and_text_list = [
            [book, self.remove_duplicates(sorted(text))] for book, text in zip(book_titles, texts)
        ]
        self.book_and_text_list.sort()

    def remove_duplicates(self, text):
        # Helper to remove duplicates
        unique_words = []
        for word in text:
            if word not in unique_words:
                unique_words.append(word)
        return unique_words

    def distinct_words(self, book_title):
        index = self.binary_search(book_title)
        return self.book_and_text_list[index][1] if index is not None else []

    def count_distinct_words(self, book_title):
        index = self.binary_search(book_title)
        return len(self.book_and_text_list[index][1]) if index is not None else 0

    def search_keyword(self, keyword):
        return [
            book[0] for book in self.book_and_text_list 
            if self.binary_search_keyword(book[1], keyword) != -1
        ]

    def print_books(self):
        for book, text in self.book_and_text_list:
            print(f"{book}: " + " | ".join(text) if text else f"{book}: ")

    # Binary search functions
    def binary_search(self, book_title):
        low, high = 0, len(self.book_and_text_list) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.book_and_text_list[mid][0] == book_title:
                return mid
            elif self.book_and_text_list[mid][0] < book_title:
                low = mid + 1
            else:
                high = mid - 1
        return None

    def binary_search_keyword(self, arr, keyword):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == keyword:
                return mid
            elif arr[mid] < keyword:
                low = mid + 1
            else:
                high = mid - 1
        return -1


class JGBLibrary(DigitalLibrary):
    def __init__(self, name, params):
        self.name = name 
        self.book_list = []
        self.params = params
        self.collision_type = 'Chain' if name == "Jobs" else 'Linear' if name == "Gates" else 'Double'
        self.book_txt_hashmap = ht.HashMap(self.collision_type, self.params)

    def add_book(self, book_title, text):
        self.book_list.append(book_title)
        hashset_txt = ht.HashSet(self.collision_type, self.params)
        for word in text:
            hashset_txt.insert(word)
        self.book_txt_hashmap.insert((book_title, hashset_txt))

    def distinct_words(self, book_title):
        hashset_txt = self.book_txt_hashmap.find(book_title)
        if hashset_txt is None:
            return []
        return [word for word in hashset_txt.table if word is not None]

    def count_distinct_words(self, book_title):
        hashset_txt = self.book_txt_hashmap.find(book_title)
        return hashset_txt.key_count if hashset_txt is not None else 0

    def search_keyword(self, keyword):
        return [
            book_title for book_title in self.book_list 
            if self.book_txt_hashmap.find(book_title) and self.book_txt_hashmap.find(book_title).find(keyword)
        ]

    def print_books(self):
        for bucket in self.book_txt_hashmap.table:
            if bucket:
                for book in (bucket if isinstance(bucket, list) else [bucket]):
                    if book:
                        print(f"{book[0]}:", book[1])
