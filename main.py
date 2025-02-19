def sorting(letters):
  return letters["count"]

def charactercount(characters):
 character_count = {}
 characters = characters.lower()
 for character in characters:
  if character in character_count:
     character_count[character] += 1
  else:  
       character_count[character] = 1
 return character_count    
  
  
def wordcount(text):
  return len(text.split())


def main():
 with open("books/frankenstein.txt") as f:
  file_contents = f.read()
 count = wordcount(file_contents)
 totalcharacters = charactercount(file_contents)

 letters = [{"char": char, "count": char_count} for char, char_count in totalcharacters.items() if char.isalpha()]

 letters.sort(reverse=True, key=sorting)
  
 
 print(f"--- Begin report of books/frankenstein.txt ---")
 print(f"{count} words found in the document\n")
 
 for letter in letters:
    print(f"The '{letter['char']}' character was found {letter['count']} times")
 print("--- End report ---")
main()

