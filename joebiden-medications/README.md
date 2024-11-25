# Overall Idea
This an example problem of a `two-time pad` where you control the key. You can
give it as many plain texts to produce and cipher texts as you want, but your
goal is make a key such the given plain text produces the cipher text.

I wrapped the problem in a Joe Biden's meme, as per lore, Biden refuses to refer
to "Donald Trump" by name. This is for complete satire and hopefully someone
gets a laugh out of it.

# Solution Approach
There are a couple of important properties of the 'encryption' alogorithm:

    - The plaintext and ciphertext are transitive 
    (where `plaintext` -> `ciphertext` and `ciphertext` -> same `plaintext`)

    - Only one char in the key changes one char in the plaintext and ciphertext
- the goal plain text and goal cipher text are the same length.

You can either recalc (xor + remainder) what the key should be, or brute force. 
I would recommend brute force char by char. I was debating wether or not to 
have the file available to download, but I am curious to see what kind of 
solutions people come up with once they see the source code.

Solution Key: `070003044C0B4E741F14035E`

# Building

This should be ready for cmgr. Extract the `sspivey.tar.gz` to `cmgr/challanges/`
and it should be all ready to deploy.

If you choose to deploy with docker, you'll need to include ARG when building.