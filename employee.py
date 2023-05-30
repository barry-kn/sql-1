class Employee:
#### __init__  IS A SPECIAL METHORD CALLED CONTRUCTOR
###
     def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        @property
        def email(self):
            return '{}.{}email.com'.formart(self.first,self.last)
        
        @property
        def fullname(self):
            return '{}.{}email.com'.formart(self.first,self.last)
        
        @property
        def _repr__(self):
            return '{}.{}email.com'.formart(self.first,self.last,self.pay)
