
import os
from dotenv import load_dotenv
from openai import OpenAI

# 加载 .env 文件
load_dotenv()

api_key = os.getenv("DEEPSEEK_API_KEY")
model_name = os.getenv("DEEPSEEK_MODEL", "deepseek-flash")

if not api_key:
    raise ValueError(
        "没有找到 DEEPSEEK_API_KEY，请检查 .env 文件"
    )

# 使用 OpenAI 兼容 SDK 连接 DeepSeek
client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com",
    timeout=60.0,
    max_retries=2,
)


def ask_model(system_prompt, user_prompt):
    """发送请求并返回模型生成的文本。"""

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        stream=False,
    )

    result = response.choices[0].message.content

    if not result:
        raise RuntimeError("模型没有返回有效文本")

    return result
