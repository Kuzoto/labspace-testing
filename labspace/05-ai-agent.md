# Task 4: Agentic Software Testing 🤖

You may have noticed some challenges with using AI chatbots for generating tests in the previous task, including:
* difficulties formulating prompts to achieve a reasonable output;
* an inability to execute the generated tests to collect results and coverage info;
* lack of integration with other development tools and the environment;
* etc...


## Agentic SE

An **agent** is an AI system that can pursue a multi-step goal autonomously by combining reasoning, tool use, memory, and self-correction in a loop. Agentic approaches in software engineering leverage intelligent agents that autonomously execute tasks to improve the efficiency and effectiveness of the development process.[^1] Unlike AI chatbots for prompting which often require users to interactively refine prompts and provide context (see Task 3), agents can actively analyze codebases, understand requirements, and run tools with minimal human intervention. Tools supporting agentic approaches include [Claude Code](https://code.claude.com/docs/en/overview), [GitHub Copilot](https://github.com/features/copilot/agents), and [OpenCode](https://opencode.ai/), among others.


In this task you will design an AI-based agent that automates the verification pipeline — using a locally-running open-source LLM (Qwen2.5-Coder 7B) in Claud to generate test cases, execute the tests to ensure they pass and meet coverage goals, run external tools to determine coding standards are met, and then use this information to produce a recommendation whether the code meets the specified requirements.

## Agentic Setup 🌠

There are many different methods to design and apply agents to SE and testing tasks. This activity is based on the [Constellize](https://www.constellize.com/) method by Steven Atkinson (aka Dr. A). Constellize uses memory banks (embedded knowledge), skills (prompts), and agents (personas) to overcome core challenges with AI-assisted developent. This simplified version only focuses on a sample of skills/agents and it does not incorporate the memory bank, but more details on the overall method are available [here](https://github.com/constellize/marketplace).[^2]

We will use this modified constellize method with Qwen 2.5 in Claude Code. First, run the following commands to install and configure Claude Code:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

```bash
export ANTHROPIC_AUTH_TOKEN=ollama
export ANTHROPIC_API_KEY=""
export ANTHROPIC_BASE_URL=http://localhost:11434
```

```bash
export PATH="$HOME/.local/bin:$PATH" >> ~/.bashrc && source ~/.bashrc
```

Then, launch Claude code with the qwen2.5-coder model in the Task 4 folder.

```bash
cd ~/project/task4-agent/ && ollama launch claude --model qwen2.5-coder
```

Set up the initial configurations (the default options should be fine for this workshop). Once completed, you should see a welcome screen for Claude Code with qwen2.5-coder in your terminal.

![Code Code](./images/claude.png)

Press **Ctrl^C** twice to exit Claude code and use the `clear` command to clear the terminal console. Next, we will configure our agentic testing approach. Your job will be to update the agents skills and personas to test and verify the behavior of the **command-line-quiz** application.

## Step 1: Add Requirement Specifications

Requirements are essential for understanding the functionality of a program. Using your knowledge from previous course content, update the **command-line-quiz** :fileLink[QA Engineer]{path="task4-agent/sample_app/README.md"} to add acceptance criteria to help with validating the program behavior.

## Step 2: Update Skills

**Skills** are structured workflows with defined phases and outputs — like recipes AI follows. Skills are invoked with slash commands (i.e., `/verify` or `/test` in the command line). 

An overview of the skills for this task can be found in :fileLink[skills/README.md]{path="task4-agent/.claude/skills/README.md"}.

**test**

Open :fileLink[test/SKILL.md]{path="task4-agent/.claude/skills/test/SKILL.md"}. This file outlines the behavior for generating unit tests for the application. Navigate to the `<instructions>` tag to add details about how the agent should behave when generating unit tests for the program.

**verify**

Open :fileLink[verify/SKILL.md]{path="task4-agent/.claude/skills/verify/SKILL.md"}. This file outlines the behavior for verifying the program and test suite are ready for deployment. There are four quality gates that must pass in order for the application to be designated as VERIFIED: test integrity, health check, deployment readiness, and maintainability. For each gate, update the pass criteria (what needs to happen for this gate to pass) and the _if this gate fails_ section to outline the agent behavior if the gate check fails.

## Step 3: Review Agent Personas

**Agents** are role definitions that shape how AI approaches a task — like perspectives AI adopts. While a skill defines what to do, an agent defines who is doing it.

An overview of the agents for this activity can be found in :fileLink[agents/README.md]{path="task4-agent/.claude/agents/README.md"}. Please review the personas related to each of the agents below. If desired, you may make changes to the agent roles and descriptions.

**QA Engineer**

The :fileLink[QA Engineer]{path="task4-agent/.claude/agents/qa-engineer.md"} is responsible for generating tests for the program with the intent of finding bugs.

**Feature Architect**

The :fileLink[Feature Architect]{path="task4-agent/.claude/agents/feature-architect.md"} ensures that the program meets the specified requirements and is ready for deployment to users.

## Step 4: Run the Agent

Navigate to the task directory and run the following to start Claude code:

```bash
ollama launch claude --model qwen2.5-coder
```

By typing a backslash (`/`), you should see several commands appear, including one for the added skills `/test` and `verify`. 
1. Run the `/test` command. If prompted, answer any questions provided by the agent personas to help generate unit tests. 
2. Run the `/verify` command. If prompted, answer any questions provided by the agent personas to help verify the program. An output report should be generated to provide details on the verification process.

> [!NOTE]
> You may experience extended delays, timeouts, and/or crashes for this task due to several factors (e.g., using Claude Code with a non-Anthropic OSS model, running this in a browser through an IDE in a minimal Docker container, not using the Claude Code for VS Code plugin, etc.). You can try restarting the labspace to see if that helps, but I apologize in advance if you run into any issues. If you are unable to run the agents, you may skip Step 5 and go straight to the reflection questions.

## Step 5: Review the Generated Tests

After the agent runs, open the generated test file and evaluate it:

- Does it test all the functions in `quiz.py`?
- Does it test edge cases (i.e., empty string, uppercase vs. lowercase, non-alpha characters, etc.)?
- Is the coverage low or are the tests missing important cases?
- What questions were you asked by the agent in the testing and verification process (if applicable)?
- How does the quality compare to what you would write by hand?

If you were unable to run the agent, please note so here and continue.

## Reflection

With your partner or small group, discuss the following and record your responses:

- How did the agentic approach in this task compare to the prompt-based approach for Task 3? Please discuss the process to generate tests in addition to critiquing the output generated tests.
- What criteria did you set for the test and verify skills? Why?
- If you had more time, what other checks and functionality would you include in the agents?
- In general, what are your perceptions on the future of testing and maintenance in the age of AI?

---

**Congratulations — you've completed the testing workshop tasks! 🎉**

## Submission

Please create a GitHub repo with the updated files for each task and your `reflection.txt` file, clearly labelled with the reflections for each task. (If you need a refresher on creating a GitHub repo, see the [SE Basics workshop](https://github.com/chbrown13/labspace-se-basics/blob/main/.labspace/04-git.md#-activity-lets-create-a-remote-repo)). If you encountered any issues with this workshop, please share them [here](https://github.com/chbrown13/labspace-testing/issues). To receive credit, please submit your GitHub repository link on [Canvas](https://canvas.vt.edu/courses/224123/assignments/2699644). 

[^1]: Hassan, Ahmed E., et al. "[Agentic software engineering: Foundational pillars and a research roadmap](https://arxiv.org/abs/2509.06216)". arXiv preprint arXiv:2509.06216 (2025).

[^2]: Steve Atkinson. "The Constellize Method: Building Software Systems from Knowledge". Constellize Press, October 2025.