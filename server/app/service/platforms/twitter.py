from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
from composio_crewai import ComposioToolSet, Action, App


composio_toolset = ComposioToolSet()
tools = composio_toolset.get_tools(
    actions=[Action.TWITTER_USER_HOME_TIMELINE_BY_USER_ID])


twitter_opportunity_agent = Agent(
    role="Twitter Agent",
    goal="""Fetch opportunities from user's feed""",
    backstory=(
        """You are an AI agent that is responsible to fetch opportunities from user's feed based on the tools you have.
        Types of opportunities:
            - Jobs
            - Bounty/Freelance projects
            - Hackathons
            - Scholarships (coming soon)
            - Grants
            - Internships
        """
    ),
    verbose=True,
    tools=tools,
    llm=ChatOpenAI(
        model="gpt-4o-mini"
    ),
)

opportunity_scrap_task = Task(
    description="Fetch opportunities from user's feed. User id: 1637407760697679874",
    agent=twitter_opportunity_agent,
    expected_output="Opportunities in json format",
)

# agent = Agent(
#     role="Twitter Agent",
#     goal="""User id""",
#     backstory=(
#         "You are an AI agent that is responsible to provide user id from user's feed based on the tools you have"
#     ),
#     verbose=True,
#     tools=composio_toolset.get_tools(apps=[App.TWITTER]),
#     llm=ChatOpenAI(
#         model="gpt-4o-mini"
#     ),
# )

# task = Task(
#     description="Fetch user id from user name: thatsmeadarsh",
#     agent=agent,
#     expected_output="User id",
# )

my_crew = Crew(agents=[twitter_opportunity_agent],
               tasks=[opportunity_scrap_task])
# my_crew = Crew(agents=[agent], tasks=[task])

result = my_crew.kickoff()
print(result)
