
# eProsima-CI CODE STYLE

These are some guidelines for repository style.
These are not hard rules, but more like suggestions in order to keep a uniform, clean and readable project.

---

## Yaml

### Yaml Extension

Use `.yml` extension when possible.

### Yaml Strings

Follow these rules in order to decide how to encapsulate a string:

1. Whenever applicable use the unquoted style since it is the most readable.
2. Use the single-quoted style `'` if characters such as `"` and `\` are being used inside the string to avoid escaping them and therefore improve readability. Use it also for empty strings `''`.
3. Use the double-quoted style `"` when the first two options aren't sufficient, i.e. in scenarios where more complex line breaks (`\n`) are required or non-printable characters are needed.

---

## Actions

Every action and workflow must have its own `description` tag associated with a quick look on what it does.
For further information regarding how to use it or specific design decisions, use YAML comments.
