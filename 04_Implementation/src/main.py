import csv
import random
import os


class Question:
    def __init__(self, word: str, choices: list[str], correct_index: int):
        self.word = word
        self.choices = choices
        self.correct_index = correct_index  # index ของคำตอบที่ถูกใน choices

    def shuffle_choices(self):
        """สลับลำดับตัวเลือกและอัปเดตตำแหน่งคำตอบที่ถูกต้อง"""
        indices = list(range(len(self.choices)))
        random.shuffle(indices)
        new_choices = [self.choices[i] for i in indices]
        new_correct_index = indices.index(self.correct_index)
        self.choices = new_choices
        self.correct_index = new_correct_index


class QuizApp:
    def __init__(self):
        self.questions: list[Question] = []
        self.score: int = 0
        self.incorrect_questions: list[Question] = []

    def load_vocabulary(self, file_path: str) -> None:
        """อ่านไฟล์คำศัพท์จาก CSV และสร้างรายการคำถาม"""
        if not os.path.exists(file_path):
            print(f"[ERROR] File '{file_path}' not found.")
            return

        questions: list[Question] = []

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                for row in reader:
                    # คาดหวังอย่างน้อย 6 คอลัมน์: word + 5 choices (col2 คือคำตอบถูก)
                    if len(row) < 6:
                        # ข้ามบรรทัดที่ไม่สมบูรณ์
                        continue

                    word = row[0].strip()
                    # คอลัมน์ที่ 1-5 เป็นตัวเลือก (col1 คือ correct answer)
                    choices = [c.strip() for c in row[1:6]]
                    correct_index = 0  # คำตอบที่ถูกคือตัวแรกใน choices

                    q = Question(word, choices, correct_index)
                    q.shuffle_choices()
                    questions.append(q)

            if not questions:
                print("[WARNING] No valid questions found in the file.")
                return

            self.questions = questions
            print(f"[INFO] Loaded {len(self.questions)} questions from '{file_path}'.")
        except Exception as e:
            print(f"[ERROR] Failed to read file '{file_path}': {e}")

    def start_quiz(self):
        """เริ่มทำแบบทดสอบ"""
        if not self.questions:
            print("[WARNING] No questions loaded. Please load vocabulary file first.")
            return

        self.score = 0
        self.incorrect_questions = []

        print("\n=== Start Vocabulary Quiz ===\n")

        for idx, question in enumerate(self.questions, start=1):
            print(f"Question {idx}/{len(self.questions)}")
            print(f"What is the meaning of: {question.word}?")
            for i, choice in enumerate(question.choices, start=1):
                print(f"{i}) {choice}")

            user_answer = self._ask_for_answer(len(question.choices))

            if user_answer - 1 == question.correct_index:
                print("✅ Correct!\n")
                self.score += 1
            else:
                print("❌ Incorrect.\n")
                self.incorrect_questions.append(question)

        self.show_summary()

    def _ask_for_answer(self, num_choices: int) -> int:
        """ถามคำตอบจากผู้ใช้และตรวจว่าเป็นตัวเลขในช่วงที่กำหนด"""
        while True:
            try:
                raw = input(f"Your answer (1-{num_choices}): ").strip()
                answer = int(raw)
                if 1 <= answer <= num_choices:
                    return answer
                else:
                    print(f"Please enter a number between 1 and {num_choices}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def show_summary(self):
        """แสดงสรุปผลคะแนน"""
        total = len(self.questions)
        correct = self.score
        incorrect = total - correct
        percent = (correct / total * 100) if total > 0 else 0

        print("===== Quiz Summary =====")
        print(f"Score: {correct}/{total} ({percent:.2f}%)")
        print(f"Correct: {correct}")
        print(f"Incorrect: {incorrect}\n")

        if self.incorrect_questions:
            print("You might want to review these words:")
            for q in self.incorrect_questions:
                correct_answer = q.choices[q.correct_index]
                print(f"- {q.word} -> {correct_answer}")
        else:
            print("Great job! No incorrect answers. 🎉")
        print()


def main():
    app = QuizApp()
    default_file = "vocab.csv"

    while True:
        print("=== Vocabulary Quiz Generator ===")
        print("1. Load vocabulary file")
        print("2. Start quiz")
        print("3. Exit")

        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            file_path = input(f"Enter vocabulary file name (default: {default_file}): ").strip()
            if file_path == "":
                file_path = default_file
            app.load_vocabulary(file_path)
        elif choice == "2":
            app.start_quiz()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid menu option. Please select 1-3.\n")


if __name__ == "__main__":
    main()
