#imports
import turtle as turt
import random
import time

#setup

wn = turt.Screen()
wn.setup(1920,1000)

top_writer = turt.Turtle()
font_setup = ("Arial", 20, "normal")
top_writer.penup()
top_writer.hideturtle()
top_writer.speed(0)

bot_writer = turt.Turtle()
bot_writer.penup()
bot_writer.hideturtle()
bot_writer.speed(0)


word_index_top = 0
word_index_bottom = 0

width = 2
length = 15
line = ((-5, 0), (width, 0), (width, length), (-5, length))
turt.register_shape("line", line)

cursor = turt.Turtle()
cursor.penup()
cursor.shape("line")
cursor.teleport(-600, 100)

timer = 20
counter_interval = 1000   #1000 represents 1 second
timer_up = False
counter = turt.Turtle()
counter.hideturtle()
counter.penup()
counter.teleport(350,300)

word_index = 0

current_line = "top"  # Track which line is currently being typed
abc_top = []  # Text for top line
abc_bottom = []  # Text for bottom line

words = [
    # Top 50 common words
    "the", "be", "to", "of", "and", "a", "in", "that", "have", "I",
    "it", "for", "not", "on", "with", "he", "as", "you", "do", "at",
    "this", "but", "his", "by", "from", "they", "we", "say", "her", "she",
    "or", "an", "will", "my", "one", "all", "would", "there", "their", "what",
    "so", "up", "out", "if", "about", "who", "get", "which", "go", "me",

    # 35 more common words
    "when", "make", "can", "like", "time", "no", "just", "him", "know", "take",
    "people", "into", "year", "your", "good", "some", "could", "them", "see", "other",
    "than", "then", "now", "look", "only", "come", "its", "over", "think", "also",
    "back", "after", "use", "two", "how", "our", "work", "first", "well", "way",
    "even", "new", "want", "because", "any", "these", "give", "day", "most", "us",

    # 15 uncommon / expressive words
    "serendipity", "ephemeral", "luminous", "quixotic", "mellifluous",
    "zephyr", "labyrinthine", "halcyon", "ethereal", "ineffable",
    "petrichor", "cacophony", "obfuscate", "panacea", "sonder"
]

#functions
def countdown():
    global timer, timer_up, word_index,timer
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up", font=font_setup)
        timer_up = True
        print("time is up", timer_up)
        counter.teleport(0,0)
        counter.write("Your Words Per Miniute is " + str((word_index/5)/(20/60.)), font=font_setup)
    else:
        counter.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval) 

def pick_10_words():
    return_string = ""
    for n in range(10):
        return_string += f"{(words[random.randint(0, len(words) - 1)])} " 
    return list(return_string)

def write_top_line():
    
    """Write only the top line"""
    # Clear only the top line area 
    top_writer.clear()
    top_writer.penup()
    top_writer.teleport(-600, 100)
    top_writer.pendown()
    # Clear a specific area for top line
    top_writer.color("white")
    top_writer.begin_fill()
    for _ in range(2):
        top_writer.forward(1200)  # Width of text area
        top_writer.right(90)
        top_writer.forward(30)    # Height of text line
        top_writer.right(90)
    top_writer.end_fill()
    top_writer.color("black")
    
    # Write the top line text
    top_writer.penup()
    top_writer.teleport(-600, 100)
    for n in range(len(abc_top)):
        top_writer.write(abc_top[n], font=font_setup)
        top_writer.setx(float(top_writer.xcor() + 20))

def write_bottom_line():
    
    """Write only the bottom line"""
    # Clear only the bottom line area
    bot_writer.clear()
    bot_writer.penup()
    bot_writer.teleport(-600, 25)
    bot_writer.pendown()
    # Clear a specific area for bottom line
    bot_writer.color("white")
    bot_writer.begin_fill()
    for _ in range(2):
        bot_writer.forward(1200)  # Width of text area
        bot_writer.right(90)
        bot_writer.forward(30)    # Height of text line
        bot_writer.right(90)
    bot_writer.end_fill()
    bot_writer.color("black")
    
    # Write the bottom line text
    bot_writer.penup()
    bot_writer.teleport(-600, 25)
    for n in range(len(abc_bottom)):
        bot_writer.write(abc_bottom[n], font=font_setup)
        bot_writer.setx(float(bot_writer.xcor() + 20))

def write_both_lines():
    """Write both lines by calling individual write functions"""
    write_top_line()
    write_bottom_line()
    
def check_keypress(key):
    global word_index_top, word_index_bottom, current_line, abc_top, abc_bottom, word_index
    
    # Check if time is up before processing key press
    if timer_up:
        print("Time's up! Typing disabled.")
        top_writer.hideturtle()
        top_writer.clear()
        bot_writer.hideturtle()
        bot_writer.clear()
        cursor.hideturtle()
        return
    
    if current_line == "top":
        if word_index_top < len(abc_top):
            if key == abc_top[word_index_top]:
                word_index_top += 1
                word_index += 1
                print(f"Correct! Top line - Index: {word_index_top}, Character: '{key}'")
                cursor.setx(float(cursor.xcor() + 20))
                
                # Check if we've reached the end of top line
                if word_index_top >= len(abc_top):
                    switch_to_bottom_line()
            else:
                print(f"Wrong! Expected: '{abc_top[word_index_top]}', Got: '{key}'")
    
    else:  # current_line == "bottom"
        if word_index_bottom < len(abc_bottom):
            if key == abc_bottom[word_index_bottom]:
                word_index_bottom += 1
                word_index += 1
                print(f"Correct! Bottom line - Index: {word_index_bottom}, Character: '{key}'")
                cursor.setx(float(cursor.xcor() + 20))
                
                # Check if we've reached the end of bottom line
                if word_index_bottom >= len(abc_bottom):
                    switch_to_top_line()
            else:
                print(f"Wrong! Expected: '{abc_bottom[word_index_bottom]}', Got: '{key}'")

def switch_to_bottom_line():
    global current_line, word_index_top, abc_top
    print("Switching to bottom line...")
    
    # Generate new text for top line
    abc_top = pick_10_words()
    word_index_top = 0
    
    # Move cursor to bottom line
    current_line = "bottom"
    cursor.teleport(-600, 25)
    
    # Update only the top line with new text
    write_top_line()

def switch_to_top_line():
    global current_line, word_index_bottom, abc_bottom
    print("Switching to top line...")
    
    # Generate new text for bottom line
    abc_bottom = pick_10_words()
    word_index_bottom = 0
    
    # Move cursor to top line
    current_line = "top"
    cursor.teleport(-600, 100)
    
    # Update only the bottom line with new text
    write_bottom_line()

def bind_keys():
    # Bind all possible characters that might appear
    all_chars = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for char in all_chars:
        wn.onkeypress(lambda l=char: check_keypress(l), char)

def initialize_game():
    global abc_top, abc_bottom, current_line, word_index_top, word_index_bottom
    
    # Generate initial text for both lines
    abc_top = pick_10_words()
    abc_bottom = pick_10_words()
    
    # Start with top line
    current_line = "top"
    word_index_top = 0
    word_index_bottom = 0
    
    # Position cursor at top line
    cursor.teleport(-600, 100)
    
    # Draw both lines
    write_both_lines()

# Initial setup
initialize_game()

#main loop
bind_keys()
wn.listen()
wn.ontimer(countdown, counter_interval) 
wn.mainloop()