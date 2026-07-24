# class Factory:
#     def __init__(self,material,zips,pockets):
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets
# reebok = Factory("Leather",3,3)
# campus = Factory("nylon",2,2)
# print(reebok.material)        






class Menu:
    def __init__(self,material,zips,pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets
reebok = Menu("Leather",3,3)
campus = Menu("nylon",2,2)
print(reebok.material) 