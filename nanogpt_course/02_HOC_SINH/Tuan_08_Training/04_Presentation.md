# Shooting Basketballs — How AI Self-Corrects

How does a child learn to shoot a basketball into a hoop?
*   On the first try, the child throws too hard, and the ball flies over the backboard. The brain registers: *"Too much force, angled too high"*.
*   On the second try, the child reduces the force, but the ball falls short of the rim. The brain registers: *"Not enough force"*.
*   After hundreds of trials and micro-adjustments to the posture and force, the child naturally finds the perfect form to score consistently.

Training a Large Language Model works on the exact same principle. The AI brain starts with completely random weights (parameters). The training loop is a sequence of actions repeated thousands of times:

1.  **Get Batch:** Select a random group of input sequences `X` and targets `Y`. The target `Y` is just the sequence `X` shifted right by one character (since we predict the next character).
2.  **Forward & Loss:** Let the model predict the next character and measure its "surprise" using the **Cross-Entropy Loss** function. If the model guesses completely wrong, the Loss will be very high; if it guesses correctly and confidently, the Loss will be very low.
3.  **Backward:** The Backpropagation algorithm calculates: *"To reduce the Loss, how much should we adjust each parameter up or down?"*. This direction of adjustment is called the **Gradient**.
4.  **Step:** The **AdamW** optimizer adjusts the weights slightly in the direction of the Gradient using a tiny step size called the **Learning Rate**.

Over thousands of loops, the model slowly rewrites its own "brain" until it can predict the next character with high accuracy.
