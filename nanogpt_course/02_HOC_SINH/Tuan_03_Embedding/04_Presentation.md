# The Map of Meanings and Word Coordinates

Humans understand the word `"cat"` because we have seen cats in real life. But to a computer, a cat is just the number `12` (Token ID). How can the computer understand that `"cat"` and `"dog"` are furry, four-legged animals, while a `"computer"` is an electronic device?

To solve this, AI engineers invented **Embedding** — a method that turns every word into a **vector coordinate** on a **high-dimensional map of meanings**.

Imagine a 3D map of a classroom:
*   The X-axis represents the level of *"interest in sports"*.
*   The Y-axis represents the level of *"interest in arts"*.
*   The Z-axis represents the level of *"interest in gaming"*.

Each student in the classroom has a coordinate (X, Y, Z) representing their hobbies. Students who like soccer and gaming will sit very close to each other on this map, while students who love painting will sit in another corner.

The `nn.Embedding` layer in PyTorch does exactly this. It assigns each Token ID a list of float numbers (e.g., 96 numbers for our mini model, or 768 for GPT-2). Initially, these numbers are random, but through training, words with similar meanings (like `"king"` and `"emperor"`) will automatically move closer together on this map, creating a magical semantic representation space.

However, if we only embed the meaning of words, the model won't distinguish between `"I love you"` and `"You love me"`, because both sentences contain the same words. Therefore, we need **Position Embedding**. This is a secondary coordinate map showing *"this word is at index 1, that word is at index 2"*. We add these two coordinates together before feeding them into the AI brain.
