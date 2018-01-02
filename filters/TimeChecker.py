from filters import kernelize as k, utils, centroid_extraction as ce
import astropy.wcs as a
import cv2
import numpy as np
import time


class TimeChecker:

	def __init__(self):
		"""
		Constructor
		"""
		self.lastMark = time.time()
		self.sum = 0
		return

	def mark_time(self, descr, print_time=True):
		now = time.time()
		self.sum = self.sum + (now - self.lastMark)
		if print_time:
			print("Duration of {0}: {1}ms".format(descr, np.round(1000*(now - self.lastMark), 3)))
		self.lastMark = now
		return

	def total(self):
		print("Total duration: {0}ms".format(np.round(1000*self.sum, 3)))
		return