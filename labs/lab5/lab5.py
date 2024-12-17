class Povtory(str):
    def povtory_sliv(self, s):
        
        words = s.lower().split()
        symv3 = []
        
        
        for i in words:
            if len(i) > 3:
                symv3.append(i) 
        
        
        for word in symv3:
            if symv3.count(word) > 1:
                return True
        return False
       


    def palindrome(self):
        ryadok = self.replace(" ", "").lower()
        return ryadok == ryadok[::-1]


s = str(input("Введіть рядок: "))

s = Povtory(s)


print("Наявність повторів слів > 3 символів - ",s.povtory_sliv(s))  

print("Наявність паліндромів - ",s.palindrome()) 