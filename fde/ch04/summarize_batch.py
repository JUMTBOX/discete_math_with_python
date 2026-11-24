import os 
import sys
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

from summarize_poc import summarize

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    sys.exit("OPENAI_API_KEY 없음")

client = OpenAI()

folder = Path(sys.argv[1] if len(sys.argv) > 1 else "fde/ch04/data")
files = sorted(folder.glob("*.txt"))
print(f"회의록 {len(files)}건 요약 시작")

sections = []
for path in files:
    print(f"  - {path.name}")
    sections.append(f"### {path.stem}\n\n{summarize(path)}")


response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role":"user","content":"다음 회의 요약들을 종합해서 '이번 주 핵심 3줄'을 만들어 주세요:\n\n" + "\n\n".join(sections)}],
    temperature=0
)

briefing = (f"## 주간 브리핑\n\n{response.choices[0].message.content}\n\n---\n\n" + "\n\n".join(sections))
Path("fde/ch04/weekly_briefing.md").write_text(briefing, encoding="utf-8")
print("\nweekly_briefing.md 생성 완료")