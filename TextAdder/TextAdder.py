def append_text_to_line(text, line):
    line = line.rstrip()
    line += text
    line += '\n'                
    return line


with open('input.txt', encoding='utf-8') as inf:
    all_the_lines = inf.readlines()

with open('output.txt', 'w', encoding='utf-8') as outf:
    for line in all_the_lines:
        outf.write(append_text_to_line (".com", line)) # CHANGE .com TO WHATEVER TEXT YOU WOULD LIKE
