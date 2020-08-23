"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    # TODO: need to implement this
    def __init__(self, first_name, last_name, email, password):
                    
            self.first_name = first_name
            self.last_name = last_name
            self.email = email
            self.password = password
         
            
    def __repr__(self):
        """Convenience method to show information about melon in console."""

        return "<Customer: {}, {}, {}, {}>".format(self.first_name, self.last_name, self.email, 
            self.password)


def read_customer_from_file(filepath):
   
    customers = {}

    with open(filepath) as file:
        for line in file:
        # customers = filepath.open()
            line = line.rstrip().split('|')
            fn, ln, email, pw = line

            customers[email] = Customer(fn,ln,email,pw)

    return customers
            

def get_by_email(email):

    return customers[email]

customers = read_customer_from_file('customers.txt')