## 🛡️ Proposing or Refining Guardrails

Guardrails are critical for ensuring safe, readable, and compliant agent behavior. We welcome contributions that improve agent hygiene, prevent misuse, or enhance traceability.

### 🧩 Guardrail Types

- **Behavioral**: Prevents agents from acting outside defined roles.
- **Structural**: Enforces naming conventions, modularity, or trace logs.
- **Compliance**: Ensures outputs meet ethical or legal standards.

### 📐 Contribution Guidelines

1. **Describe the Guardrail Clearly**
   - What behavior does it enforce or prevent?
   - Why is it necessary?

2. **Provide a Test Case**
   - Add a JSON file to `examples/` that demonstrates the guardrail in action.
   - Include both valid and invalid scenarios.

3. **Implement in a Modular Way**
   - Guardrails should be easy to toggle or extend.
   - Avoid hardcoded logic—use config-driven design if possible.

4. **Document the Guardrail**
   - Add a comment block explaining its purpose and scope.
   - If applicable, link to related issues or discussions.

### 🧪 Example Test Case Format

```json
{
  "input": {
    "agent_role": "data_cleaner",
    "user_request": "delete all logs"
  },
  "expected_behavior": "Reject request with compliance warning"
}
