# code dependencies
import kb_services
import parsing
import interpretation
# network toolkit
import networkx as nx
# regular expressions 
import re
# drawing
import networkx.drawing
import matplotlib.pyplot as plt

G = kb_services.load_semantic_network()
sentence = "what is the location of each drink"



analized_sentences = interpretation.sentence_grounder(G, sentence)	
#print "inicio:::::::", analized_sentences
commands = []
for each_caracterized_sentence in analized_sentences:
	print "generatiing expression to planner from ", each_caracterized_sentence["objects"]
	commands.append(interpretation.generate_dependency(G, each_caracterized_sentence))

print "commands to planner..."	
for each in commands:
	print each
	
# knowledge basesolved_elements[each_element]
