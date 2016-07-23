import sublime, sublime_plugin

deu = "Das Magazin ist spezialisiert auf Artikel über Geografie, Natur, Geschichte, Wissenschaft und Kultur. Materialien mit einer großen Anzahl von Fotografien geliefert."
eng = "The magazine specializes in articles about geography, nature, history, science and culture. Materials are supplied with a large number of photographs."
ind	= "Majalah ini mengkhususkan diri dalam artikel tentang geografi, alam, sejarah, ilmu pengetahuan dan kebudayaan. Bahan disediakan dengan sejumlah besar foto."
ita = "La rivista specializzata in articoli su geografia, natura, storia, scienza e cultura. I materiali sono forniti con un gran numero di fotografie."
rus = "Журнал специализируется на статьях о географии, природе, истории, науке и культуре. Материалы снабжаются большим количеством фотографий."
zho = "该杂志专门从事有关地理，自然，历史，科学和文化的文章。材料具有大量的照片提供。"

class LoremLangIta(sublime_plugin.TextCommand):
	def run(self, edit):
		selection = self.view.sel()
		for region in selection:
			region_text = self.view.substr(region)
			self.view.replace(edit, region, ita)
class LoremLangInd(sublime_plugin.TextCommand):
	def run(self, edit):
		selection = self.view.sel()
		for region in selection:
			region_text = self.view.substr(region)
			self.view.replace(edit, region, ind)
class LoremLangDeu(sublime_plugin.TextCommand):
	def run(self, edit):
		selection = self.view.sel()
		for region in selection:
			region_text = self.view.substr(region)
			self.view.replace(edit, region, deu)
class LoremLangEng(sublime_plugin.TextCommand):
	def run(self, edit):
		selection = self.view.sel()
		for region in selection:
			region_text = self.view.substr(region)
			self.view.replace(edit, region, eng)
class LoremLangRus(sublime_plugin.TextCommand):
	def run(self, edit):
		selection = self.view.sel()
		for region in selection:
			region_text = self.view.substr(region)
			self.view.replace(edit, region, rus)
class LoremLangZho(sublime_plugin.TextCommand):
	def run(self, edit):
		selection = self.view.sel()
		for region in selection:
			region_text = self.view.substr(region)
			self.view.replace(edit, region, zho)
			