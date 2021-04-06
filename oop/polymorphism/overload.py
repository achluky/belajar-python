from multipledispatch import dispatch

class Employee:
    @dispatch()
    def Hello_Emp(self):
        print("Hello")
    @dispatch(object)
    def Hello_Emp(self, e_name):
        print("Hello "+ e_name)

        
emp1=Employee()
emp1.Hello_Emp()
emp1.Hello_Emp("Besant")


# class Employee:
#     def Hello_Emp(self, e_name = None):
#         if e_name is not None :
#             print("Hello "+ e_name)
#         else:
#             print("Hello")