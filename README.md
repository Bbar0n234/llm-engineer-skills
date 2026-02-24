# LLM Engineer Skills

Коллекция навыков (skills) для [Claude Code](https://docs.anthropic.com/en/docs/claude-code) от практикующего LLM-инженера.

Каждый навык — это `SKILL.md` файл с инструкциями, паттернами и примерами, которые Claude Code подгружает в контекст при решении соответствующих задач.

## Навыки

| Навык | Описание |
|-------|----------|
| [Schema-Guided Reasoning](skills/schema-guided-reasoning/SKILL.md) | Паттерн направленного рассуждения LLM через Pydantic-схемы: structured output, constrained decoding, cascade, routing, adaptive planning |
| [Prompt Engineering](skills/prompt-engineering/SKILL.md) | Принципы написания системных промптов: signal-to-noise, Goldilocks zone, итеративная разработка, антипаттерны |
| [Meeting Summarizer](skills/meeting-summarizer/SKILL.md) | Транскрипция и суммаризация митингов: аудио/видео → транскрипт (AssemblyAI) → структурированное саммари с решениями, задачами и инсайтами |
| [AIDD Methodology](skills/aidd-methodology/SKILL.md) | AI-Driven Development — методология ведения проектов с LLM-агентом: Context First, двухуровневое планирование, итерации, ADR, структура документации |
| [Skill Authoring](skills/skill-authoring/SKILL.md) | Создание и структурирование скиллов для Claude Code: шаблоны, расположения, progressive disclosure, чеклист |

## Установка

Скопируй нужный навык в `~/.claude/skills/`:

```bash
git clone https://github.com/Bbar0n234/llm-engineer-skills.git
cp -r llm-engineer-skills/skills/schema-guided-reasoning ~/.claude/skills/
cp -r llm-engineer-skills/skills/prompt-engineering ~/.claude/skills/
```

После копирования Claude Code автоматически подхватит навыки — перезапуск не требуется.

## Автор

Станислав Феоктистов — LLM-инженер.

## Лицензия

[MIT](LICENSE)
