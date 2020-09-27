# note_maker.py
# Generates Note objects that contain all of the information needed to render
# notes on a staff including their y location on the staff (relatively to the
# top of the screen), the location of the correct image, the length value of
# the note, and the name.

# The images of quarter note are 15x45px

import pygame


# position of notes is relative to middle bar of staff
def make_chirps():
    list_of_chirps = []

    chirp_0_991 = pygame.mixer.Sound("snd/0-991.ogg")
    chirp_0_992 = pygame.mixer.Sound("snd/0-992.ogg")
    chirp_0_993 = pygame.mixer.Sound("snd/0-993.ogg")
    chirp_0_994 = pygame.mixer.Sound("snd/0-994.ogg")
    chirp_0_995 = pygame.mixer.Sound("snd/0-995.ogg")
    chirp_0_996 = pygame.mixer.Sound("snd/0-996.ogg")
    chirp_0_997 = pygame.mixer.Sound("snd/0-997.ogg")
    chirp_0_998 = pygame.mixer.Sound("snd/0-998.ogg")
    chirp_0_999 = pygame.mixer.Sound("snd/0-999.ogg")
    chirp_1_000 = pygame.mixer.Sound("snd/1-000.ogg")
    chirp_1_001 = pygame.mixer.Sound("snd/1-001.ogg")
    chirp_1_002 = pygame.mixer.Sound("snd/1-002.ogg")
    chirp_1_003 = pygame.mixer.Sound("snd/1-003.ogg")
    chirp_1_004 = pygame.mixer.Sound("snd/1-004.ogg")
    chirp_1_005 = pygame.mixer.Sound("snd/1-005.ogg")
    chirp_1_006 = pygame.mixer.Sound("snd/1-006.ogg")
    chirp_1_007 = pygame.mixer.Sound("snd/1-007.ogg")
    chirp_1_008 = pygame.mixer.Sound("snd/1-008.ogg")
    chirp_1_009 = pygame.mixer.Sound("snd/1-009.ogg")

    list_of_chirps.append(chirp_0_991)
    list_of_chirps.append(chirp_0_992)
    list_of_chirps.append(chirp_0_993)
    list_of_chirps.append(chirp_0_994)
    list_of_chirps.append(chirp_0_995)
    list_of_chirps.append(chirp_0_996)
    list_of_chirps.append(chirp_0_997)
    list_of_chirps.append(chirp_0_998)
    list_of_chirps.append(chirp_0_999)
    list_of_chirps.append(chirp_1_000)
    list_of_chirps.append(chirp_1_001)
    list_of_chirps.append(chirp_1_002)
    list_of_chirps.append(chirp_1_003)
    list_of_chirps.append(chirp_1_004)
    list_of_chirps.append(chirp_1_005)
    list_of_chirps.append(chirp_1_006)
    list_of_chirps.append(chirp_1_007)
    list_of_chirps.append(chirp_1_008)
    list_of_chirps.append(chirp_1_009)

    return list_of_chirps