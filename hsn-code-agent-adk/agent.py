from adk_components.policy import route_intent
from adk_components.context_manager import extract_codes
from adk_components.fulfillment import FulfillmentEngine

def main():
    agent = FulfillmentEngine("data/HSN_SAC.xlsx")
    print("HSN Code Validation Agent (Google ADK Structured)")

    while True:
        user_input = input(">> ")
        if user_input.lower() in ["exit", "quit"]:
            break

        intent = route_intent(user_input)
        if intent == "ValidateHSNCode":
            codes = extract_codes(user_input)
            results = agent.validate(codes)
            for code, result in results:
                print(f"{code}: {result}")
        else:
            print("Sorry, I didn't understand that. Try again.")

if __name__ == "__main__":
    main()
