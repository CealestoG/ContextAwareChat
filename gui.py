import gradio as gr
from orchestration import ContextAwareChatBot
from chat_history_db import init_db, log_message, export_history_to_txt
import uuid
import atexit

init_db()
session_id = str(uuid.uuid4())
bot = ContextAwareChatBot()


@atexit.register
def save_chat():
    export_history_to_txt(session_id)

def respond_to_query(user_input):
    if user_input.strip().lower() == "/reset":
        bot.reset_context()
        log_message(session_id, "user", "/reset")
        log_message(session_id, "assistant", "Chat context has been reset.")
        return " Chat context has been reset."
    elif user_input.strip().lower() == "/exit":
        log_message(session_id, "user", "/exit")
        log_message(session_id, "assistant", "Exiting is disabled in GUI mode. Please close the tab or stop the server.")
        return " Exiting is disabled in GUI mode. Please close the tab or stop the server."

    log_message(session_id, "user", user_input)
    bot_response = bot.chat(user_input)
    log_message(session_id, "assistant", bot_response)
    return bot_response

iface = gr.Interface(
    fn=respond_to_query,
    inputs=gr.Textbox(lines=2, placeholder="Ask something..."),
    outputs=gr.Textbox(label="Bot Response"),
    title=" Context-Aware Chatbot (Offline)",
    description="Chat with an offline LLM-powered assistant. Use /reset to reset context."
)

if __name__ == "__main__":
    print(f" Session ID: {session_id}")
    iface.launch()
