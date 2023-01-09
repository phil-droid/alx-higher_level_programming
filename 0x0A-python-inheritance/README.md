Python Inheritance

Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.Create a Child Class

To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class.
When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

 The child's __init__() function overrides the inheritance of the parent's __init__() function.
 To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function

Use the super() Function

Python also has a super() function that will make the child class inherit all the methods and properties from its parent.
By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.
If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.
