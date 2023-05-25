# Lab_2_TMPS - The Darkest Stronghold Game.
## by Plesca Alexandru

## Task : 
    1. Choose an OO programming language and a suitable IDE or Editor (No frameworks/libs/engines allowed).

    2. Select a domain area for the sample project.

    3. Define the main involved classes and think about what instantiation mechanisms are needed.

    4. Based on the previous point, implement at least 2 creational design patterns in your project.

## General Theory : 
Creational design patterns are a category of design patterns that focus on the process of object creation. They provide a way to create objects in a flexible and controlled manner, while decoupling the client code from the specifics of object creation. Creational design patterns address common problems encountered in object creation, such as how to create objects with different initialization parameters, how to create objects based on certain conditions, or how to ensure that only a single instance of an object is created. There are several creational design patterns that have their own strengths and weaknesses. Each of it is best suited for solving specific problems related to object creation. By using creational design patterns, developers can improve the flexibility, maintainability, and scalability of their code.

## Description :
The app is a game where the player navigates a character through a series of levels. The game uses the following creational design patterns:
    Factory Method - to create different types of levels
    Abstract Factory - to create different types of characters
    Singleton - to ensure there is only one instance of the game manager
    Builder - to create complex objects such as the game map

## Here is were these 4 patterns were used
  * Factory Method pattern: The LevelFactory class is an example of the Factory Method pattern. It provides a way to create different types of Level objects (EasyLevel, MediumLevel, and HardLevel) based on a given input (level_type). This allows for a more flexible and extensible way of creating objects than simply instantiating them directly.

  * Abstract Factory pattern: The CharacterFactory class is an example of the Abstract Factory pattern. It provides a way to create different types of Character objects (Warrior and Mage) based on a given input (character_type). Like the Factory Method pattern, this allows for more flexibility and extensibility when creating objects.

  * Singleton pattern: The GameManager class is an example of the Singleton pattern. Only one instance of this class is allowed to exist, which is accessed through the get_instance() method. This ensures that there is only one GameManager object controlling the game at any given time.

  * Builder pattern: The MapBuilder and MapDirector classes are an example of the Builder pattern. They provide a way to construct a complex object (map) step by step, by adding rows to the map one at a time. The MapBuilder class represents the actual builder, while the MapDirector class provides the steps for building the map.
