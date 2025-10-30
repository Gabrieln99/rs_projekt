# rs_projekt

Sustav omogućuje unos i pohranu podataka o osobnim dokumentima (npr. putovnice, osobne iskaznice, potvrde) te njihovu verifikaciju pomoću blockchaina.
Kod unosa dokumenta provjerava se OIB korisnika, a podaci se kriptografski potpisuju i spremaju u blockchain (ili zapis o njima — hash dokumenta).

Kada osoba npr. dođe na granicu, sustav omogućuje provjeru autentičnosti dokumenta — uspoređuje hash dokumenta s onim koji je zapisan na blockchainu i time potvrđuje da dokument nije mijenjan i da je važeći.

Korisnik također može preuzeti svoj dokument u PDF obliku ili vidjeti status verifikacije.
