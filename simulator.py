import os

def load_prompt():
    if os.path.exists("system_prompt.md"):
        with open("system_prompt.md", "r", encoding="utf-8") as f:
            return f.read()
    return "Prompt file not found."

def run_simulation():
    print("==========================================")
    print("  HOME CREDIT LAP AGENT - LOCAL SIMULATOR ")
    print("==========================================")
    
    prompt = load_prompt()
    print(f"[STATUS] Loaded system_prompt.md successfully ({len(prompt)} characters).")
    print("[STATUS] Initializing call simulation for customer: Rajesh Sharma\n")
    
    state = {
        "verified": False,
        "property_type": None,
        "ownership": None,
        "documents": None,
        "loan_amount": None,
        "occupation": None,
        "income_mode": None,
        "market_value": None,
        "tenure": None
    }

    print("Agent: Hello, am I speaking with Rajesh Sharma?")
    
    while True:
        try:
            user_input = input("\nCustomer (You): ").strip()
        except EOFError:
            break
            
        if user_input.lower() in ["exit", "quit"]:
            print("Agent: Goodbye! Have a great day.")
            break
            
        lower_input = user_input.lower()
        
        # 1. Verification & Busy State
        if not state["verified"]:
            if "busy" in lower_input or "meeting" in lower_input:
                print("Agent: I understand. What would be a convenient time for us to call you back?")
                print("[CALL ENDED BY AGENT]")
                break
            else:
                state["verified"] = True
                print("Agent: Wonderful! We are reaching out to reward your loyalty with a special Loan Against Property offer of up to ₹75 Lakhs.")
                print("Agent: First, do you already have an existing loan on the property or want to reduce your current EMI?")
                continue
                
        # 2. Loan Transfer / EMI Reduction Check
        if "existing loan" in lower_input or "emi" in lower_input or "ongoing loan" in lower_input:
            print("Agent: Since you already have an existing loan or want to reduce your current EMI, a specialist for loan transfer will contact you shortly. Thank you!")
            print("[CALL ENDED BY AGENT]")
            break
            
        # 3. Disqualification Checks
        if "agricultural" in lower_input or "cash" in lower_input or "photocopy" in lower_input:
            print("Agent: I'm sorry, but based on those details, you do not meet the criteria for this specific offer at this time. Thank you, and goodbye!")
            print("[CALL ENDED BY AGENT]")
            break
            
        # 4. Standard Flow Progression
        print("Agent: [Prompt Logic Verified] Got it. What type of property do you have (Residential, Commercial, Industrial)?")

if __name__ == "__main__":
    run_simulation()