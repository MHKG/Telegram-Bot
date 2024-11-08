from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi"):
        return "Hi, how are you?"

    if user_message in ("fine", "i am fine"):
        return "Great"

    if user_message in ("how are you", "how are you?"):
        return "I am fine. Thank you."

    if user_message in ("who are you", "who are you?"):
        return "I am just a chatbot."

    if user_message in ("what is the time", "what is the time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)

    return "I don't understand."
