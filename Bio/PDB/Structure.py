# Copyright (C) 2002, Thomas Hamelryck (thamelry@vub.ac.be)
# This code is part of the Biopython distribution and governed by its
# license.  Please see the LICENSE file that should have been included
# as part of this package.  


# My Stuff
from Entity import Entity


class Structure(Entity):
	"""
	The Structure class contains a collection of Model instances.
	"""
	def __init__(self, id):
		self.level=4
		Entity.__init__(self, id)

	# Special methods

	def __repr__(self):
		return "<Structure id=%s>" % self.get_id()

	# Private methods

	def _sort(self, m1, m2):
		"""Sort models.

		This sorting function sorts the Model instances in the Structure instance.
		The sorting is done based on the model id, which is a simple int that 
		reflects the order of the models in the PDB file.

		Arguments:
		o m1, m2 - Model instances
		"""
		return cmp(m1.get_id(), m2.get_id())

