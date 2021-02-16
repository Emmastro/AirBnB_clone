#!/usr/bin/python3
"""[summary]
"""

import cmd
import models

class HBNBCommand(cmd.Cmd):

    intro = 'Welcome to the Airbnb console. Type help or ? to list commands.\n'
    prompt = '(hbnb) '

    def __init__(self, completekey='tab', stdin=None, stdout=None):
        super().__init__(completekey, stdin, stdout)

    
    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit()
    
    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
        """
        if arg == "": #TODO: make this common check a property
            print('** class name missing **')
            return
        try:
            model = models.classes[arg]()
            models.storage.new(model)
            models.storage.save()
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
            model = self.storage.find(model_name, model_id)
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
            self.storage.delete(model_name, model_id)           
            self.storage.save()

        except Exception as e: #TODO: make this exception a property for commands taking model and id

            if arg.count(' ') == 0:
                print("** instance id missing **")
            elif arg.count(' ') > 1:
                print("** too many arguments (2 arguments required)**")
            else:
                print(e)

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        if arg == "": #TODO: make this common check a property
            print([x.__str__() for x in models.storage.all().values()])
        else:

            try:
                model = self.get_model(arg)
                resp = []
                for l in self.storage.all().values():
                    if type(l) == model:
                        resp.append(l.__str__())

            except Exception as e:
                print(e)
                return

            return resp

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

            self.storage.update(model_name, model_id, attribute_name, attribute_value)            
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

        raise Exception("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()