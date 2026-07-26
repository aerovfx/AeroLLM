# The Council of Experts and Solo Reflection Time

When humans read a poem, our brains do not focus on just one single aspect:
*   One part of our brain pays attention to the **rhyme** (melody).
*   Another part focuses on the **subject and verb** (grammar).
*   Another part focuses on the **emotion** (sadness or joy).

If the AI model had only one attention head (Single-head attention), its viewpoint would be limited and it could only learn one type of connection. To make the AI truly smart, we need **Multi-Head Attention**.

Imagine organizing a product design meeting. Instead of having just one person make decisions, you invite 4 experts: one for finance, one for art, one for engineering, and one for marketing. All 4 experts read the same design request (Query, Key, Value) but analyze it from their own professional angles. Once they finish discussing, we merge their outputs (Concatenate) into a single optimized design.

However, after the group discussion (Attention), each word needs its own private time to process the gathered information and draw conclusions. This is the job of the **MLP (Multi-Layer Perceptron)** layer, also known as the Feed-Forward Network.

In the MLP layer, the word's information is expanded 4 times larger to "think" deeper, passed through the **GELU** non-linear activation function to discard useless details, and compressed back to its original size. This operation runs independently for each word, with no cross-talk between words, preserving the individuality of the data.
