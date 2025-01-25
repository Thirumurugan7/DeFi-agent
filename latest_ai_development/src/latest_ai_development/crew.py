# src/latest_ai_development/crew.py
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from .tools.transfer_tool import TransferTool

@CrewBase
class TokenTransferCrew():
    """Token Transfer crew"""

    @agent
    def validator(self) -> Agent:
        return Agent(
            config=self.agents_config['validator'],
            verbose=True
        )

    @agent
    def transfer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['transfer_agent'],
            verbose=True,
            tools=[TransferTool()]
        )

    @task
    def validate_transfer(self) -> Task:
        return Task(
            config=self.tasks_config['validate_transfer']
        )

    @task
    def execute_transfer(self) -> Task:
        return Task(
            config=self.tasks_config['execute_transfer']
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Token Transfer crew"""
        return Crew(
            agents=[self.validator(), self.transfer_agent()],
            tasks=[self.validate_transfer(), self.execute_transfer()],
            process=Process.sequential,
            verbose=True,
        )
