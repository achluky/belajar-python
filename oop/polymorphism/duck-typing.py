class Duck:
    def quack(self):
        print("Wek wek")
    def feathers(self):
        print( "Bebek itu memiliki bulu berwarna putih dan abu-abu.")
 
class Person:
    def quack(self):
        print( "Orang itu meniru bebek.")
    def feathers(self):
        print( "Orang tersebut mengambil bulu dari tanah dan menunjukkannya.")
 
def in_the_forest(duck):
    duck.quack()
    duck.feathers()
 
def game():
    donald = Duck()
    john = Person()
    in_the_forest(donald)
    in_the_forest(john)

game()