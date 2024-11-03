### Idea
The machine is meant to become the artist, and Gschichtefritz will present this "machine art" to explore the boundaries between artificial intelligence and artistic intelligence.

*Note:* The Transformer architecture, and thus the Large Language Models (LLMs) like GPT based on it, did not exist at that time.

### Concept
The song Dino Stampf Stampf, now with 35 verses (from the children's stories of the Blue Dino), will serve as a "large existing dataset" / "Big Data."
The computer is meant to learn from this text alone. It won’t receive any additional information about language, words, grammar, or anything else.
Afterward, the computer should generate text on its own.

### Result
I read the generated text aloud a video:  

[![YouTube Video](https://img.youtube.com/vi/466jykoAUdI/0.jpg)](https://www.youtube.com/watch?v=466jykoAUdI)  

Occasionally, words or short phrases from the original text appeared, followed by various word mixes or entirely new words that still sounded like Swiss German. The result reminds me of Dadaism and Franz Hohler's Totemügerli, with the difference that the text wasn’t created by a human but was written by a computer within milliseconds.

### How Does It Work?

I used a character-based Recurrent Neural Network with Long Short-Term Memory cells, or "LSTM RNN." Character-based means that instead of feeding words into the computer, we give it individual characters. Since capitalization is irrelevant for this task, I converted all letters to lowercase. For instance, "Gmües" becomes "gmües," reducing the song's character vocabulary to 38 distinct symbols (lowercase letters "abcdef...z," umlauts "üöä," punctuation, spaces, and line breaks). The neural network is then trained to predict the next character by providing it with the current text and the correct answer, character by character. In machine learning, this is called "supervised learning," where the network receives both input and the correct output during training.

Here’s a step-by-step example: The network should learn from the text "gmües iss ich de ganzi tag."

#### Training:

1. The first character ("g") is provided as input, with the "correct answer"—the expected output—being the next character, "m" from "gmües." It's like saying, "If you want to learn what I’m teaching, you first need to know that after 'g' comes 'm.'"
1. The second character, "m," is given as input with the expected output "ü." It’s like telling the network, "If you see an 'm' and previously saw a 'g,' you should output 'ü'." The network must remember the "g" from the previous step, hence the use of a "Recurrent Neural Network," which relies not only on the current input but also on the sequence of previous inputs. LSTM cells provide the ability to store this context information.
1. The third character, "ü," is given as input with "e" as the output.
1. The fourth character, "e," is given as input with "s" as the output.
1. The fifth character, "s," is given as input with a space " " as the output. By now, the network has learned the word "gmües" and that it should be followed by a space.
This process is repeated across the entire 6,662-character song many times. I deliberately left out the chorus.

#### Sampling:
Next, we feed the neural network an initial sequence (e.g., "wa") and repeatedly ask for the next character. This quickly results in a text of any desired length.

A neural network's quality isn’t judged by how well it memorizes the input. Memorizing is trivial for a computer. The goal is to learn something general, producing fitting output even for previously unseen input. This also influences training. If the network’s settings (hyperparameters) are unsuitable or the training period is too short, it will underfit, generating short, random-looking character strings, like "wai se ee i i snnih." At the other extreme, if the network memorizes too much and is overtrained, it will largely replicate the original text it was trained on.

Those familiar with the song may recognize in the generated output certain original phrases, alongside amusing, Swiss German-sounding words like "nürzs" or "gmüch," or word variations like "furke" instead of "gurke." The "denttergine" probably has something to do with an eggplant, and the "himbeerine" would certainly be something the Blue Dino would love to try.

This was inspired by Andrej Karpathy's blog post [The Unreasonable Effectiveness of Recurrent Neural Networks](https://karpathy.github.io/2015/05/21/rnn-effectiveness/).
