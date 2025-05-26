import streamlit as st

# Basic email templates
EMAIL_TEMPLATES = {
    "Professional": (
        "Subject: Unlock Efficiency with {offering}\n\n"
        "Hi there,\n\n"
        "I'm {name} from {company}. I wanted to quickly share how our solution, {offering}, can help your team. "
        "One key benefit is that it {benefit}. We'd love to discuss how we could support your goals.\n\n"
        "Would you be open to a quick call this week?\n\n"
        "Best regards,\n{name}"
    ),
    "Friendly": (
        "Subject: Thought you might like this 🙂\n\n"
        "Hey there!\n\n"
        "I'm {name} from {company}. Just reaching out to share something cool – it's called {offering}. "
        "It’s helped others by {benefit}, and I thought it might be useful to you too.\n\n"
        "Let me know if you want to chat!\n\n"
        "Cheers,\n{name}"
    ),
    "Urgent": (
        "Subject: Don't miss this opportunity with {offering}!\n\n"
        "Hi,\n\n"
        "I’m {name} from {company}. I wanted to reach out quickly about {offering}, a solution that could make a huge difference for your team by {benefit}. "
        "Opportunities like this don’t last long — let's connect this week?\n\n"
        "Looking forward to your reply.\n\n"
        "Regards,\n{name}"
    )
}

# AI-like Expander
def expand_email(email: str) -> str:
    # Very simple example of "AI-style" expansion (handwritten, rule-based for now)
    replacements = {
        "Hi there,": "I hope this message finds you well.",
        "Just reaching out": "I'm reaching out because I genuinely believe this could be of great value to you.",
        "Wanted to quickly share": "I wanted to take a moment to introduce something that I believe could significantly benefit your operations.",
        "Let me know if you want to chat": "I'd be happy to schedule a time to talk if you're interested.",
        "Would you be open to a quick call": "Would you be open to a short conversation to explore how this might help your goals?"
    }
    for key, value in replacements.items():
        email = email.replace(key, value)
    return email

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="AI Cold Email Generator", page_icon="🤖", layout="centered")
st.title("📧 Cold Email Generator ")

with st.form("email_form"):
    offering = st.text_input("🔧 What are you offering? (e.g., AI analytics tool)", "")
    benefit = st.text_input("💡 Key Benefit (e.g., reduces churn by 30%)", "")
    tone = st.selectbox("🎯 Tone of the email", list(EMAIL_TEMPLATES.keys()))
    name = st.text_input("🖊️ Your Name", "")
    company = st.text_input("🏢 Your Company Name", "")

    submitted = st.form_submit_button("Generate & Expand Email")

    if submitted:
        if all([offering, benefit, tone, name, company]):
            base_email = EMAIL_TEMPLATES[tone].format(
                offering=offering.strip(),
                benefit=benefit.strip(),
                name=name.strip(),
                company=company.strip()
            )
            expanded_email = expand_email(base_email)
            st.success("✅ Expanded email generated!")
            st.text_area("📬 Expanded Email", value=expanded_email, height=300)
        else:
            st.error("Please fill in all the fields.")
