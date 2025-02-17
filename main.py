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
 print (count)
 totalcharacters = charactercount(file_contents)
 print(f"Total unique characters: {len(totalcharacters)}")  # Number of unique characters
 # Print a sample of character counts
 print("Sample of character frequencies:")
 print(dict(list(totalcharacters.items())[:10]))  # Display the first 10 character frequencies
main()

