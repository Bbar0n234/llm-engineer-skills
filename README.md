# LLM Engineer Skills

Коллекция навыков (skills) для [Claude Code](https://docs.anthropic.com/en/docs/claude-code) от практикующего LLM-инженера.

Каждый навык — это `SKILL.md` файл с инструкциями, паттернами и примерами, которые Claude Code подгружает в контекст при решении соответствующих задач.

## Навыки

| Навык | Описание |
|-------|----------|
| [Schema-Guided Reasoning](skills/schema-guided-reasoning/SKILL.md) | Паттерн направленного рассуждения LLM через Pydantic-схемы: structured output, constrained decoding, cascade, routing, adaptive planning |
| [Prompt Engineering](skills/prompt-engineering/SKILL.md) | Принципы написания системных промптов: signal-to-noise, Goldilocks zone, итеративная разработка, антипаттерны |

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
