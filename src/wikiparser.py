import wikipedia

wikipedia.set_lang("sv")

def page( obj ):
	return wikipedia.page(obj)

def search( obj ):
	return wikipedia.search(obj)