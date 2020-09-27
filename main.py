# main.py
# Displays a staff with randomly generated notes appearing at regular intervals

import sys, pygame, random
import note_maker

random.seed()
pygame.init()

# Set canvas size, background refresh color, note speed
# Speed - shows a note every n milliseconds
size = width, height = 400, 200
white = 255, 255, 255
speed = 1000

screen = pygame.display.set_mode(size)

# Container of Note objects
list_of_qNotes = note_maker.make_Notes()

# Containers for pygame Surface objects
list_of_staff_notes = []
list_of_staff_notes_rect = []

# x position of first note
x_note_start = 75
# x distance between notes
x_increment = 30
# counter used for incrementing x distance
m = 0

# Fill note and rect lists with random notes to be displayed on the staff.
for n in range(len(list_of_qNotes)):
    random_int = random.randint(0, len(list_of_qNotes) - 1)

    note_obj = pygame.image.load(
        list_of_qNotes[random_int].image).convert_alpha()
    note_rect = note_obj.get_rect()
    note_rect.y = list_of_qNotes[random_int].staff_pos
    note_rect.x = x_note_start + x_increment * m

    list_of_staff_notes.append(note_obj)
    list_of_staff_notes_rect.append(note_rect)

    m = m + 1

# Make note
staff = pygame.image.load("art/staff.gif")
staff_rect = staff.get_rect()

# Set time variables for note appearance tempo
init_time = pygame.time.get_ticks()
time_increment = 1500

# Main loop reveals notes at fixed interval
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # Clear image, add empty staff, add starting notes
    screen.fill(white)
    screen.blit(staff, staff_rect)
    screen.blit(list_of_staff_notes[0], list_of_staff_notes_rect[0])

    # Every 1000 ms, print a new note
    current_time = pygame.time.get_ticks()
    for n in range(int(current_time / speed)):
        screen.blit(list_of_staff_notes[n], list_of_staff_notes_rect[n])

    pygame.display.flip()
