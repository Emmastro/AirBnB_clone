#!/usr/bin/python3
"""[summary]
"""

import cmd
from models.base_model import BaseModel
from engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):

    intro = 'Welcome to the turtle shell.   Type help or ? to list commands.\n'
    prompt = '(hbnb) '
    file = None
    models = [BaseModel]
    storage = FileStorage()

    def __init__(self, completekey='tab', stdin=None, stdout=None):
        super().__init__(completekey, stdin, stdout)


    def do_quit(self):
        """Quit command to exit the program"""
        self.close()
        return True
    
    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
        """
        if arg == "": #TODO: make this common check a property
            print('** class name missing **')
            return
        try:
            model = self.get_model(arg)()
            model.save()
            print(model.id)
        except Exception as e:
            print(e)


    def do_show(self, arg):
        """Prints the string representation of an instance based on the class `name` and `id`
        """
        if arg == "": #TODO: make this common check a property
            print('** class name missing **')
            return

        try:
            model_name, model_id = arg.split(' ')
            model = self.get_model(model_name)
            model = self.storage.find(model, id) #TODO: raise error with ** no instance found ** if not found
            print(model.__str__())

        except Exception as e:

            if arg.count(' ') == 0:
                print("** instance id missing **")
            elif arg.count(' ') > 1:
                print("** too many arguments (2 arguments required)**")
            else:
                print(e)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change into the JSON file)."""

        if arg == "": #TODO: make this common check a property
            print('** class name missing **')
            return

        try:
            model_name, model_id = arg.split(' ')
            model = self.get_model(model_name)
            model = self.storage.delete(model, id) #TODO: raise error if model with id `id` not found            
            self.storage.save()

        except Exception as e: #TODO: make this exception a property for commands taking model and id

            if arg.count(' ') == 0:
                print("** instance id missing **")
            elif arg.count(' ') > 1:
                print("** too many arguments (2 arguments required)**")
            else:
                print(e)
    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)
        
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """

        if arg == "": #TODO: make this common check a property
            print('** class name missing **')
            return

        try:
            #TODO: Handle case where the value to update has a space character
            model_name, model_id, attribute_name, attribute_value = arg.split(' ')

            model = self.get_model(model_name)
        
            model = self.storage.update(model, id, attribute_name, attribute_value) #TODO: raise error if model with id `id` not found            
            self.storage.save()

        except Exception as e: #TODO: make this exception a property for commands taking model and id

            if arg.count(' ') == 0:
                print("** instance id missing **")
            elif arg.count(' ') == 1:
                print("** attribute name missing **")
            elif arg.count(' ') == 2: 
                print("** value missing **")
            elif arg.count(' ') > 3: #TODO: Allow this case, and ignore the extra arguments
                print("** too many arguments (2 arguments required)**")
            else:
                print(e)
    
    def get_model(self, value):
        for model in self.models:
            if model.__name__ == value:
                 return model

        raise Exception("** class doesn't exist **")

    def close(self):
        if self.file:
            self.file.close()
            self.file = None


def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))

if __name__ == '__main__':
    HBNBCommand().cmdloop()