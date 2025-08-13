import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool
from typing import List

# Disable telemetry
os.environ["CREWAI_TELEMETRY_ENABLED"] = "false"
# Make sure your Serper API key is set
# export SERPER_API_KEY="your_api_key_here"

# Initialize the Serper tool for Norway
serper_tool = SerperDevTool(
    country="no",
    locale="no",
    location="Norway",
    n_results=5
)

@CrewBase
class MarketingCrew():
    """MarketingCrew for Norwegian content"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Agents
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'], # type: ignore[index]
            verbose=True,
            tools=[serper_tool]
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'], # type: ignore[index]
            verbose=True
        )

    @agent
    def content_creator_social(self) -> Agent:
        return Agent(
            config=self.agents_config['content_creator_social'], # type: ignore[index]
            verbose=True
        )

    @agent
    def content_blog_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['content_blog_writer'], # type: ignore[index]
            verbose=True
        )

    @agent
    def seo_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['seo_specialist'], # type: ignore[index]
            verbose=True
        )

    # Tasks
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'], # type: ignore[index]
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'], # type: ignore[index]
            output_file='report.md'
        )

    @task
    def content_social_task(self) -> Task:
        return Task(
            config=self.tasks_config['content_social_task'], # type: ignore[index]
        )

    @task
    def blog_task(self) -> Task:
        return Task(
            config=self.tasks_config['blog_task'], # type: ignore[index]
        )

    @task
    def seo_task(self) -> Task:
        return Task(
            config=self.tasks_config['seo_task'], # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the MarketingCrew crew"""
        return Crew(
            agents=self.agents,  # auto-created by @agent
            tasks=self.tasks,    # auto-created by @task
            process=Process.sequential,  # tasks depend on previous
            verbose=True,
        )
