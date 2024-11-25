# Starting your Pokemon journey

- Namespace: picoctf/18739f24
- ID: pokemon-journey
- Type: custom
- Category: Heap overflow
- Points: 40
- Templatable: no
- MaxUsers: 1

## Description

Welcome new pokemon trainer to the world of pokemon! You are starting your
journey and you'll need a pokemon pal to be your companion. I have a pikachu for
you! Please don't mind any other pokemon I may have in the back... 

## Details

Connect to the program with netcat:

`$ nc {{server}} {{port}}`

The program's binary can be downloaded {{url_for("pokemon", "here")}}.

## Hints

- Have you ever heard of a heap overflow?
- `telescope` and `info proc map` will be your best friends.

## Solution Overview

1. Run the program in `gdb` and break right before pikachu

2. Look at the address allocations using `info proc map`

3. `telescope` at the start address of the heap 
(add `-l 200` to find the fp)

4. See where your input is overwritting and count the difference between 
the overflow and the fp

5. Replace fp with `&mewtwo`

## Challenge Options

## Learning Objective

Understand how a heap overflow works.

## Attributes

- author: sspivey
