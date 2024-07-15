class Car:

    """def __init__(self,numbers,moisture,weight):
        self.numbers= numbers
        self.moisture = moisture
        self.weight = weight"""

    def insert(self):
        numbers = list(input( 'Enter the number of bag:'))
        moisture = list(input('Enter the moisture content:'))
        weight = list(input('Enter the total weight of the bag:'))
        lent = len(moisture)
        return (numbers,moisture,weight,lent)
    def summation(self,numbers,moisture,weight):
        for i in numbers:
            ii = sum(i)
        for j in moisture:
           jj = sum(j)
        for k in weight:
            kk = sum(k)
        print(f' The total weigh is :{kk}')
        return (ii,jj,kk)
    def moisture(self,jj,lent):
        mois = (jj/lent)+0.5
        diff = mois-8
        return mois,diff
    def discount(self,ii,kk,diff,lent):
        dis = (kk * diff * lent)/(100*ii)

car = Car()
print(car.insert())
car.summation(car.insert())
car.moisture()
car.discount()


