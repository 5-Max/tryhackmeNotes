# C++
## Hello World
-  Bjarne Stroustrup created c++ in 1979, added object-oriented programming to C, 
-  extensions are typically .cpp , 
```c++
#include <iostream>

int main() {

  std::cout << "Hello World!\n";

}
```
## Compile & Execute
- work flow = { Code | Save | Compile | Execute }
- ```g++ hello.cpp``` will compile to a.out , then execute ```./a.out```
- to name executable ```g++ hello.cpp -o hello```

## Variables
-   `int`: integer numbers
-   `double`: floating-point numbers
-   `char`: individual characters
-   `string`: a sequence of characters
-   `bool`: true/false values

Must, Must be declared
```c++
int = year;
year = 1998;
```
```c++
// combining into one line
int year = 1998;
```
### Operators
-   `+` addition
-   `-` subtraction
-   `*` multiplication
-   `/` division
-   `%` modulo (divides and gives the remainder)

chaining , we concactenate using << operator

```c++
std::cout << "Player score: " << score << "\n";
```

### User Input
```c++
#include <iostream>

int main() {

 int tip = 0;

 int total = 0;

  

 std::cout << "What is the total amount:";
 std::cin >> total;
 std::cout << "Enter tip amount: ";
 std::cin >> tip;
 std::cout << "You paid " << tip + total << " dollars." << "\n";

}
```
### The freeking tip calculator
[[tip_calculator.cpp]]

### Challenge Temperature
```c++
#include <iostream>

int main() {

 double tempf;
 double tempc;

 std::cout << "What's the temperature in F?";
 std::cin >> tempf;

 tempc = (tempf - 32) / 1.8;

 std::cout << "The temp is " << tempc << " degrees Celsius." << "\n"; 

}
```

```c++
#include <iostream>

using namespace std;

int main() {

 double tempf;
 double tempc;

 cout << "What's the temperature in F?";
 cin >> tempf;

 tempc = (tempf - 32) / 1.8;

 cout << "The temp is " << tempc << " degrees Celsius." << "\n"; 

}
```
### BMI
```c++
#include <iostream>

int main() {

 double height, weight, bmi;
 
 // Ask user for their height

 std::cout << "Type in your height (m): ";
 std::cin >> height;
 
 // Now ask the user for their weight and calculate BMI

 std::cout << "Type in your weight (kg): ";
 std::cin >> weight;
 
 bmi = weight / (height * height);
 
 std::cout << "Your BMI is " << bmi << "\n";

 return 0;

}
```

## Conditionals & Logic
```c++
#include <iostream>

int main() {

 double ph;

 std::cout << "What is the ph?";
 std::cin >> ph;

 // Write the if, else if, else here:

	 if (ph > 7) {
	   std::cout << "Basic\n";
	 } else if (ph < 7) {
	   std::cout << "Acidic\n";
	 } else {
	   std::cout << "Neutral";
	 }
}
```
## Your weight in other planets
[[galactic_wheight_calculator.cpp]]

## Logical operators
-   `&&`: the `and` logical operator
-   `||`: the `or` logical operator
-   `!`: the `not` logical operator
```c++
// Coin flip
#include <iostream>
#include <stdlib.h>
#include <ctime>

int main() {
  
  // Create a number that's 0 or 1
  
  srand (time(NULL));
  int	coin = rand() % 2;
  
  // If number is 0: Heads
  // If it is not 0: Tails
  
  if (coin == 0) {
  
    std::cout << "Heads\n";
  
  }
	else {
	
    std::cout << "Tails\n";
  
  }
  
}
```
Leap Year exercise
```c++
#include <iostream>

int main() {

 int year = 0;

 std::cout << "Input a year \n";
 std::cin >> year;

 if (year > 999 && year < 10000) {

   if (!(year % 4) || !(year % 400)){

     std::cout << "This is a Leap year!\n";

     } else {

       std::cout << "This is not a Leap year!\n";
	 } 

     } else {

       std::cout << "please enter a 4 digit year\n";
 }
}
```

## Loops
while loop , 
```c++
#include <iostream>

int main() {

  int guess;
  
  int tries = 0;

  std::cout << "I have a number 1-10.\n";
  std::cout << "Please guess it: ";
  std::cin >> guess;
 
  // Write a while loop here:
  while (guess != 8  && tries < 50) {
    std::cout << "Wrong, try again: ";
    std::cin >> guess;

    tries++;
  }
  if (guess == 8) {
    std::cout << "You got it!\n";
  }  
}
```

Quiz
https://en.wikipedia.org/wiki/EDSAC
```c++
#include <iostream>

int main() {

 int i = 0;
 int square = 0;

 // Write a while loop here:
 
	 while (i !=10) {
	 std::cout << i << " ";
	 square = i * i ;
	 i++;
	 std::cout << square <<"\n";

 } 
}

// messing around making example into a for loop // not tested

	for (i =0;i < 10;i++){
	  std::cout << i << " ";
	  square = i * i ;
	  std::cout << square << "\n";
	}
```
### their solution is a bit cleaner
```c++

while (i < 10) {  
  
 square = i * i;  
  
 std::cout << i << "  " << square << "\n";  
  
 i++;  
  
}

// and even more clean,,,

while (i < 10) {  
  
 std::cout << i << "  " << i * i << "\n";  
  
 i++;  
  
}
```

## For loops
```c++
#include <iostream>

int main() {

 for (int i = 0; i < 10; i++) {

 std::cout << "I will not throw paper airplanes in class.\n";

 }
}
```
99 bottles of pop on the wall
```c++
#include <iostream>

int main() {

 // Write a for loop here:

 for (int i = 99; i > 0; i--) {

 std::cout << i << " bottles of pop on the wall.\n
 Take one down and pass it around.\n" 
 << i - 1 << " bottles of pop on the wall.\n\n";

 }
 std::cout << "No more bottles of pop on the wall.\n";
 std::cout << "No more bottles of pop.\n";
 std::cout << "Go to the store and buy some more,\n";
 std::cout << "99 bottles of pop on the wall.\n";
}
```
# Bugs
https://en.wikipedia.org/wiki/Grace_Hopper

Errors
-   **Compile-time errors:** Errors found by the compiler.
-   **Syntax errors**: Errors that occur when we violate the rules of C++ syntax.
-   **Type errors**: Errors that occur when there are mismatch between the types we declared.
-   **Link-time errors:** Errors found by the linker when it is trying to combine object files into an executable program.
-   **Run-time errors:** Errors found by checks in a running program.
-   **Logic errors:** Errors found by the programmer looking for the causes of erroneous results.
```c++
int main() {

 int num = 0;
 int sum = 0;

 std::cout << "Enter a number: ";
 std::cin >> num;

 for (int i = 1; i <= num; i++) {
	 sum = sum + i;
	 std::cout << i << " ";
	 }
 std::cout << "Sum: " << sum << "\n";
}
```
randomly pics a saying,
```c++
#include <iostream>
#include <stdlib.h>
#include <ctime>

int main() {
    
  srand (time(NULL));
  int	fortune = rand() % 10;
  
  if (fortune == 0) {
    std::cout << "Flattery will go far tonight.\n";  
  } else if (fortune == 1) {    
    std::cout << "Don't behave with cold manners.\n";  
  } else if (fortune == 2) {    
    std::cout << "May you someday be carbon neutral\n";    
  } else if (fortune == 3) {    
    std::cout << "You have rice in your teeth.\n";   
  } else if (fortune == 4) {   
    std::cout << "A conclusion is simply the place where you got tired of thinking.\n";   
  } else if (fortune == 5) {   
    std::cout << "No snowflake feels responsible in an avalanche.\n";    
  } else if (fortune == 6) {    
    std::cout << "He who laughs last is laughing at you.\n";    
  } else if (fortune == 7) {    
    std::cout << "If you look back, you'll soon be going that way.\n";    
  } else if (fortune == 8) {   
    std::cout << "You will die alone and poorly dressed.\n";      
  } else if (fortune == 9) {
    std::cout << "The fortune you seek is in another cookie.\n";
  }
}
```

## Vectors
A _vector_ is a sequence of elements that you can access by index.
we need the library
```#include <vector>```
```std::vector<type> <name>;```

can not be changed

with value:
```std::vector<double> location = {42.651443, -73.749302};```

with size:
```std::vector<double> location(2);```

##### .push_back()
adds new element to the back of vector

##### .pop_back()
removes elements from the "back" of a vector

##### .size()
returns the size of vector

```c++
#include <iostream>
#include <vector>

int main() {

 std::vector<double> delivery_order;
 delivery_order.push_back(8.99);
 delivery_order.push_back(3.75);
 delivery_order.push_back(0.99);
 delivery_order.push_back(5.99);

 // Calculate the total using a for loop:

 double total = 0.0;

 for (int i = 0; i < delivery_order.size(); i++) {
   total = delivery_order[i] + total;
   td::cout << delivery_order[i] << " " << total << "\n";
 }
 std::cout << total;
}
```


Write a program to find the sum of even numbers and the product of odd numbers in a vector.

For example:

Suppose we have a vector that is `{2, 4, 3, 6, 1, 9}`.
```c++
#include <iostream>
#include <vector>

int main() {
  std::vector<int> all_numbers = {2,4,3,6,1,9};

  int total_numbers = 0;
  int odd_numbers = 1;

  for (int i = 0; i < all_numbers.size(); i++) {
    //std::cout << all_numbers[i] << " ";
    if (all_numbers[i] % 2 == 0) {
      total_numbers = total_numbers + all_numbers[i];
    } else {
      odd_numbers = odd_numbers * all_numbers[i];
  }
}
  std::cout << "Sum of even: " << total_numbers << "\n";
  std::cout << "Product of odd: " << odd_numbers;
}
```

## Functions

### Built-in Functions
```c++
#include <iostream>

int main() {

 // This seeds the random number generator:

 srand (time(NULL));

 // Use rand() below to initialize the_amazing_random_number

 int the_amazing_random_number = rand() % 29;
 std::cout << the_amazing_random_number;
}
```
find the square root of any number with cmath
```c++
#include <cmath>

std::cout << sqrt(9) << "\n";
```
### Declare and Define
Declaration
  return type
  name
  parameters (if any)
  
Definition

Call 

```c++
#include <iostream>

void make_sandwich() {  
  
 std::cout << "bread\n";  
 std::cout << "egg\n";  
 std::cout << "cheese\n";  
 std::cout << "avocado\n";  
 std::cout << "bread\n";  
  
}

int main() {
  make_sandwich();
}
```

Void functions - good for just printing lines to terminal - aka subroutine - has no return value

If the function is not a void function then it has to return something and return value must be the same as the function's return type.

```c++
#include <iostream>

// Define get_emergency_number() below:
void get_emergency_number(string emergency_number) {
  std::cout << "Dial" << emergency_number;
}

int main() {
  
  // Original emergency services number 
  std::string old_emergency_number = "999";
  
  // For nicer ambulances, faster response times
  // and better-looking drivers
  std::string new_emergency_number = "0118 999 881 999 119 725 3";
  
  // Call get_emergency_number() below with
  // the number you want!
  get_emergency_number(new_emergency_number);
  
}
```
Multiple parameters
```c++
#include <iostream>

	// Define name_x_times() below:
void name_x_times(std::string name, int x) {
  
  while (x > 0) {
    std::cout << name;
    x--;
  }
}

int main() {
  
  std::string my_name = "Add your name here!\n";
  int some_number = 5; // Change this if you like!
  	// Call name_x_times() below with my_name and some_number
  name_x_times(my_name, some_number);
}
```

Challenge #1
```c++
#include <iostream>

// Define introduction() here:

void introduction(std::string first_name,std::string last_name) {
  std::cout << last_name << ", " << first_name << " " << last_name;
}

int main() {
  
  introduction("Beyonce", "Knowles");
  
}
```
Challenge #2 (this one got me, you have to RETURN SOMETHING)
```c++
#include <iostream>

// Define average() here:
double average(double num1, double num2) {
  return (num1 + num2) / 2;
}

int main() {
  
  std::cout << average(42.0, 24.0) << "\n";
  std::cout << average(1.0, 2.0) << "\n";
  
}
```
Challenge #3
```c++
#include <iostream>
#include <cmath>

// Define tenth_power() here:
int tenth_power(int num) {
  num = num * num * num * num * num * num * num * num * num * num;
  return num;
}

int main() {
  
  std::cout << tenth_power(0) << "\n";
  std::cout << tenth_power(1) << "\n";
  std::cout << tenth_power(2) << "\n";
  
}
```
Challenge #4
this one was interesting,
```c++
#include <iostream>
#include <vector>

// Define first_three_multiples() here:

std::vector<int> first_three_multiples(int num) {
  std::vector<int> mul = {num, num * 2, num * 3};
  return mul;
}

int main() {
  
  for (int element : first_three_multiples(8)) {
    std::cout << element << "\n";
  }
  
}
```
Challenge #5
```c++
#include <iostream>

// Define needs_water() here:
std::string needs_water(int days,bool is_succulent) {
  if (days > 3 && is_succulent == false) {
   return "Time to water the plant.";
  } else if (days <= 12 && is_succulent == true) {
     return "Don't water the plant!"; 
  } else if (days >= 13 && is_succulent == true) {
    return "Go ahead and give the plant a little water.";
  } else {
    return "Don't water the plant!";
  }
}

int main() {
  std::cout << needs_water(10, false) << "\n";
}
```
Challenge #6
```c++
#include <iostream>

// Define is_palindrome() here:

bool is_palindrome(std::string text) {
  
  std::string reversed_text = "";
  
  for (int i = text.size() - 1; i >= 0; i--) {
    reversed_text += text[i];
  }
  
  if (reversed_text == text) {
    return true;
  }
  return false;
}

int main() {
  std::cout << is_palindrome("madam") << "\n";
  std::cout << is_palindrome("ada") << "\n";
  std::cout << is_palindrome("lovelace") << "\n";
}
```
### Scope
local vs global variable

Multi file 

file 1 main.cpp file 2 my_functions.cpp

main.cpp
```c++
#include <iostream>

// Add declarations here:

double average(double num1, double num2);
int tenth_power(int num);
bool is_palindrome(std::string text);

int main() {
  
  std::cout << is_palindrome("racecar") << "\n";
  std::cout << tenth_power(3) << "\n";
  std::cout << average(8.0, 19.0) << "\n";
  
}
```
my_functions.cpp
```c++
#include <iostream>
#include <cmath>

// Add definitions here:
double average(double num1, double num2) {
  return (num1 + num2) / 2;
}

int tenth_power(int num) {
  return pow(num, 10);
}

bool is_palindrome(std::string text) {
  std::string reversed_text = "";
  
  for (int i = text.size() - 1; i >= 0; i--) {
    reversed_text += text[i];
  }
  
  if (reversed_text == text) {
    return true;
  }
  
  return false;
}
```
then compile
```g++ main.cpp my_functions.cpp```

#### Making a header
ideally we want to see only the main function in the main.cpp
create a file with an extension of hpp or h for header and put declarations there
and we put the definitions in another cpp file
remember to create the header
```#include "name_of_file.hpp"```
#### inline functions
usually found in the header file, tells compiler to add body of function when that function is called , to make execution faster (or it could make it slower), you need to test to see if it helps or not.

#### Default Arguments
we can define a default value on the definition of the function

#### Function overload
>"What if you want a function to accept an argument that can be either an `int` OR a `double`? Or what if you want some function parameters to be optional? C++ has a trick up its sleeve just for such situations."

#### Function templates
allows to add data types as parameters
https://en.cppreference.com/w/cpp/header

Allows you to do a fuction overload but cleaner and making the parameter flexible.
> "Templates let us choose the type implementation right when you call the function. The type we choose may apply to the return type, a parameter type, or both."

So let's change this from a function overload to a function template 
three files:

```c++
//									main.cpp
#include <iostream>
#include "numbers.hpp"

int main() {
  std::cout << get_smallest(100, 60) << "\n";
  std::cout << get_smallest(2543.2, 3254.3) << "\n";
}
//                              	numbers.hpp

int get_smallest(int num1, int num2);

double get_smallest(double num1, double num2);

	
//									numbers.cpp
// Remove everything here:

int get_smallest(int num1, int num2) {
 return num2 < num1? num2 : num1;
}
double get_smallest(double num1, double num2) {
 return num2 < num1? num2 : num1;
}
```
#### Becomes
```c++
//									main.cpp
#include <iostream>
#include "numbers.hpp"

int main() {
  std::cout << get_smallest(100, 60) << "\n";
  std::cout << get_smallest(2543.2, 3254.3) << "\n";
}
//                              	numbers.hpp
template <typename T>

T get_smallest(T num1, T num2) {
 return num2 < num1? num2 : num1;
}
```

### Classes and Objects
In the header file, after a class declaration you have to use a semicolon,,
```c++
class Song {}; 
```

class Student {
-  attributes:
		name (string)
		gpa (number)
		year (string) ie freshman,sophmore,junior,senior
		has scholarship (bool)
-  functions
		has honors()  is gpa greater than 3.5
		has scholarship() if has honors is true give scholarship

};

instance of a class is an object 

other examples

class Lightbulb {
  isOn (bool)
  watts (number)
  
  turnOn{}
}

class Microphone {
	color (string)
	isAnalog (bool)
	
	record()
}

class Animal {
	color (string)
	age (number)
	
	speak()
}

class Date {
  month (int)
  year (int)
  
  toString 
}


#### the song title example

[[main.cpp]]
[[files/Class_Song 1/song.hpp]]
[[files/Class_Song 1/song.cpp]]
### public or private

song title and artist

[[music.cpp]]
[[files/Class_Song 2/song.hpp]]
[[files/Class_Song 2/song.cpp]]

## Constructors

