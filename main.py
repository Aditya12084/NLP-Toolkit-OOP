import os
from user_manager import UserManager
from nlp_services import SentimentAnalysis, NamedEntityRecognition, LanguageDetection

class NLPApp(UserManager):
    def __init__(self):
        super().__init__()
        self.api_key = os.getenv("NLP_CLOUD_API_KEY") or "your-real-api-key"
        self.__first_menu()

    def __first_menu(self):
        while True:
            choice = input("""
            Hi! How would you like to proceed?
            1. Not a member? Register
            2. Already a member? Login
            3. Exit
            Choose option (1/2/3): """)

            if choice == '1':
                if self.register():
                    self.__second_menu()
            elif choice == '2':
                if self.login():
                    self.__second_menu()
            elif choice == '3':
                exit()
            else:
                print("Invalid choice. Try again.")

    def __second_menu(self):
        while True:
            choice = input("""
            Choose an NLP task:
            1. Named Entity Recognition (NER)
            2. Language Detection
            3. Sentiment Analysis
            4. Logout
            Enter your choice (1/2/3/4): """)

            if choice == '1':
                para = input("Enter the paragraph: ")
                entity = input("What entity would you like to search for? ")
                ner = NamedEntityRecognition(self.api_key)
                ner.process_text(para, entity)

            elif choice == '2':
                para = input("Enter the paragraph: ")
                lang = LanguageDetection(self.api_key)
                lang.process_text(para)

            elif choice == '3':
                para = input("Enter the paragraph: ")
                sentiment = SentimentAnalysis(self.api_key)
                sentiment.process_text(para)

            elif choice == '4':
                print("Logged out.")
                break
            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    app = NLPApp()
