#!/usr/bin/python
# coding: utf-8
#
# MicroNovels, copyright (c) 2016 Ben Kybartas <bkybartas@gmail.com>
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# 29 November 2014

import random

def get_word_count(novel):
    return len(novel.split())

intro = "Welcome to Cave Quest II: The Deathlabyrinth of Grozk.\nType \"Help\" at any point for instructions\n"
novel = intro + "\n"

while (get_word_count(novel) < 50000):
	if (random.random() < 0.3):
		novel += "> Go " + random.choice(["North", "South", "East", "West"]) + "\n"
		novel += "You are in a " + random.choice(["grimy", "rusty", "dusty", "shadowy", "rocky"]) + " " + random.choice(["cavern", "factory", "room", "space station", "cafeteria", "bar"]) + ".\n"
		novel += "There are some " + random.choice(["items", "things", "objects", "useful items", "potential traps"]) + " here.\n"
	else:
		verb = random.choice(["Look", "Examine", "Push", "Pull", "Open","Talk", "Take", "Pick up"])
		item = random.choice(["Rock", "Door", "Letter", "Knife", "Rope", "Crowbar", "Key Card", "Object", "Old Man", "Coin", "Lantern", "Gun", "Map", "Oil Can", "Water Bottle"])

		novel += "> " + verb + " " + item + "\n"
		result = random.choice(["Don't know how to \"" + verb + "\" something.", 
			"I don't see any " + item + " here.",
			"Ok.",
			"Don't know how to \"" + verb + "\"",
			"You have died!\n> Restart\n\n" + intro,
			"Confused? Type \"Help\" for instructions.",
			"That's something we don't understand.",
			"You try to " + verb + " the " + item + " but you can't.",
			"Try something else."])
		novel += result + "\n"
novel += "> Quit\nAre you sure?\n> y"
file = open("Ifeelitletsmeusemyimaginationmore.txt", "w")
file.write(novel)
file.close() 