import re
import yaml

CONFIG_PATH = "config/agent_config.yaml"

def load_config(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def check_variable_names(code, config):
    flagged = []
    pattern = re.compile(r"\b([a-zA-Z_][a-zA-Z0-9_]*)\b")
    allowed = set(config["overrides"]["allow_names"])
    blacklist = set(config["hygiene"]["ambiguous_names"])
    for line_num, line in enumerate(code.splitlines(), 1):
        for match in pattern.findall(line):
            if match in blacklist and match not in allowed:
                flagged.append((line_num, match))
    return flagged

def check_comments(code, config):
    missing = []
    hints = config["hygiene"]["comment_hints"]
    allowed = set(config["overrides"]["allow_comments"])
    for line_num, line in enumerate(code.splitlines(), 1):
        if "#" in line:
            comment = line.split("#", 1)[1].strip().lower()
            if not any(hint in comment for hint in hints) and comment not in allowed:
                missing.append((line_num, comment))
    return missing

def run_guardrail(code, config):
    print("🔍 Running semantic hygiene check...\n")

    bad_vars = check_variable_names(code, config) if config["hygiene"]["enforce_variable_names"] else []
    weak_comments = check_comments(code, config) if config["hygiene"]["enforce_comments"] else []

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
    config = load_config(CONFIG_PATH)
    with open("sample_agent_output.py", "r") as f:
        code = f.read()
    run_guardrail(code, config)
