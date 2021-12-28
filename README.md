# *OOP Ex_3*

In this project we have created a data structure of a weighted and oriented graph in Python, as part of our OOP course at Ariel university. The following project is the fourth project of our course and represents a 'translation and comparation' for the previous project.

## Classes:
* Node - Represents the graph's vertices
* Edge - Represents the graph's edges
* DiGraph - Represents the graph
* GraphAlgo - Algorithems that can be execute on the graph
* TestGraph - Test class
* GraphInterface - An abstract class which represents an interface of a graph
* GraphAlgoInterface - An abstract class which represents an interface of a graph
* main - Contains check methods


## How To Load A Graph:

In the main.py class, go to main method and create a GraphAlgo by the following instructions -
* graph = GraphAlgo()
* file = '../data/A5.json' (enter a jason file you wuold like to load)
* graph.load_from_json(file)
* graph.plot_graph
