from haystack import indexes
from cmpds.models import Compound

class CompoundIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True,use_template=True)

	def get_model(self):
		return Compound

	# def index_queryset(self, using=None):
	# 	"""Used when the entire index for model is updated."""
 #        return self.get_model().objects.all()	# could have changed to filter by date?