from textwrap import dedent
from crewai import Task


class SoftwareDevTasks():
    def create_user_story(self, agent):
        return Task(description=dedent(f"""Your assignment involves the transformation of the given text into a meticulously crafted user story, adhering to the following structured format:
        1. **User Story:** Commence by pinpointing and explicitly defining the user's role. Construct the user story utilizing the template 'As a [role], I want [feature] so that [benefit]'.
        2. **Importance:** Elaborate on the cruciality of this user story within the scope of the project. Illuminate its influence on the overarching objectives and its capacity to address particular requisites or challenges.
        3. **Recommendation Steps:** Chart out the essential steps to fulfill the user story. This should encompass any requisite research, design, development, and testing phases.
        4. **Acceptance Criteria:** Determine and describe the criteria that will signify the user story's completion. These criteria should be quantifiable and verifiable.
        5. **Prerequisites:**  List any prerequisites that must be met before the user story can be initiated.
        6. **Thinks to think about:** List any thinks that should be considered before the user story can be initiated.

        Your endeavor is to ensure each element is thoroughly articulated and distinctly delineated, contributing to an exhaustive comprehension of the user story and its relevance to the project.

        Your final submission must encapsulate the user story, emphasizing its significance, recommended steps for achievement, and acceptance criteria, all constructed as per the guidance provided above.

                        """),
                    agent=agent,
                    expected_output="The user story, emphasizing its significance, recommended steps for achievement, and acceptance criteria, prerequisites, and things to thinks about all constructed as per the guidance provided above."
                    )

    def critisize_user_story(self, agent):
        return Task(description=dedent(f"""Your task is to conduct a thorough examination of the story provided, with the objective of uncovering any discrepancies, lacunae, or inconsistencies present within the narrative framework, character evolution, storyline advancement, or backdrop portrayal. Identify segments that exhibit a lack of lucidity, profundity, or cohesion. Subsequent to pinpointing these deficiencies, develop precise recommendations aimed at rectifying each identified gap, thereby augmenting the narrative's overall calibre. Propose enhancements such as elaborating on the characters' histories, enriching the setting's description, elucidating plot developments, or ameliorating the tale's continuity. Ensure that your propositions are constructive, tailored to fortify the story's appeal and intensify reader engagement.
        check user story for INVEST criteria, and in the end suggest how to implement this criteria to the user story.

         Your ultimate deliverable must consist of a detailed analysis pinpointing the narrative's shortcomings, accompanied by actionable suggestions for improvement, crafted as per the instructions delineated above.
         Do not recommend to split user story on multiple stories

        recommendation to improvement should be related to each section. Like

        SECTION_NAME
        RECOMMENDATION
        """),
                    agent=agent
                    )

    def improve_user_story(self, agent):
        return Task(description=dedent(f"""your task is improve user story according to recommendation. 
        leave same structure. 
        if recommendation gives you some improvements use it and add to user story.
        do not exclude anything from your user story. if recommendation is to exclude something, do not exclude it.
        in the end add things that was recommended to improved. 
        it is allowed to change structure a bit, but do not change things a lot. 
        """),
                    agent=agent
    )

    # TODO fix formater tasks
    # def task_format_content(self, agent, context_task):
    #     return Task(
    #     description=dedent(f"""Format the story content in markdown"""),
    #     expected_output='The entire user content formatted in markdown, with each section titled and the content below it. NUmneration shoud be own for each section.',
    #     context=[context_task],
    #     output_file="story.md",
    #     agent=agent
    #     )