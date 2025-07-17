from orchestration import ContextAwareChatBot
import time

def main():
    print(" Starting context-aware offline chatbot...")
    print(" Loading knowledge base and AI models")
    start_time = time.time()
  
    chatbot = ContextAwareChatBot(user_id="user_001")
    
    init_time = time.time() - start_time
    print(f" System ready in {init_time:.2f} seconds")
    print(" Type your questions (commands: /reset, /exit)")
    
    while True:
        try:
            user_input = input("\nYou: ").strip()
            
            
            if user_input.lower() == '/exit':
                break
            elif user_input.lower() == '/reset':
                chatbot.reset_context()
                print("Conversation context reset")
                continue
                
            start = time.time()
            response = chatbot.chat(user_input)
            latency = time.time() - start
            
            print(f"\n Bot ({latency:.2f}s): {response}")
            
        except KeyboardInterrupt:
            print("\n Session ended")
            break

if __name__ == "__main__":
    main()