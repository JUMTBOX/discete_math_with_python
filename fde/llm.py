import os
import sys

from dotenv import load_dotenv
from openai import OpenAI

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    sys.exit("OPENAI_API_KEY가 없습니다. .env 파일을 확인하세요.")


client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "FDE(Forward Deployed Engineer)를 한 문장으로 설명해 줘."}
    ]
)

print(response.choices[0].message.content)
print(f"\n사용 토큰: 입력 {response.usage.prompt_tokens} / 출력 {response.usage.completion_tokens}")