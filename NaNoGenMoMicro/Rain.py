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
novel = ""
for i in range(50000):
	line = ""
	for j in range(random.randint(1,90)): line += random.choice([" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","/"])
	line += random.choice(["spl","pl"]) + random.choice(["a","o","i"]) + random.choice(["t","p"])
	for j in range(100 - len(line)): line += random.choice([" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","/"])
	novel += line + "\n"
file = open("WatchingProceduralRainOnTheWindow.txt", "w")
file.write(novel)
file.close() 