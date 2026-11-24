import os
import sys

from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    sys.exit("OPENAI_API_KEY 없음")

client = OpenAI()

PROMPT = """
다음 회의록에서 아래 3가지를 뽑아 주세요.

1. 결정 사항 (무엇을 하기로 했나)
2. 할 일 (누가, 언제까지)
3. 리스크 (진행을 막을 수 있는 것)

회의록: {text}
"""

def summarize(path: str) -> str:
    text = Path(path).read_text(encoding="utf-8")
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user", "content": PROMPT.format(text=text)}],
        temperature=0
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "data/회의록_0706_주간품질회의.txt"
    print(f"==={Path(path).name} 요약 ===\n")
    print(summarize(path))