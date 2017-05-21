

class trajectory(object):
	def __init__(self, initial_dict):
		self.initial_time = initial_dict.key()
		self.initial_x = initial_dict[self.initial_time][0]
		self.initial_y = initial_dict[self.initial_time][1]
		self.initial_z = initial_dict[self.initial_time][2]
		self.initial_vx = 0
		self.initial_vy = 0
		self.initial_vz = 0

	def followup_positioning(self, positioning_dict):
		
	def 