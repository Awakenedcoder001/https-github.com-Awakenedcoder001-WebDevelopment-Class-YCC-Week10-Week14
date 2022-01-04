import datetime.datetime
def retirment(yob):
    data = "Years left for retirment"
    
    def retirment_slot(retirment_slot):
        current_year=datetime.datetime.now.year
        print(curent_year)

        current_age=current_year-yob
        print(f"Current age is : {current_age}")

        retirment_years=retirment_slot-current_age
        print(f"{retirment_years} {data}")

    return retirment_slot

func1 = retirment(1980) #address of retirment_slot address
func1(60)

