def parse_str(title):
    title = title.replace(' ', '').lower()
    if title == '':
        return '-'
    return title

def parse_int(number):
    if type(number) == int:
        return number
    else:
        return -1
    #return (number.replace(' ', '')).lower()


class Row:
    def __init__(self, csv_row, amount_fields):
        
        self.csv_row = csv_row
        
        #self.amount_fields = amount_fields
        
        self.rec_id = int(csv_row['rec_id'])
        
        self.given_name = parse_str(csv_row['given_name'])
        
        self.surname = parse_str(csv_row['surname'])
        
        self.street_number = parse_str(csv_row['street_number'])
        
        self.address_1 = parse_str(csv_row['address_1'])
        
        self.address_2 = parse_str(csv_row['address_2'])
        
        self.suburb = parse_str(csv_row['suburb'])
        
        self.postcode = parse_str(csv_row['postcode'])
        
        self.state = parse_str(csv_row['state'])
        
        self.date_of_birth = parse_str(csv_row['date_of_birth'])
        
        self.age = parse_str(csv_row['age'])
        
        self.phone_number = parse_str(csv_row['phone_number'])
        
        self.soc_sec_id = parse_str(csv_row['soc_sec_id'])
        
        #self.blocking_number = int(csv_row['blocking_number']) 
       
        
    """
    comparison function that need only for data visualization
    in write_sorted() function
    """
    def __lt__(self, other):
        return ((self.surname < other.surname) or
    (self.surname == other.surname and self.given_name < other.given_name))