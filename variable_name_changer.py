folder = input("What's the path? Please specify the file extension: ")
folder.replace('/', '//')
with open(folder, "r", encoding="utf-8") as file:
    text = file.read()
old_variable = input("The name of your variable: ")
new_variable = input("New variable name: ")
template = ['=', ' =', '= ',
            '/', ' /', '/ ',
            '*', ' *', '* ',
            '**', ' **', '** ',
            '%', ' %', '% ',
            '//', ' //', '// ',
            '.', ' .', '. ',
            '(', '( ', ' )', ')']

new_text = text
for temp in template:
    new_text = new_text.replace(f"{old_variable}{temp}", f"{new_variable}{temp}")
    new_text = new_text.replace(f"{temp}{old_variable}", f"{temp}{new_variable}")

with open(folder, "w", encoding="utf-8") as f:
    f.write(new_text)    