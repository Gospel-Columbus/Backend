#Nesting functions accessing variable scope.

def display_message(message):
    "hello"
    def message_sender():
        
        "nested function"
        
        print(message)
    message_sender()
        
display_message("Show me the money!")