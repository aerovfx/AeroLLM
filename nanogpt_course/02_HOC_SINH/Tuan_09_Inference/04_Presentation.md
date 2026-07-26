# The Creative Slider of Artificial Intelligence

Once the AI is trained, how does it generate text? This process is called **Inference**. The AI writes text word by word: it reads your prompt, predicts the next word, appends it, and then reads the entire new sentence to predict the following word.

However, if at each prediction step, the AI always selects the word with the absolute highest probability (called **Greedy Sampling**), the generated output will be incredibly boring, repetitive, and robotic. Humans, on the other hand, occasionally choose unexpected or unique words.

To control the AI's personality, scientists introduced a fascinating parameter: **Temperature** (creative temperature).
*   **Low Temperature (Temperature < 0.5):** The AI becomes very cautious and conservative. It magnifies the difference between the top word and the rest, making the most likely word dominate. The output is highly logical and repetitive, perfect for solving math or writing code.
*   **Medium Temperature (Temperature = 0.7 - 1.0):** The AI achieves an ideal balance between logic and creativity. It writes naturally and smoothly.
*   **High Temperature (Temperature > 1.2):** The AI becomes highly creative, adventurous, and erratic. It flattens the probability differences between words, allowing the AI to sample rare words. The output is highly unexpected and creative, but if set too high (like `2.0`), the AI will generate gibberish and spell words incorrectly.

To prevent the AI from picking completely nonsensical words (e.g., choosing `"galaxy"` while describing a recipe), we apply **Top-K Sampling**. We restrict the AI to sample only from the top $K$ (e.g., 50) highest-scoring words, filtering out all the irrelevant vocabulary.
