# Název zápočťáku

Tento zápočtový program se zabývá popisem tvorby zápočtového programu.

Může být klidně v angličtině (a asi to tak je i lepší).

Nejprve se hodí napsat nějakou zkrácenou verzi specifikace (summary), aby bylo jasné, co projekt dělá.
Tento projekt například popisuje, jak by měl vypadat repozitář se zápočtovým programem.

## Použití / Usage

Pro spuštění s defaultními parametry spusťte [main.py](zapoctak/main.py).


Příklad použití v kódu 🐍:

```python
from zapoctak import napis_zapoctak

muj_zapoctak = napis_zapoctak(jazyk='python', zajimavost=17)
print(muj_zapoctak[::-1].upper())

muj_zapoctak = napis_zapoctak(jazyk='🐍', zajimavost=3)
print(muj_zapoctak)
```

Výsledek:

```
NPOYYPYYPYHHPNOOO🐍
🐍🐍🐍
```

Je hezké mít hned na začátku různé příklady vstupů a výstupů, obrázky, a podobně.

Inspirujte se u jiných knihoven, například:
- [tqdm](https://github.com/tqdm/tqdm) (progress bar, doporučuji využívat :)),
- [transformers](https://github.com/huggingface/transformers) (jazyková záležitost).

## Instalace a požadavky

Co je potřeba, aby si uživatel nainstaloval?

V pythonu je zvykem závislosti specifikovat v souboru [requirements.txt](requirements.txt), ale o tom více v částí o
[python balíčcích](#jak-na-python-package). 

## Dokumentace

Podstatná část dokumentace je tvořena dobře čitelným, místy okomentovaným kódem.

### Jak na markdown (README)

Pokud na githubu umístíte soubor s názvem `README.md` do nějaké složky, automaticky se ve webovém rozhraní zobrazí.

Toho můžete využít i u vnořených složek. Markdown soubor editujte v libovolném textovém editoru.

Tady je několik přehledných návodů:
- https://gist.github.com/PurpleBooth/109311bb0361f32d87a2,
- https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46,
- [Markdown demo](https://markdown-it.github.io/).

### Jak na python package

Zápočťák nemusí být nutně přímo python package (stačí použít normální adresářovou strukturu),
ale pokud byste chtěli, aby Váš program mohli snadno používat (importovat) i jiní, tady je pár odkazů, jak na to:
- https://packaging.python.org/tutorials/packaging-projects/,
- https://blog.easyaspy.org/post/14/2019-05-05-how-to-submit-a-package-to-pypi.