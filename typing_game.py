#imports
import turtle as  turt
import random

#setup
word_writer = turt.Turtle()
font_setup = ("Arial", 20, "normal")
word_writer.penup
word_writer.hideturtle

word_writer.teleport(-400, 100)

word_index = 0



common_words = [
    "the", "be", "to", "of", "and", "a", "in", "that", "have", "I",
    "it", "for", "not", "on", "with", "he", "as", "you", "do", "at",
    "this", "but", "his", "by", "from", "they", "we", "say", "her", "she",
    "or", "an", "will", "my", "one", "all", "would", "there", "their", "what",
    "so", "up", "out", "if", "about", "who", "get", "which", "go", "me"
]

#functions
def pick_10_words():
    return_string = ""
    for n in range(10):
        return_string += f"{(common_words[random.randint(0, len(common_words) - 1)])} "
    return return_string
    

    
abc = list(pick_10_words())
print(f"{abc}")
def write_line (word):
    for n in range(len(word)):
        word_writer.write(word[n], font=font_setup)
        word_writer.setx(float(word_writer.xcor() + 20))
    
def check_keypress(key):
    global word_index
    if key == abc[word_index]:
        word_index += 1
        print(word_index)
        
def bind_keys():
    for letter in abc:
        wn.onkeypress(lambda l=letter: check_keypress(l), letter)

write_line(abc)

#main loop
wn = turt.Screen()
bind_keys()
wn.listen()
wn.mainloop()


