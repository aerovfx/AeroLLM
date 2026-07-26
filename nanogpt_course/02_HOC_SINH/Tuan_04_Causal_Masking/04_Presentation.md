# Blindfolded Next-Word Prediction

Imagine taking a fill-in-the-blank exam. The exam requires you to continue writing a story from left to right. But instead of only seeing the pages you've already read, the proctor shows you the next pages containing all the answers. What would you do? Of course, you would copy the answers without thinking.

When AI learns a language, if there is no mechanism to prevent this, it will do the same "cheating." This phenomenon is called **future information leakage**. To fix this, we need a technical blindfold called **Causal Masking**.

In PyTorch, we represent this blindfold as a **Lower Triangular Matrix** (`tril`). Look at this 4x4 matrix:
```text
1  0  0  0
1  1  0  0
1  1  1  0
1  1  1  1
```
*   Row 1 represents the 1st word: It can only look at itself (1), the next positions are blocked (0).
*   Row 2 represents the 2nd word: It can look at word 1 and 2, but not 3 and 4.
*   ... and so on.

In the Attention calculation, the blocked positions (0) are replaced with **negative infinity** ($-\infty$) using `masked_fill`. When passed through the Softmax function to compute attention weights, since $e^{-\infty} = 0$, the probability of attending to future words is completely crushed to 0%.

Thanks to this magical blindfold, the AI is forced to use its brain and learn how to reason using only past words to predict the next one.
