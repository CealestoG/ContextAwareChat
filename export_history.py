from chat_history_db import get_history
import sys

def export_history_to_txt(session_id, filename="chat_history.txt"):
    history = get_history(session_id)
    
    if not history:
        print(f"No history found for session ID: {session_id}")
        return

    with open(filename, "w", encoding="utf-8") as f:
        for sender, message, timestamp in history:
            f.write(f"[{timestamp}] {sender}: {message}\n")

    print(f"Chat history saved to '{filename}'")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python export_history.py <session_id> [filename]")
    else:
        session_id = sys.argv[1]
        filename = sys.argv[2] if len(sys.argv) > 2 else "chat_history.txt"
        export_history_to_txt(session_id, filename)
