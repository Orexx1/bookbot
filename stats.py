def charactercount(characters):
 character_count = {}
 characters = characters.lower()
 for character in characters:
  if character.isalpha():
   if character in character_count:
      character_count[character] += 1
   else:  
       character_count[character] = 1
 return character_count    
  