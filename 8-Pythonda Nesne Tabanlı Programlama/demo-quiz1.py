#Question

class Question():
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer


q1 = Question("Türkiye'nin başkenti neresidir?", ["İzmir","İstanbul", "Ankara", "Bursa"], "Ankara")
q2 = Question("Atatürk kaç tarihinde doğmuştur?", ["1991","1881","1938","1960"], "1881")
q3 = Question("Gökkuşağı kaç renkten oluşur?", ["2","9","7","5"], "7")
q4 = Question("Türkiye kaç bölgeye ayrılmıştır? ", ["3","5","7","9"], "7")
q5 = Question("21 Haziran hangi mevsimin başlangıdır?", ["İlkbahar","Yaz","Sonbahar","Kış"], "Yaz")

questions = [q1,q2,q3,q4,q5]

#Quiz

class Quiz():
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]



    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Soru{self.questionIndex + 1} : {question.text}")

        for q in question.choices:
            print("-" + q)

        answer = input("Cevap: ")
        self.guess(answer)
        self.loadQuestion()

    def guess(self,answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex +=1

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print("Score:",self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = (self.questionIndex + 1)

        if questionNumber > totalQuestion:
            print("Quiz Bitti.")

        else: 
            print(f"Question {questionNumber} of {totalQuestion}".center(100,"*"))


quiz = Quiz(questions)

quiz.loadQuestion()



