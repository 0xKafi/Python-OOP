class Star_Cinema:
    hall_list = []

    def entry_hall(self,hall_obj):
        Star_Cinema.hall_list.append(hall_obj)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.seat = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        self.show_tpl = (id, movie_name, time)
        self.show_list.append(self.show_tpl)
        self.matrix = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.seat[id] = self.matrix

    def book_seat(self, id, booking):
        for position in booking:
            row = position[0]
            col = position[1]
            ctn = 0
            if(row < self.rows and row >= 0 and col >= 0 and col <self.cols):
                matrix = self.seat[id]
                if(matrix[row][col] == 1):
                    print(f"THIS SEAT ({row},{col}) ALREADY BOOKED BY SOMEONE!")
                else:
                    matrix[row][col] = 1
                    ctn += 1
            else:
                print(f"THIS SEAT ({row}, {col}) INVALID!")

        print(f"{ctn} SEAT BOOKED!")

    def view_show_list(self):
        for show in self.show_list:
            print(f"Show ID: {show[0]}, Movie Name: {show[1]}, Time: {show[2]}")

    def view_available_seat(self, id):
        print("\nUPDATED SEAT MATRIX: ")
        matrix = self.seat[id]

        for i in range(self.rows):
            print(f"\t   {matrix[i]}")

        self.count_seat = 0

        for i in range(self.rows):
            for j in range(self.cols):
                if(matrix[i][j] == 0):
                    pass
                    #print(f"\t  row: {i} column: {j}")
                else:
                    self.count_seat += 1;
        
        if(self.rows * self.cols == self.count_seat):
            print("ALL SEAT BOOKED!")
        else:
            print(f"{self.rows * self.cols - self.count_seat} SEAT AVAILABLE")

    

hall_one = Hall(4,4,1)
hall_two = Hall(5,5,2)
hall_one.entry_show(111,"Iron Man","10:00 AM")
hall_one.entry_show(125,"Spider Man", "02:00 PM")
hall_two.entry_show(825,"Bat Man","10:00 AM")
hall_two.entry_show(525,"Super Man", "02:00 PM")
main_hall = Star_Cinema()
hall1 = main_hall.hall_list[0]
hall2 = main_hall.hall_list[1]

def check_id(id):
    it = 0
    for item in main_hall.hall_list:
        for idx in item.seat.keys():
            if(idx == id):
                return it
        it += 1
    return -1

while True:
    print("\n1. VIEW ALL SHOW\n2. VIEW AVAILABLE SEAT\n3. BOOK SEAT\n4. EXIT\nENTER OPTION:")
    op = int(input())

    if(op == 1):
        print("\nRUNNING SHOW LIST: \n")
        for show in main_hall.hall_list:
            show.view_show_list()
    elif(op == 2):
        print("ENTER SHOW ID: ")
        id = int(input()) 
        bol = check_id(id)
        if bol == -1:
            print("WRONG ID ENTERTD")
        else:
            main_hall.hall_list[bol].view_available_seat(id)
    
    elif(op == 3):
        print("ENTER SHOW ID: ")
        id = int(input()) 
        bol = check_id(id)
        if bol == -1:
            print("WRONG ID ENTERTD")
        else:
            print("NUMBER OF SEAT: ")
            num = int(input())
            booking_list = []
            for i in range(num):
                print("ENTER THE SEAT ROW: ")
                row = int(input())
                print("ENTER THE SEAT COLUMN: ")
                col = int(input())
                tup = (row,col)
                booking_list.append(tup)
            main_hall.hall_list[bol].book_seat(id,booking_list)

    elif(op == 4):
        break

