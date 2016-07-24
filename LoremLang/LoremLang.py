import sublime, sublime_plugin, urllib.request, json, ast

#view.run_command('lorem_lang')

deu = "Das Magazin ist spezialisiert auf Artikel über Geografie, Natur, Geschichte, Wissenschaft und Kultur. Materialien mit einer großen Anzahl von Fotografien geliefert."
eng = "The magazine specializes in articles about geography, nature, history, science and culture. Materials are supplied with a large number of photographs."
ind	= "Majalah ini mengkhususkan diri dalam artikel tentang geografi, alam, sejarah, ilmu pengetahuan dan kebudayaan. Bahan disediakan dengan sejumlah besar foto."
ita = "La rivista specializzata in articoli su geografia, natura, storia, scienza e cultura. I materiali sono forniti con un gran numero di fotografie."
rus = "Журнал специализируется на статьях о географии, природе, истории, науке и культуре. Материалы снабжаются большим количеством фотографий."
zho = "该杂志专门从事有关地理，自然，历史，科学和文化的文章。材料具有大量的照片提供。"

class ComplexEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, complex):
			return [obj.real, obj.imag]
		# Let the base class default method raise the TypeError
		return json.JSONEncoder.default(self, obj)

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
class Translate(sublime_plugin.TextCommand):
	def run(self, edit):
		v = self.view
		selection = v.substr(v.sel()[0]) # to string
		###
		text_to_translate = selection
		language = "zho"
		response = urllib.request.urlopen('https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20160724T014826Z.b6cb21e320ea3e41.dbae97aa8f8ac6336c07d5931fc159acfca4e5f2&text='+text_to_translate+'&lang='+language+'')
		res = response.read()
		lst=eval(res)
		translate = lst['text']
		my_translate = str(translate)
		my_translate = my_translate[2:-2]
		# print(my_translate) # show translate in console
		v.replace(edit, v.sel()[0], my_translate)