# AI 学习规划助手（AI Study Planner）

一个基于 Python 和 DeepSeek API 开发的多 Agent 学习规划助手。用户输入学习目标、每日可投入时间和学习周期后，系统通过多个 Agent 协作，自动生成学习计划、拆解每日任务，并对计划进行检查与优化。

## ✨ 项目简介

在学习新知识或掌握新技能时，学习者经常面临目标不明确、任务安排不合理、缺乏阶段性检查等问题。

本项目尝试使用多 Agent 协作的方式，将学习规划任务拆分为三个环节：

1. **规划 Agent（Planner Agent）**：根据用户的学习目标和时间安排，生成整体学习计划。
2. **任务拆解 Agent（Task Agent）**：将整体计划拆分为具体、可执行的每日学习任务。
3. **审核 Agent（Review Agent）**：检查学习计划的合理性、可执行性和时间分配，并提出优化建议。

通过多个 Agent 的分工协作，帮助用户制定更加清晰、合理的学习计划。

## 🎯 项目功能

- **学习目标输入**：支持用户输入想要学习的内容或技能。
- **时间规划**：根据每日可用学习时间和学习周期制定计划。
- **学习计划生成**：自动生成阶段性学习安排。
- **每日任务拆解**：将学习目标细化为可执行的任务。
- **计划审核与优化**：检查计划是否合理，并提供改进建议。
- **多 Agent 协作**：通过不同角色的提示词完成规划、拆解和审核。

## 🛠️ 技术栈

| 技术 | 用途 |
|---|---|
| Python | 项目主要开发语言 |
| DeepSeek API | 提供大语言模型能力 |
| OpenAI Python SDK | 通过兼容接口调用模型 |
| python-dotenv | 从 `.env` 文件读取环境变量 |
| Multi-Agent | 实现不同 Agent 之间的任务分工 |
| Git / GitHub | 项目版本管理与代码托管 |

## 📁 项目结构

```text
python_multi_agent/
├── main.py              # 程序入口，接收用户输入并组织 Agent 协作
├── agents.py            # 定义 Agent 及其角色提示词
├── model_client.py      # 封装 DeepSeek API 调用
├── .env                 # 存放 API 密钥（不上传到 GitHub）
├── .gitignore           # 配置 Git 忽略文件
├── requirements.txt     # 项目依赖清单
└── README.md            # 项目说明文档
```

> `.venv/` 是 Python 虚拟环境目录，通常不需要上传到 GitHub。`.env` 中的 API 密钥也必须保密。

## 🚀 环境要求

- Python 3.10 或更高版本（建议使用 Python 3.11 或 3.12）
- 可正常访问的 DeepSeek API 服务
- DeepSeek API Key
- Git（如果需要使用 GitHub 管理项目）

## ⚙️ 安装与运行

### 1. 克隆项目

```bash
git clone https://github.com/你的GitHub用户名/python_multi_agent.git
cd python_multi_agent
```

将命令中的仓库地址替换为你自己的 GitHub 仓库地址。

### 2. 创建虚拟环境

Windows 用户可以在 VS Code 终端中执行：

```powershell
python -m venv .venv
```

激活虚拟环境：

**PowerShell：**

```powershell
.\.venv\Scripts\Activate.ps1
```

如果遇到 PowerShell 脚本执行策略限制，可以临时执行：

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

然后再次激活虚拟环境。

**或者使用 CMD：**

```cmd
.venv\Scripts\activate.bat
```

### 3. 安装依赖

如果项目中已有 `requirements.txt`：

```bash
python -m pip install -r requirements.txt
```

如果尚未创建依赖文件，可以执行：

```bash
python -m pip install openai python-dotenv
```

### 4. 配置 API Key

在项目根目录创建 `.env` 文件，添加以下内容：

```dotenv
DEEPSEEK_API_KEY=替换为你的DeepSeek_API_Key
DEEPSEEK_MODEL=deepseek-flash
```

请将示例密钥替换为你自己的有效 API Key。如果该模型名称不可用，请根据 DeepSeek 当前提供的模型列表调整 `DEEPSEEK_MODEL`。

### 5. 运行项目

```bash
python main.py
```

根据终端提示输入学习目标、每日可用时间和学习周期，即可尝试生成学习计划。

## 💡 使用示例

假设用户输入：

```text
学习目标：学习 Python 编程
每日可用时间：2 小时
学习周期：14 天
```

系统将依次完成以下任务：

1. Planner Agent：制定 14 天的整体学习路线。
2. Task Agent：将学习路线细化为每日学习任务。
3. Review Agent：审核时间安排和任务难度，并提出优化建议。

最终输出包括整体学习计划、每日任务清单以及计划审核结果。

> 以上为预期使用示例，实际输出内容取决于模型响应和当前项目代码。

## 🔄 Agent 工作流程

```text
用户输入学习需求
        ↓
Planner Agent
生成整体学习计划
        ↓
Task Agent
拆解每日学习任务
        ↓
Review Agent
审核并提出优化建议
        ↓
输出最终学习规划
```

## 🔐 安全说明

- 不要将真实 API Key 上传到 GitHub。
- 确保 `.gitignore` 中包含 `.env` 和 `.venv/`。
- 不要在代码、README、截图或提交记录中公开 API 密钥。
- 如果 API Key 意外泄露，应及时在服务提供方处撤销或更换。

建议 `.gitignore` 至少包含：

```gitignore
.env
.venv/
venv/
__pycache__/
*.pyc
```

## 📌 当前项目说明

本项目目前定位为一个用于学习 Python、LLM API 调用和多 Agent 协作的练习项目。

当前设计采用顺序执行方式，由规划 Agent、任务拆解 Agent 和审核 Agent 依次完成工作。后续可以根据实际开发进度扩展更多功能。

## 🔮 后续优化方向

- [ ] 增加异常处理和 API 调用失败重试机制。
- [ ] 优化学习计划的格式和可读性。
- [ ] 支持根据用户基础水平定制学习路线。
- [ ] 增加学习进度记录与计划调整功能。
- [ ] 使用 LangGraph 管理 Agent 的状态和执行流程。
- [ ] 开发 Web 用户界面，提升交互体验。
- [ ] 增加学习计划导出功能，例如 Markdown 或 PDF。

## 📚 学习收获

通过本项目，可以练习和理解：

- Python 项目结构与模块化开发。
- 第三方 API 的调用与封装。
- 环境变量和 API 密钥管理。
- Agent 角色设计与提示词编写。
- 多 Agent 顺序协作的基本思路。
- Git 与 GitHub 的基本使用。

## 📄 License

本项目目前尚未指定开源许可证。如需公开开源，可以根据项目用途选择合适的许可证，例如 MIT License。
