Copilot sai kyllä ihan melko järkevän ratkaisun luotua. Vähän se otti
shortcutteja, kuten varastos-dictin kanssa alunperin ja try: exceptaamalla
kaikki virheet. Myös ei lisännyt dependenssejä manifestiin pyytämättä.

Sessiota seuraamalla huomaa, että Copilot ei "ymmärrä" koodia, vaan aina
esimerkiksi session alussa lukaisee koodin ja vilkaisee aiemmat commitit. Myös
jotain muuttaessa Copilot hakee Bashillä paikkoja, joissa koodia pitää muuttaa.
Vähän monimutkaisemmalla koodilla ei varmasti onnistuisi Copilot tekemään
bugitonta koodia, ei ehkä edes ollenkaan toimivaa koodia. Tuntuu, ettei Copilot
yhtään mieti, mikä olisi paras tai järkevin tapa, tai mikä on koodin laadulta
parasta. No, sehän on tekoäly, se ei oikein voi miettiä.
