# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def vloz(self, prvok):
#         if self.head is None:
#             self.head = prvok
#         else:
#             aktualny = self.head
#             while aktualny.next:
#                 aktualny = aktualny.next
#             aktualny.next = prvok
#
#     def vloz_na_zaciatok(self, prvok):
#         prvok.next = self.head
#         self.head = prvok
#
#     def vypis(self):
#         aktualny = self.head
#         print(aktualny.data)
#         while aktualny.next:
#             aktualny = aktualny.next
#             print(aktualny.data)
#
#
# class Prvok:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# mojLinked = LinkedList()
# prvok1 = Prvok("Milan")
# mojLinked.vloz(prvok1)
# prvok2 = Prvok("Jozo")
# mojLinked.vloz(prvok2)
# prvok3 = Prvok("Fero")
# mojLinked.vloz(prvok3)
# novy_prvok = Prvok("novy")
# mojLinked.vloz_na_zaciatok(novy_prvok)
# mojLinked.vypis()
# print("test")
#
#
#
#
#
# stack = []
# stack.append("Patrik")
# stack.append("Milan")
# stack.append("Lukas")
# print(stack)
# stack.pop()
# print(stack)
#
# queue = []
# queue.append("Patrik")
# queue.append("Milan")
# queue.append("Lukas")
# print(queue)
# queue.pop(0)
# print(queue)

class Convert:
    @staticmethod
    def toimperial(m,y):
        return m*y

    def tometric(m,y):
        return m/y


print(Convert.toimperial(1,1.0936))
print(Convert.tometric(1,1.0936))