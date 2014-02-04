import unittest
import heart.node as node

class NodeTests(unittest.TestCase):
	def test_getting_node(self):
		result = node.getChildren("Pick a Topic")
		self.assertTrue("Partying" in result, "Partying was not a child of the node, but expected.")

	def test_bad_activity_name(self):
		result = node.getChildren("Does not exist")
		self.assertTrue(result == None, "Partying was not a child of the node, but expected.")
	
	def test_leaf_node(self):
		result = node.getChildren("Dhokla")
		self.assertTrue(result == None, "No child rows expected, but received %s." % result)
		
		
if __name__ == "__main__":
	unittest.main()