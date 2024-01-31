from datetime import datetime, timedelta

class LearningChecklist:
    def __init__(self):
        self.topics = [
            "Variables and Data Types",
            "User Input",
            "Conditional Statements",
            "Loops",
            "Functions with Parameters",
            "Recursion",
            "List",
            "Dictionaries",
            "String Manipulation",
            "File Handling",
            "Error Handling",
            "Classes",
            "Object",
            "Methods",
            "Functions"
        ]
        self.progress = {topic: [False] * 15 for topic in self.topics}
        self.start_date = datetime.now()

    def display_checklist(self):
            print("\nLearning Checklist") 
            print("Reminder: I have started a journey that i must see it completed.")
            print("Current Date:",self.start_date.strftime("%Y-%m-%d"))
            for i, topic in enumerate(self.topics):
                completion_status = " ".join("✅" if day else "❌"  for day in self.progress[topic])
                print(f"{i + 1}. {topic} - {completion_status}")

    def mark_complete(self, topic_number):
            if 1<= topic_number <= len(self.topics):
                current_day = (datetime.now() - self.start_date).days
                self.progress[self.topics[topic_number - 1]][current_day]=True
                print(f"Great job! '{self.topics[topic_number - 1]}marked as completed for day {current_day +1}.")
            else:
                print("Invalid topic number.")

    def run(self):
            while (datetime.now() - self.start_date).days < 15:
                self.display_checklist()
                topic_number = int(input("Enter the number of the topic you completed(or 0 to exit): "))

                if topic_number==0:
                    print("Exiting the learning checklist. Keep up the good work")
                    break
                self.mark_complete(topic_number)

if __name__=="__main__":
    checklist = LearningChecklist()
    checklist.run() 
