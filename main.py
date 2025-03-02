import sys 
from stats import charactercount

def sorting(letters):
  return letters["count"]

def wordcount(text):
  return len(text.split())

def main():
 if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_book>")
        sys.exit(1)
 book_path = sys.argv[1]
 
 with open(book_path) as f:
      file_contents = f.read()
 count = wordcount(file_contents)
 totalcharacters = charactercount(file_contents)

 letters = [{"char": char, "count": char_count} for char, char_count in totalcharacters.items() if char.isalpha()]

 letters.sort(reverse=True, key=sorting)
  
 
 print(f"--- Begin report of {book_path} ---")
 print(f"{count} words found in the document\n")
 
 for char, count in sorted(totalcharacters.items()):
    print(f"{char}: {count}")
 print("--- End report ---")
main()

