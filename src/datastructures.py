"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from flask import Flask, request, jsonify, url_for

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            }
        ]

    # This method generates a unique incremental ID
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        ## You have to implement this method
        ## Append the member to the list of _members
        new_member= [
            {
                "first_name" : self.first_name,
                "last_name" : self.last_name,
                "age" : self.age,
                "lucky_numbers": [self.lucky_numbers],
            }
        ]
        self._members.append(new_member)
        return jsonify(self._members), 200
    

    def delete_member(self, id):
        ## You have to implement this method
        ## Loop the list and delete the member with the given id
        new_member = list(filter(
            lambda x: x["id"] != id,
            self._member))
        self._member = new_member

        book_idx = [self[id] for self in self._members].index(id)
        del self[self._members]
        return "", 200

    def get_member(self, id)-> tuple[str, int]:
        self = next(filter(lambda x: id == x["id"],self._member), None)
        return jsonify(self), 200
   ## You have to implement this method
        ## Loop all the members and return the one with the given id

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
    