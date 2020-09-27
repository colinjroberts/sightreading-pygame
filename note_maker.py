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


# position of notes is relative to middle bar of staff
def make_Notes():
    list_of_notes = []

    # Prev 52
    qnote_b3 = Note("QA3", "art/qnote-onebar-stemtop.gif", 5, "quarter")
    list_of_notes.append(qnote_b3)

    # Prev 47
    qnote_c4 = Note("QB3", "art/qnote-midbar-stemtop.gif", 0, "quarter")
    list_of_notes.append(qnote_c4)

    # Prev 42
    #qnote_c4 = Note("QC4", "art/qnote-stemtop.gif", 0, "quarter")
    #list_of_notes.append(qnote_c4)

    # Prev 37
    qnote_d4 = Note("QD4", "art/qnote-stemtop.gif", -5, "quarter")
    list_of_notes.append(qnote_d4)

    # Prev 32
    qnote_e4 = Note("QE4", "art/qnote-stemtop.gif", -10, "quarter")
    list_of_notes.append(qnote_e4)

    # Prev 27
    qnote_f4 = Note("QF4", "art/qnote-stemtop.gif", -15, "quarter")
    list_of_notes.append(qnote_f4)

    # Prev 21
    qnote_g4 = Note("QG4", "art/qnote-stemtop.gif", -21, "quarter")
    list_of_notes.append(qnote_g4)

    # Prev 15
    qnote_a4 = Note("QA4", "art/qnote-stemtop.gif", -27, "quarter")
    list_of_notes.append(qnote_a4)

    # Prev 42
    qnote_b4 = Note("QB4", "art/qnote-stembottom.gif", 0, "quarter")
    list_of_notes.append(qnote_b4)

    # Prev 37
    qnote_c5 = Note("QC5", "art/qnote-stembottom.gif", -6, "quarter")
    list_of_notes.append(qnote_c5)

    # Prev 31
    qnote_d5 = Note("QD5", "art/qnote-stembottom.gif", -11, "quarter")
    list_of_notes.append(qnote_d5)

    # Prev 25
    qnote_e5 = Note("QE5", "art/qnote-stembottom.gif", -17, "quarter")
    list_of_notes.append(qnote_e5)

    # Prev 20
    qnote_f5 = Note("QF5", "art/qnote-stembottom.gif", -22, "quarter")
    list_of_notes.append(qnote_f5)

    # Prev 15
    qnote_g5 = Note("QG5", "art/qnote-stembottom.gif", -27, "quarter")
    list_of_notes.append(qnote_g5)

    # Prev 5
    qnote_a5 = Note("QB5", "art/qnote-midbar-stembottom.gif", -32, "quarter")
    list_of_notes.append(qnote_a5)

    # Prev 0
    qnote_b5 = Note("QC6", "art/qnote-onebar-stembottom.gif", -38, "quarter")
    list_of_notes.append(qnote_b5)

    # Prev 10
    qnote_c6 = Note("QA5", "art/qnote-twomidbar-stembottom.gif", -46,
                    "quarter")
    list_of_notes.append(qnote_c6)

    return list_of_notes