# Joe Biden's Medications

- Namespace: picoctf/18739f24
- ID: joebiden-medications
- Type: custom
- Category: Crypto
- Points: 20
- Templatable: no
- MaxUsers: 1

## Description

You have access to Joe Biden's medications. You have been tasked by the KGB so that in his upcoming speech he replaces "Come on man." with "Donald Trump".
Change his medications so that he will slip up. (Disclaimer: this is complete satire, and meant to be taken as a joke.)

## Details

Connect to the program with netcat:

`$ nc {{server}} {{port}}`

The program's source code can be downloaded {{url_for("joebiden.py", "here")}}.

## Hints

- the meds [key] are initially randomly generated. Notice anything weird when you input a hexstring of 24 zeros?
- Is this actually a two-time pad problem?
- Wait, the encryption method is transitive?

## Solution Overview

Figure out how the messages (equal in char length) are mapped to each other. The xor method actually just counts the integer difference between the input and output characters. It is easiest to do it by brute forcing char by char.

## Challenge Options

## Learning Objective

Understand mapping and a simple two-time pad problem.

## Attributes

- author: sspivey
