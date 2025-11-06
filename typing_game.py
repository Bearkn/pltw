
#imports
import turtle as turt
import random
import time

#setup

wn = turt.Screen()
wn.setup(1920,1000)

word_writer = turt.Turtle()
font_setup = ("Arial", 20, "normal")
word_writer.penup()
word_writer.hideturtle()
word_writer.teleport(-600, 100)
word_writer.speed(0)

word_index = 0

width = 2
length = 15
line = ((-5, 0), (width, 0), (width, length), (-5, length))
turt.register_shape("line", line)

cursor = turt.Turtle()
cursor.penup()
cursor.shape("line")
cursor.teleport(-600, 100)

timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False
counter = turt.Turtle()
counter.hideturtle()
counter.penup()
counter.teleport(350,300)


abc = []

words = [
    "the", "be", "to", "of", "and", "a", "in", "that", "have", "I",
    "it", "for", "not", "on", "with", "he", "as", "you", "do", "at",
    "this", "but", "his", "by", "from", "they", "we", "say", "her", "she",
    "or", "an", "will", "my", "one", "all", "would", "there", "their", "what",
    "so", "up", "out", "if", "about", "who", "get", "which", "go", "me",
    # uncommon words added
    "serendipity", "ephemeral", "sonder", "luminous", "quixotic",
    "mellifluous", "zephyr", "labyrinthine", "halcyon", "ethereal",
    "sonder", "ineffable", "petrichor", "sonder", "cacophony",
    "sonder", "obfuscate", "sonder", "panacea", "sonder", "sonder",
    "sonder", "sonder", "sonder", "sonder", "sonder"
]


#functions
def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up", font=font_setup)
        timer_up = True
    else:
        counter.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval) 

def pick_10_words():
    global abc
    return_string = ""
    for n in range(10):
        return_string += f"{(words[random.randint(0, len(words) - 1)])} " 
    abc = list(return_string)
    print(f"New words: {''.join(abc)}")

def write_line(word):
    word_writer.clear()
    word_writer.teleport(-600, 100)
    for n in range(len(word)):
        word_writer.write(word[n], font=font_setup)
        word_writer.setx(float(word_writer.xcor() + 20))
    
def check_keypress(key):
    global word_index
    global abc
    if word_index < len(abc):
        if key == abc[word_index]:
            word_index += 1
            print(f"Correct! Index: {word_index}, Character: '{key}'")
            cursor.setx(float(cursor.xcor() + 20))
            
            # Check if we've reached the end
            if word_index >= len(abc):
                next_line()
        else:
            print(f"Wrong! Expected: '{abc[word_index]}', Got: '{key}'")

def bind_keys():
    # Clear existing bindings
    wn.onkeypress(None, "a")
    wn.onkeypress(None, "b")
    
    # Bind all possible characters that might appear
    all_chars = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for char in all_chars:
        wn.onkeypress(lambda l=char: check_keypress(l), char)
        
def next_line():
    global word_index
    word_writer.clear()
    print("Generating new words...")
    word_index = 0
    word_writer.teleport(-600, 100)
    cursor.teleport(-600, 100)
    pick_10_words()
    write_line(abc)
    bind_keys()  # Rebind keys for new text

# Initial setup
pick_10_words()
write_line(abc)

#main loop

bind_keys()
wn.listen()
wn.ontimer(countdown, counter_interval) 
wn.mainloop()