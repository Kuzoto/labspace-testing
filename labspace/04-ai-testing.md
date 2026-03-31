# Task 3: AI-Generated Tests 🧪 

Unit testing is critical for software development and project success,[^1] yet a very time-consuming and burdensome task for software engineers---leading them to avoid writing unit tests altogether.[^2] Recent advancements in generative AI and LLMs have rapidly transformed how code is built and testing.[^3] 

In Tasks 1 and 2 you debugged and tested code manually. However, in this task you will explore using AI to generate tests for a given program. AI-generated testing capabilities are increasingly appearing in real software engineering pipelines and development tools,[^4] and this task uses a local open-source to simulate this task within a given codebase.

## The Model

The labspace runs [Ollama](https://ollama.com/), which hosts models locally. The agent uses **Qwen2.5-Coder 7B**, an open-source code-specialized model from Alibaba that performs well on tasks like test generation and code analysis.[^5]

## The Target Application

The agent will analyze :fileLink[sample_app/quiz.py]{path="task3-ai/sample_app/quiz.py"}. This application is a command-line tool allowing users to create and take simple quizzes in the terminal. 

### Key Features
1. **Question Creation:** 
* Users can interactively create and define their own quiz questions.
* Prompts the user to enter both the question and the correct answer.
2. **Quiz Storage:**
* Saves quizzes in JSON format, allowing for easy storage and retrieval.
* Quizzes are named by the user and saved as separate files.
3. **Quiz Loading:**
* Users can load existing quizzes to take them at any time.
* Checks if the quiz file exists before attempting to load it, providing user feedback.
4. **Quiz Randomization:**
* Randomizes the order of questions to ensure a different experience each time the quiz is taken.
5. **User Interface:**
* Provides a command-line menu for a user-friendly experience, allowing easy navigation between creating, taking, and exiting the quiz.
6. **Score Tracking:**
* Tracks and displays the user’s score after taking the quiz, providing immediate feedback.

You can run the program in the terminal and try it out.

```bash
cd ~/project/task3-ai/ && python sample_app/quiz.py
```

As you can also probably see, there are no tests for this application. Our goal is to try and fix this with AI...

## Step 1: Pull the Model

Before the agent can run, pull the model into the Ollama service. This downloads ~4 GB and
only needs to happen once — the model is cached in a named volume. _(This might take a while...)_

```bash
ollama pull qwen2.5-coder:7b
```

> [!NOTE]
> This command blocks until the pull completes and then prints a JSON summary. It may take
> a few minutes depending on network speed. Subsequent runs skip the download entirely.

Verify the model is ready with the following command:

```bash
curl -s http://ollama:11434/api/tags | python3 -m json.tool
```

You should see `qwen2.5-coder:7b` listed under `"models"`.

## Step 2: Generate Unit Tests

Next, we will use Qwen2.5-Coder to generate tests for this program. For this task, we will use a simple approaching---prompting the AI model to generate tests for this program. Use the following command to generate tests for the quiz.py file, using your own prompt:

```bash
ollama run qwen2.5-coder:7b "<your-prompt-here>"
```

> [!NOTE]
> A simple prompt could be something like "_Generate tests for quiz.py_". But you probably want to provide a prompt that is more specific.

Review the generated tests and answer the following reflection questions

## Reflection
Find a partner or form a small group to discuss the following (your responses should be added to the `reflection.txt` file):

- What prompt did you use to generate the tests? How could the prompt be improved? What challenges did you face forming the prompt?
- Evaluate the AI-generated tests. What did the model do well? What did it struggle with? Would you accept these tests as is to test this system in a production environment? Why or why not? 
- If applicable, provide insights on whether the AI-generated tests passed or failed and the effectiveness of the generated tests in terms of code coverage. If you were unable to assess this, please explain why.
- What are your experiences with using AI tools for testing? Summarize your and your classmates responses in the discussion (e.g., others' experiences, tools used, etc.).

Once this is complete, you are ready to move on to the final tasks!

[^1]: Ellims, Michael, James Bridges, and Darrel C. Ince. "[The economics of unit testing](https://doi.org/10.1007/s10664-006-5964-9)". Empirical Software Engineering 11.1 (2006): 5-31.
[^2]: LaToza, T. D., Venolia, G., and DeLine, R. "[Maintaining mental models: a study of developer work habits](https://doi.org/10.1145/1134285.1134355)". In Proceedings of the 28th international conference on Software engineering (Shanghai China, May 2006), ACM, pp. 492–501.
[^3]: Schäfer, Max, et al. "[An empirical evaluation of using large language models for automated unit test generation](https://doi.org/10.1109/TSE.2023.3334955)". IEEE Transactions on Software Engineering 50.1 (2023): 85-105.
[^4]: See https://survey.stackoverflow.co/2025/ai#developer-tools-ai-tool-plan-to-partially-use-ai and https://dora.dev/research/2025/
[^5]: https://qwen.ai/blog?id=qwen2.5-coder-family