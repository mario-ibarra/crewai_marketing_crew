# Marketing Crew AI Project

[![crewAI](https://img.shields.io/badge/powered%20by-crewAI-green?style=for-the-badge)](https://www.crewai.com/)
[![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)](https://www.python.org/)

This project utilizes the `crewai` framework to create an autonomous crew of AI agents designed for marketing research and content creation. The crew collaborates to analyze a given topic, gather information, and produce a comprehensive report or article.

The current configuration is set up to research and write about **"How AI and AI tools are used in small businesses around Norway, and what the future market is for these tools"** (original: _"Hvordan AI og AI-verktøy brukes i småbedrifter rundt om i Norge, og hva som er fremtidsmarkedet for disse verktøyene"_).

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
  - [Running the Crew](#running-the-crew)
  - [Training the Crew](#training-the-crew)
  - [Replaying a Task](#replaying-a-task)
  - [Testing the Crew](#testing-the-crew)
- [Customization](#customization)
  - [Changing the Topic](#changing-the-topic)
  - [Modifying Agents and Tasks](#modifying-agents-and-tasks)
- [Contributing](#contributing)
- [License](#license)

## Project Description

The `MarketingCrew` is a team of specialized AI agents built with `crewai`. Each agent has a distinct role, from market research to content writing and final review. They work sequentially and collaboratively, passing their findings to the next agent in line, ensuring a well-researched, structured, and polished final output.

This project serves as a powerful example of how to automate complex workflows using multi-agent systems.

## Features

- **Autonomous Agent Collaboration:** Agents work together to achieve a common goal without manual intervention.
- **Specialized Roles:** The crew likely consists of agents like:
  - `MarketResearchAnalyst`: Scans the web for current trends, data, and articles on the given topic.
  - `ContentStrategist`: Defines the structure, key points, and narrative flow of the final article.
  - `ContentWriter`: Drafts the article based on the research and strategy provided.
  - `Editor`: Reviews the drafted content for clarity, grammar, and accuracy.
- **Dynamic Inputs:** Easily change the research topic directly from the `main.py` file.
- **Advanced `crewai` Features:** Includes built-in support for `train`, `replay`, and `test` functionalities for iterative development and evaluation.

## Project Structure

The project was initialized using `uv init` and follows a standard Python project layout.

## Installation

Follow these steps to set up and run the project locally.

**1. Prerequisites**

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) - A fast Python package installer and resolver.
- Git

**2. Clone the Repository**

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name

# LLM Provider (e.g., OpenAI, Groq, Anthropic)
OPENAI_API_KEY="sk-..."
# OPENAI_MODEL_NAME="gpt-4o" # Optional, defaults to gpt-4

# Search Tool (e.g., Serper, Tavily)
SERPER_API_KEY="..."

# Create a virtual environment
uv venv

# Activate the virtual environment
# On macOS/Linux
source .venv/bin/activate
# On Windows
.venv\Scripts\activate

# Install dependencies from pyproject.toml
uv pip sync pyproject.toml