# 👤 Object Creation in Python (Person Class)

## 📌 Description

This Python program demonstrates the basic concept of **object creation** using a class. It shows how to create an object, assign values, and display them.

---

## 🚀 Features

* Defines a `Person` class
* Creates an object using constructor
* Assigns values using a method
* Displays object data

---

## 🛠️ How It Works

1. A class `Person` is created with attributes:

   * `name`
   * `age`

2. Methods:

   * `setInfo()` → Sets the values
   * `getInfo()` → Displays the values

3. In the main program:

   * An object `p` is created
   * Values are assigned using `setInfo()`
   * Data is displayed using `getInfo()`

---

## 💻 Code

```python id="p9x2ld"
class Person:
    def __init__(self):
        self.name = ""
        self.age = 0

    def setInfo(self, nm, a):
        self.name = nm
        self.age = a

    def getInfo(self):
        print("Name   :", self.name)
        print("Age    :", self.age)


# Main program
p = Person()   # object creation
p.setInfo("Akshay", 26)
p.getInfo()
```

---

## ▶️ Example Output

```id="u7m3rs"
Name   : Akshay
Age    : 26
```

---

## 📚 Concepts Used

* Class and Object
* Object creation
* Instance variables
* Methods

---

## 🎯 Use Case

This program helps beginners understand:

* How an object is created from a class
* How data is stored and accessed using methods

---

## 🔧 Future Improvements

* Use constructor to initialize values directly
* Take input from user
* Create multiple objects
* Add validation for age

---

## 📄 License

This project is open-source and free to use.


<img width="851" height="746" alt="image" src="https://github.com/user-attachments/assets/f10f5095-d5c1-4517-a098-bb4dbfffda3c" />
