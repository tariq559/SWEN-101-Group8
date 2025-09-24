# Unit 03 Practice Problems

The goal of these "mini practica" is to give you practice with coding problems similar to those that you will see on the midterm practica. You will be required to solve each problem with minimal assistance. You should use these mini-practica as an opportunity to gauge your preparedness for the exams.

You should create all of your required files in this folder along with these
instructions.

Each mini-practicum counts as a homework assignment.

---

1. Create a new package `src\main\java\unit04\practicum` and implement your solution in that package.

2. A fighter in the Moral Combat (MC) fighting game has the following behavior:
   * All fighters have a an attack and each has a different attack damage value.  You can get the amount of damage of their next attack (a positive integer) using a method.
   * All fighters take damage differently and each figher can recieve damage (a positive integer).
   * A fighter is unconscious if health drops to 0.

   Create a new type to represent fighters.

3. Create a class that allows two MC fighters to do battle in an arena.
   * Battle continues as long as both fighters are conscious.
   * During each round of battle, both fighters damage each other.
   * At the end of battle, the winner is announced (using its toString()),  
      *e.g. "Sonyo wins!" If both fighters are unconscious, it is a draw.*

4. Use the table below to implement at least two fighters, each in its own
   class. Then add a main method to your arena class and have the fighters do
   battle. Each time the fighter attacks or is damaged, it should print a
   message.

| Name | Health | Attack | Taking Damage |
| -- | -- | -- | -- |
| SubFreezing | 100 |  Attack hits for 25 to 50 damage | 25% Chance to dodge all damage |
| Jacks | 200 | 75% change to attack with armored arms for 40 damage, 25% change to attack with missles for 75 damage | No modification |
| Kenshin | 150 | Sword hits for 45 | 50% chance to block; damage reduced by half (rounded down).|
| Goku | 200 | Bash has a 75% chance to hit for 75, and a  25% chance to miss (0 damage) | If health is below 50, rage causes damage taken to be reduced by 10. |
