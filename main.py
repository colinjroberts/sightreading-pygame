# main.py
# Displays a staff with randomly generated notes appearing at regular intervals

import sys, pygame, random
import note_maker

random.seed()
pygame.init()

# Set canvas size, background refresh color, note speed
# Speed - shows a note every n milliseconds
size = width, height = 800, 600
white = 255, 255, 255
speed = 1000

screen = pygame.display.set_mode(size)

chirp = pygame.mixer.Sound('snd/1-000.ogg')

# Container of Note objects
list_of_qNotes = note_maker.make_Notes()

# Containers for pygame Surface objects
list_of_staff_notes = []
list_of_staff_notes_rect = []

# y of mid line in top row
initial_score_y_offset = 133
# x position of first note in top row
x_note_start_first_line = 150
# x distance between notes
x_increment_first_line = 40
# counter used for incrementing x distance
m = 0

for n in range(16):
    random_int = random.randint(0, len(list_of_qNotes) - 1)

    note_obj = pygame.image.load(
        list_of_qNotes[random_int].image).convert_alpha()
    note_rect = note_obj.get_rect()

    note_rect.y = list_of_qNotes[random_int].staff_pos + initial_score_y_offset
    note_rect.x = x_note_start_first_line + x_increment_first_line * m

    list_of_staff_notes.append(note_obj)
    list_of_staff_notes_rect.append(note_rect)

    m = m + 1

# mod 20
# y of mid line in top row
score_subsequent_y_offset = 80
# x position of first note in top row
x_note_start = 27
# x distance between notes
x_increment = 38
# counter used for incrementing x distance
for n in range(100):
    random_int = random.randint(0, len(list_of_qNotes) - 1)

    y = 1 + n // 20
    m = n % 20
    note_obj = pygame.image.load(list_of_qNotes[random_int %
                                                16].image).convert_alpha()
    note_rect = note_obj.get_rect()

    note_rect.y = list_of_qNotes[random_int %
                                 16].staff_pos + initial_score_y_offset + (
                                     score_subsequent_y_offset * y)
    note_rect.x = x_note_start + x_increment * m

    list_of_staff_notes.append(note_obj)
    list_of_staff_notes_rect.append(note_rect)

# Make note
# Each staff is 80 px from the last. First starts at 115
staff = pygame.image.load("art/largescore.gif")
staff_rect = staff.get_rect()

# Set time variables for note appearance tempo
init_time = pygame.time.get_ticks()
time_increment = 1500
timer = init_time
frame = 0

clock = pygame.time.Clock()
te = 0
screen.blit(staff, staff_rect)
screen.blit(list_of_staff_notes[0], list_of_staff_notes_rect[0])
screen.blit(list_of_staff_notes[1], list_of_staff_notes_rect[1])

my_event = pygame.USEREVENT + 1
pygame.time.set_timer(my_event, 1000)

pygame.event.set_allowed(pygame.QUIT)
pygame.event.set_allowed(pygame.ACTIVEEVENT)
pygame.event.set_allowed(pygame.KEYDOWN)
pygame.event.set_allowed(pygame.USEREVENT)
pygame.event.set_blocked(pygame.MOUSEMOTION)

# Main loop reveals notes at fixed interval
while 1:

    event = pygame.event.wait()
    print(event)

    # Schedule the next event
    if event.type == my_event:
        chirp.play()
        print(pygame.time.get_ticks() - timer)
        timer = pygame.time.get_ticks()

        #for n in range(116):
        #    screen.blit(list_of_staff_notes[n], list_of_staff_notes_rect[n])

        screen.blit(list_of_staff_notes[frame],
                    list_of_staff_notes_rect[frame])

        frame += 1
        pygame.display.flip()

    elif event.type == pygame.KEYDOWN:
        sys.exit()
    elif event.type == pygame.QUIT:
        sys.exit()

    # dt = clock.tick(8)
    # te += dt
    # print(te)

    # if te > speed:

    #     # Clear image, add empty staff, add starting notes
    #     #screen.fill(white)
    #     chirp.play()

    #     #for n in range(116):
    #     #    screen.blit(list_of_staff_notes[n], list_of_staff_notes_rect[n])
    #     screen.blit(list_of_staff_notes[0], list_of_staff_notes_rect[0])
    #     screen.blit(list_of_staff_notes[1], list_of_staff_notes_rect[1])

    #     screen.blit(list_of_staff_notes[frame],
    #                 list_of_staff_notes_rect[frame])
    #     frame += 1

    #     #for n in range(int(pygame.time.get_ticks() / speed)):
    #     #    screen.blit(list_of_staff_notes[n], list_of_staff_notes_rect[n])
    #     te = 0
