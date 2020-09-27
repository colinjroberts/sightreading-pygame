# note_maker.py
# Generates Note objects that contain all of the information needed to render
# notes on a staff including their y location on the staff (relatively to the
# top of the screen), the location of the correct image, the length value of
# the note, and the name.

# The images of quarter note are 15x45px

import pygame


# Each note object will have a name, image, staff_pos, note_type
class Note():
    def __init__(self, name, image, staff_pos, note_value):
        self.name = name
        self.image = image
        self.staff_pos = staff_pos
        self.note_value = note_value


def make_Notes():

    list_of_notes = []

    qnote_d4 = Note("QD4", "art/qnote-stemtop.gif", 37, "quarter")
    list_of_notes.append(qnote_d4)

    qnote_e4 = Note("QE4", "art/qnote-stemtop.gif", 32, "quarter")
    list_of_notes.append(qnote_e4)

    qnote_f4 = Note("QF4", "art/qnote-stemtop.gif", 27, "quarter")
    list_of_notes.append(qnote_f4)

    qnote_g4 = Note("QG4", "art/qnote-stemtop.gif", 21, "quarter")
    list_of_notes.append(qnote_g4)

    qnote_a4 = Note("QA4", "art/qnote-stemtop.gif", 15, "quarter")
    list_of_notes.append(qnote_a4)

    qnote_b4 = Note("QB4", "art/qnote-stembottom.gif", 42, "quarter")
    list_of_notes.append(qnote_b4)

    qnote_c5 = Note("QC5", "art/qnote-stembottom.gif", 37, "quarter")
    list_of_notes.append(qnote_c5)

    qnote_d5 = Note("QD5", "art/qnote-stembottom.gif", 31, "quarter")
    list_of_notes.append(qnote_d5)

    qnote_e5 = Note("QE5", "art/qnote-stembottom.gif", 25, "quarter")
    list_of_notes.append(qnote_e5)

    qnote_f5 = Note("QF5", "art/qnote-stembottom.gif", 20, "quarter")
    list_of_notes.append(qnote_f5)

    qnote_g5 = Note("QG5", "art/qnote-stembottom.gif", 15, "quarter")
    list_of_notes.append(qnote_g5)

    return list_of_notes