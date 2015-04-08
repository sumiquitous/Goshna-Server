class DisplayFlight:
	def __init__(self, id, date, airline_short, source_short, dest_short, number, departure_time, airline_id, dest_id, source_id):
		self.id = id
		self.date = date
		self.airline_short = airline_short
		self.source_short = source_short
		self.dest_short = dest_short
		self.number = number
		self.departure_time = departure_time
		self.airline_id = airline_id
		self.dest_id = dest_id
		self.source_id = source_id

	def to_json(self):
		return {
			'id': self.id,
			'date': self.date,
			'airline_short': self.airline_short,
			'source_short': self.source_short,
			'dest_short': self.dest_short,
			'number': self.number,
			'departure_time': self.departure_time,
			'airline_id': self.airline_id,
			'dest_id': self.dest_id,
			'source_id': self.source_id
		}

