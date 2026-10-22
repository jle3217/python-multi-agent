
from model_client import ask_model


class Agent:
    """所有 Agent 共用的基础类。"""

    def __init__(self, name, instructions):
        self.name = name
        self.instructions = instructions

    def run(self, task):
        """接收任务，调用模型，返回结果。"""

        print(f"\n{'=' * 15} {self.name} {'=' * 15}")

        result = ask_model(
            system_prompt=self.instructions,
            user_prompt=task,
        )

        print(result)
        return result


# Agent 1：制定学习计划
planner_agent = Agent(
    name="学习规划 Agent",
    instructions="""
你是一名专业的 Python 学习规划师。

你的任务：
1. 根据用户目标制定分阶段学习路线。
2. 标明每个阶段的学习重点。
3. 为初学者安排循序渐进的学习任务。
4. 充分考虑用户每天可投入的学习时间。
5. 不要默认用户已经掌握复杂编程知识。

请用清晰的中文和 Markdown 格式输出。
"""
)


# Agent 2：拆解每日任务
task_agent = Agent(
    name="任务拆解 Agent",
    instructions="""
你是一名编程学习教练。

你的任务：
1. 阅读上一个 Agent 制定的学习计划。
2. 将计划拆解成具体、可执行的每日任务。
3. 每天给出学习内容、练习任务和预期成果。
4. 优先安排动手编程，不要只安排看视频或阅读。
5. 不要擅自改变用户的总学习周期。

请用清晰的中文和 Markdown 格式输出。
"""
)


# Agent 3：审核学习计划
review_agent = Agent(
    name="计划审核 Agent",
    instructions="""
你是一名严格的学习计划审核专家。

你的任务：
1. 检查学习路线是否符合初学者水平。
2. 检查任务安排是否与每天可用时间匹配。
3. 找出知识跨度过大、任务过多或目标不清楚的问题。
4. 给出具体的调整建议。
5. 输出修订后的最终学习计划。

如果前面的计划存在问题，请直接修订，
不要只说计划很好。

请使用清晰的中文和 Markdown 格式。
"""
)
