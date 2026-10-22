
from agents import (
    planner_agent,
    task_agent,
    review_agent,
)


def run_multi_agent(goal, hours_per_day, days):
    """运行完整的多 Agent 学习规划流程。"""

    # 将用户需求整理成统一的任务描述
    user_request = f"""
    我的学习目标：{goal}
    每天可学习时间：{hours_per_day} 小时
    计划学习周期：{days} 天

    请根据以上条件制定学习方案。
    """

    # 第一步：规划 Agent 制定学习路线
    print("\n第一阶段：制定学习路线")

    plan = planner_agent.run(user_request)

    # 第二步：任务 Agent 接收第一步的结果
    print("\n第二阶段：拆解每日任务")

    task = f"""
    用户原始需求：
    {user_request}

    学习规划 Agent 的输出：
    {plan}

    请将这份学习计划拆解为每日任务。
    """

    daily_tasks = task_agent.run(task)

    # 第三步：审核 Agent 检查并修订
    print("\n第三阶段：审核与修订")

    review_input = f"""
    用户原始需求：
    {user_request}

    学习路线：
    {plan}

    每日任务：
    {daily_tasks}

    请审核以上内容，修正不合理之处，
    并输出完整的最终学习计划。
    """

    final_result = review_agent.run(review_input)

    return final_result


if __name__ == "__main__":
    print("===== Python 多 Agent 学习规划助手 =====")

    goal = input("你想学习什么？例如：Python 多 Agent：").strip()

    hours_text = input("每天可以学习几小时？例如：1：").strip()
    days_text = input("计划学习多少天？例如：14：").strip()

    try:
        hours = float(hours_text)
        days = int(days_text)

        if not goal:
            raise ValueError("学习目标不能为空")

        if hours <= 0 or days <= 0:
            raise ValueError("学习时间和天数必须大于 0")

        result = run_multi_agent(goal, hours, days)

        print("\n\n===== 最终学习计划 =====\n")
        print(result)

    except ValueError as error:
        print(f"输入错误：{error}")

    except Exception as error:
        print(f"程序执行失败：{error}")
        print("请检查 API Key、模型名称、网络连接和账户额度。")
