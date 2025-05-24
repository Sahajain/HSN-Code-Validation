#  HSN Code Validation Agent (Google ADK Framework)

This agent validates HSN codes using a master dataset, following the Google ADK (Agent Developer Kit) architecture.

##  Agent Components

- **Intent:** ValidateHSNCode
- **Entity:** HSNCode (Regex-matched)
- **Policy:** Route inputs based on keywords
- **Fulfillment:** Reads Excel file and checks code validity
- **Context Manager:** Extracts codes from user input

##  Structure
- `intents.json`: Defines intents & training phrases
- `entities.json`: Defines the HSN code pattern
- `fulfillment.py`: Executes validation logic
- `policy.py`: Maps input to intent
- `context_manager.py`: Extracts codes from input
- `agent.py`: Main loop simulating agent behavior

##  Run the Agent
```bash
python agent.py
```

Example input:
```
>> Validate 01012100, 9999
```


