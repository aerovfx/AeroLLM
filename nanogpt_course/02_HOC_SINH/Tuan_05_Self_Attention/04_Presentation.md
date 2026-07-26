# The Meeting of the Words

Imagine reading this sentence:
`"The dog chased the cat because it was fast."`

How do you know whether the word **"it"** refers to the dog or the cat? As humans, we understand this instantly based on grammatical context and logical actions (a dog chases a cat because the dog is faster, or the cat runs away because the cat is fast). But for a computer, words are just soulless vector coordinates. How can a computer know that **"it"** should link closely with **"the dog"** (or "the cat")?

The biggest breakthrough solving this problem was introduced in 2017 under the name **Self-Attention** — the heart of the Transformer architecture.

The Self-Attention mechanism works like a **smart library catalog system**. Each word in the sentence is assigned 3 distinct vectors, playing different roles:
1.  **Query (Q):** Represents what the word is looking for. (For example, the word `"it"` sends a query: *"Who am I? Who is doing the action of being fast?"*).
2.  **Key (K):** Represents the label of the word for others to match against. (For example, the word `"the dog"` has a key label: *"I am a noun, subject, doing the chasing"*).
3.  **Value (V):** Represents the actual content and meaning the word brings if selected.

The matching process works like this:
*   Each word takes its **Query (Q)** and multiplies it with the **Key (K)** of all other words in the sentence (matrix dot product) to produce similarity scores.
*   This score is divided by the square root of the vector dimension ($\sqrt{d_k}$) to keep numbers stable, then passed through the **Softmax** function to generate attention weights (percentages). (For example, `"it"` might assign 70% attention to `"the dog"`, 20% to `"the cat"`, and 10% to other words).
*   Finally, we multiply these weights with the corresponding **Value (V)** vectors to merge the information.

Thanks to this mechanism, the word `"it"` after passing through the attention layer carries the contextual meaning of `"the dog"`. This is how AI understands the deep context of language!
