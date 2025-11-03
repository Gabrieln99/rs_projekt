# rs_projekt

Sustav omogućuje unos, pohranu i verifikaciju dokumenata (npr. putovnice, osobne iskaznice, potvrde) pomoću blockchain tehnologije.
Kod unosa dokumenta provjerava se OIB korisnika, a podaci se kriptografski potpisuju i spremaju u blockchain.
Kada osoba, primjerice, dođe na granicu, sustav omogućuje provjeru autentičnosti dokumenta uspoređujući hash dokumenta s onim koji je zapisan na blockchainu, čime se potvrđuje da dokument nije mijenjan i da je važeći.
Korisnik također može preuzeti svoj dokument u PDF obliku ili vidjeti status verifikacije.

# Tok rada sustava:

##### Unos podataka – korisnik ili službenik unosi podatke o osobi i dokumentu (OIB, ime, vrsta dokumenta).

##### Verifikacija OIB-a – sustav provjerava ispravnost OIB-a (algoritamski ili preko API-ja).

##### Blockchain zapis (smart contract) – hash dokumenta i osnovni metapodaci spremaju se u blockchain (npr. Ethereum testnet ili lokalni blockchain).

##### Generiranje PDF-a – dokument se sprema kao PDF koji sadrži QR kod (QR vodi do blockchain zapisa).

##### Verifikacija – na granici, službenik skenira QR kod ili upiše ID, a sustav provjerava u blockchainu je li dokument autentičan i važeći.



Update sa sata: 3.11.2025:
QR osobna , osobna se skenira i netko potvrđuje vaš identitet uzivo
