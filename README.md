# Midterm 1

Exam rules available on MyCourses @ Instructor Materials>
Kumor>Midterm 01> Exam Rules

Make sure you read the entire assignment before you start part one.

You should feel free to create additional methods and classes as needed, but you should use the exact same nouns as those used in the problem statements whenever possible.

## Background

We are starting a petting Zoo for cute animals.  To do that we are going to need to create a computer system to manage all the cute animals.

## Part 1 (10)

Like most zoos, our zoo is going to be organized by species.  I have selected the cutest ones for our zoo and put them into this UML diagram for you to implement.

![UML for Part 1](./img/part1.png)

### Part 2 (20)

Each species has some important properties that should be accessible.  These are:

* A true or false if the species is endangered.
* A number that tells you their average life expectancy in years
* The maximum weight for the species in lbs.

The table below has the information.  

| Name | Endangered | Life Expectancy | Max Weight |
| -- | --  | -- | -- |
| Cat | No | 15 | 30 |
| Koala | Yes | 12 | 30.5 |
| Capybara | No | 8 | 150 |
| Cabbit | Yes | 10000 | 10000 |
| Porg | No | 3 | 7.5 |
| Pikachu | No | 28 | 16.8 |

Your solution should use the appropriate types and methods for full credit.

## Part 3 (20)

Like any zoo we need to name our animals

You have been provided a NameMaker class

* Complete the method getNames to return an array of Strings from the animalNames.txt file in the data folder.  
  * The first line of the file is the number of items in the array, and all the other entries are the names.  
  * If there is an error the function should return a null.
  * You should not hardcode the size of the array into your final solution and the list your return should only contain the names in the file.
* Complete the method getRandomName to return a random name from the names returned by getNames.

## Part 4 (25)

Now that we have a species and name generator we need to make our Animal class.

Each animal in the zoo should have properties for name, species, and weight.

* All the properties of an animal should have accessors.
* The weight should also have a mutator as the animals can gain or lose weight.  
* You need to make sure animals can only have a positive non-zero weight that is less than their max weight.  If an illegal weight is entered a checked IllegalArgumentException should be thrown.
* Each animal is created with a default weight equal to half their species' max weight.
* Create a toString method that outputs the following `<name> - <species> - <weight>`.  The displayed weight should be in whole numbers only.  So, for a Cat you should see `Garfield - CAT - 15`.

## Part 5 (20)

In the Animal class create a static method makeZoo that returns an Array of animals.

* The array should contain one of each species.  
* Use the getRandomName function you previously implemented to get a name for your animal.
* The method should make sure that two animals cannot have the same name before returning.

Create a main method that gets the results of the makeZoo method and prints the output of the toString method.  
