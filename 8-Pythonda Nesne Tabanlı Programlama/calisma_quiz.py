class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer   


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print (f"Soru {self.questionIndex + 1}: {question.text}")

        for q in question.choices:
            print("-" + q)

        answer = input("Cevap: ")
        self.quess(answer)
        self.loadQuestion()
    
    def quess(self,answer):
        question = self.getQuestion()
        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print("Score: ", self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print("Ouiz Bitti.")
        else:
            print(f"Question {questionNumber} of {totalQuestion}".center(100,"*"))
            
       



q1 = Question("Türkiye'nin başkneti neresidir?",["ankara","istanbul","izmir","bursa"],"ankara")
q2 = Question("Türkiye kaç bölgeden oluşmaktadır?",["7","9","5","8"], "7")
q3 = Question("Türkiye'nin en yüksek dağı?", ["ağrı","elmalı","toroslar","ılgaz"], "ağrı")
q4 = Question("Türkiye'nin kuzeyindeki denizin adı nedir?", ["ege","akdeniz","karadeniz","hazar"],"karadeniz")
q5 = Question("Ege bölgesinin bitki örtüsü nedir?", ["maki","bozkır","kırsal","karasal"],"maki")

questions = [q1,q2,q3,q4,q5]

quiz = Quiz(questions)
quiz.loadQuestion()


