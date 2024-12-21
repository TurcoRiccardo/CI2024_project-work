# Simbolic Regression
Symbolic regression (SR) is a type of regression analysis that searches the space of mathematical expressions to find the model that best fits a given dataset, both in terms of accuracy and simplicity. In this solution we use a Genetic Programming algorithm to find the expected expression based on the MSE (Mean Square Error) value.

## Input Dataset
The algorithm takes as input a file containing a dataset with the X values ​​and the expected output Y

## Operation implemented
- Double Operation:
    - add
    - sub
    - mul
    - div
    - pow
- Single Operation:
    - neg
    - sin
    - cos
    - tan
    - exp
    - log
    - sqrt
    - abs
    - pow2

## Parent Selection
For parent selection we use Tournament Selection

## Mutation
The mutation algorithm take in input one individual and generates a new one, the new individual undergoes a mutation of the type:
- modify a operation with probability 1/operation_num in the expression
- add a new operation in a random location in the tree
- replace a value in the tree with another value
- modify a param incrementing or decrementing it (if there is at least one parameter in the expression)

## Crossover
The crossover algorithm take in input two individuals and generates a new one, for generating the new individual we take the first double operation in the first Individual and set in its right subtree a random subtree of the second Individual

## Fitness
The fitness function is composed by the MSE (Mean Square Error) and the number of operations present in the Individual

## Simplify the tree
Algorithm that takes an Individual as input and modifies it by eliminating useless operations that may be present in the tree such as:
- sum of 0
- sbtraction of 0
- multiplication by 1
- division by 1
- double negative
- exponential of the logarithm
- logarithm of the exponential

## Initial Population
The algorithm generate a random initial population with minimal dimension of the Individual equal to the number of value in the X dataset

## Genetic Programming Algorithm
We use a Tree-based Genetic Programming to find the solution, we generate two new offspring taking 2 parent whit Parent Selection, we perform crossover between the first and second parent and between the second and first parent, we apply the mutation on the results of the crossover operations and we apply the simplification to the result of the mutation. After we evaluate the fitness and we insert the ofspring in the population.