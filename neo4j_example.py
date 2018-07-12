# -*- coding: utf-8 -*-
from py2neo import Graph, Node, Relationship


graph = Graph("http://neo4j:123456@localhost:7474/db/data/")


def create_node():
    # create node
    node1 = Node("Person", name="Alice")
    node2 = Node("Person", name="Bob")
    graph.create(node1)
    graph.create(node2)

    #create relationship

    node1_kown_node2 = Relationship(node1, "KOWN", node2)
    node1_kown_node2['value'] = 1


    node2_kown_node1 = Relationship(node2, "KOWN", node1)
    node2_kown_node1['value'] = 1

    graph.create(node1_kown_node2)
    graph.create(node2_kown_node1)

    #update the value
    node1_kown_node2['value'] += 1
    graph.push(node1_kown_node2)


def add_attribute():
    node = Node("Person", name="Fred")
    node['age'] = 12
    node.labels.add("Student")
    node.properties["employee_no"] = 3456
    graph.create(node)


def cypher_create():
    """
    create node by cypher
    :return:
    """
    graph.cypher.execute("CREATE (a:Person {name:{N}})", {"N": "yangyy"})


def find():

    nodes = graph.find(label="Person")
    for node in nodes:
        print node['name']
       
    # find the relationship
    for rel in graph.match(start_node=node, rel_type="KOWN"):
        print rel
        print(rel.end_node.properties["name"])


if __name__ == '__main__':
    # create_node()
    # cypher_create()
    # add_attribute()
    find()

