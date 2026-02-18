def calculate_payroll():
    try:
        
        hours_str = input("Enter Hours Worked: ")
        rate_str = input("Enter Rate per Hour: ")
       
        hours = float(hours_str)
        rate = float(rate_str)
       
        if hours <= 40:
            pay = hours * rate
            print(f"Regular Hours: {hours}")
            print(f"Total Pay: ${pay:.2f}")
        else:
            
            regular_hours = 40
            overtime_hours = hours - 40
            
            
            overtime_rate = rate * 1.5
            
           
            regular_pay = regular_hours * rate
            overtime_pay = overtime_hours * overtime_rate
            total_pay = regular_pay + overtime_pay
            
            
            print(f"Regular Hours: {regular_hours}")
            print(f"Overtime Hours: {overtime_hours:.2f}")
            print(f"Regular Pay: ${regular_pay:.2f}")
            print(f"Overtime Pay: ${overtime_pay:.2f}")
            print(f"Total Pay: ${total_pay:.2f}")
            
    except ValueError:
        print("Invalid input. Please enter numerical values.")


calculate_payroll()
