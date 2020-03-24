# -*- coding: utf-8 -*-
import csv

class Contact:
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:
    def __init__(self):
        self._contacts = []

    def add(self,name,phone,email):
        contact = Contact(name,phone,email)
        self._contacts.append(contact)
        self._save()
    
    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def delete(self,name):
        for idx,contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break
    
    def search(self,name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()

    def update(self,name,phone,email):
        for idx,contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                self._contacts[idx].name = name
                self._contacts[idx].phone = phone
                self._contacts[idx].email = email
                print('** El contacto ha sido actualizado **')
                self._print_contact(contact)
                break
        else:
            self.add(name,phone,email)
            print('*****************************************************') 
            print('El contacto no existe, se ha agregado como uno nuevo') 
            print('*****************************************************')

    def _not_found(self):
        print('***************')
        print(' No encontrado ')
        print('***************')
    
    def _print_contact(self,contact):
        print('--- * --- * --- * --- * --- * --- * --- * ---')
        print('Nombre: {}'.format(contact.name))
        print('Teléfono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('--- * --- * --- * --- * --- * --- * --- * ---')

    def _save(self):
        with open('Platzi/agenda/contacts.csv','w',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(('name','phone','email'))
            for contact in self._contacts:
                writer.writerow((contact.name, contact.phone, contact.email))


def run():

    contact_book = ContactBook()
    with open('Platzi/agenda/contacts.csv','r',newline='') as f:
        reader = csv.reader(f)
        next(reader)
        for idx, row in enumerate(reader):
            if not row:
                continue
            contact_book.add(row[0],row[1],row[2])


    while True:
        command = str(input('''
        ¿Qué deseas hacer?
        
        [a]gregar contacto
        [ac]tualizar contacto
        [b]uscar contacto
        [e]liminar contacto
        [l]istar contactos
        [s]salir
        '''))

        if command == 'a':
            name = str(input('Escribe el nombre del contacto: '))
            phone = str(input('Escribe el número de teléfono del contacto: '))
            email = str(input('Escribe el email del contacto: '))
            contact_book.add(name,phone,email)
        elif command == 'ac':
            name = str(input('ACTUALIZACIÓN: Escribe el nombre del contacto: '))
            phone = str(input('ACTUALIZACIÓN: Escribe el número de teléfono del contacto: '))
            email = str(input('ACTUALIZACIÓN: Escribe el email del contacto: '))
            contact_book.update(name,phone,email)
        elif command == 'b':
            name = str(input("Escribe el nombre de contacto a buscar: "))
            contact_book.search(name)
        elif command == 'e':
            name = str(input("Escribe el nombre de contacto a elminar: "))
            contact_book.delete(name)
        elif command == 'l':
            contact_book.show_all()
        elif command == 's':
            print('salir')
            break
        else:
            print('commando no reconocido')
            continue

if __name__ == "__main__":
    print('B I E N V E N I D O  A  L A  A G E N D A')
    run()