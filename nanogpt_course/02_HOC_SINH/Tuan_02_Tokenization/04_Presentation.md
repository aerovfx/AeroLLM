# The Computer's Secret Code Translator

When you type: `"Hello there!"` into an AI chat window, do you think the machine actually reads those letters?

The truth is, computers are completely "illiterate." No matter how smart they seem, the supercomputers training AI are just oversized pocket calculators: they do not understand letters or words; they only understand **numbers**. For AI to read human text, we need a "translator" at the entrance. This tool is called a **Tokenizer**, and its process is called **Tokenization**.

Imagine playing a secret code game with your best friend. You agree on a simple code:
*   The letter `a` becomes `1`
*   The letter `b` becomes `2`
*   The letter `c` becomes `3`
*   ... and so on.

When you want to send the word `"cab"`, you write the sequence `[3, 1, 2]` on paper. When your friend receives this sequence, they look up the numbers in the codebook to translate it back into `"cab"`. In the AI world, translating text to numbers is called `encode`, and translating numbers back to text is called `decode`.

In the simplest version of nanoGPT, we use **character-level tokenization**. If your text contains only 65 unique characters (uppercase, lowercase, spaces, punctuation), then your vocabulary (Vocabulary) size is just 65. This makes it very easy for the computer to compute and learn, and it never encounters "out-of-vocabulary" words (since all words are made from these 65 characters).

However, large models like OpenAI's GPT-4 use a more advanced algorithm called **BPE** (Byte Pair Encoding). Instead of splitting every single character, it groups common character sequences together into a single token ID (for example, the word `"student"` might be treated as 1 token instead of 7 separate letters).

While tokenization makes AI processing fast, it also causes some funny side effects. For instance, because the word `"Strawberry"` is split by the tokenizer into chunks like `str`, `aw`, and `berry`, when you ask: *"How many 'r's are in the word Strawberry?"*, ChatGPT might get it wrong. This happens because the AI does not see the individual letters; it only sees the sequence of token IDs!
