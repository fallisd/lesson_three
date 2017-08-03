input_filename = 'poem.txt'
output_filename = 'output.txt'

# store contents of input file in a list named "lines"
with open(input_filename, 'r') as f:
    lines = f.readlines()

# Open file for writing
target = open(output_filename, 'w')

# Assignment
# Read in the file from poem.txt and write the poem to output.txt with the following modifications
#   
#   1. Add a title to the poem
#   2. Add the author's name at the end of the poem with a blank line in between
#   3. Capitalize the first word of every line
#   4. Delete all lines that begin with the word "Delete" (This is the same as not writing those lines to the output file)
#   5. Change all occurrences of "it's" to "its"
#   6. Indent every second line with two spaces
#   7. Add a colon at the end of the fourth line
#   8. Add a blank line after every fourth line.
#   9. Add a numbered Stanza heading to the beginning of each stanza
#   10. Add a period at the end of every stanza that doesn't already have punctuation  
#   11. Write the line number and a space before each line (Make sure they are numbered correctly: The last line should be 20)
#   12. Add an extra space after the single digit lines to preserve the indentation
#
#    
#
# Keep in mind:
# There are many ways the modifications could be done. The solution should be as concise as possible.
# Fewer lines of code doesn't necessarily mean that the code is better, but duplicating operations that 
# could be done in a loop is inefficient while writing and it requires more time to modify the code if 
# it is duplicated in several places.
# Try to make the operations general. The operations shouldn't be specific to the words
# of just one poem but it could be applied to others without modifying the code. 

#-----------------------------
# write code here
#-----------------------------

# These two lines will write a copy of the poem to output_filename.
# You can make modifications in the loop or outside the loop, depending on what is required.
target.write("Stanzas\n")

lines[3] = lines[3].replace('\n', ':\n')

count = 0

for line in lines:
   if not line.startswith('Delete'):
       cap_line = line[0].upper() + line[1:]
       cap_line = cap_line.replace("It's", "Its")
       
       if count % 2 != 0:
           cap_line  = "  " + cap_line
       
       if ((count + 1) % 4) == 0:
           if not cap_line.endswith(':\n'):
               cap_line = cap_line.replace('\n', '.\n')
       
       if count % 4 == 0:
           target.write('\n')
           target.write("Stanza " + str(count//4 + 1) + '\n')
       if count < 9:
           cap_line = ' ' + cap_line
       
       cap_line = str(count + 1) + ' ' + cap_line
       target.write(cap_line)
       
       count = count + 1
       

       
target.write("\n\nBy Emily")
#-----------------------------
#
#-----------------------------

# Close the file
target.close()






