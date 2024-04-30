#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Employee:
    def __init__(self, empid, name, basic_salary, experience_years):
        self.empid = empid
        self.name = name
        self.basic_salary = basic_salary
        self.experience_years = experience_years
        self.hra = 0
        self.da = 0
        self.pf = 0
        self.bonus = 0
        self.net_salary = 0

    # Getter and setter methods
    def get_empid(self):
        return self.empid

    def set_empid(self, empid):
        self.empid = empid

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_basic_salary(self):
        return self.basic_salary

    def set_basic_salary(self, basic_salary):
        self.basic_salary = basic_salary

    def get_experience_years(self):
        return self.experience_years

    def set_experience_years(self, experience_years):
        self.experience_years = experience_years

    # Calculative functions
    def calculate_hra(self):
        self.hra = 0.35 * self.basic_salary

    def calculate_da(self):
        self.da = 0.58 * self.basic_salary

    def calculate_pf(self):
        self.pf = 0.095 * self.basic_salary

    def calculate_bonus(self):
        if self.experience_years >= 30:
            self.bonus = 0.59 * self.basic_salary
        elif self.experience_years >= 23:
            self.bonus = 0.51 * self.basic_salary
        elif self.experience_years >= 15:
            self.bonus = 0.45 * self.basic_salary
        elif self.experience_years >= 7:
            self.bonus = 0.33 * self.basic_salary
        else:
            self.bonus = 0.16 * self.basic_salary

    def calculate_net_salary(self):
        self.net_salary = self.basic_salary + self.da + self.hra - self.pf + self.bonus


# Driver code to test the Employee class
if __name__ == "__main__":
    emp_id = input("Enter employee ID: ")
    emp_name = input("Enter employee name: ")
    emp_basic_salary = float(input("Enter basic salary: "))
    emp_experience = int(input("Enter years of experience: "))

    # Creating an instance of the Employee class
    employee = Employee(emp_id, emp_name, emp_basic_salary, emp_experience)

    # Calculating various components
    employee.calculate_hra()
    employee.calculate_da()
    employee.calculate_pf()
    employee.calculate_bonus()
    employee.calculate_net_salary()

    # Displaying the results
    print("\nEmployee Details:")
    print("ID:", employee.get_empid())
    print("Name:", employee.get_name())
    print("Basic Salary:", employee.get_basic_salary())
    print("Experience (in years):", employee.get_experience_years())
    print("\nCalculated Components:")
    print("HRA:", employee.hra)
    print("DA:", employee.da)
    print("PF:", employee.pf)
    print("Bonus:", employee.bonus)
    print("\nNet Salary:", employee.net_salary)


# In[2]:


class NumberList:
    def __init__(self, nums):
        self.nums = nums
        self.newlist = []

    def process_numbers(self):
        n = len(self.nums)
        for i in range(n // 2):
            pair_sum = self.nums[i] + self.nums[n - i - 1]
            self.newlist.append(pair_sum)

    def remove_duplicates(self):
        self.newlist = list(set(self.newlist))

    def convert_to_tuple(self):
        self.newlist = tuple(self.newlist)

    def display_result(self):
        print("Processed Numbers:", self.newlist)


# Driver code to test the NumberList class
if __name__ == "__main__":
    try:
        n = int(input("Enter the number of elements (should be even): "))
        if n % 2 != 0:
            raise ValueError("Number of elements should be even.")
        
        numbers_list = [float(input(f"Enter number {i + 1}: ")) for i in range(n)]

        # Creating an instance of NumberProcessor
        number_processor = NumberList(numbers_list)

        # Processing the numbers
        number_processor.process_numbers()

        # Removing duplicates
        number_processor.remove_duplicates()

        # Converting to tuple
        number_processor.convert_to_tuple()

        # Displaying the result
        number_processor.display_result()

    except ValueError as ve:
        print(f"Error: {ve}")


# In[4]:


class MyNumber:
    def __init__(self, num=0):
        self.num = num

    def set_num(self, num):
        self.num = num

    def get_num(self):
        return self.num

    def add(self, other):
        result = MyNumber(self.num + other.get_num())
        return result

    def raised_to(self, other):
        result = MyNumber(self.num ** other.get_num())
        return result

    def concat(self, other):
        result = MyNumber(int(str(self.num) + str(other.get_num())))
        return result

    def max(self, other):
        result = MyNumber(max(self.num, other.get_num()))
        return result

    def min(self, other):
        result = MyNumber(min(self.num, other.get_num()))
        return result


# Driver code to test the MyNumber class
if __name__ == "__main__":
    n1 = MyNumber(4)
    n2 = MyNumber()
    n2.set_num(2)

    # Addition
    n3 = n1.add(n2)
    print("Addition is", n3.get_num())  # 7

    # Exponentiation
    n3 = n1.raised_to(n2)
    print(n1.get_num(), "raised to", n2.get_num(), "is", n3.get_num())  # 32

    # Concatenation
    n3 = n1.concat(n2)
    print("Concatenation answer is", n3.get_num())  # 25

    # Maximum
    n3 = n1.max(n2)
    print("Max is", n3.get_num())  # 5

    # Minimum
    n3 = n1.min(n2)
    print("Min is", n3.get_num())  # 2


# In[ ]:




