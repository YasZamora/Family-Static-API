
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:

    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [{
            "id": self._generateId(),
            "name":"John"+last_name,
            "first_name": "John",
            "last_name": last_name,
            "age": 33,
            "lucky_numbers": [7, 13, 22]
        }, 
        {
            "id": self._generateId(),
            "name":"Jane"+last_name,
            "first_name": "Jane",
            "last_name":last_name,
            "age": 35,
            "lucky_numbers": [10, 14, 3]
        },
        {
            "id": self._generateId(),
            "name":"Jimmy"+last_name,
            "first_name": "Jimmy",
            "last_name":last_name,
            "age": 5,
            "lucky_numbers": [1]
        }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        result = {"done": False}
        id = self._generateId()
        try:
            member['id']=id
            self._members.append(member)
            return self._members
        except Exception as e:
            print(f"result: {e}")    


    def delete_member(self, id):
        # fill this method and update the return
        result = {"done": False}
        try:
            for element in self._members:
                if int(element["id"]) == int(id):
                    self._members.remove(element)
                    result ["done"] = True
            # self._members.remove(self.get_member(id))
            # self._members = list(filter(lambda member: id != member["id"], self._members)) 
            # self._members = [member for member in self._members if not (member['id'] == id)]
            # print(self._members)
            # result["done"] = True
        except Exception as e:
            print(f"get_member: {e}")
        return result

    # def get_member(self, id):
    #     # fill this method and update the return
    #     pass 

    def get_member(self, id):
        result = {}
        try:
            for member in self._members:
                if member["id"] == id:
                    result = member
        except Exception as e:
            print(f"get_member: {e}")
        return result                    

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
