from faker import Faker
fake=Faker()
class hangman_word:
    def __init__(self):
        self.__word=fake.word()
        self.__guess=[]
        self.__wrong=0
        self.__count=0
        self.__tries=0
    
    def count(self):
        for letter in self.__word:
            self.__guess+="_ "
        self.__count=len(self.__word)
        self.__guess.pop()
        hangman_word.tries(self)

    def get_word(self):
        return self.__word

    def get_guess(self):
        guess=""
        for letter in self.__guess:
            guess+=letter
        return guess

    def guess_word(self,word):
        position=0
        for letter in self.__word:
            if letter==word:
                self.__guess[0+2*position]=word
            position+=1
        if word not in self.__word:
            print("\nYou got it wrong")
            hangman_word.wrong(self)
            choices=hangman_word.get_tries(self)-hangman_word.get_wrong(self)
            print(choices, "choices remaining \n")
        
    def wrong(self):
        self.__wrong+=1

    def get_wrong(self):
        return self.__wrong

    def get_word_guess(self):
        guess=""
        for letter in self.__guess:
            if letter!=" ":
                guess+=letter
        return guess

    def tries(self):
        if self.__count<5:
            self.__tries=10
        elif 5<=self.__count and self.__count<8:
            self.__tries=12
        else:
            self.__tries=15

    def get_tries(self):
        return self.__tries

    def get_count(self):
        return self.__count


class game:
    def __init__(self):
        self.__to_do=""
        self.__x=hangman_word()
        self.__win=None
        self.__guess_list=[]
        self.__guess_word=0
        self.__guess=""

    def main(self):
        while self.__to_do!="exit":
            self.__to_do=(input("do you want to play or exit: ")).lower()
            if self.__to_do=="play":
                game.play()
            elif self.__to_do!="exit":
                print("not an option")
            else:
                print("thank you")
    def play(self):
        print("play hangman game \n")
        self.__x=hangman_word()
        self.__guess_list=[]
        self.__x.count()
        game.game_logic()

    def game_logic(self):
        print(self.__x.get_guess()+"\n")
        self.__guess=(input("put in a letter to guess or the entire word(one try): ")).lower()
        self.__guess_word=len(self.__guess)
        if self.__guess_word==self.__x.get_count():
            game.word_guess()
        else:
            game.letter_guess()

    def win_decision(self):
        if self.__win==False:
            print("\nYou lost")
            print("The word is", self.__x.get_word()+"\n")
        else:
            print("\n"+self.__x.get_word())
            print("You won \n")
        game.main()
    
    def word_guess(self):
        if self.__guess==self.__x.get_word():
            self.__win=True
        else:
            self.__win=False
        game.win_decision()

    def letter_guess(self):
        if self.__guess_word>1:
            print("\nput in one letter \n")
            game.game_logic()
        elif self.__guess.isalpha()==False:
            print("\nput in a letter \n")
            game.game_logic()
        elif self.__guess in self.__guess_list:
            print("\nput in something different \n")
            game.game_logic()
        self.__guess_list+=self.__guess
        self.__x.guess_word(self.__guess)
        if self.__x.get_word_guess()==self.__x.get_word():
            self.__win=True
            game.win_decision()
        elif self.__x.get_wrong()==self.__x.get_tries():
            self.__win=False
            game.win_decision()
        game.game_logic()

game=game()
game.main()



