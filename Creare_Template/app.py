from DAO.ui_dao import Interface, Window

database = Interface()
print(database.config)
window = Window(500, 150)
window.run()

# if __name__ == '__main__':
#     window = Window(500, 150)
#     window.run()
