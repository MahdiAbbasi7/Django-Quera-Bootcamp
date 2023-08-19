from datetime import datetime, timedelta

class Product():
    def __init__(self, product_name, price, off):
        self.product_name = product_name
        self.price = price
        self.off = off

    def __str__(self) -> str:
        return self.product_name

class Comment():
    website = "python_hub.com"

    # instance method(usually has "self")
    def __init__(self, product, name, description, likes, dislikes ):
        self.product = product
        self.name = name
        self.description = description
        self.likes = likes
        self.dislikes = dislikes
        self.date = datetime.now()
    
    # instance method
    def show(self):
        print( f"product: {self.product} \n"
                f"name: {self.name}\n"
                f"description: {self.description}\n"
                f"likes: {self.likes} and dislikes: {self.dislikes}\n"
                f"date: {self.date}"
               )
        
    # class method
    @classmethod
    def info(cls): # cls -> Abrevations of "class"
        print(f"website: {cls.website}")
    
    @classmethod
    def censor(cls, product, name, description, likes, dislikes): # create object
        print ("The comment was censored!!!")
        sc = description.replace("fuck" , "****")
        return cls( product, name, sc, likes, dislikes)

    @staticmethod 
    # you can use this method out of class(inheritance is not implemented) or use inside your classes 
    def elapsed_time(time): 
        print (f"Elapsed time: {datetime.now() - time} " )

python_course = Product("Python course_ Zero to Herooo",0,0)
c1 = Comment(python_course,"Ali", "The greatest coures for python in 2025", 10000, 20)
c1.show()
print(40 * "*")
Comment.info()
print(40 * "*")
c2 = Comment.censor(python_course, "Ali", "fuck,The greatest coures for python in 2025", 10000, 20)
c2.show()
Comment.elapsed_time(c2.date - timedelta(days = 2 , hours = 4))

