from abc import ABC, abstractmethod


class Primary(ABC):

    @abstractmethod
    def get_something(self):
        pass

    @abstractmethod
    def send_something(self):
        pass




class GetElement_from(Primary):

    def send_something(self):
        print("do something")

    def get_something(self):
        print("get something")


    def get_element(self,data):
        if len(data) > 1:
            return 1, "single_element"
        return 0, "error message"

    def get_elements(self,data):

        return 1, "list_of elements"


var = GetElement_from()