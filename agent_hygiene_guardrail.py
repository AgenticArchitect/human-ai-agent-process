import re

# 🚫 Common ambiguous variable names to flag
AMBIGUOUS_NAMES = {"foo", "bar", "baz", "temp", "data", "val", "x", "y", "z"}

# ✅ Required comment patterns
COMMENT_HINTS = ["why", "purpose", "intent", "rationale"]

def check_variable_names(code):
    flagged = []
    pattern = re.compile(r"\b([a-zA-Z_][a-zA-Z0-9_]*)\b")
    for line_num, line in enumerate(code.splitlines(), 1):
        for match in pattern.findall(line):
            if match in AMBIGUOUS_NAMES:
                flagged.append((line_num, match))
    return flagged

def check_comments(code):
    missing = []
    for line_num, line in enumerate(code.splitlines(), 1):
        if "#" in line:
            comment = line.split("#", 1)[1].strip().lower()
            if not any(hint in comment for hint in COMMENT_HINTS):
                missing.append((line_num, comment))
    return missing

def run_guardrail(code):
    print("🔍 Running semantic hygiene check...\n")

    bad_vars = check_variable_names(code)
    weak_comments = check_comments(code)

    if bad_vars:
        print("🚫 Ambiguous variable names found:")
        for line, name in bad_vars:
            print(f"  Line {line}: '{name}'")

    if weak_comments:
        print("\n⚠️ Comments lacking rationale:")
        for line, comment in weak_comments:
            print(f"  Line {line}: '{comment}'")

    if not bad_vars and not weak_comments:
        print("✅ All checks passed. Code is semantically clean.")

# Example usage
if __name__ == "__main__":
    with open("sample_agent_output.py", "r") as f:
        code = f.read()
    run_guardrail(code)
